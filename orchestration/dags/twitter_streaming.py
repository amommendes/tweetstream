from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from tweetstream.consumers.twitter_streaming import TwitterStreamingConsumer
from tweetstream.clients.spark import SparkClient

default_args = {
    "owner": "tweeetstream",
    "depends_on_past": False,
    "start_date": days_ago(1),
    "email": ["tweetstream@team.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def main():
    spark_client = SparkClient(
        session_config={
            "spark.jars": "/usr/local/airflow/dags/tweetstream/libs/spark-sql-kafka-0-10_2.12-3.0.1.jar,"
            "/usr/local/airflow/dags/tweetstream/libs/kafka-clients-2.5.0.jar,"
            "/usr/local/airflow/dags/tweetstream/libs/spark-token-provider-kafka-0-10_2.12-3.0.1.jar,"
            "/usr/local/airflow/dags/tweetstream/libs/commons-pool2-2.8.0.jar",
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


dag = DAG(
    dag_id="twitter_streaming",
    default_args=default_args,
    description="Tweets Streaming Consumer",
    schedule_interval=timedelta(days=1),
)

start_job_task = PythonOperator(
    dag=dag,
    task_id="start_streaming",
    python_callable=main,
    execution_timeout=None,
)
