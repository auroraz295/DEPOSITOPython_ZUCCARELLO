from modulo_libro import Libro
from modulo_biblioteca import Biblioteca

#ANALISI
#analisi totale disponibili, prenotati, venduti
def analisi_totale(biblioteca):
    print(f"Totale libri disponibili: {len(biblioteca.get_catalogo_completo())}")
    print(f"Totale libri prenotati: {len(biblioteca.get_catalogo_prenotati())}")
    print(f"Totale libri venduti: {len(biblioteca.get_catalogo_venduti())}")

#analisi numero libri per genere    
def analisi_generi(biblioteca):
    #contatori generi
    gialli = 0
    fantasy = 0 
    fantascienza = 0
    distopico = 0
    classico = 0 
    
    for libro in biblioteca.get_catalogo_completo():
        if libro.get_genere() == "Giallo":
            gialli +=1
            
        elif libro.get_genere() == "Fantasy":
            fantasy +=1
        
        elif libro.get_genere() == "Fantascienza":
            fantascienza +=1
            
        elif libro.get_genere() == "Distopico":
            distopico +=1
        
        elif libro.get_genere() == "Classico":
            classico +=1    
        
    #stampa numero libri per genere    
    print(f"Genere Giallo: {gialli} - Genere Fantasy: {fantasy} - Genere Fantascienza: {fantascienza} - Genere Distopico: {distopico} - Genere Classico: {classico}")
        
        
        