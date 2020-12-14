from tweetstream.clients.twitter import TwitterClient
from tweetstream.consumers.twitter import TwitterConsumer


def main():
    client = TwitterClient()
    consumer = TwitterConsumer(client=client, hashtags=["#covid"])
    consumer.start()


if __name__ == "__main__":
    main()
