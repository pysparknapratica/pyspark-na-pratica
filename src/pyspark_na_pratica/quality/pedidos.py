from pyspark.sql import Column, DataFrame
from pyspark.sql import functions as F

UFS_VALIDAS = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",
    "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
    "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO",
]


def condicao_pedido_valido() -> Column:
    return (
        F.col("pedido_id").isNotNull()
        & F.col("estado").isin(UFS_VALIDAS)
        & (F.col("quantidade") > 0)
        & (F.col("valor") >= 0)
    )


def separar_validos_invalidos(df: DataFrame) -> tuple[DataFrame, DataFrame]:
    condicao = condicao_pedido_valido()

    validos = df.filter(condicao)

    invalidos = (
        df
        .filter(~condicao)
        .withColumn(
            "motivo_rejeicao",
            F.when(F.col("pedido_id").isNull(), F.lit("PEDIDO_ID_NULO"))
            .when(~F.col("estado").isin(UFS_VALIDAS), F.lit("UF_INVALIDA"))
            .when(F.col("quantidade") <= 0, F.lit("QUANTIDADE_INVALIDA"))
            .otherwise(F.lit("VALOR_INVALIDO")),
        )
    )

    return validos, invalidos
