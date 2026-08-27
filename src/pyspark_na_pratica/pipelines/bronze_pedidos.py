from pathlib import Path

from pyspark.sql import functions as F

from pyspark_na_pratica.schemas.pedidos import PEDIDOS_SCHEMA
from pyspark_na_pratica.session import create_spark_session


def main() -> None:
    spark = create_spark_session("BronzePedidos")

    raiz = Path("data")
    entrada = raiz / "raw/pedidos.csv"
    saida = raiz / "bronze/pedidos"

    df_raw = (
        spark.read
        .option("header", True)
        .schema(PEDIDOS_SCHEMA)
        .csv(str(entrada))
    )

    df_bronze = (
        df_raw
        .withColumn("_source_file", F.input_file_name())
        .withColumn("_ingestion_timestamp", F.current_timestamp())
        .withColumn("_source_system", F.lit("ARQUIVO_CSV"))
    )

    (
        df_bronze.write
        .mode("overwrite")
        .parquet(str(saida))
    )

    print("=== BRONZE ===")
    print(f"Registros ingeridos: {df_bronze.count():,}")
    print("Metadados técnicos:")
    print("- _source_file")
    print("- _ingestion_timestamp")
    print("- _source_system")

    spark.stop()


if __name__ == "__main__":
    main()
