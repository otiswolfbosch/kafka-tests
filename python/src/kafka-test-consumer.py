from kafka import KafkaConsumer 

KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "test-otis"
print("starting program")

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER)
print("consumer created")

for msg in consumer:
    print (msg)

print("messages printed")