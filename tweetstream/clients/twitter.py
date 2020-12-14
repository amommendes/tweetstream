from tweepy import OAuthHandler
from tweetstream.utils.logger import Logger
from tweetstream.resources.credential_handler import CredentialHandler

logger = Logger()
logger.basicConfig()


class TwitterClient:
    """
    Constructs auth object used in the tweepy API/Streaming objects
    """

    def __init__(self):
        self.auth = self.get_auth()

    @staticmethod
    def get_auth():
        handler = CredentialHandler()
        credentials = handler.get_credentials()
        auth = OAuthHandler(
            consumer_key=credentials.get("API_KEY"),
            consumer_secret=credentials.get("API_SECRET_KEY"),
        )
        auth.set_access_token(
            key=credentials.get("ACCESS_TOKEN"),
            secret=credentials.get("ACCESS_TOKEN_SECRET"),
        )
        return auth
