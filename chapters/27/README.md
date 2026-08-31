# Capítulo 27 — Structured Streaming

> O conteúdo completo deste capítulo faz parte da edição comercial do livro **PySpark na Prática — Engenharia de Dados do Zero à Produção**. Este diretório contém orientações técnicas complementares do laboratório.

## Objetivo

O laboratório demonstra o uso de Structured Streaming com arquivos JSON, checkpoint e gravação contínua em Parquet.

## Caminhos utilizados no livro

Diretório de entrada:

`data/stream/eventos`

Checkpoint da consulta:

`checkpoints/eventos`

Saída da camada Bronze:

`data/bronze/eventos`

Fluxo do laboratório:

```text
data/stream/eventos
        |
        v
Structured Streaming
        |
        +---- checkpoint ----> checkpoints/eventos
        |
        v
data/bronze/eventos
```

## Exemplo utilizado

```python
df_stream = (
    spark.readStream
    .format("json")
    .schema(EVENTOS_SCHEMA)
    .load("data/stream/eventos")
)

query = (
    df_stream
    .writeStream
    .format("parquet")
    .option(
        "checkpointLocation",
        "checkpoints/eventos"
    )
    .option(
        "path",
        "data/bronze/eventos"
    )
    .start()
)

query.awaitTermination()
```

## Como executar o laboratório

1. Crie ou utilize `data/stream/eventos`.
2. Inicie a query de streaming.
3. Adicione arquivos JSON ao diretório de entrada gradualmente.
4. Observe os novos micro-batches.
5. Inspecione `data/bronze/eventos`.
6. Observe o conteúdo criado em `checkpoints/eventos`.

Os arquivos de checkpoint são artefatos de execução e não devem ser editados manualmente.

## Observação

O diretório `data/checkpoints` existente na estrutura geral do repositório é reservado para outros experimentos e organizações de dados.

O laboratório específico deste capítulo utiliza:

`checkpoints/eventos`

Isso mantém o companion repository alinhado exatamente ao caminho apresentado no livro.
