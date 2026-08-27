from pyspark.sql import SparkSession


def create_spark_session(app_name: str, master: str = "local[*]") -> SparkSession:
    return (
        SparkSession.builder
        .appName(app_name)
        .master(master)
        .config("spark.sql.session.timeZone", "UTC")
        .getOrCreate()
    )
