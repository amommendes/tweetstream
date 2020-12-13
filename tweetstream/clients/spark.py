from pyspark.sql import SparkSession
import logging
from tweetstream.utils.logger import Logger
import findspark

logger = Logger()
logger.basicConfig()
pyspark_log = logging.getLogger('pyspark')
pyspark_log.setLevel(logging.ERROR)

class SparkClient:
    def __init__(self, session_params=None):
        self.session = None
        self.session_params = session_params

    def get_session(self):
        findspark.init()
        if not self.session:
            session_builder = SparkSession.builder
            if self.session_params:
                for param, val in self.session_params.items():
                    session_builder.config(param, val)
            self.session = session_builder.getOrCreate()
        return self.session
