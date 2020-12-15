from tweepy.streaming import StreamListener
import json
from tweetstream.utils.logger import Logger

logger = Logger()
logger.basicConfig()


class TwitterStreamListener(StreamListener):
    """
    Twitter Listener for streaming
    See: http://docs.tweepy.org/en/latest/streaming_how_to.html#step-1-creating-a-streamlistener
    """

    def __init__(self, sink):
        self.sink = sink

    def on_data(self, raw_data):
        try:
            raw_data = json.loads(raw_data)
            logger.info(f"Twitter Listener sending data to sink")
            self.sink.send("twitter", raw_data)
            return True

        except BaseException as error:
            logger.error(f"Error while getting data from Twitter: {error}")
            return True

    def on_error(self, status):
        logger.error(f"Error in Twitter API. Status = {status}")
        return True
