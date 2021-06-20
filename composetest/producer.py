# Import KafkaProducer from Kafka library
from kafka import KafkaProducer
from time import sleep

# Define server with port
bootstrap_servers = ['localhost:9092']

# Define topic name where the message will publish
topicName = 'First_Topic'

# Initialize producer variable
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

# Publish text in defined topic
#producer.send(topicName, b'Hello from kafka...')

for e in range(1000):
    producer.send(topicName, b'Hello from kafka...')
    sleep(3)

# Print message
print("Message Sent")