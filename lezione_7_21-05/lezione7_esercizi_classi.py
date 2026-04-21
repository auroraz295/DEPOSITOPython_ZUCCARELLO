#Esercizio 1 
#Crea una classe chiamata Punto. 
#Questa classe dovrebbe avere:
# - Due attributi: x e y, per rappresentare le coordinate del
#   punto nel piano.
# - Un metodo muovi che prenda in input un valore per dx e un
#    valore per dy e modifichi le coordinate del punto di questi valori.
# - Un metodo distanza_da_origine che restituisca la distanza del
#   punto dall'origine (0,0) del piano.


class Punto:
    #creo le due variabili per i due punti cartesiani
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def muovi(self, dx, dy):
        #sommo i valori iniziali con i nuovi dati 
        self.x += dx
        self.y += dy
      
        print(f"Hai spostato le tue coordinate in: ({self.x},{self.y}).")
        
    def distanza_da_origine(self):
        #la distanza dal punto (0,0) si calcola con il teorema di pitagora di radice di x^2+y^2
        distanza = ((self.x**2) + (self.y**2)) ** 0.5
        print(f"La distanza dal punto (0,0) con coordinate ({self.x},{self.y}) è di {distanza}")
        
p1 = Punto(5,2)
p1.distanza_da_origine()
p1.muovi(7,1)
p1.distanza_da_origine()

#Esercizio 2      
#Crea una classe chiamata Libro. 
#Questa classe dovrebbe avere:
# - Tre attributi: titolo, autore e pagine.
# - Un metodo descrizione che restituisca una stringa del tipo
#"Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".

class Libro:
    #creo le tre variabili per i tre attributi
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def descrizione(self):
        print(f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine.")
        
libro1 = Libro("The Host", "Stephenie Meyer", 312)    

libro1.descrizione()    