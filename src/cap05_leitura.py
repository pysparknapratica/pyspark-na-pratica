from pyspark_na_pratica.session import create_spark_session

spark = create_spark_session("Cap05Leitura")

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("data/raw/pedidos.csv")
)
df.show(truncate=False)
df.printSchema()
spark.stop()
