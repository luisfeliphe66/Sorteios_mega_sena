from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from fpdf import FPDF
# import os

def extract_data(**kwargs):
    # Simulate extracting data from a source and storing it in a CSV file
    df = pd.read_csv('/data/base_mega_sena.csv')
    df.to_csv('/data/base_mega_sena_extracted.csv', index=False)

# def preprocess_data(**kwargs):
#     ti = kwargs['ti']
#     df = pd.read_csv('/opt/airflow/dags/titanic_extracted.csv')
    
#     df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
#     df['Age'] = df['Age'].fillna(df['Age'].median())
#     df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    
#     ti.xcom_push(key='preprocessed_data', value=df.to_dict())

# def analyze_sex_survivors(**kwargs):
#     ti = kwargs['ti']
#     df_dict = ti.xcom_pull(task_ids='preprocess_data', key='preprocessed_data')
#     df = pd.DataFrame.from_dict(df_dict)
    
#     sex_survivors = df[df['Survived'] == 1]['Sex'].value_counts().to_dict()
#     sex_survivors = {'Feminino' if k == 'female' else 'Masculino': v for k, v in sex_survivors.items()}
#     ti.xcom_push(key='sex_survivors', value=sex_survivors)

# def analyze_embarked_survivors(**kwargs):
#     ti = kwargs['ti']
#     df_dict = ti.xcom_pull(task_ids='preprocess_data', key='preprocessed_data')
#     df = pd.DataFrame.from_dict(df_dict)
    
#     embarked_survivors = df[df['Survived'] == 1]['Embarked'].value_counts().to_dict()
#     ti.xcom_push(key='embarked_survivors', value=embarked_survivors)

# def analyze_class_survivors(**kwargs):
#     ti = kwargs['ti']
#     df_dict = ti.xcom_pull(task_ids='preprocess_data', key='preprocessed_data')
#     df = pd.DataFrame.from_dict(df_dict)
    
#     class_survivors = df[df['Survived'] == 1]['Pclass'].value_counts().to_dict()
#     ti.xcom_push(key='class_survivors', value=class_survivors)

# def analyze_sex_class_survivors(**kwargs):
#     ti = kwargs['ti']
#     df_dict = ti.xcom_pull(task_ids='preprocess_data', key='preprocessed_data')
#     df = pd.DataFrame.from_dict(df_dict)
    
#     sex_class_survivors = df[df['Survived'] == 1].groupby(['Pclass', 'Sex']).size().to_dict()
#     sex_class_survivors = {f"{key[0]}_{key[1]}": value for key, value in sex_class_survivors.items()}
#     ti.xcom_push(key='sex_class_survivors', value=sex_class_survivors)

# def analyze_sex_embarked_survivors(**kwargs):
#     ti = kwargs['ti']
#     df_dict = ti.xcom_pull(task_ids='preprocess_data', key='preprocessed_data')
#     df = pd.DataFrame.from_dict(df_dict)
    
#     sex_embarked_survivors = df[df['Survived'] == 1].groupby(['Embarked', 'Sex']).size().to_dict()
#     sex_embarked_survivors = {f"{key[0]}_{key[1]}": value for key, value in sex_embarked_survivors.items()}
#     ti.xcom_push(key='sex_embarked_survivors', value=sex_embarked_survivors)

# def analyze_age_survivors(**kwargs):
#     ti = kwargs['ti']
#     df_dict = ti.xcom_pull(task_ids='preprocess_data', key='preprocessed_data')
#     df = pd.DataFrame.from_dict(df_dict)
    
#     age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
#     age_labels = ["0-10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80"]
#     df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)
    
#     age_survivors = df[df['Survived'] == 1]['AgeGroup'].value_counts().to_dict()
#     ti.xcom_push(key='age_survivors', value=age_survivors)

# def generate_report(**kwargs):
#     ti = kwargs['ti']
#     sex_survivors = ti.xcom_pull(task_ids='analyze_sex_survivors', key='sex_survivors')
#     embarked_survivors = ti.xcom_pull(task_ids='analyze_embarked_survivors', key='embarked_survivors')
#     class_survivors = ti.xcom_pull(task_ids='analyze_class_survivors', key='class_survivors')
#     sex_class_survivors = ti.xcom_pull(task_ids='analyze_sex_class_survivors', key='sex_class_survivors')
#     sex_embarked_survivors = ti.xcom_pull(task_ids='analyze_sex_embarked_survivors', key='sex_embarked_survivors')
#     age_survivors = ti.xcom_pull(task_ids='analyze_age_survivors', key='age_survivors')
    
#     pdf = FPDF()
#     pdf.add_page()
    
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt="Relatório de Análise dos Dados do Titanic", ln=True, align='C')
    
#     pdf.cell(200, 10, txt="Sobreviventes por Gênero:", ln=True)
#     for key, value in sex_survivors.items():
#         pdf.cell(200, 10, txt=f"    {key}: {value}", ln=True)
    
#     pdf.cell(200, 10, txt="Sobreviventes por Porto de Embarque:", ln=True)
#     portos = {'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'}
#     for key, value in embarked_survivors.items():
#         pdf.cell(200, 10, txt=f"    {portos[key]}: {value}", ln=True)
    
#     pdf.cell(200, 10, txt="Sobreviventes por Classe:", ln=True)
#     classes = {'1': 'Primeira Classe', '2': 'Segunda Classe', '3': 'Terceira Classe'}
#     for key, value in class_survivors.items():
#         pdf.cell(200, 10, txt=f"    {classes[str(key)]}: {value}", ln=True)
    
#     pdf.cell(200, 10, txt="Sobreviventes por Classe e Sexo:", ln=True)
#     for key, value in sex_class_survivors.items():
#         classe, sexo = key.split('_')
#         genero = 'Feminino' if sexo == 'female' else 'Masculino'
#         pdf.cell(200, 10, txt=f"    {classes[classe]} - {genero}: {value}", ln=True)
    
#     pdf.cell(200, 10, txt="Sobreviventes por Sexo e Porto de Embarque:", ln=True)
#     for key, value in sex_embarked_survivors.items():
#         porto, sexo = key.split('_')
#         genero = 'Feminino' if sexo == 'female' else 'Masculino'
#         pdf.cell(200, 10, txt=f"    {portos[porto]} - {genero}: {value}", ln=True)
    
#     pdf.cell(200, 10, txt="Sobreviventes por Faixa Etária:", ln=True)
#     for key, value in age_survivors.items():
#         faixa_etaria = f"Idade de {key.split('-')[0]} a {key.split('-')[1]} anos"
#         pdf.cell(200, 10, txt=f"    {faixa_etaria}: {value}", ln=True)
    
#     reports_dir = '/opt/airflow/dags/reports'
#     if not os.path.exists(reports_dir):
#         os.makedirs(reports_dir)
    
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x=list(sex_survivors.keys()), y=list(sex_survivors.values()))
#     plt.title('Sobreviventes por Gênero')
#     plt.xlabel('Gênero')
#     plt.ylabel('Quantidade de Sobreviventes')
#     plt.savefig(os.path.join(reports_dir, 'sobreviventes_por_genero.png'))
    
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x=[portos[key] for key in embarked_survivors.keys()], y=list(embarked_survivors.values()))
#     plt.title('Sobreviventes por Porto de Embarque')
#     plt.xlabel('Porto de Embarque')
#     plt.ylabel('Quantidade de Sobreviventes')
#     plt.savefig(os.path.join(reports_dir, 'sobreviventes_por_porto.png'))
    
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x=[classes[str(key)] for key in class_survivors.keys()], y=list(class_survivors.values()))
#     plt.title('Sobreviventes por Classe')
#     plt.xlabel('Classe')
#     plt.ylabel('Quantidade de Sobreviventes')
#     plt.savefig(os.path.join(reports_dir, 'sobreviventes_por_classe.png'))

#     # Gráfico para sobreviventes por classe e sexo
#     sex_class_df = pd.DataFrame.from_dict(sex_class_survivors, orient='index').reset_index()
#     sex_class_df[['Classe', 'Sexo']] = sex_class_df['index'].str.split('_', expand=True)
#     sex_class_df.columns = ['Index', 'Quantidade', 'Classe', 'Sexo']
#     sex_class_df['Classe'] = sex_class_df['Classe'].map(classes)
#     sex_class_df['Sexo'] = sex_class_df['Sexo'].map({'male': 'Masculino', 'female': 'Feminino'})
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x='Classe', y='Quantidade', hue='Sexo', data=sex_class_df)
#     plt.title('Sobreviventes por Classe e Sexo')
#     plt.xlabel('Classe')
#     plt.ylabel('Quantidade de Sobreviventes')
#     plt.legend(title='Sexo')
#     plt.savefig(os.path.join(reports_dir, 'sobreviventes_por_classe_sexo.png'))

#     # Gráfico para sobreviventes por sexo e porto de embarque
#     sex_embarked_df = pd.DataFrame.from_dict(sex_embarked_survivors, orient='index').reset_index()
#     sex_embarked_df[['Porto', 'Sexo']] = sex_embarked_df['index'].str.split('_', expand=True)
#     sex_embarked_df.columns = ['Index', 'Quantidade', 'Porto', 'Sexo']
#     sex_embarked_df['Porto'] = sex_embarked_df['Porto'].map(portos)
#     sex_embarked_df['Sexo'] = sex_embarked_df['Sexo'].map({'male': 'Masculino', 'female': 'Feminino'})
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x='Porto', y='Quantidade', hue='Sexo', data=sex_embarked_df)
#     plt.title('Sobreviventes por Sexo e Porto de Embarque')
#     plt.xlabel('Porto de Embarque')
#     plt.ylabel('Quantidade de Sobreviventes')
#     plt.legend(title='Sexo')
#     plt.savefig(os.path.join(reports_dir, 'sobreviventes_por_sexo_porto.png'))

#     # Gráfico para sobreviventes por faixa etária
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x=list(age_survivors.keys()), y=list(age_survivors.values()))
#     plt.title('Sobreviventes por Faixa Etária')
#     plt.xlabel('Faixa Etária')
#     plt.ylabel('Quantidade de Sobreviventes')
#     plt.savefig(os.path.join(reports_dir, 'sobreviventes_por_faixa_etaria.png'))

#     pdf.cell(200, 10, txt="Gráficos:", ln=True)
#     pdf.image(os.path.join(reports_dir, 'sobreviventes_por_genero.png'), x=10, y=None, w=180)
#     pdf.image(os.path.join(reports_dir, 'sobreviventes_por_porto.png'), x=10, y=None, w=180)
#     pdf.image(os.path.join(reports_dir, 'sobreviventes_por_classe.png'), x=10, y=None, w=180)
#     pdf.image(os.path.join(reports_dir, 'sobreviventes_por_classe_sexo.png'), x=10, y=None, w=180)
#     pdf.image(os.path.join(reports_dir, 'sobreviventes_por_sexo_porto.png'), x=10, y=None, w=180)
#     pdf.image(os.path.join(reports_dir, 'sobreviventes_por_faixa_etaria.png'), x=10, y=None, w=180)

#     pdf.output('/opt/airflow/dags/reports/relatorio_titanic.pdf')

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
}

dag = DAG(
    'mega_sena_analysis',
    default_args=default_args,
    description='Análise dos dados do Mega Sena',
    schedule_interval=None,
)

extract_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

# preprocess_data_task = PythonOperator(
#     task_id='preprocess_data',
#     python_callable=preprocess_data,
#     dag=dag,
# )

# analyze_sex_survivors_task = PythonOperator(
#     task_id='analyze_sex_survivors',
#     python_callable=analyze_sex_survivors,
#     dag=dag,
# )

# analyze_embarked_survivors_task = PythonOperator(
#     task_id='analyze_embarked_survivors',
#     python_callable=analyze_embarked_survivors,
#     dag=dag,
# )

# analyze_class_survivors_task = PythonOperator(
#     task_id='analyze_class_survivors',
#     python_callable=analyze_class_survivors,
#     dag=dag,
# )

# analyze_sex_class_survivors_task = PythonOperator(
#     task_id='analyze_sex_class_survivors',
#     python_callable=analyze_sex_class_survivors,
#     dag=dag,
# )

# analyze_sex_embarked_survivors_task = PythonOperator(
#     task_id='analyze_sex_embarked_survivors',
#     python_callable=analyze_sex_embarked_survivors,
#     dag=dag,
# )

# analyze_age_survivors_task = PythonOperator(
#     task_id='analyze_age_survivors',
#     python_callable=analyze_age_survivors,
#     dag=dag,
# )

# generate_report_task = PythonOperator(
#     task_id='generate_report',
#     python_callable=generate_report,
#     dag=dag,
# )

extract_data_task 
# >> preprocess_data_task
# preprocess_data_task >> [analyze_sex_survivors_task, analyze_embarked_survivors_task, analyze_class_survivors_task, analyze_sex_class_survivors_task, analyze_sex_embarked_survivors_task, analyze_age_survivors_task]
# [analyze_sex_survivors_task, analyze_embarked_survivors_task, analyze_class_survivors_task, analyze_sex_class_survivors_task, analyze_sex_embarked_survivors_task, analyze_age_survivors_task] >> generate_report_task