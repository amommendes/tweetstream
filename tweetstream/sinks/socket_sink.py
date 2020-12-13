import socket
from threading import Thread
from tweetstream.utils.logger import Logger

logger = Logger()
logger.basicConfig()


class SocketSink():
    def __init__(self, host_bind='localhost', host_port=3333):
        self.host = host_bind
        self.port = host_port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _setup_server(self):
        logger.info("Setting up socket sink")
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(5)
        logger.info(f"{self.host} listening on port: {self.port}")
        connection, address = self.socket_server.accept()
        return connection

    def get_sink(self):
        sink = self._setup_server()
        logger.info("Accepting socket messages")
        return sink

