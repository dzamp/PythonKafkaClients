import time
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import avro.schema




class Messenger(object):

    def __init__(self):
        pass

    def get_message(self, timestamp):
        pass



class AvroMessenger(Messenger):

    def get_message(self):
        example_time = int(round(time.time() * 1000))  # alert_start_time

        message = {

            "alert_id": 4,
            "alert_level": "LOW",
            "alert_title": "Warning",
            "alert_text": "This is a warning",
            "alert_category": "RISK",
            "alert_start_time": example_time,
            "alert_end_time": example_time,
            "alert_status": "ALERT_ACTIVE",
            "tracked_entity_id": 2,
            "latitude": 37.983810,
            "longitude": 23.727539,
            "time": example_time

        }
        print("Message: {}".format(message))

        return message



def run( messenger):
    """Produce messages according to the specified Avro schema"""
    value_schema = avro.schema.Parse(open("schemas/Alert.avsc","rb").read())
    conf = {'bootstrap.servers': "temple.di.uoa.gr:9092",
            'schema.registry.url': "http://temple.di.uoa.gr:8081"}
    avro_producer = AvroProducer(conf, default_value_schema=value_schema)

    while True:


        # Assemble avro-formatted message filled with generated data
        message = messenger.get_message()

        # Publish the message under the specified topic on the message bus
        avro_producer.produce(topic="FusionAlert", value=message)

        # Flush the buffer
        avro_producer.flush()

        # Wait a second
        time.sleep(1.0 / 1.0)


if __name__ == "__main__":

    messenger = AvroMessenger()
    run( messenger)
  
