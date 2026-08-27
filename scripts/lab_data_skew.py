from pyspark.sql import functions as F

from pyspark_na_pratica.session import create_spark_session

spark = create_spark_session("LabDataSkew")
try:
    df_skew = (
        spark.range(0, 1_000_000)
        .withColumn(
            "chave",
            F.when(F.col("id") < 900_000, F.lit("HOT_KEY"))
            .otherwise(F.concat(F.lit("K_"), F.col("id"))),
        )
    )

    counts = (
        df_skew
        .groupBy("chave")
        .count()
        .orderBy(F.desc("count"))
    )

    first = counts.first()
    assert first["chave"] == "HOT_KEY"
    assert first["count"] == 900_000
    print("DATA_SKEW_SMOKE_OK hot_key=900000 total=1000000 pct=90%")
finally:
    spark.stop()
