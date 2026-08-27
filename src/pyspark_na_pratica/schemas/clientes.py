from pyspark.sql.types import BooleanType, StringType, StructField, StructType

CLIENTES_SCHEMA = StructType([
    StructField("cliente_id", StringType(), False),
    StructField("nome", StringType(), True),
    StructField("estado", StringType(), True),
    StructField("ativo", BooleanType(), True),
])
