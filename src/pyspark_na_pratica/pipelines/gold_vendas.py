from pathlib import Path

from pyspark_na_pratica.session import create_spark_session
from pyspark_na_pratica.transforms.pedidos import kpis_por_estado


def main() -> None:
    spark = create_spark_session("GoldVendas")

    raiz = Path("data")
    df_silver = spark.read.parquet(str(raiz / "silver/pedidos"))

    df_gold = kpis_por_estado(df_silver)

    (
        df_gold
        .write
        .mode("overwrite")
        .parquet(str(raiz / "gold/vendas_por_estado"))
    )

    df_gold.orderBy("faturamento", ascending=False).show(truncate=False)
    spark.stop()


if __name__ == "__main__":
    main()
