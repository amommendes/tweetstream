import json


class CredentialHandler():
    def __init__(self, path="tweetstream/resources/api.json"):
        self.path = path

    @staticmethod
    def _read_credentials_file(path):
        with open(path) as file:
            data = json.load(file)
        return data

    def get_credentials(self):
        credentials = self._read_credentials_file(self.path)
        return credentials
