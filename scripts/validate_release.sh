#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

source /etc/os-release
if [[ "${ID:-}" != "ubuntu" || "${VERSION_ID:-}" != "24.04" ]]; then
  echo "ERRO: release deve ser validada em Ubuntu 24.04. Ambiente atual: ${PRETTY_NAME:-desconhecido}" >&2
  exit 1
fi

PY_MINOR="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
if [[ "$PY_MINOR" != "3.12" ]]; then
  echo "ERRO: esperado Python 3.12, encontrado $PY_MINOR" >&2
  exit 1
fi

JAVA_MAJOR="$(java -version 2>&1 | sed -n '1s/.*version "\([0-9]*\).*/\1/p')"
if [[ "$JAVA_MAJOR" != "17" ]]; then
  echo "ERRO: esperado Java 17, encontrado $JAVA_MAJOR" >&2
  exit 1
fi

python scripts/audit_paths.py
ruff check src tests scripts/*.py
pytest -q
python scripts/smoke_spark.py
echo "== Bronze pipeline =="
python -m pyspark_na_pratica.pipelines.bronze_pedidos

test -d data/bronze/pedidos
find data/bronze/pedidos -name "*.parquet" | grep -q .

echo "BRONZE_OK"

python -m pyspark_na_pratica.pipelines.silver_pedidos
python -m pyspark_na_pratica.pipelines.gold_vendas
python scripts/smoke_delta.py
python scripts/lab_data_skew.py

echo "RELEASE_VALIDATION_OK Ubuntu=24.04 Python=3.12 Java=17 Spark=4.0.1 Delta=4.0.1"
