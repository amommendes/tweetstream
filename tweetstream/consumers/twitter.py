from tweetstream.utils.logger import Logger
from tweetstream.sinks.socket_sink import SocketSink
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
        sink = SocketSink().get_sink()
        logger.info("Socket sink defiened")
        stream = Stream(self.client.auth, TwitterStreamListener(sink))
        stream.filter(track=self.hashtags)
