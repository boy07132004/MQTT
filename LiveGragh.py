import CT
from collections import deque
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib.animation as ani

def on_connect(client, userdata, flags, rc):
    client.subscribe('xyz')
    
def on_message(client, userdata, msg):
    global ads
    global x
    global y
    global z
    if ads.read()>3200:
        _x,_y,_z = msg.payload.decode('utf-8').split(',')
    else:
        _x,_y,_z = 0,0,0
    for i in ('x','y','z'):
        eval(i).popleft()
        eval(i).append(float(eval('_'+i)))

def animate(i):
    for line,ls in ((line_x,x),(line_y,y),(line_z,z)):
        line.set_ydata(ls)
    return 0

if __name__ == "__main__":
    x = deque([0]*200)
    y = deque([0]*200)
    z = deque([0]*200)

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    xs  = list(range(200)) 
    ax1.set_ylim([-2.5,2.5])
    line_x, = ax1.plot(xs,x,'r')
    line_y, = ax1.plot(xs,y,'g')
    line_z, = ax1.plot(xs,z,'b')
    ax1.legend([line_x,line_y,line_z],['X','Y','Z'])
    ani = ani.FuncAnimation(fig,animate,interval=50)
    ads = CT.ADS1115()
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set('raspi3b', 'ml6a01')
    client.connect("192.168.0.161", 1883, 60)
    
    client.loop_start()
    plt.show()
    client.loop_stop()
    client.disconnect()