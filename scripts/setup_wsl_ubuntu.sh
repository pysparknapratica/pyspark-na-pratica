#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${PROJECT_ROOT}/.venv"

ok(){ printf "\033[32m[OK]\033[0m %s\n" "$1"; }
info(){ printf "\033[36m[INFO]\033[0m %s\n" "$1"; }
fail(){ printf "\033[31m[ERRO]\033[0m %s\n" "$1" >&2; exit 1; }

echo "PySpark na Prática — Preparação do Ambiente WSL"

info "[1/9] Verificando WSL"
grep -qiE "(microsoft|wsl)" /proc/version 2>/dev/null || fail "WSL não detectado."
ok "WSL detectado."

info "[2/9] Verificando Ubuntu 24.04"
source /etc/os-release
[[ "${ID:-}" == "ubuntu" ]] || fail "Use Ubuntu 24.04 LTS."
[[ "${VERSION_ID:-}" == "24.04" ]] || fail "Versão detectada: ${VERSION_ID:-desconhecida}. Esperado: 24.04."
ok "Ubuntu ${VERSION_ID}"

info "[3/9] Instalando dependências do sistema"
sudo apt update
sudo apt install -y openjdk-17-jdk python3 python3-pip python3-venv git curl
ok "Dependências do sistema instaladas."

info "[4/9] Verificando Python"
PYTHON_VERSION="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
[[ "${PYTHON_VERSION}" == "3.12" ]] || fail "Python ${PYTHON_VERSION}; esperado 3.12."
ok "$(python3 --version)"

info "[5/9] Verificando Java"
JAVA_MAJOR="$(java -version 2>&1 | awk -F[\".] '/version/ {print $2}' | head -n1)"
[[ "${JAVA_MAJOR}" == "17" ]] || fail "Java ${JAVA_MAJOR:-desconhecido}; esperado 17."
JAVA_BIN="$(readlink -f "$(command -v java)")"
export JAVA_HOME="$(dirname "$(dirname "${JAVA_BIN}")")"
export PATH="${JAVA_HOME}/bin:${PATH}"
ok "Java 17 / JAVA_HOME=${JAVA_HOME}"

info "[6/9] Criando ambiente virtual"
cd "${PROJECT_ROOT}"
if [[ ! -d "${VENV_DIR}" ]]; then
  python3 -m venv "${VENV_DIR}"
fi
source "${VENV_DIR}/bin/activate"
ok ".venv ativo."

info "[7/9] Instalando o projeto"
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
ok "Dependências Python instaladas."

info "[8/9] Executando smoke test"
python scripts/smoke_spark.py
ok "Spark smoke test aprovado."

info "[9/9] Resumo"
echo "AMBIENTE_PREPARADO_OK"
echo "Ubuntu=${VERSION_ID}"
echo "Python=$(python --version | awk '{print $2}')"
echo "Java=${JAVA_MAJOR}"
echo "Spark=$(python -c 'import pyspark; print(pyspark.__version__)')"
echo "Delta=4.0.1"
echo "Venv=${VENV_DIR}"
echo
echo "Em uma nova sessão:"
echo "  cd \"${PROJECT_ROOT}\""
echo "  source .venv/bin/activate"
echo "  bash scripts/validate_environment.sh"
