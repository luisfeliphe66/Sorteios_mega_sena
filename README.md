# Sorteios Mega Sena - Spark

`Integrantes:`
- Luis Feliphe Da Silva Batista.
- Cesar Oliveira.
- José Fernando Brandão Conte.

# Analise de dados:
- Vamos analisar os dados da Mega-Sena neste notebook.
- `base_mega_sena.zip` contém a base de dados do SUS/MegaSena de 2022.

# ETL:
- `Make`: Automação para estrutura do projeto.
- `caminho_arquivo_zip`, `diretorio_destino`:  Carregando os dados do AIRFLOW.
- `delete_coluna_ordem`: Importações e Definição da Função
- `contagem_bolas`, `contagem_bolas.plot`:  Gráfico de Barras com as Contagens nos Concursos.
- `sorted_group`: Exibi os Números da Sorte.
- `ultimos_numeros`, `ultimos_numeros.plot`:  Gráfico de Barras com os Números Mais Sorteados.

# Código-fonte
- `Sorteios_mega_sena.ipynb` é o arquivo principal desenvolvido em python com a biblioteca spark para processamento de dados.


# Referências
- Documentação para ambiente [Spark](https://spark.apache.org/docs/latest/)
- base_mega_sena.zip contém a base de dados do SUS/MegaSena de 2023.

# Sorteios Mega Sena - Airflow

# Código-fonte
- `mega_sena.py` é o arquivo principal desenvolvido em python com a biblioteca airflow para criação do fluxo ETL.

# ETL
- `extract_task`: Extrair os dados para um data frame;
- `zip_task`: Compactar o arquivo `base_mega_sena.cvs` em `base_mega_sena.zip` para processamento dos dados;
- `Make`: Automação para estrutura do projeto.

```bash
* MAKE

# Comandos para iniciar a execução do projeto

# Subir os containers
make up

# Derrubar os containers
make down

# Compilar código-fonte
make deploy

```
# Referências
- Documentação para ambiente [Airflow](https://airflow.apache.org/docs/)
 e [Docker](https://docs.docker.com/reference/)
