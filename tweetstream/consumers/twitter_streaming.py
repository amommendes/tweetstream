from tweetstream.utils.logger import Logger

logger = Logger()
logger.basicConfig()


class TwitterStreamingConsumer:
    """
    Consume data from Kafka using Spark Streaming Structured
    """

    def __init__(
        self,
        spark,
        topic="twitter",
        output_path="file:///tmp/consumer",
        checkpoint="/tmp/checkpoint",
        format="parquet",
        bootstrap_servers="localhost:9092",
    ):
        self.spark = spark
        self.output_path = output_path
        self.format = format
        self.bootstrap_servers = bootstrap_servers
        self.checkpoint = checkpoint
        self.topic = topic

    def start(self):
        """
        Reads streaming data from Kafka source and starts writing process.
        The process is triggered once, meaning that all available data will be processed and job finishes
        """
        logger.info("Creating read stream")
        tweets_df = (
            self.spark.readStream.format("kafka")
            .option("kafka.bootstrap.servers", self.bootstrap_servers)
            .option("startingOffsets", "earliest")
            .option("subscribe", self.topic)
            .load()
        )

        logger.info("Converting binary fields to string")
        tweets_df_cast = tweets_df.selectExpr(
            "CAST(value AS STRING) as value",
            "CAST(key AS STRING) as key",
            "`timestamp`",
        )
        logger.info("Writing stream")

        writer = (
            tweets_df_cast.writeStream.format(self.format)
            .option("path", self.output_path)
            .option("checkpointLocation", self.checkpoint)
            .trigger(once=True)
            .start()
        )

        logger.info(f"Writing status {writer.status}")
        writer.awaitTermination()
