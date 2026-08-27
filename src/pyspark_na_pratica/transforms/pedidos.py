from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def padronizar_pedidos(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn("estado", F.upper(F.trim(F.col("estado"))))
        .withColumn("produto", F.trim(F.col("produto")))
        .withColumn("quantidade", F.col("quantidade").cast("int"))
    )


def selecionar_colunas_silver(df: DataFrame) -> DataFrame:
    return df.select(
        "pedido_id",
        "cliente_id",
        "estado",
        "produto_id",
        "produto",
        "quantidade",
        "valor",
    )


def kpis_por_estado(df: DataFrame) -> DataFrame:
    return (
        df
        .groupBy("estado")
        .agg(
            F.sum("valor").alias("faturamento"),
            F.countDistinct("pedido_id").alias("qtd_pedidos"),
            F.avg("valor").alias("ticket_medio"),
        )
    )
