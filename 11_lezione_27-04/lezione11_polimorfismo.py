#POLIMORFISMO

class Persona:
        
    def parla():
        print("Sto parlando.")
        
class PersonaSorda(Persona):
    def parla():
        print("Sto parlando con il linguaggio dei segni.")
        
class PersonaCieca(Persona):
    def parla():
        print("Sto parlando con il braille.")
        
def fai_parlare(utente: Persona):
    utente.parla()
    
persona1 = PersonaSorda()

persona1.fai_parlare()
    
#SIMULAZIONE OVERLOADING 

class Stampa:
    def mostra(self, a=None, b=None):
        if a is not None and b is not None:
            print(a+b)
        elif a is not None:
            print(a)
        else: 
            print("Niente da mostrare")
        
prova1 = Stampa.mostra(2,3)
prova2 = Stampa.mostra(())
prova3 = Stampa.mostra(3)

#DUCK TYPING
class Cerchio:
    def disegna(self):
        print("Disegno un cerchio")
        
class Rettangolo:
    def disegna(self):
        print("Disegno un rettangolo")
        
class Rombo():
    def disegna(self):
        print("Disegno un rombo")
        
def disegna_figura(figura):
    figura.disegna()
    
figure = [Cerchio(), Rettangolo(), Rombo()]

for figura in figure:
    disegna_figura(figura)