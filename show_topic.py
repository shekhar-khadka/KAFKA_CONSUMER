from confluent_kafka import Consumer

################
c = Consumer({'bootstrap.servers': '20.120.90.207:9092', 'group.id': 'kafka-multi-video-stream', 'auto.offset.reset': 'earliest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)

e
