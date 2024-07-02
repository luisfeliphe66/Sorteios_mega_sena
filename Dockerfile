# Usando a imagem base do Bitnami Airflow
FROM bitnami/airflow:2

# Definindo variáveis de ambiente
ENV AIRFLOW_DATABASE_NAME=bitnami_airflow \
    AIRFLOW_DATABASE_USERNAME=bn_airflow \
    AIRFLOW_DATABASE_PASSWORD=bitnami1 \
    AIRFLOW_EXECUTOR=CeleryExecutor

# Expondo a porta 8080 para o webserver do Airflow
EXPOSE 8080

# Comando para iniciar o servidor do Airflow
CMD ["airflow", "webserver"]