import paho.mqtt.client as mqtt

def on_connect(client, userdata,flags, rc):
    client.subscribe("rand")

def on_message(client, userdata, msg):
    print(msg.topic," ",msg.payload.decode('utf-8'))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('raspi3b',password='ml6a01')
client.connect("192.168.0.111",1883,60)

client.loop_forever()
