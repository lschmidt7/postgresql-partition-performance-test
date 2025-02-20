CREATE DATABASE teste;

CREATE TABLE leitura (
    leitura_id SERIAL PRIMARY KEY,
    leitura_datahora TIMESTAMP NOT NULL,
) PARTITION BY RANGE(leitura_datahora);

CREATE TABLE leitura_2025_01 PARTITION OF leitura
FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');

CREATE TABLE leitura_2025_02 PARTITION OF leitura
FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');

CREATE TABLE leitura_2025_03 PARTITION OF leitura
FOR VALUES FROM ('2025-03-01') TO ('2025-04-01');

CREATE TABLE leitura_dados (
    leitura_dados_id SERIAL,
    leitura_dados_chave INTEGER,
    leitura_dados_valor FLOAT,
    leitura_id INTEGER NOT NULL
) PARTITION BY RANGE(leitura_id)