from dataclasses import dataclass

from pyspark.sql import DataFrame


@dataclass(frozen=True)
class QualityMetrics:
    total: int
    validos: int
    invalidos: int

    @property
    def taxa_qualidade(self) -> float:
        if self.total == 0:
            return 1.0
        return self.validos / self.total


def calcular_metricas(
    df_total: DataFrame,
    df_validos: DataFrame,
    df_invalidos: DataFrame,
) -> QualityMetrics:
    return QualityMetrics(
        total=df_total.count(),
        validos=df_validos.count(),
        invalidos=df_invalidos.count(),
    )
