-- Q1
SELECT count(l.*)
FROM leitura AS l
WHERE l.leitura_datahora >= '2029-05-23 00:00:00'
  AND l.leitura_datahora < '2029-05-24 00:00:00';

SELECT count(ld.*)
FROM leitura AS l,
     leitura_dados AS ld
WHERE l.leitura_datahora >= '2029-05-23 00:00:00'
  AND l.leitura_datahora < '2029-05-24 00:00:00'
  AND ld.leitura_id = l.leitura_id;

SELECT count(ld.*)
FROM leitura AS l,
     leitura_dados AS ld
WHERE l.leitura_datahora >= '2029-05-23 00:00:00'
  AND l.leitura_datahora < '2029-05-24 00:00:00'
  AND ld.leitura_data >= '2029-05-23'
  AND ld.leitura_data < '2029-05-24'
  AND ld.leitura_id = l.leitura_id;