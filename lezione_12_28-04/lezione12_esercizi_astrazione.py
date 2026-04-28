#ESERCIZIO 1 
#Un'azienda vuole gestire i suoi impiegati tramite un sistema informatico. Esistono
#diversi ruoli all'interno dell'ufficio, ma tutti gli impiegati hanno alcune
#caratteristiche comuni, come il nome, il cognome e lo stipendio. 
#Inoltre, ogni impiegato ha un metodo per calcolare il suo stipendio mensile, che
#può variare a seconda del ruolo.


#import per la classe astratta
from abc import ABC, abstractmethod
'''
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
'''
#ESERCIZIO 2
#Sistema Astratto di Trasporto Merci

#CLASSE ASTRATTA
class VeicoloTrasporto(ABC):
    def __init__(self, targa:str, peso_massimo:int):
        self._targa = targa
        self._peso_massimo = peso_massimo
        
        #inizializzazione a zero
        carico_attuale = 0 
        self._carico_attuale = carico_attuale
    
    #se il peso da caricare è minore del peso massimo, si aggiunge il carico    
    def carica(self, peso):
        if peso <= self._peso_massimo:
            self._carico_attuale += peso
            return self._carico_attuale
        else:
            print("Peso non consentito, supera la capacità del veicolo.")
    
    #inizializza il carico attuale di nuovo a zero
    def scarica(self):
        self._carico_attuale = 0
        return self._carico_attuale
    
    #METODO ASTRATTO per il costo manutenzione
    @abstractmethod
    def costo_manutenzione():
        pass
    
    #restituisce targa e carico
    def get_targa(self):
        return self._targa
        
    def get_carico(self):
        return self._carico_attuale

#SOTTOCLASSI CONCRETE   
class Camion(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo, numero_assi:int):
        super().__init__(targa, peso_massimo)
        
        self._numero_assi = numero_assi
    
    #override costo manutenzione con personalizzazione numero assi    
    def costo_manutenzione(self):
        self._costo_manutenzione = (100*self._numero_assi) + (1*self._carico_attuale)
        return self._costo_manutenzione
    
    def get_tipo(self):
        tipo = "Camion"
        return tipo
        
        
    
class Furgone(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo, alimentazione:str):
        super().__init__(targa, peso_massimo)
        
        self._alimentazione = alimentazione
    
    #override costo manutenzione con personalizzazione elettrico/diesel
    def costo_manutenzione(self):
        if self._alimentazione == "Elettrico":
            self._costo_manutenzione = 200 + (1*self._carico_attuale)
            return self._costo_manutenzione
        elif self._alimentazione == "Diesel":
            self._costo_manutenzione = 150 + (1*self._carico_attuale)
            return self._costo_manutenzione
        else:
            print("Costo manutenzione non disponibile.")  
        
    def get_tipo(self):
        tipo = "Furgone"
        return tipo
         
        
class Motocarro(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo, anni_servizio:int):
        super().__init__(targa, peso_massimo)
        
        self._anni_servizio = anni_servizio
    
    def costo_manutenzione(self):
        self._costo_manutenzione = (50*self._anni_servizio) + (1*self._carico_attuale)
        return self._costo_manutenzione
    
    #da rivedere con tyype(v)
    def get_tipo(self):
        tipo = "Motocarro"
        return tipo
        

#MAIN
class GestoreFlotta:
    def __init__(self):
        veicoli = []
        self.veicoli = veicoli
        
    def aggiungi_veicolo(self, veicolo:VeicoloTrasporto):
        self.veicoli.append(veicolo)
    
    def rimuovi_veicolo(self, targa):
        #check di ogni veicolo nella lista
        for v in self.veicoli:
            #se una targa di un veicolo corrisponde alla targa immessa, rimuove dalla lista
            if v.get_targa() == targa:
                self.veicoli.remove(v)
    
    def costo_totale_manutenzione(self):
        somma_costo = 0
        for v in self.veicoli:
            somma_costo +=  v.costo_manutenzione() 
        print(f"Somma costi manutenzione: {somma_costo}")
    
    def stampa_veicoli(self):
        for v in self.veicoli:
            print(f"Targa veicolo: {v.get_targa()}- Tipo veicolo: {v.get_tipo()} - Carico attuale: {v.get_carico()}")
    
v1 = Camion("XC102DY", 200, 3)
v2 = Furgone("AA374HC", 350, "Diesel")
v3 = Furgone("GN812WA", 250, "Elettrico")
v4 = Motocarro("LT459SZ", 400, 15)


gestione = GestoreFlotta()

gestione.aggiungi_veicolo(v1)
gestione.aggiungi_veicolo(v2)
gestione.aggiungi_veicolo(v3)
gestione.aggiungi_veicolo(v4)
gestione.stampa_veicoli()
gestione.costo_totale_manutenzione()
v1.carica(100)
gestione.stampa_veicoli()

while True:
    comando = input("Vuoi aprire il Gestore Flotta? SI / NO ")
    match comando:
        case "SI":
            comando2 = int(input("Cosa vuoi fare? 1. Aggiungere un veicolo - 2. Rimuovere un veicolo - 3. Stampare la somma dei costi di manutenzione - 4. Stampare tutti i veicoli - "))
            match comando2:
                case 1:
                    targa = input("Scrivi la targa: ")
                    peso_massimo = int(input("Inserisci il peso massimo in kg: "))
                    numero_assi = int(input("Se è un camion, inserisci il numero di assi: "))
                    alimentazione = input("Se è un furgone, inserisci l'alimentazione: Diesel / Elettrico")
                    anni_servizio = int(input("Se è un motocarro, inserisci gli anni di servizio: "))
                    
                    camion = Camion(targa, peso_massimo, numero_assi)
                    furgone = Furgone(targa, peso_massimo, alimentazione)
                    motocarro = Motocarro(targa, peso_massimo, anni_servizio)
                    
                    if camion:
                        pass
                        
                case 2:
                    pass
                
                case 3:
                    pass
                
                case 4:
                    pass
                
                case _:
                    print("Opzione non disponibile.")
                    
        
        case "NO":
            print("Gestore flotta chiuso.")
            break
        
        case _: 
            print("Opzione non disponibile.")