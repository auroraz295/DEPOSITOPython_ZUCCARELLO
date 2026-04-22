#Esercizio 5 @staticmethod: 
#Crea una classe chiamata Convertitore. Questa classe dovrebbe avere:
# - Un metodo statico euro_in_dollari che accetti un importo in euro e 
#   restituisca il valore convertito in dollari, usando un tasso fisso di 1.08.
# - Un metodo statico km_in_miglia che accetti una distanza in chilometri e 
#   restituisca il valore convertito in miglia, usando un fattore fisso di 0.621371.
#Testa la classe chiamando entrambi

class Convertitore:
    #dato che si devono utilizzare i metodi statici non occorre
    #creare gli oggetti con il metodo costruttore def init
    
    #metodo statico per calcolare la conversione in dollaro
    @staticmethod
    def euro_in_dollari(importo):
        conversione_dollaro = importo * 1.08
        return conversione_dollaro
    
    #metodo statico per calcolare la distanza in miglia
    @staticmethod
    def km_in_miglia(distanza):
        conversione_miglia = distanza * 0.621371
        return conversione_miglia
    
calcolo1 = Convertitore.euro_in_dollari(20)
calcolo2 = Convertitore.km_in_miglia(34)

print(f"La conversione da euro in dollari è di {calcolo1}.")
print(f"La conversione da km in miglia è di {calcolo2}.")

#Esercizio 6 @classmethod: 
#Crea una classe chiamata Animale. Questa classe deve avere:
# - Un attributo di classe numero_animali, inizializzato a 0.
# - Due attributi di istanza: nome e specie, passati al costruttore.
#   Il costruttore deve incrementare numero_animali di 1 ogni volta che viene creato un nuovo animale.
# - Un metodo di classe quanti_animali che stampi una stringa del tipo 
#   "Numero di animali creati: 'numero_animali'".
#Crea almeno 3 oggetti Animale e poi chiama quanti_animali direttamente dalla classe,
# senza usare nessuna delle istanze create.

class Animale:
    #attributo di classe
    numero_animali = 0
    
    #definisco le variabili per l'animale
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
        
        #contatore che aumenta ogni volta che viene creato un nuovo animale
        Animale.numero_animali += 1
        
    #metodo di classe per stampare il totale animali creati    
    @classmethod
    def quanti_animali(cls):
        print(f"Numero di animali creati: {cls.numero_animali}.")  #IMPORTANTE METTERE CLS.
        
#creazione animali        
animale1 = Animale("Milu", "Cane")
animale2 = Animale("Kiko", "Tartaruga")
animale3 = Animale("Speedy", "Pesce")
animale4 = Animale("Pippo", "Pesce")

#chiamo direttamente dalla classe e non le singole istanze animale1, 2 ecc
Animale.quanti_animali()