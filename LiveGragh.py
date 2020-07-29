import matplotlib.pyplot as plt
import matplotlib.animation as ani
from collections import deque

x = deque([0]*200)
y = deque([0]*200)
z = deque([0]*200)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xs  = list(range(200)) 
ax1.set_ylim([-4,4])
line_x, = ax1.plot(xs,x)
line_y, = ax1.plot(xs,y)
line_z, = ax1.plot(xs,z)
import random 
def rand():
    global x
    global y
    global z
    while 1:
        for i,j in ((x,-2),(y,0),(z,2)):
            i.popleft()
            i.append(j+random.random())
        time.sleep(0.01)
            

def animate(i):
    for line,ls in ((line_x,x),(line_y,y),(line_z,z)):
        line.set_ydata(ls)
    return 0#line_x,line_y,line_z

import threading
import time
if __name__ == "__main__":
    threading.Thread(target=rand).start()
    ani = ani.FuncAnimation(fig,animate,interval=10)
    plt.show()