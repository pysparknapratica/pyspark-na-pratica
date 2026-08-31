# Diretório auxiliar de checkpoints

Este diretório faz parte da estrutura geral do projeto e pode ser utilizado por laboratórios ou experimentos que organizem checkpoints dentro de `data/`.

Os artefatos de checkpoint gerados durante execuções devem permanecer fora do versionamento quando aplicável.

## Capítulo 27 — Structured Streaming

O laboratório do Capítulo 27 utiliza especificamente:

`checkpoints/eventos`

e não:

`data/checkpoints/eventos`

Essa diferença é intencional e mantém o repositório compatível com o caminho utilizado na edição comercial do livro.
