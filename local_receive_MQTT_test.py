#!/usr/bin/python3

from sense_hat import SenseHat
import paho.mqtt.client as paho
import time

sense = SenseHat()
sense.set_rotation(180)

mybuffer = ''
  
def on_subscribe(client, userdata, mid, granted_qos):
    print('Subscribed')
    
def on_message(client, userdata, msg):
    #print(msg.topic + str(msg.payload))
    mybuffer = 'dupa'
    print('my buffer '+ mybuffer)
    #sense.show_message(str(msg.payload), scroll_speed = 0.1)
    
client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('broker.mqttdashboard.com', 1883)    
client.subscribe('/andrzej/sensorki')

client.loop_forever()

print('suprise '+ mybuffer)

#client.loop_stop(force=False)


    

    
    
