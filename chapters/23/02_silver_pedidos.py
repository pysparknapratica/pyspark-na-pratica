from pyspark.sql import functions as F

catalog = "amazontech"
df = spark.table(f"{catalog}.bronze.pedidos")

df_silver = (
    df
    .withColumn("estado", F.upper(F.trim("estado")))
    .withColumn("quantidade", F.col("quantidade").cast("int"))
    .withColumn("valor", F.col("valor").cast("decimal(12,2)"))
)

df_validos = df_silver.filter(
    F.col("pedido_id").isNotNull()
    & (F.col("quantidade") > 0)
    & (F.col("valor") >= 0)
)

(
    df_validos.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable(f"{catalog}.silver.pedidos")
)
