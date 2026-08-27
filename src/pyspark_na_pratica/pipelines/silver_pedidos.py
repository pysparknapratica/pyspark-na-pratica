from pathlib import Path

from pyspark_na_pratica.quality.pedidos import separar_validos_invalidos
from pyspark_na_pratica.session import create_spark_session
from pyspark_na_pratica.transforms.pedidos import (
    padronizar_pedidos,
    selecionar_colunas_silver,
)
from pyspark_na_pratica.utils.metrics import calcular_metricas


def main() -> None:
    spark = create_spark_session("SilverPedidos")

    raiz = Path("data")
    entrada = raiz / "bronze/pedidos"
    saida = raiz / "silver/pedidos"
    quarentena = raiz / "quarantine/pedidos"

    df_raw = spark.read.parquet(str(entrada))

    df_padronizado = padronizar_pedidos(df_raw)
    df_silver = selecionar_colunas_silver(df_padronizado)

    validos, invalidos = separar_validos_invalidos(df_silver)
    metricas = calcular_metricas(df_silver, validos, invalidos)

    validos.write.mode("overwrite").parquet(str(saida))
    invalidos.write.mode("overwrite").parquet(str(quarentena))

    print("=== DATA QUALITY ===")
    print(f"Total analisado: {metricas.total:,}")
    print(f"Registros válidos: {metricas.validos:,}")
    print(f"Registros inválidos: {metricas.invalidos:,}")
    print(f"Taxa de qualidade: {metricas.taxa_qualidade:.1%}")

    spark.stop()


if __name__ == "__main__":
    main()
