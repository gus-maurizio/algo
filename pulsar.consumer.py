#!/usr/local/Cellar/python@3.9/3.9.12/bin/python3
import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('my-topic',
                            subscription_name='my-sub')

try:
    while True:
        msg = consumer.receive()
        print(f'Received message: <{msg.data()}>')
        consumer.acknowledge(msg)
except KeyboardInterrupt:
    print('Ended')


client.close()
