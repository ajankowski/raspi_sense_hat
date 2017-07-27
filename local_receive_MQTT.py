#!/usr/bin/python3

from sense_hat import SenseHat
import time
import paho.mqtt.client as paho
#import json


sense = SenseHat()
  
def on_subscribe(client, userdata, mid, granted_qos):
    print('Subscribed')
    
def on_message(client, userdata, msg):
    print(msg.topic + str(msg.payload))
    mybuffer=msg.payload
    sense.show_message(str(msg.payload), scroll_speed = 0.1)
    return mybuffer
  
    
    
client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('broker.mqttdashboard.com', 1883)    
client.subscribe('/andrzej/sensorki') 

print(mybuffer)    
print("3")

client.loop_forever()


    

    
    
