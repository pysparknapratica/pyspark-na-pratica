# Capítulo 31 — Projeto Final: Lakehouse Completo

> O conteúdo completo do capítulo faz parte da edição comercial. Este diretório orienta o uso dos dados sintéticos complementares do projeto final.

## Objetivo do companion

O projeto final começa pelo domínio **pedidos**, que concentra o fluxo Bronze → Silver → Gold usado ao longo do livro. Para permitir que o leitor estenda o Lakehouse aos demais domínios citados no capítulo, o repositório também disponibiliza datasets sintéticos relacionados.

## Datasets RAW

| Domínio | Dataset | Uso didático |
|---|---|---|
| Clientes | `data/raw/clientes.csv` | dimensão de clientes e clientes ativos |
| Produtos | `data/raw/produtos.csv` | catálogo e vendas por produto |
| Pedidos | `data/raw/pedidos.csv` | núcleo do pipeline |
| Itens | `data/raw/itens_pedido.csv` | granularidade item/pedido e joins |
| Pagamentos | `data/raw/pagamentos.csv` | status financeiro e receita aprovada |
| Entregas | `data/raw/entregas.csv` | SLA logístico e atrasos |

## Relacionamentos

```text
clientes
   |
   | cliente_id
   v
pedidos ---------> pagamentos
   |
   | pedido_id
   +-------------> entregas
   |
   +-------------> itens_pedido -----> produtos
```

Os dados são **100% sintéticos** e existem somente para estudo.

## Sugestão de evolução do Lakehouse

Implemente um domínio de cada vez:

1. Pedidos — Bronze, Silver, qualidade e Gold.
2. Itens — valide chaves e valores; depois faça join com produtos.
3. Pagamentos — separe pagamentos aprovados, pendentes e recusados.
4. Entregas — derive `entregue_no_prazo` comparando `data_entrega` com `data_prevista`.
5. Clientes — produza indicadores como clientes ativos.
6. Gold — construa produtos de consumo, por exemplo:
   - faturamento por estado;
   - vendas por produto;
   - receita aprovada;
   - taxa de pagamentos não aprovados;
   - SLA de entregas;
   - clientes ativos.

## Casos intencionais para exercícios

- Há pagamento `PENDENTE`.
- Há pagamento `RECUSADO`.
- Há entrega atrasada.
- Há entrega no prazo.
- Há pedido em trânsito.
- Há pedido aguardando pagamento.
- Há entrega cancelada.

Esses casos existem propositalmente para permitir exercícios de qualidade, regra de negócio, joins e observabilidade.

## Regra importante

Não avance para outro domínio enquanto o anterior não tiver:

- schema definido;
- validações;
- tratamento de inválidos;
- resultado reexecutável;
- teste ou evidência de qualidade.

O objetivo do Capítulo 31 não é apenas produzir tabelas, mas demonstrar integração, reprocessamento e confiabilidade ponta a ponta.
