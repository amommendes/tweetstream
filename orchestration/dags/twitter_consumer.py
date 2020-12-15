from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from tweetstream.clients.twitter import TwitterClient
from tweetstream.consumers.twitter import TwitterConsumer

default_args = {
    'owner': 'tweeetstream',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['tweetstream@team.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

hashtags = Variable.get("hashtags", ["#covid"])

def main():
    client = TwitterClient()
    consumer = TwitterConsumer(client=client, hashtags=hashtags)
    consumer.start()

dag = DAG(
    dag_id="twitter_consumer",
    default_args=default_args,
    description="Tweets Consumer",
    schedule_interval=timedelta(days=1)
)

start_job_task = PythonOperator(
    dag=dag,
    task_id="start_consumer",
    python_callable=main,
    execution_timeout=None,
)



