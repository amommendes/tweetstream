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
            has_extended_tweet = "extended_tweet" in raw_data
            tweet = raw_data.get("text", {})
            if has_extended_tweet:
                tweet = raw_data.get("extended_tweet").get("full_text")
            logger.info(f"Twitter Listener sending data to sink")
            self.sink.send("twitter", json.dumps(tweet).encode("utf-8"))
            return True

        except BaseException as error:
            logger.error(f"Error while getting data from Twitter: {error}")
            return True

    def on_error(self, status):
        logger.error(f"Error in Twitter API. Status = {status}")
        return True
