# PySpark na Prática

## Engenharia de Dados do Zero à Produção

Repositório oficial de apoio ao livro **PySpark na Prática — Engenharia de Dados do Zero à Produção**, de **Elison P Melgueiro**.

Este repositório reúne os códigos-fonte, datasets sintéticos, scripts, testes automatizados, exemplos e materiais técnicos utilizados nos laboratórios práticos do livro.

> **Importante:** o texto integral do livro não é distribuído neste repositório. O GitHub funciona como laboratório técnico e material complementar da obra comercial.

---

## 📘 Sobre o livro

**PySpark na Prática — Engenharia de Dados do Zero à Produção** foi desenvolvido para conduzir o leitor de forma progressiva desde os fundamentos do Apache Spark e PySpark até conceitos e práticas utilizados em projetos modernos de Engenharia de Dados.

Ao longo do material são abordados temas como:

- Apache Spark;
- PySpark;
- DataFrames;
- leitura e escrita de dados;
- schemas e tipos;
- transformações;
- qualidade de dados;
- agregações;
- joins;
- Window Functions;
- ETL e ELT;
- Data Lake;
- arquitetura Lakehouse;
- arquitetura Medallion;
- Parquet;
- particionamento;
- paralelismo;
- Data Skew;
- Catalyst Optimizer;
- Adaptive Query Execution;
- Spark SQL;
- Delta Lake;
- Databricks;
- Jobs e Workflows;
- governança de dados;
- processamento incremental;
- Structured Streaming;
- observabilidade;
- testes;
- pipelines de produção;
- CI/CD;
- projeto final de Engenharia de Dados.

O objetivo é aproximar o aprendizado de situações encontradas no trabalho de um Engenheiro de Dados.

---

## 🎯 Objetivo deste repositório

Este repositório é o **laboratório oficial de apoio ao livro**.

Aqui o leitor poderá executar os exemplos apresentados durante o aprendizado e acompanhar a evolução de um projeto PySpark estruturado de forma progressiva.

A separação é intencional:

```text
LIVRO
│
├── conceitos
├── explicações
├── arquitetura
├── decisões técnicas
├── exercícios
└── orientação didática

            +

REPOSITÓRIO
│
├── código
├── datasets sintéticos
├── scripts
├── testes
├── pipelines
└── automação

            ↓

     APRENDIZADO PRÁTICO
```

---

## 🏗️ Arquitetura utilizada

Os principais laboratórios utilizam uma arquitetura de dados em camadas:

```text
                    DATA SOURCE
                         │
                         ▼
                     data/raw
                         │
                         ▼
                    ┌─────────┐
                    │ BRONZE  │
                    └────┬────┘
                         │
                         ▼
                    ┌─────────┐
                    │ SILVER  │
                    └────┬────┘
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
       dados válidos             inválidos
             │                       │
             │                 ┌────────────┐
             │                 │ QUARANTINE │
             │                 └────────────┘
             ▼
        ┌─────────┐
        │  GOLD   │
        └────┬────┘
             │
             ▼
      dados analíticos
```

Esse fluxo permite trabalhar conceitos importantes como:

- ingestão;
- rastreabilidade;
- metadados técnicos;
- qualidade de dados;
- isolamento de registros inválidos;
- transformação;
- agregação;
- indicadores;
- arquitetura Medallion.

---

## 🧪 Estudo de caso

Os laboratórios utilizam dados sintéticos para representar cenários empresariais.

Nenhum dado pessoal ou empresarial real é necessário para executar o projeto.

Os exemplos permitem trabalhar situações como:

```text
clientes
produtos
pedidos
vendas
distribuição
qualidade de dados
faturamento
indicadores
```

---

# 💻 Ambiente oficial

O ambiente de referência utilizado no projeto é:

| Tecnologia | Versão |
|---|---|
| Ubuntu | 24.04 LTS |
| Python | 3.12 |
| Java | OpenJDK 17 |
| Apache Spark / PySpark | 4.0.1 |
| Delta Lake | 4.0.1 |

No Windows, a arquitetura recomendada é:

```text
Windows
   │
   ▼
WSL2
   │
   ▼
Ubuntu 24.04 LTS
   │
   ├── Python 3.12
   ├── Java 17
   ├── PySpark 4.0.1
   └── Delta Lake 4.0.1
```

---

# 🚀 Preparação automática no WSL

Para facilitar a configuração inicial, o projeto possui um instalador automatizado.

O script foi testado em uma instalação **limpa do WSL2 com Ubuntu 24.04 LTS**, inclusive sem Java previamente instalado.

Na raiz do projeto execute:

```bash
bash scripts/setup_wsl_ubuntu.sh
```

O instalador verifica e prepara o ambiente necessário para os laboratórios.

Entre as etapas estão:

```text
Verificar WSL
      ↓
Verificar Ubuntu 24.04
      ↓
Instalar dependências
      ↓
Verificar Python 3.12
      ↓
Instalar/verificar Java 17
      ↓
Criar .venv
      ↓
Instalar projeto
      ↓
Instalar dependências Python
      ↓
Executar Spark Smoke Test
```

Ao final, o resultado esperado é semelhante a:

```text
AMBIENTE_PREPARADO_OK
Ubuntu=24.04
Python=3.12.x
Java=17
Spark=4.0.1
Delta=4.0.1
```

---

# 🔎 Validação do ambiente

Depois da instalação, o ambiente pode ser auditado executando:

```bash
bash scripts/validate_environment.sh
```

Resultado esperado:

```text
ENVIRONMENT_OK
Ubuntu=24.04
Python=3.12
Java=17
Spark=4.0.1
Delta=4.0.1
```

O validador verifica os principais componentes necessários para executar os laboratórios.

---

# 🧹 Instalação manual

Quem quiser compreender cada etapa da preparação também pode realizar a instalação manual.

Clone o repositório:

```bash
git clone https://github.com/pysparknapratica/pyspark-na-pratica.git
```

Entre no diretório:

```bash
cd pyspark-na-pratica
```

Crie o ambiente virtual:

```bash
python3 -m venv .venv
```

Ative:

```bash
source .venv/bin/activate
```

Atualize o `pip`:

```bash
python -m pip install --upgrade pip
```

Instale o projeto e as dependências de desenvolvimento:

```bash
python -m pip install -e ".[dev]"
```

---

# 🔥 Spark Smoke Test

Antes de executar pipelines maiores, podemos verificar se o Spark está funcionando:

```bash
python scripts/smoke_spark.py
```

Resultado esperado:

```text
SPARK_SMOKE_OK version=4.0.1 timezone=UTC count=100
```

Esse teste confirma que uma SparkSession pode ser criada e que operações básicas estão funcionando.

---

# 🧱 Pipeline Bronze

A camada Bronze representa a primeira etapa do pipeline.

Execute:

```bash
python -m pyspark_na_pratica.pipelines.bronze_pedidos
```

Exemplo de resultado:

```text
=== BRONZE ===
Registros ingeridos: 10

Metadados técnicos:
- _source_file
- _ingestion_timestamp
- _source_system
```

A Bronze preserva os dados ingeridos e acrescenta informações de rastreabilidade.

---

# 🥈 Pipeline Silver

Execute:

```bash
python -m pyspark_na_pratica.pipelines.silver_pedidos
```

Nessa etapa são aplicadas regras de qualidade.

Exemplo:

```text
=== DATA QUALITY ===
Total analisado: 10
Registros válidos: 8
Registros inválidos: 2
Taxa de qualidade: 80.0%
```

Os registros válidos seguem para Silver.

Os inválidos podem ser direcionados para:

```text
data/quarantine/
```

Assim, problemas de qualidade não precisam ser simplesmente descartados.

---

# 🥇 Pipeline Gold

Execute:

```bash
python -m pyspark_na_pratica.pipelines.gold_vendas
```

Exemplo de saída:

```text
+------+-----------+-----------+------------+
|estado|faturamento|qtd_pedidos|ticket_medio|
+------+-----------+-----------+------------+
|AM    |6050.00    |3          |2016.666667 |
|PA    |3680.00    |2          |1840.000000 |
|SP    |1500.00    |2          |750.000000  |
|RJ    |120.00     |1          |120.000000  |
+------+-----------+-----------+------------+
```

A camada Gold representa dados preparados para consumo analítico.

---

# 🔄 Pipeline completo

O laboratório principal pode ser representado como:

```text
data/raw
    │
    ▼
BRONZE
    │
    ▼
data/bronze
    │
    ▼
SILVER
    │
    ├──────────────► QUARANTINE
    │
    ▼
data/silver
    │
    ▼
GOLD
    │
    ▼
data/gold
```

---

# 🧪 Testes automatizados

O projeto possui testes automatizados.

Execute:

```bash
pytest -q
```

Eles ajudam a validar componentes como:

- ingestão;
- transformações;
- qualidade;
- schemas;
- comportamento esperado das pipelines.

---

# 🔍 Qualidade do código

O projeto utiliza `ruff` para análise estática.

Execute:

```bash
ruff check src tests scripts
```

O resultado esperado é:

```text
All checks passed!
```

---

# 🧭 Auditoria de caminhos

O livro e o projeto foram desenvolvidos de forma integrada.

Para ajudar a detectar referências inválidas durante o desenvolvimento foi criado:

```bash
python scripts/audit_paths.py
```

Durante a preparação da release, o resultado esperado é:

```text
PATH_AUDIT_OK references=... missing=0
```

---

# 🧊 Delta Lake

O projeto possui suporte a Delta Lake.

Para validar a integração:

```bash
python scripts/smoke_delta.py
```

O teste cria uma pequena tabela Delta, grava registros e realiza a leitura novamente.

Resultado esperado:

```text
DELTA_SMOKE_OK rows=2
```

---

# ⚖️ Data Skew

O repositório também possui um laboratório dedicado à demonstração de Data Skew:

```bash
python scripts/lab_data_skew.py
```

O cenário gera uma chave extremamente concentrada para demonstrar o problema.

Exemplo:

```text
DATA_SKEW_SMOKE_OK hot_key=900000 total=1000000 pct=90%
```

---

# ⚠️ Avisos comuns no WSL

Durante a inicialização do Spark podem aparecer mensagens como:

```text
WARN Utils: Your hostname ... resolves to a loopback address
```

ou:

```text
WARN NativeCodeLoader:
Unable to load native-hadoop library for your platform...
using builtin-java classes where applicable
```

Esses avisos foram observados durante os testes do projeto em WSL2.

Eles não impediram a execução do Spark nem das pipelines testadas.

É importante diferenciar:

```text
WARN
   ↓
aviso

ERROR / Exception
   ↓
falha que precisa ser investigada
```

Um `WARN` não significa automaticamente que a aplicação falhou.

---

# 📁 Estrutura do projeto

A estrutura pública é organizada aproximadamente desta forma:

```text
pyspark-na-pratica/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── chapters/
│   ├── 01/
│   ├── 02/
│   ├── ...
│   └── 32/
│
├── config/
│
├── data/
│   ├── raw/
│   ├── sample/
│   ├── delta/
│   └── stream/
│
├── docs/
│
├── notebooks/
│
├── scripts/
│   ├── audit_paths.py
│   ├── lab_data_skew.py
│   ├── setup_wsl_ubuntu.sh
│   ├── validate_environment.sh
│   ├── smoke_spark.py
│   ├── smoke_delta.py
│   └── validate_release.sh
│
├── src/
│   └── pyspark_na_pratica/
│       ├── pipelines/
│       ├── quality/
│       ├── schemas/
│       ├── transforms/
│       └── utils/
│
├── tests/
│
├── .env.example
├── .gitignore
├── CHAPTERS.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

# 📚 Materiais por capítulo

O diretório:

```text
chapters/
```

organiza os materiais complementares correspondentes aos capítulos.

Exemplo:

```text
chapters/
│
├── 01/
│   └── README.md
│
├── 02/
│   └── README.md
│
├── ...
│
├── 23/
│   ├── README.md
│   ├── 01_bronze_pedidos.py
│   ├── 02_silver_pedidos.py
│   └── 03_gold_vendas.py
│
└── 32/
    └── README.md
```

Esses materiais complementam os exercícios.

**Eles não correspondem ao manuscrito integral do livro.**

---

# 🔄 Integração contínua

O repositório utiliza GitHub Actions.

O workflow executa automaticamente verificações como:

```text
Checkout
   ↓
Python
   ↓
Java
   ↓
Instalação
   ↓
Lint
   ↓
Auditoria
   ↓
Testes
   ↓
Spark Smoke
   ↓
Bronze
   ↓
Silver
   ↓
Gold
   ↓
Delta Smoke
```

Isso ajuda a impedir que alterações futuras quebrem silenciosamente os laboratórios.

---

# ✅ Ambiente validado

Além dos testes locais de desenvolvimento, o projeto passou por uma validação em uma **segunda distribuição WSL recém-instalada**.

O estado inicial desse ambiente era:

```text
Ubuntu 24.04.4 LTS
Python 3.12.3
Git 2.43.0
Java não instalado
```

O instalador automatizado conseguiu preparar o restante do ambiente.

Depois foram executados com sucesso:

```text
setup_wsl_ubuntu.sh       OK
validate_environment.sh   OK
Spark Smoke               OK
Bronze                    OK
Silver                    OK
Data Quality              OK
Quarantine                OK
Gold                      OK
```

O objetivo desse teste foi reproduzir de maneira mais próxima a experiência de um leitor preparando seu laboratório pela primeira vez.

---

# 🧰 Principais tecnologias

O projeto trabalha principalmente com:

- Python;
- PySpark;
- Apache Spark;
- Spark SQL;
- Delta Lake;
- Parquet;
- Git;
- GitHub;
- GitHub Actions;
- Linux;
- Ubuntu;
- WSL2;
- Java;
- pytest;
- Ruff.

Ao longo do livro também são discutidos conceitos relacionados a Databricks, Lakehouse e Engenharia de Dados em produção.

---

# 👨‍💻 Para quem é este projeto?

Este material foi pensado principalmente para:

- estudantes de Engenharia de Dados;
- desenvolvedores Python interessados em Big Data;
- profissionais migrando para Engenharia de Dados;
- analistas de dados;
- engenheiros de software;
- profissionais estudando Apache Spark;
- leitores do livro *PySpark na Prática*.

Não é necessário começar como especialista em Spark.

A proposta é evoluir progressivamente.

---

# 🗺️ Jornada de aprendizado

Uma visão simplificada da progressão é:

```text
Fundamentos
     ↓
DataFrames
     ↓
Transformações
     ↓
Qualidade
     ↓
Joins
     ↓
Window Functions
     ↓
ETL / ELT
     ↓
Data Lake
     ↓
Lakehouse
     ↓
Parquet
     ↓
Performance
     ↓
Spark SQL
     ↓
Delta Lake
     ↓
Databricks
     ↓
Streaming
     ↓
Testes
     ↓
Produção
     ↓
Projeto Final
```

---

# 📖 Livro × repositório

É importante compreender a função de cada material.

### Livro

O livro contém a experiência educacional completa:

- explicações;
- conceitos;
- contexto;
- raciocínio;
- exemplos comentados;
- exercícios;
- arquitetura;
- decisões técnicas;
- progressão didática.

### Repositório

O GitHub contém principalmente:

- código;
- scripts;
- dados sintéticos;
- testes;
- arquivos de configuração;
- materiais complementares.

Em resumo:

```text
Livro
   +
GitHub
   =
experiência completa
```

---

# 🔐 Segurança

Nunca envie credenciais para este repositório.

Arquivos como:

```text
.env
.env.*
```

são ignorados pelo Git.

Quando necessário, utilize:

```text
.env.example
```

apenas como modelo de configuração.

Nunca publique:

- senhas;
- tokens;
- chaves privadas;
- credenciais de cloud;
- connection strings reais.

---

# 📜 Licenciamento

## Código-fonte

O código-fonte, scripts, testes e exemplos técnicos disponibilizados neste repositório são licenciados conforme os termos do arquivo:

```text
LICENSE
```

A licença aplicável ao código **não transfere direitos autorais sobre o livro**.

## Livro

O livro:

**PySpark na Prática — Engenharia de Dados do Zero à Produção**

é uma obra autoral independente do código disponibilizado neste repositório.

O texto integral, estrutura editorial, capítulos, edição comercial, elementos gráficos e demais componentes autorais da publicação não são distribuídos sob a licença do código.

```text
© 2026 Elison P Melgueiro
Todos os direitos reservados.
```

A reprodução, distribuição ou comercialização do conteúdo integral do livro depende de autorização do autor, exceto nos limites permitidos pela legislação aplicável.

---

# 🤝 Contribuições

O repositório tem como objetivo principal servir como material oficial de apoio ao livro.

Correções técnicas e relatos de problemas podem ser enviados por meio das ferramentas disponibilizadas pelo GitHub.

Ao relatar um problema, procure informar:

```text
Sistema operacional
Versão do Python
Versão do Java
Versão do PySpark
Comando executado
Mensagem de erro
```

Isso facilita a reprodução do problema.

---

# 🐛 Encontrou um problema?

Antes de abrir uma issue, execute:

```bash
bash scripts/validate_environment.sh
```

Depois:

```bash
pytest -q
```

E:

```bash
ruff check src tests scripts
```

Essas informações ajudam a separar problemas de ambiente de problemas no código.

---

# 📌 Status do projeto

O projeto passou por validações envolvendo:

```text
✓ estrutura do repositório
✓ caminhos utilizados pelo material
✓ Python
✓ Java
✓ PySpark
✓ Delta Lake
✓ testes automatizados
✓ lint
✓ Spark smoke test
✓ Data Skew
✓ Bronze
✓ Silver
✓ Data Quality
✓ Quarantine
✓ Gold
✓ WSL limpo
✓ integração contínua
```

O repositório continuará evoluindo conforme necessário para acompanhar o material oficial.

---

# 👤 Autor

**Elison P Melgueiro**

Autor de:

**PySpark na Prática — Engenharia de Dados do Zero à Produção**

---

# ⚠️ Aviso educacional

Este projeto possui finalidade educacional.

Os dados fornecidos são sintéticos e foram desenvolvidos exclusivamente para demonstrações e laboratórios de Engenharia de Dados.

Resultados, arquiteturas e decisões apresentadas nos exercícios devem ser avaliados de acordo com os requisitos específicos de cada ambiente de produção.

---

## PySpark na Prática

```text
Aprender
   ↓
Executar
   ↓
Entender
   ↓
Testar
   ↓
Otimizar
   ↓
Construir
```

**Engenharia de Dados se aprende também colocando os dados para trabalhar.**