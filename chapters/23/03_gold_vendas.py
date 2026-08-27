from pyspark.sql import functions as F

catalog = "amazontech"
df = spark.table(f"{catalog}.silver.pedidos")

df_gold = (
    df.groupBy("estado")
    .agg(
        F.sum("valor").alias("faturamento"),
        F.countDistinct("pedido_id").alias("qtd_pedidos"),
        F.avg("valor").alias("ticket_medio"),
    )
)

(
    df_gold.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable(f"{catalog}.gold.vendas_por_estado")
)
