'''
docker pull hivemq/hivemq4
docker run -it --rm --name hivemq -p 8080:8080 -p 1883:1883 hivemq/hivemq4
open http://localhost:8080
'''

import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
broker_address="127.0.0.1"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","house/bulbs/+")
client.subscribe("house/bulbs/bulb1")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","OFF")
client.publish("house/bulbs/bulb1","ON")
time.sleep(4) # wait
client.publish("house/bulbs/bulb1","WHAT")
time.sleep(1) # wait
client.loop_stop() #stop the loop