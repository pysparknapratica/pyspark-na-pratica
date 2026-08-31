# Capítulo 23 — Databricks na Prática

> O conteúdo completo deste capítulo faz parte da edição comercial do livro. Este diretório contém materiais técnicos complementares do laboratório Databricks.

## Objetivo

Implementar a AmazonTech Commerce no Databricks usando:

- notebook/script PySpark;
- Unity Catalog;
- Catalog / Schema / Table;
- Volume;
- Delta Lake;
- Bronze / Silver / Gold;
- Lakeflow Jobs.

> Os exercícios consideram Databricks Free Edition para aprendizagem. Recursos corporativos podem exigir outro tipo de workspace/conta.

## Dataset utilizado

O laboratório utiliza o arquivo sintético:

`data/raw/pedidos.csv`

Esse arquivo já está disponível neste repositório.

No Databricks, faça upload do arquivo para:

`/Volumes/amazontech/bronze/landing/pedidos.csv`

O script `01_bronze_pedidos.py` espera encontrar o arquivo exatamente nesse caminho.

## Preparando o Volume

No ambiente descrito no livro, o Volume segue a convenção:

`/Volumes/<catalog>/<schema>/<volume>/`

Exemplo utilizado:

`/Volumes/amazontech/bronze/landing/`

Depois do upload, confirme que o arquivo está disponível como:

`/Volumes/amazontech/bronze/landing/pedidos.csv`

## Ordem de execução

Execute os materiais nesta ordem:

1. `01_bronze_pedidos.py`
2. `02_silver_pedidos.py`
3. `03_gold_vendas.py`

Fluxo esperado:

`pedidos.csv → Bronze → Silver → Gold`

O primeiro script lê o CSV do Volume e cria `amazontech.bronze.pedidos`.

O segundo aplica tipagem e regras de qualidade e cria `amazontech.silver.pedidos`.

O terceiro agrega os dados e cria `amazontech.gold.vendas_por_estado`.

## Observação sobre notebooks

Os arquivos `.py` deste diretório podem ser usados como referência para criar/importar notebooks ou tarefas no Databricks. O importante é preservar a ordem Bronze → Silver → Gold descrita no capítulo.

## Arquivos deste capítulo

- `01_bronze_pedidos.py` — ingestão e camada Bronze;
- `02_silver_pedidos.py` — tratamento, tipagem e camada Silver;
- `03_gold_vendas.py` — agregações e camada Gold.

Assim, o leitor consegue reproduzir o laboratório sem precisar deduzir qual dataset utilizar ou onde carregá-lo.
