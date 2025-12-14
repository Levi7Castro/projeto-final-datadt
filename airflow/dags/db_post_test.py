from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime

def testa_postgres():
    hook = PostgresHook(postgres_conn_id="postgres_origem")
    df = hook.get_pandas_df("SELECT 1")
    print(df)

with DAG(
    dag_id="teste_postgres_conn",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
):
    PythonOperator(
        task_id="testar",
        python_callable=testa_postgres
    )
