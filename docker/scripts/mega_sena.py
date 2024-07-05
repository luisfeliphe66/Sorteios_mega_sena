from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
import zipfile
import os

from datetime import datetime
import pandas as pd

### Funções para PythonOperator

# Função para descompactar o arquivo ZIP
def unzip():
    filepath_zip = '/data/base_mega_sena.zip'
    folder_zip = '/data'
    filename_csv = 'base_mega_sena.csv'

    if zipfile.is_zipfile(filepath_zip):
        with zipfile.ZipFile(filepath_zip, 'r') as zip_ref:
            zip_ref.extract(filename_csv, path=folder_zip)
        print(f"Arquivo extraído para {folder_zip}")
    else:
        print(f"{filepath_zip} não é um arquivo ZIP válido.")

# Função para ler o arquivo CSV
def extract(**kwargs):
    df = pd.read_csv('/data/base_mega_sena.csv', encoding='ISO-8859-1', sep=';')
    
    print(df.head())
    
    return df

# Definir DAG
dag = DAG(
    'mega_sena',
    schedule_interval=None,
    start_date=datetime(2024, 7, 3),
    catchup=False
)

# Tarefa para descompactar o arquivo CSV
unzip_task = PythonOperator(
    task_id='unzip_task',
    python_callable=unzip,
    provide_context=True,
    dag=dag
)

# Tarefa para ler o arquivo CSV
extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract,
    provide_context=True,
    dag=dag
)

(unzip_task >> extract_task)