# Troubleshooting

## Verificações iniciais

```bash
java -version
python --version
python -c "import pyspark; print(pyspark.__version__)"
```

## Java

O laboratório oficial usa OpenJDK 17.

## Ambiente virtual

```bash
source .venv/bin/activate
```

## Testes

```bash
pytest -q
```

## Delta

Para os capítulos Delta, use a linha PySpark 4.0.x com delta-spark 4.0.x conforme o ambiente oficial do repositório.
