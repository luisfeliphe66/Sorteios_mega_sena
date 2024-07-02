from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

# Função para ler os dados
def read_data(**kwargs):
    df = pd.read_csv('/mnt/data/base_mega_sena/data/base_mega_sena.csv')
    kwargs['ti'].xcom_push(key='dataframe', value=df)

# Função para filtrar os dados por período
def filter_data(start_date, end_date, **kwargs):
    df = kwargs['ti'].xcom_pull(key='dataframe', task_ids='read_data')
    df['data'] = pd.to_datetime(df['data'])
    filtered_df = df[(df['data'] >= start_date) & (df['data'] <= end_date)]
    kwargs['ti'].xcom_push(key='filtered_dataframe', value=filtered_df)

# Função para contar o número mais frequente e salvar o resultado em um arquivo CSV
def count_numbers(**kwargs):
    df = kwargs['ti'].xcom_pull(key='filtered_dataframe', task_ids='filter_data')
    most_common_number = df['bola'].value_counts().idxmax()
    kwargs['ti'].xcom_push(key='most_common_number', value=most_common_number)
    
    # Cria um DataFrame com o resultado
    result_df = pd.DataFrame({'most_common_number': [most_common_number]})
    
    # Define o caminho do arquivo
    export_dir = '/home/MegaSena/Resultado'
    result_csv_path = os.path.join(export_dir, 'most_common_number.csv')
    
    # Salva o DataFrame em um arquivo CSV
    result_df.to_csv(result_csv_path, index=False)
    print(f'O arquivo CSV com o resultado foi salvo em: {result_csv_path}')

# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definir o DAG
dag = DAG(
    'mega_sena',
    default_args=default_args,
    description='Análise da Mega Sena',
    schedule_interval=timedelta(days=1),
)

# Tasks
read_data_task = PythonOperator(
    task_id='read_data',
    python_callable=read_data,
    provide_context=True,
    dag=dag,
)

filter_data_task = PythonOperator(
    task_id='filter_data',
    python_callable=filter_data,
    provide_context=True,
    op_kwargs={'start_date': '2023-01-01', 'end_date': '2023-12-31'},
    dag=dag,
)

count_numbers_task = PythonOperator(
    task_id='count_numbers',
    python_callable=count_numbers,
    provide_context=True,
    dag=dag,
)

# Definir a ordem de execução
read_data_task >> filter_data_task >> count_numbers_task
