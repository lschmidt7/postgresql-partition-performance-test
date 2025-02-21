Esse repositório tem o propósito de medir o desempenho de leitura de registros de um banco de dados Postgres sob condição de uma certa carga de dados.
O propósito é entender a melhor estratégia de indices e particionamentos para melhoria do desempenho.

## Estrutura

A estrutura original (EO) é a seguinte

```sql
CREATE TABLE leitura (
    leitura_id SERIAL PRIMARY KEY,
    leitura_datahora TIMESTAMP NOT NULL
);

CREATE TABLE leitura_dados (
    leitura_dados_id SERIAL PRIMARY KEY,
    leitura_dados_chave INTEGER,
    leitura_dados_valor FLOAT,
    leitura_id INTEGER NOT NULL,
    CONSTRAINT fk_leitura_id FOREIGN KEY (leitura_id) REFERENCES leitura(leitura_id)
);
```

Os indices utilizados

I1
```sql
CREATE INDEX leitura_datahora_idx ON leitura (leitura_datahora);
```

I2
```sql
CREATE INDEX leitura_id_idx ON leitura_dados (leitura_id);
```

Os particionamentos utilizados

P1
```sql
-- na tabela leitura
PARTITION BY RANGE(leitura_datahora)
-- existe 1 partição para cada mês
```

P2
```sql
-- na tabela leitura_dados
PARTITION BY RANGE(leitura_id)
-- existe 1 partição para cada mês baseado no leitura_datahora que existe na tabela leitura
```

## Dados

* Foram inseridos 10000000 (10 milhões) de registros na tabela leitura e 100000000 (100 milhões) de registros na tabela leitura_dados.

* Para cada leitura existem 10 dados atrelados a ela

## Consultas

Consulta Q1
```sql
SELECT count(l.*)
FROM leitura AS l
WHERE l.leitura_datahora >= '2029-05-23 00:00:00'
  AND l.leitura_datahora < '2029-05-24 00:00:00';
```

Consulta Q2
```sql
SELECT count(ld.*)
FROM leitura AS l
     leitura_dados AS ld
WHERE l.leitura_datahora >= '2029-05-23 00:00:00'
  AND l.leitura_datahora < '2029-05-24 00:00:00'
  AND ld.leitura_id = l.leitura_id;
```

## Cenários

* C1: EO
* C2: EO + I1
* C3: EO + I1 + I2
* C4: EO + I1 + I2 + P1
* C5: EO + I1 + I2 + P1 + P2

Obs: o particionamento em leitura_dados(leitura_id) visa imitar o particionamento referenciado existente no Oracle por meio de uma trigger no insert

## Resultados

Os resultados foram computados de cada consulta em relação a cada cenário.

| Consultas | C1 | C2 | C3 | C4 | C5 |
| --------- | -- | -- | -- | -- | -- |
| Q1        |    |    |    |    |    |
| Q2        |    |    |    |    |    |