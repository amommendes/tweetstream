import json
from tweetstream.utils.logger import Logger
from kafka import KafkaProducer

logger = Logger()
logger.basicConfig()


class KafkaSink:
    """
    Sinks tweets into topic using Kafka producer
    """

    def __init__(self, bootstrap_servers="kafka:9092"):
        self.bootstrap_servers = bootstrap_servers

    def get_sink(self):
        logger.info("Configuring Kafka sink")
        producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            api_version=(0, 10, 0),
            value_serializer=lambda message: json.dumps(message).encode("utf-8"),
        )
        return producer
