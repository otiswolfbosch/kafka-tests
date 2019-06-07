from confluent_kafka import Producer

KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "test-otis"

p = Producer({'bootstrap.servers': KAFKA_SERVER})
print("producer created")

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

p.poll(0)
print("poll called")

p.produce(KAFKA_TOPIC, "hello world", callback=delivery_report)
print("data produced")

p.flush()
print("flush completed")