from decimal import Decimal

from pyspark_na_pratica.schemas.pedidos import PEDIDOS_SCHEMA
from pyspark_na_pratica.transforms.pedidos import padronizar_pedidos


def test_padronizar_estado(spark):
    dados = [
        ("P1", "C1", " am ", "PR1", "Mouse", 1, Decimal("40.00")),
    ]

    df = spark.createDataFrame(dados, PEDIDOS_SCHEMA)
    result = padronizar_pedidos(df).first()

    assert result["estado"] == "AM"
