import pytest
from tweetstream.resources.credential_handler import CredentialHandler

@pytest.fixture
def credentials_handler():
    credentials_handler = CredentialHandler()
    return credentials_handler
