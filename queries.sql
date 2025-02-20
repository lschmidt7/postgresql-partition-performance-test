-- 171 ms -> 4ms
SELECT count(l.*)
FROM leitura AS l
WHERE l.leitura_datahora >= '2029-05-23 00:00:00'
  AND l.leitura_datahora < '2029-05-24 00:00:00';