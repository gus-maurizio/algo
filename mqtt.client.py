import paho.mqtt.client as mqtt #import the client1

broker_address="127.0.0.1"
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
client.publish("house/main-light","OFF")#publish
