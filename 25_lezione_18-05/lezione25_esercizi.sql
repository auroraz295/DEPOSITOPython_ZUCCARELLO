USE world;

#PK - ID // FK COUNTRYCODE
SELECT * FROM city;

#PK - CODE (countrycode)
SELECT * FROM country;

#PK - COUNTRYCODE
SELECT * FROM countrylanguage;

#1. Recuperare la lingua (countrylanguage) e la nazione (country) di ogni città
SELECT city.id, city.name AS cityname, country.name AS countryname, countrylanguage.language, countrylanguage.percentage
FROM ((city INNER JOIN country ON city.countrycode = country.code)
		INNER JOIN countrylanguage on city.countrycode = countrylanguage.countrycode)
ORDER BY city.id ASC; 

#2. Recuperare numero città per nazione, ordinarli in base al numero città
SELECT COUNT(city.name) as citynumber, country.name
FROM city INNER JOIN country on city.countrycode = country.code
GROUP BY country.name
ORDER BY citynumber DESC;

#3. Recuperare lista repubbliche con aspettativa di vita >70 anni e lingua parlata
SELECT country.name, country.lifeexpectancy, countrylanguage.language, country.governmentform
FROM country INNER JOIN countrylanguage ON country.code = countrylanguage.countrycode
WHERE country.governmentform LIKE "%Republic%" AND country.lifeexpectancy > 70
ORDER BY country.lifeexpectancy;

#4. Recuperare le lingue parlate per nazione con la percentuale di utilizzo
SELECT country.name, countrylanguage.language, countrylanguage.percentage
FROM country INNER JOIN countrylanguage ON country.code = countrylanguage.countrycode
ORDER BY countrylanguage.percentage DESC;

#5. Recuperare le nazioni e la percentuale della lingua più parlata
SELECT country.name, MAX(countrylanguage.percentage) as percentage
FROM country INNER JOIN countrylanguage ON country.code = countrylanguage.countrycode
GROUP BY country.name;

#6. Fare diventare una subquery il punto 5 per mostrare la lingua più parlata
# di una nazione con la percentuale
SELECT country.name, countrylanguage.language, countrylanguage.percentage
FROM country INNER JOIN countrylanguage ON country.code = countrylanguage.countrycode
WHERE countrylanguage.percentage = (SELECT MAX(percentage) 
									FROM countrylanguage as tabella2
                                    WHERE tabella2.countrycode = countrylanguage.countrycode)


