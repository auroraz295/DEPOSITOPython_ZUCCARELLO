USE world;

#1. Utilizzo di DISTINCT e WHERE
#Elencare, senza ripetizioni, tutte le regioni (Region) dei paesi 
#che appartengono al continente (Continent) 'Europe'.

SELECT * FROM world.country;

SELECT DISTINCT Region 
FROM world.country
WHERE Continent = 'Europe';

#2. Combinazione di WHERE, ORDER BY
#Elencare i nomi (Name) e la popolazione (Population) delle città (City) degli Stati Uniti (CountryCode = 'USA') 
#che hanno una popolazione superiore a 1.000.000 abitanti, ordinando i risultati dalla città più popolosa alla meno popolosa.

SELECT Name, District, Population
FROM world.city
WHERE CountryCode = 'USA' AND Population >= 1000000
ORDER BY Population DESC;

#3. GROUP BY con funzioni di aggregazione
#Mostrare per ogni continente (Continent) presente nella tabella Country:
# - Il numero totale di paesi appartenenti a ciascun continente.
# - La popolazione totale del continente.
#Ordinare il risultato per popolazione totale in ordine decrescente.

SELECT Continent, COUNT(DISTINCT Region) AS Paesi, SUM(Population) AS PTOT
FROM world.country
GROUP BY Continent
ORDER BY PTOT DESC;

## 

#4. Si consideri un database che contiene informazioni su una libreria. 

#1) Inserimento dati (INSERT INTO)
#Inserire almeno 6 nuovi libri nella tabella Libri usando il comando SQL INSERT INTO.
#I libri devono appartenere a generi e autori diversi, ed essere pubblicati in anni differenti.

#2) Aggregazione e raggruppamento (GROUP BY)
#Scrivere una query che, usando il comando GROUP BY, mostri per ogni genere:
# - il numero totale di libri presenti;
# - il prezzo medio dei libri appartenenti a quel genere.
#La query dovrà restituire il risultato ordinato alfabeticamente per genere.

#3) Ordinamento risultati (ORDER BY)
#Scrivere una query che elenchi tutti i libri pubblicati dopo l’anno 2010 ordinati in modo decrescente
#per anno di pubblicazione e, in caso di anno uguale, in ordine crescente per prezzo.

CREATE DATABASE libri;

USE libri;

CREATE TABLE Libri (
    id INT PRIMARY KEY,
    titolo VARCHAR(100),
    autore VARCHAR(100),
    genere VARCHAR(50),
    prezzo DECIMAL(5,2),
    anno_pubblicazione INT
);

INSERT INTO Libri (id, titolo, autore, genere, prezzo, anno_pubblicazione)
VALUES (11, 'The Host', 'Stephenie Meyer', 'Fantascienza', 16.50, 2008),
	   (12, 'Divergent', 'Veronica Roth', 'Distopico', 14.90, 2011),
       (13, 'Harry Potter e i Doni della Morte', 'J.K. Rowling', 'Fantasy', 22.00, 2007),
       (14, 'Hunger Games', 'Suzanne Collins', 'Distopico', 15.00, 2008),
       (15, 'Shadowhunters: Città di Ossa', 'Cassandra Clare', 'Urban Fantasy', 17.50, 2007),
	   (16, 'Maze Runner: Il Labirinto', 'James Dashner', 'Fantascienza', 13.50, 2009);

SELECT genere, COUNT(titolo) AS NumLibri, AVG(prezzo) AS PrezzoMedio
FROM Libri
GROUP BY genere
ORDER BY genere ASC;

SELECT *
FROM Libri
WHERE anno_pubblicazione > 2010
ORDER BY anno_pubblicazione DESC, prezzo ASC; 

