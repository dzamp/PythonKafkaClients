import time
import uuid
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
        start_time = int(round(time.time() * 1000)) # alert_start_time

        message = {

            "alert_id": str(uuid.uuid4()),
            "alert_level": "LOW",
            "alert_title": "Warning",
            "alert_text": "This is a warning",
            "alert_start_time": start_time,
            "alert_end_time":  start_time + 5000, # 5 seconds later
            "alert_status": "ALERT_ACTIVE",
            "tracked_entity_id": 2,
            "latitude": 37.983810,
            "longitude": 23.727539,
            "time": int(round(time.time() * 1000)), #now
            "ciram_details": {
              "threat" : "LOW",
              "impact" : "MEDIUM",
              "vulnerability" : "LOW"
            },
        }
        print("Message: {}".format(message))

        return message




def run( messenger):
    """Produce messages according to the specified Avro schema"""
    value_schema = avro.schema.Parse(open("schemas/RiskAlert.avsc","rb").read())
    conf = {'bootstrap.servers': "temple.di.uoa.gr:9092",
            'schema.registry.url': "http://temple.di.uoa.gr:8081"}
    avro_producer = AvroProducer(conf, default_value_schema=value_schema)
    while True:


        # Assemble avro-formatted message filled with generated data
        message = messenger.get_message()

        # Publish the message under the specified topic on the message bus
        avro_producer.produce(topic="RiskAlert", value=message)

        # Flush the buffer
        avro_producer.flush()

        # Wait a second
        time.sleep(1.0 / 1.0)


if __name__ == "__main__":

    messenger = AvroMessenger()
    run( messenger)
  
