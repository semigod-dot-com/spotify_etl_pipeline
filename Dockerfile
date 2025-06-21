FROM apache/airflow:2.8.1-python3.10

# Install dbt
RUN pip install dbt-core dbt-postgres

# Optional: install other dependencies like pandas, requests, etc.
# RUN pip install pandas requests

# Optional: copy dbt project inside container (you can also mount it with volume)
# COPY ./semi /opt/airflow/semi
