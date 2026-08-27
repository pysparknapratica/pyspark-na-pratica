from decimal import Decimal

from pyspark_na_pratica.quality.pedidos import separar_validos_invalidos
from pyspark_na_pratica.schemas.pedidos import PEDIDOS_SCHEMA


def test_separar_validos_invalidos(spark):
    dados = [
        ("P1", "C1", "AM", "PR1", "Mouse", 1, Decimal("40.00")),
        ("P2", "C2", "XX", "PR1", "Mouse", 1, Decimal("40.00")),
        ("P3", "C3", "PA", "PR1", "Mouse", 0, Decimal("40.00")),
    ]

    df = spark.createDataFrame(dados, PEDIDOS_SCHEMA)

    validos, invalidos = separar_validos_invalidos(df)

    assert validos.count() == 1
    assert invalidos.count() == 2

    motivos = {row["motivo_rejeicao"] for row in invalidos.collect()}
    assert motivos == {"UF_INVALIDA", "QUANTIDADE_INVALIDA"}
