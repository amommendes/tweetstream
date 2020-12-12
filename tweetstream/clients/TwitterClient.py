from tweepy import API, AppAuthHandler
from tweetstream.logger import Logger
from tweetstream.resources.credential_handler import CredentialHandler

logger = Logger("TwitterClient")

class TwitterClient():
    def __init__(self):
        self.auth = self.get_auth()

    @staticmethod
    def get_auth():
        handler = CredentialHandler()
        credentials = handler.get_credentials()
        return AppAuthHandler(
            consumer_key=credentials.API_KEY,
            consumer_secret=credentials.API_SECRET_KEY
    )

    def get_client(self):
        client = API(self.auth)
        return client
