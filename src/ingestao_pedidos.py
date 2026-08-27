from pyspark_na_pratica.schemas.pedidos import PEDIDOS_SCHEMA
from pyspark_na_pratica.session import create_spark_session

spark = create_spark_session("IngestaoPedidos")

df_pedidos = (
    spark.read
    .option("header", True)
    .schema(PEDIDOS_SCHEMA)
    .csv("data/raw/pedidos.csv")
)

df_pedidos.show(truncate=False)
df_pedidos.printSchema()
print("Registros:", df_pedidos.count())
spark.stop()
