from pyspark_na_pratica.session import create_spark_session

spark = create_spark_session("Cap04DataFrame")

dados = [
    (1001, "AM", "Notebook", 1, 3500.00),
    (1002, "PA", "Mouse", 2, 80.00),
    (1003, "SP", "Monitor", 1, 1200.00),
    (1004, "AM", "Teclado", 1, 150.00),
    (1005, "RJ", "Mouse", 3, 120.00),
]
colunas = ["pedido_id", "estado", "produto", "quantidade", "valor"]
df = spark.createDataFrame(dados, colunas)
df.show(truncate=False)
df.printSchema()
print("Colunas:", df.columns)
print("Registros:", df.count())
spark.stop()
