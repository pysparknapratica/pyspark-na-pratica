from pyspark.sql.types import (
    DecimalType,
    IntegerType,
    StringType,
    StructField,
    StructType,
)

PEDIDOS_SCHEMA = StructType([
    StructField("pedido_id", StringType(), False),
    StructField("cliente_id", StringType(), True),
    StructField("estado", StringType(), True),
    StructField("produto_id", StringType(), True),
    StructField("produto", StringType(), True),
    StructField("quantidade", IntegerType(), True),
    StructField("valor", DecimalType(12, 2), True),
])
