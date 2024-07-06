from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import zipfile
import pandas as pd
from datetime import datetime
import os

### Funções para PythonOperator

# Função para compactar o arquivo CSV em ZIP
def zip_csv():
    csv_filepath = '/data/base_mega_sena.csv'
    zip_filepath = '/data/base_mega_sena.zip'

    with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(csv_filepath, os.path.basename(csv_filepath))

    # Alterar permissões do arquivo ZIP para o usuário
    os.chmod(zip_filepath, 0o666)
    os.chown(zip_filepath, os.getuid(), os.getgid())

    print(f"Arquivo CSV comprimido em {zip_filepath} com permissões para o usuário 'luis'.")

# Função para ler o arquivo ZIP e extrair o dataframe
def extract(**kwargs):
    zip_filepath = '/data/base_mega_sena.zip'

    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        with zip_ref.open('base_mega_sena.csv') as csv_file:
            df = pd.read_csv(csv_file, encoding='ISO-8859-1', sep=';')

    # Enviar dataframe para XCom
    kwargs['ti'].xcom_push(key='dataframe', value=df.to_dict())
    return df

# Definir DAG
dag = DAG(
    'mega_sena',
    schedule_interval=None,
    start_date=datetime(2024, 7, 3),
    catchup=False
)

# Tarefa para compactar o arquivo CSV em ZIP
zip_task = PythonOperator(
    task_id='zip_task',
    python_callable=zip_csv,
    dag=dag
)

# Tarefa para ler o arquivo ZIP e extrair o dataframe
extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract,
    provide_context=True,
    dag=dag
)

(zip_task >> extract_task )
