#!/usr/bin/env bash
set -euo pipefail

source .venv/bin/activate
python -m pyspark_na_pratica.pipelines.bronze_pedidos
