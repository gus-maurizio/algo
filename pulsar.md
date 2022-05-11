# Run Pulsar
```bash
docker run -it --rm --name pulsar-server \
  -p 6650:6650 -p 8080:8080 \
  -v /tmp/data:/pulsar/data \
  apachepulsar/pulsar bin/pulsar standalone

curl -s http://localhost:8080/admin/v2/persistent/public/default/my-topic/stats | python -m json.tool
```
## Run Consumer
Make sure you run the pip3 and python3 for a supported python version (3.8).
```python
#!/usr/local/Cellar/python@3.8/3.8.13/bin/python3
import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('my-topic',subscription_name='my-sub')

while True:
    msg = consumer.receive()
    print("Received message: '%s'" % msg.data())
    consumer.acknowledge(msg)

client.close()
```

## Run Producer
Make sure you run the pip3 and python3 for a supported python version (3.8).
```python
#!/usr/local/Cellar/python@3.8/3.8.13/bin/python3
import pulsar,sys
from datetime import datetime

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic')
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10
ts = datetime.now().isoformat()
for i in range(1,N+1):
    producer.send((f'hello-pulsar {ts} {i:03d}').encode('utf-8'))

client.close()
```
