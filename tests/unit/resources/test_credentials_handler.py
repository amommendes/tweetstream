import pytest
from unittest.mock import patch
from tweetstream.resources.credential_handler import CredentialHandler

class TestCredentialsHandler:

    @pytest.mark.parametrize(
        "path",
        ["tweetstream/resources/api.json"]
    )
    def test__read_credentials_file(self, path, credentials_handler):

        # arrange & act
        credentials_object = credentials_handler._read_credentials_file(path)

        #assert
        assert "API_KEY" in credentials_object
        assert "API_SECRET_KEY" in credentials_object
        assert "TOKEN" in credentials_object

    @patch.object(CredentialHandler, '_read_credentials_file',
                  return_value={
                      "API_KEY": "user",
                      "API_SECRET_KEY": "secret_key",
                      "TOKEN": "user_token"
                  })
    def test_get_credentials(self, credentials_handler_mocked, credentials_handler):

        # arrange & act
        credentials = credentials_handler.get_credentials()

        #assert
        credentials_handler._read_credentials_file.assert_called_once()
        assert "API_KEY" in credentials
        assert "API_SECRET_KEY" in credentials
        assert "TOKEN" in credentials
