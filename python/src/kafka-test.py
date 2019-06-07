from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

from time import sleep

KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "test-otis"


print("program starting")

# admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_SERVER, client_id='test')
# print("admin client created")

# admin_client.create_topics([NewTopic(name='test', num_partitions=1, replication_factor=1)])
# print("added topic(s)")

# producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, api_version=(0, 10, 1), value_serializer=str.encode, batch_size=0)
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
print("producer created")

# byteArray = bytearray("Test String", 'utf-8')
# print("bytearray created")

for i in range(10000):
    f = producer.send(KAFKA_TOPIC, value=b'test string')
    sleep(0.5)
    print("data sent {}".format(f.get(timeout=30)))
