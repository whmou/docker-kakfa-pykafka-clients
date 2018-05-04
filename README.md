# docker-kakfa-pykafka-clients
A helloworld level project to play with kafka on your mac 
Include 2 main parts:
- Build kafka cluster by docker (with easy 2-line command)
- Use pykafka to create python kafka clients as producer and consumer
 
Structure: <br/>
![Structure](https://github.com/whmou/docker-kakfa-pykafka-clients/blob/master/structure.png)

## Kafka by Docker 
### Start the docker kafka service

The following commands will start a container with Kafka and Zookeeper,
Mapped ports: Zookeeper:2181, Kafka:9092
```console
$ cd main/feature_insights/visualization/
$ docker run -d -p 9092:9092 -p 2181:2181 --env ADVERTISED_HOST=127.0.0.1 --env ADVERTISED_PORT=9092 --name kafka -h 127.0.0.1 spotify/kafka
```
Now the service is running in the docker container.

### Generate a topic named "test"
```console
$ docker exec kafka /opt/kafka_2.11-0.10.1.0/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
```
### List topics to check status
```console
$ docker exec kafka /opt/kafka_2.11-0.10.1.0/bin/kafka-topics.sh --list --zookeeper localhost:2181
```
the output should be:
```console
test
```

## Pykafka producer & consumer
### pip install [pykafka](https://github.com/Parsely/pykafka)
```console
$sudo pip install pykafka
```
### pykafka producer

```python
from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9092")
print client.topics
topic = client.topics['test']
with topic.get_sync_producer() as producer:
    producer.produce('Hello World docker-kakfa-pykafka-clients!')
```

### pykafka consumer

```python
from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9092")
print client.topics
topic = client.topics['test']
consumer = topic.get_simple_consumer()
for message in consumer:
    if message is not None:
        print message.offset, message.value
```

The output should be:
```console
Hello World docker-kakfa-pykafka-clients!
```

Have fun!

