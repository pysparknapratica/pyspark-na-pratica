#!/usr/bin/env bash
set -euo pipefail

sudo apt update
sudo apt install -y openjdk-17-jdk python3 python3-venv python3-pip git

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"

echo
echo "Ambiente instalado."
echo "Ative com: source .venv/bin/activate"
python --version
java -version
