import pytest
from tweetstream.clients.twitter import TwitterClient


@pytest.fixture
def client():
    client = TwitterClient()
    return client
