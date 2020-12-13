from tweetstream.consumers.twitter_streaming import TwitterStreamingConsumer
from tweetstream.clients.spark import SparkClient

def main():
    spark_client = SparkClient()
    spark = spark_client.get_session()
    consumer = TwitterStreamingConsumer(spark=spark)
    consumer.start()

if __name__ == "__main__":

    main()