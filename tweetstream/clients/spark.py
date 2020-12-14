from pyspark.sql import SparkSession
import logging
from tweetstream.utils.logger import Logger
import findspark

logger = Logger()
logger.basicConfig()

class SparkClient:
    def __init__(self, session_config=None):
        self.spark_session = None
        self.session_config = session_config

    def get_session(self):
        findspark.init()
        if not self.spark_session:
            session_builder = SparkSession.builder
            if self.session_config:
                for param, val in self.session_config.items():
                    session_builder.config(param, val)
            self.spark_session = session_builder.getOrCreate()
        return self.spark_session
