# Sorteios Mega Sena - Airflow

`Integrantes:`
- Luis Feliphe Da Silva Batista.
- Cesar Oliveira.
- José Fernando Brandão Conte.

# Analise de dados:
- Vamos analisar os dados da Mega-Sena neste notebook.
- base_mega_sena.zip contém a base de dados do SUS/MegaSena de 2023.

# Código-fonte
- `mega_sena.py` é o arquivo principal desenvolvido em python com a biblioteca airflow para criação do fluxo ETL.

# ETL
- zip_task: Descompactar o arquivo `base_mega_sena.zip` em `base_mega_sena.csv` para processamento dos dados;
- extract_task: Extrair os dados para um data frame;
```bash

# Comandos para iniciar a execução do projeto

# Subir os containers
make up

# Derrubar os containers
make down

# Compilar código-fonte
make deploy
