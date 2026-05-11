USE gestioneordini;
SELECT * FROM libri;
SELECT * FROM venditelibri;

#ESERCIZIO 1 
#INNER JOIN + WHERE + LIKE 
SELECT libri.id AS IDLibro, libri.titolo AS TitoloLibro, libri.autore AS AutoreLibro, venditelibri.id AS IDVendita, venditelibri.data_vendita AS DataVendita, venditelibri.negozio AS Negozio
FROM libri INNER JOIN venditelibri ON libri.id = venditelibri.id_libro
WHERE libri.autore LIKE '%king%';

#ESERCIZIO 2
#LEFT JOIN + WHERE + BETWEEN
SELECT libri.titolo AS Libro, libri.anno_pubblicazione AS AnnoPubblicazione, libri.prezzo AS Prezzo, venditelibri.data_vendita AS DataVendita
FROM libri LEFT JOIN venditelibri ON libri.id = venditelibri.id_libro
WHERE libri.anno_pubblicazione BETWEEN 2000 AND 2010;

#ESERCIZIO 3
#INNER JOIN + WHERE + IN
SELECT libri.titolo AS Libro, venditelibri.negozio AS Negozio, venditelibri.quantita, (venditelibri.quantita * libri.prezzo) AS PrezzoTOT
FROM libri INNER JOIN venditelibri ON libri.id = venditelibri.id_libro
WHERE venditelibri.negozio IN ('9 Oriole Lane', '98558 Milwaukee Point', '98016 Esch Trail');

#ESERCIZIO 4 
#RIGHT JOIN + WHERE + LIKE + BETWEEN
SELECT libri.titolo AS Titolo, venditelibri.data_vendita AS DataVendita, libri.prezzo AS Prezzo, venditelibri.negozio AS Negozio
FROM libri RIGHT JOIN venditelibri ON libri.id = venditelibri.id_libro 
WHERE venditelibri.negozio LIKE '%Drive%' AND libri.anno_pubblicazione BETWEEN 2022-12-31 AND 2020-01-01;

#ESERCIZIO 5 
#INNER JOIN + WHERE COMBINATO
SELECT libri.titolo AS Titolo, libri.genere AS genere, libri.autore AS AutoreLibro, libri.prezzo AS Prezzo, libri.anno_pubblicazione AS AnnoPubblicazione, venditelibri.data_vendita AS DataVendita, venditelibri.negozio AS Negozio
FROM libri INNER JOIN venditelibri ON libri.id = venditelibri.id_libro
WHERE libri.genere IN ('Fantasy', 'Horror', 'Drama') AND venditelibri.negozio LIKE '%plaza%' AND venditelibri.data_vendita > 2015
ORDER BY venditelibri.data_vendita DESC;

