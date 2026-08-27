from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession


def create_delta_spark_session(
    app_name: str,
    master: str = "local[*]",
) -> SparkSession:
    builder = (
        SparkSession.builder
        .appName(app_name)
        .master(master)
        .config(
            "spark.sql.extensions",
            "io.delta.sql.DeltaSparkSessionExtension",
        )
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        .config("spark.sql.session.timeZone", "UTC")
    )

    return configure_spark_with_delta_pip(builder).getOrCreate()
