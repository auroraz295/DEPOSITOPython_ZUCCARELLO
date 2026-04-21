USE gestioneordini;
SHOW TABLES;
SELECT * FROM ordini;
SELECT * FROM clienti;

#Esercizio 1 – INNER JOIN  Obiettivo:
#Visualizza l’elenco dei clienti che hanno effettuato almeno un ordine.
#Per ciascuno, mostra: nome del cliente, data dell’ordine e importo.

SELECT clienti.nome AS nome, ordini.data_ordine as data_ordine, ordini.importo as importo
FROM clienti INNER JOIN ordini ON clienti.id = ordini.id_cliente;

#Esercizio 2 – LEFT JOIN   Obiettivo:
#Visualizza tutti i clienti, inclusi quelli che non hanno mai effettuato ordini.
#Mostra per ciascuno: nome del cliente, data dell’ordine (se presente) e importo (se presente).

SELECT clienti.nome AS nome, ordini.data_ordine as data_ordine, ordini.importo as importo
FROM clienti LEFT JOIN ordini ON clienti.id = ordini.id_cliente;

#Esercizio 3 – RIGHT JOIN   Obiettivo:
#Visualizza tutti gli ordini, anche quelli che non hanno un cliente associato (caso anomalo).
#Mostra per ciascuno: nome del cliente (se esiste), data dell’ordine e importo.

SELECT clienti.nome AS nome, ordini.data_ordine as data_ordine, ordini.importo as importo
FROM clienti RIGHT JOIN ordini ON clienti.id = ordini.id_cliente;
