#ESERCIZIO 1 
#Un'azienda vuole gestire i suoi impiegati tramite un sistema informatico. Esistono
#diversi ruoli all'interno dell'ufficio, ma tutti gli impiegati hanno alcune
#caratteristiche comuni, come il nome, il cognome e lo stipendio. 
#Inoltre, ogni impiegato ha un metodo per calcolare il suo stipendio mensile, che
#può variare a seconda del ruolo.

#import per la classe astratta
from abc import ABC, abstractmethod

#CLASSE ASTRATTA
#nelle classi astratte va sempre (ABC) dato che è un'ereditarietà da abc
class Impiegato(ABC):
    def __init__(self, nome:str, cognome:str, stipendio_base:float):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base
      
    #METODO ASTRATTO   
    #va solo prima dei metodi astratti  
    @abstractmethod
    def calcola_stipendio():
        pass
    
#EXTRA - CLASSE ASTRATTA PROMOZIONE
class Promozione(ABC):
    @abstractmethod
    def promozione_stipendio():
        pass  
 
#CLASSI DERIVATE     
class ImpiegatoFisso(Impiegato, Promozione):
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)

    def calcola_stipendio(self):
        return self.stipendio_base
    
    #funzione extra, se lo stipendio è minore uguale di 1000, lo stipendio aumenta 
    def promozione_stipendio(self):
        if self.stipendio_base <=1000:
            self.bonus_promozione = 250
            self.stipendio_promozione = self.stipendio_base + self.bonus_promozione
            return self.stipendio_promozione 
    
    #funzione informazioni, chiamo il self.calcola_stipendio()
    def informazioni(self):
        print(f"Nome: {self.nome} - Cognome: {self.cognome} - Stipendio: {self.calcola_stipendio()} - Nuovo stipendio: {self.promozione_stipendio()}")
 
    
#aggiunta di n_vendite per il bonus provvigione     
class ImpiegatoAProvvigione(Impiegato, Promozione):
    def __init__(self, nome, cognome, stipendio_base, n_vendite:int):
        super().__init__(nome, cognome, stipendio_base)
        self.n_vendite = n_vendite
        self.bonus_vendite = 8.50
        
    def calcola_stipendio(self):
        #aggiungo un bonus provvigione che moltiplica per il numero delle vendite 
        self.provvigione = self.n_vendite * self.bonus_vendite
        self.stipendio_tot = self.provvigione + self.stipendio_base
        return self.stipendio_tot
    
    #funzione extra, se si ha un n_vendite maggiore uguale di 10, lo stipendio aumenta
    def promozione_stipendio(self):
        if self.n_vendite >= 10:
            self.bonus_promozione = 200
            self.stipendio_promozione = self.stipendio_base + self.bonus_promozione
            return self.stipendio_promozione 
 
            
    #funzione informazioni, chiamo il self.calcola_stipendio()
    def informazioni(self):
        print(f"Nome: {self.nome} - Cognome: {self.cognome} - Stipendio: {self.calcola_stipendio()} - Vendite totali: {self.n_vendite} - Nuovo stipendio: {self.promozione_stipendio()}")

            
    
#creo due impiegati        
p1 = ImpiegatoFisso("Chiara", "Rossi", 1250.5)
p2 = ImpiegatoAProvvigione("Maria", "Bianchi", 1050, 12)
p3 = ImpiegatoFisso("Luca", "Verdi", 985.5)
p4 = ImpiegatoAProvvigione("Marco", "Bianchi", 1050, 8)

p1.informazioni()
p2.informazioni()
p3.informazioni()
p4.informazioni()