from tweetstream.utils.logger import Logger

logger = Logger()
logger.basicConfig()


class TwitterStreamingConsumer():

    def __init__(self, spark, output_path="file:///tmp/consumer", format="parquet", host="localhost", port="9092"):
        self.spark = spark
        self.output_path = output_path
        self.format = format
        self.host = host
        self.port = port

    def start(self):
        logger.info("Creating read stream")
        tweets_df = self.spark \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", ":".join([self.host, self.port])) \
            .option("startingOffsets", "earliest") \
            .option("subscribe", "twitter") \
            .load()

        logger.info("Converting value")
        tweets_df_cast = tweets_df.selectExpr(
            "CAST(value AS STRING) as value",
            " CAST(key AS STRING) as key",
            "topic",
            "`timestamp`"
        )
        logger.info("Writing stream")

        writer = tweets_df_cast.\
            writeStream. \
            format(self.format). \
            option("path", self.output_path). \
            option("checkpointLocation", "/tmp/checkpoint"). \
            trigger(processingTime='15 seconds'). \
            start()

        logger.info(f"Writing status {writer.status}")
        writer.awaitTermination()

