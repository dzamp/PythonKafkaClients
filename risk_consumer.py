from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError


c = AvroConsumer({
    'bootstrap.servers': "temple.di.uoa.gr:9092",
    'group.id': 'groupid',
    'schema.registry.url': "http://temple.di.uoa.gr:8081",
    'auto.offset.reset':'latest'})

c.subscribe(["RiskAlert"])

while True:
    try:
        msg = c.poll(10)

    except SerializerError as e:
        print("Message deserialization failed for {}: {}".format(msg, e))
        break

    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    print(msg.value())

    print(msg.topic())
    # print(ast.literal_eval(json.dumps(msg.value())))

c.close()
