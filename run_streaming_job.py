from tweetstream.consumers.twitter_streaming import TwitterStreamingConsumer
from tweetstream.clients.spark import SparkClient


def main():
    spark_client = SparkClient(
        session_config={
            "spark.jars": "/home/amomluiz/projects/tweetstream/libs/spark-sql-kafka-0-10_2.11-2.4.5.jar,"
            "/home/amomluiz/projects/tweetstream/libs/kafka-clients-2.4.0.jar",
            "failOnDataLoss": "false",
        }
    )
    spark = spark_client.get_session()
    consumer = TwitterStreamingConsumer(
        spark=spark,
        output_path="hdfs://hadoop:9000/twitter/consumer",
        checkpoint="hdfs://hadoop:9000/twitter/checkpoint",
    )
    consumer.start()


if __name__ == "__main__":

    main()
