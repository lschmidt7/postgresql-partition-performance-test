CREATE DATABASE teste;

\c teste

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

CREATE INDEX leitura_datahora_idx ON leitura (leitura_datahora);

CREATE INDEX leitura_id_idx ON leitura_dados (leitura_id);