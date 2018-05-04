#import logging as log
# log.basicConfig(level=log.DEBUG)
from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9092")
print client.topics
topic = client.topics['test']
with topic.get_sync_producer() as producer:
    producer.produce('Hello World docker-kakfa-pykafka-clients!')
