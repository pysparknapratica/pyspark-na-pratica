from pyspark_na_pratica.session import create_spark_session

spark = create_spark_session("SmokeSpark")
try:
    assert spark.version == "4.0.1", f"Spark inesperado: {spark.version}"
    assert spark.conf.get("spark.sql.session.timeZone") == "UTC"
    assert spark.range(100).count() == 100
    print(f"SPARK_SMOKE_OK version={spark.version} timezone=UTC count=100")
finally:
    spark.stop()
