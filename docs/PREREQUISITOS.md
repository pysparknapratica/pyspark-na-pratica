# Pré-requisitos do Livro

## Para quem é este livro

Este livro foi desenvolvido para estudantes universitários, profissionais em transição de carreira, desenvolvedores, analistas e pessoas que desejam aprender Engenharia de Dados utilizando PySpark de forma progressiva e prática.

Você **não precisa conhecer Apache Spark, PySpark, Delta Lake ou Databricks antes de começar**. Os conceitos serão apresentados gradualmente, sempre relacionando teoria, código e situações próximas do cotidiano de Engenharia de Dados.

## Pré-requisitos de conhecimento

Para aproveitar melhor os capítulos práticos, recomendamos apenas uma base introdutória em:

- informática e organização de arquivos e diretórios;
- utilização básica de terminal;
- Python básico: variáveis, tipos de dados, `if`, `for`, funções, listas e dicionários;
- conceitos simples de dados, como tabelas, CSV e JSON.

Não é necessário conhecimento prévio de:

- Engenharia de Dados;
- computação distribuída;
- Apache Spark;
- PySpark;
- Delta Lake;
- Databricks;
- arquitetura Lakehouse.

> **E se eu ainda não souber Python?**  
> Você poderá compreender boa parte dos conceitos do livro, mas recomendamos estudar os fundamentos da linguagem antes de avançar nos exercícios mais práticos. Os códigos serão explicados passo a passo, com foco no raciocínio de Engenharia de Dados e não apenas na sintaxe.

## Pré-requisitos de hardware

Para executar o laboratório local do livro, recomendamos:

```text
Memória RAM:
8 GB no mínimo
16 GB recomendado

Processador:
64 bits, preferencialmente com múltiplos núcleos

Armazenamento:
pelo menos 20 GB livres para ambiente, dependências,
datasets e arquivos gerados durante os laboratórios
```

O Spark pode consumir bastante memória durante determinados exercícios. Máquinas com 16 GB ou mais proporcionarão uma experiência mais confortável, principalmente nos capítulos de performance, joins, particionamento e Data Skew.

## Ambiente oficial testado da edição

O ambiente de referência do projeto é:

```text
Sistema operacional:
Ubuntu 24.04 LTS 64 bits

Python:
Python 3.12

Java:
OpenJDK 17

PySpark:
4.0.x

Delta Lake:
4.0.x
```

Os exemplos foram organizados para que o estudante utilize o mesmo ambiente durante o desenvolvimento do projeto do livro.

Usuários de Windows poderão utilizar **WSL2 com Ubuntu 24.04 LTS**, mantendo o laboratório Linux utilizado nos capítulos.

## O que você aprenderá

Ao longo do livro, você evoluirá dos fundamentos até a construção de pipelines próximos de cenários profissionais. Entre os principais assuntos estão:

- fundamentos do Apache Spark e processamento distribuído;
- SparkSession, DataFrames e Spark SQL;
- schemas e tipos de dados;
- filtros, transformações, agregações e joins;
- tratamento e qualidade de dados;
- arquitetura RAW, Bronze, Silver e Gold;
- particionamento, shuffle, cache e performance;
- Delta Lake e propriedades ACID;
- cargas incrementais;
- Structured Streaming;
- testes automatizados;
- observabilidade e boas práticas;
- construção de pipelines de Engenharia de Dados;
- organização de um projeto profissional para GitHub.

## Como estudar com este livro

A recomendação é não tratar o livro apenas como material de leitura.

Use o ciclo:

```text
LER
 |
 v
ENTENDER
 |
 v
DIGITAR O CÓDIGO
 |
 v
EXECUTAR
 |
 v
ALTERAR
 |
 v
OBSERVAR O RESULTADO
 |
 v
RESOLVER O DESAFIO
```

Evite apenas copiar e colar os exemplos. Digitar, modificar e executar o código ajuda a compreender o comportamento do Spark e a desenvolver raciocínio de Engenharia de Dados.

Os arquivos de apoio do repositório acompanham os capítulos para que você possa comparar sua implementação, executar os datasets sintéticos e avançar gradualmente até o projeto final.

---

