from pyspark.sql.types import DecimalType, IntegerType, StringType, StructField, StructType

PRODUTOS_SCHEMA = StructType([
    StructField("produto_id", StringType(), False),
    StructField("descricao", StringType(), True),
    StructField("categoria", StringType(), True),
    StructField("preco", DecimalType(12, 2), True),
    StructField("estoque", IntegerType(), True),
])
