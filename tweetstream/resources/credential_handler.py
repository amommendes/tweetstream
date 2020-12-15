import json
import os

class CredentialHandler:
    """
    Simple handler to read credential files
    """
    def __init__(self, path=None):
        self.default_path = os.path.abspath(".") + "/dags/tweetstream/resources/api.json"
        self.path = self.default_path if path is None else path

    @staticmethod
    def _read_credentials_file(path):
        with open(path) as file:
            data = json.load(file)
        return data

    def get_credentials(self):
        credentials = self._read_credentials_file(self.path)
        return credentials
