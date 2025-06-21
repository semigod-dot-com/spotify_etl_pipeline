from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "semigod",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="semigod_pipeline",
    default_args=default_args,
    description="Full pipeline: Extract → Ingest → dbt run → dbt test",
    schedule_interval="0 0 * * *",  # Daily at midnight
    start_date=datetime(2024, 6, 15),
    catchup=False,
    tags=["spotify", "dbt", "pipeline"]
) as dag:

    # Step 1: Run extraction.py
    extract_task = BashOperator(
        task_id="extract_spotify_data",
        bash_command="""
        set -e
        cd /opt/airflow/extraction_scripts
        python spotify_extraction.py
        """,
    )

    # Step 2: Run ingestion.py
    ingest_task = BashOperator(
        task_id="ingest_to_postgres",
        bash_command="""
        set -e
        cd /opt/airflow/extraction_scripts
        python spotify_ingestion.py
        """,
    )

    # Step 3: Run dbt models
    dbt_run = BashOperator(
        task_id="run_dbt_models",
        bash_command="""
        set -e
        cd /opt/airflow/semi
        dbt run --profiles-dir . --target dev
        """,
    )

    # Step 4: Test dbt models
    dbt_test = BashOperator(
        task_id="run_dbt_tests",
        bash_command="""
        set -e
        cd /opt/airflow/semi
        dbt test --profiles-dir . --target dev
        """,
    )

    # Define pipeline flow
    extract_task >> ingest_task >> dbt_run >> dbt_test
