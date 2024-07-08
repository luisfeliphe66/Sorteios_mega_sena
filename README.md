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
-`caminho_arquivo_zip`, `diretorio_destino`:  Carregando os dados do AIRFLOW.
- `delete_coluna_ordem`: Importações e Definição da Função
- `contagem_bolas`, `contagem_bolas.plot`:  Gráfico de Barras com as Contagens nos Concursos.
- `ultimos_numeros`, `ultimos_numeros.plot`:  Gráfico de Barras com os Números Mais Sorteados.
- `sorted_group`: Exibi os Números da Sorte.

# Código-fonte
- `Sorteios_mega_sena.ipynb` é o arquivo principal desenvolvido em python com a biblioteca spark para processamento de dados.


Referências
Documentação para ambiente Sparkhttps://spark.apache.org/docs/latest/ e Docker
