from decimal import Decimal

from pyspark.sql import functions as F

from pyspark_na_pratica.schemas.pedidos import PEDIDOS_SCHEMA


def test_bronze_adiciona_metadados(spark):
    dados = [
        (
            "P1",
            "C1",
            "AM",
            "PR1",
            "Mouse",
            1,
            Decimal("40.00"),
        )
    ]

    df = spark.createDataFrame(dados, PEDIDOS_SCHEMA)

    resultado = (
        df
        .withColumn("_source_file", F.lit("pedidos.csv"))
        .withColumn("_ingestion_timestamp", F.current_timestamp())
        .withColumn("_source_system", F.lit("ARQUIVO_CSV"))
    )

    assert resultado.count() == 1
    assert "_source_file" in resultado.columns
    assert "_ingestion_timestamp" in resultado.columns
    assert "_source_system" in resultado.columns
