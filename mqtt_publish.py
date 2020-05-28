from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('config.ini')
IP = cfg['Others']['IP']
USER = cfg["Account"]['USER']
PASSWORD = cfg['Account']['PASSWORD']
Port  = 1883
Topic = "rand"

####################################
import paho.mqtt.client as mqtt
mqttc = mqtt.Client()
mqttc.username_pw_set(USER,password=PASSWORD)
mqttc.connect(IP,Port)

import time
start = time.perf_counter()
count = 0
while time.perf_counter()-start<=0.5:
    mqttc.publish(Topic,count)
    count+=1
    print(count)
