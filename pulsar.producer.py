#!/usr/local/Cellar/python@3.9/3.9.12/bin/python3
# #!/usr/local/Cellar/python@3.8/3.8.13_1/bin/python3
import pulsar,sys
from datetime import datetime

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic')
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10
ts = datetime.now().isoformat()
for i in range(1,N+1):
    producer.send((f'hello-pulsar {ts} {i:03d}').encode('utf-8'))

client.close()
