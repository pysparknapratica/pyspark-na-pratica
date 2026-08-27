from pyspark.sql import functions as F

# Ajuste catalog/schema conforme as permissões do seu workspace.
catalog = "amazontech"
source = "/Volumes/amazontech/bronze/landing/pedidos.csv"

df_raw = spark.read.option("header", True).csv(source)

df_bronze = (
    df_raw
    .withColumn("_ingestion_timestamp", F.current_timestamp())
    .withColumn("_source_file", F.input_file_name())
)

(
    df_bronze.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable(f"{catalog}.bronze.pedidos")
)
