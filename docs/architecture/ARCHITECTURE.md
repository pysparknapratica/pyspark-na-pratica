# Arquitetura do Projeto

## Fluxo

```text
Fontes sintéticas
      |
      v
     RAW
      |
      v
   BRONZE
      |
      +----> auditoria
      |
      v
   SILVER
      |
      +----> quarentena
      +----> métricas de qualidade
      |
      v
    GOLD
      |
      v
  Analytics
```

## Convenção do livro

- **RAW**: arquivo preservado próximo da forma recebida.
- **Bronze**: dado ingerido com schema técnico e metadados.
- **Silver**: dado limpo, padronizado, deduplicado e validado.
- **Gold**: dado orientado ao consumo e indicadores.

Essa convenção é didática e deve permanecer explícita, pois outros projetos podem usar RAW e Bronze com significados diferentes.

## Chaves oficiais

- `pedido_id`: string
- `cliente_id`: string
- `produto_id`: string

## Dinheiro

Valores monetários usam `DecimalType`, não `DoubleType`, na modelagem oficial do projeto.

## Tempo

O projeto deve distinguir:
- data/hora do evento;
- data/hora de atualização;
- data/hora de ingestão;
- data/hora de processamento.
