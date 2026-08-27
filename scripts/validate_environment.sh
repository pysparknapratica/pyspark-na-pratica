#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${PROJECT_ROOT}/.venv"

fail(){ printf "\033[31m[ERRO]\033[0m %s\n" "$1" >&2; exit 1; }
ok(){ printf "\033[32m[OK]\033[0m %s\n" "$1"; }

source /etc/os-release
[[ "${ID:-}" == "ubuntu" ]] || fail "Distribuição esperada: Ubuntu."
[[ "${VERSION_ID:-}" == "24.04" ]] || fail "Ubuntu ${VERSION_ID:-desconhecido}; esperado 24.04."
ok "Ubuntu 24.04"

PYTHON_VERSION="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
[[ "${PYTHON_VERSION}" == "3.12" ]] || fail "Python ${PYTHON_VERSION}; esperado 3.12."
ok "Python 3.12"

JAVA_MAJOR="$(java -version 2>&1 | awk -F[\".] '/version/ {print $2}' | head -n1)"
[[ "${JAVA_MAJOR}" == "17" ]] || fail "Java ${JAVA_MAJOR:-desconhecido}; esperado 17."
ok "Java 17"

[[ -x "${VENV_DIR}/bin/python" ]] || fail ".venv não encontrado."
source "${VENV_DIR}/bin/activate"
ok ".venv ativo"

python - <<'PY'
import pyspark
import delta
assert pyspark.__version__ == "4.0.1", pyspark.__version__
print("PySpark 4.0.1: OK")
print("Delta Lake: import OK")
PY

python scripts/smoke_spark.py

echo "ENVIRONMENT_OK"
echo "Ubuntu=24.04"
echo "Python=3.12"
echo "Java=17"
echo "Spark=4.0.1"
echo "Delta=4.0.1"
