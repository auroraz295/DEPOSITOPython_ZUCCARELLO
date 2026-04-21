#CREAZIONE DI UNA CLASSE
class Automobile:                                #dichiaro la classe
    numero_ruote = 4                             #attributo di classe
    
    def __init__(self, marca, modello):          #metodo costruttore
        self.marca = marca                       #attributo di istanza
        self.modello = modello                   #attributo di istanza
   
    def stampa_info(self):                       #metodo di istanza
        print(f"L'automobile è una {self.marca}, {self.modello}")
    
#__init__ metodo costruttore

#CREAZIONE OGGETTI DA UNA CLASSE
auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW", "X3")

auto1.stampa_info()
auto2.stampa_info()
 
auto1.marca = "Mercedes"                        #modifica auto1
auto1.modello = "Classe E"

auto1.stampa_info()

auto1.numero_ruote = 6                        #cambia solo il numero ruote in auto1
Automobile.numero_ruote = 6                   #cambia il numero ruote in tutta la classe

print(f"numero ruote: {auto1.numero_ruote}")
print(f"numero ruote: {auto2.numero_ruote}")


#CREAZIONE CLASSE - ESEMPIO 2
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome                  #attributo per memorizzare il nome
        self.eta = eta                    #attributo per memorizzare l'età
        
    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")    
        
p = Persona("Aurora", 25)
print(p.nome)
print(p.eta)

p.saluta()

#METODO STATICO
class Calcolatrice:
    @staticmethod
    def somma(a,b):
        return a+b
    
risultato = Calcolatrice.somma(5,3)

print(risultato)