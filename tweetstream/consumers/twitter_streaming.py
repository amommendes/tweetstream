from tweetstream.utils.logger import Logger

logger = Logger()
logger.basicConfig()


class TwitterStreamingConsumer():

    def __init__(self, spark, output_path="file:///tmp/consumer", format="parquet", host="localhost", port="3333"):
        self.spark = spark
        self.output_path = output_path
        self.format = format
        self.host = host
        self.port = port

    def start(self):
        logger.info("Creating read stream")
        tweets_df = self.spark \
            .readStream \
            .format("socket") \
            .option("host", self.host) \
            .option("port", self.port) \
            .load()

        logger.info("Writing stream")
        tweets_df.writeStream. \
            format(self.format). \
            option("path", self.output_path). \
            option("checkpointLocation", self.output_path+"/checkpoint"). \
            trigger(processingTime='2 seconds'). \
            start()

