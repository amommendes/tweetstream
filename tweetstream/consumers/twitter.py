from tweetstream.utils.logger import Logger
from tweetstream.sinks.kafka_sink import KafkaSink
from tweetstream.consumers.twitter_listener import TwitterStreamListener
from tweepy import Stream

logger = Logger()
logger.basicConfig()

class TwitterConsumer():
    def __init__(self, client, hashtags=['#COVID']):
        self.client = client
        self.hashtags = hashtags

    def start(self):
        logger.info("Starting Consumer")
        sink = KafkaSink().get_sink()
        logger.info("Sink defined")
        stream = Stream(self.client.auth, TwitterStreamListener(sink))
        stream.filter(track=self.hashtags)
