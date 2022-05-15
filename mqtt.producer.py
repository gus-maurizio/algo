import paho.mqtt.client as mqtt #import the client1
import time,sys
############
########################################
broker_address="127.0.0.1"
#broker_address="iot.eclipse.org"
topic1 = "house/bulbs/" 
topic1 +=  sys.argv[1] if len(sys.argv) > 1 else "bulb1"
print(f"creating new instance {topic1}")
client = mqtt.Client("P1") #create new instance
client.will_set(topic1,"Bulb1 Gone Offline",qos=1,retain=True)
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Publishing message to topic",topic1)
client.publish(topic1,"POFF")
client.publish(topic1,"PON")
client.publish(topic1,"PWHAT")
print('sleep')
time.sleep(20) # wait
client.loop_stop() #stop the loop