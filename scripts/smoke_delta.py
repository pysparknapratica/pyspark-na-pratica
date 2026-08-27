import shutil
from pathlib import Path

from pyspark_na_pratica.session_delta import create_delta_spark_session

path = Path("data/delta/smoke_test")
if path.exists():
    shutil.rmtree(path)

spark = create_delta_spark_session("SmokeDelta")
try:
    assert spark.version == "4.0.1", f"Spark inesperado: {spark.version}"
    df = spark.createDataFrame([(1, "ok"), (2, "delta")], ["id", "valor"])
    df.write.format("delta").mode("overwrite").save(str(path))
    result = spark.read.format("delta").load(str(path))
    assert result.count() == 2
    print("DELTA_SMOKE_OK rows=2")
finally:
    spark.stop()
