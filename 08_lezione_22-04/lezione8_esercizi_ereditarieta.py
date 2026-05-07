#ESERCIZIO 1
#Classe base Animale, classi derivate Leone, Cane, Pesce

#SUPERCLASSE 
class Animale:
    def __init__(self, nome:str, eta:int):
        self.nome = nome
        self.eta = eta
    
    #funzione verso generico
    def fai_suono(self):
            print(f"{self.nome} fa un verso generico!")
      
#SOTTOCLASSI            
class Leone(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        
    def fai_suono(self):
        print(f"{self.nome} ruggisce!")
    
    def caccia(self):
        print(f"Il leone {self.nome} sta cacciando una preda!")

class Cane(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        
    def fai_suono(self):
        print(f"{self.nome} abbaia!")    
            
    def mangia(self):
        print(f"Il cane {self.nome} sta rosicchiando un osso!")

class Pesce(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        
    def fai_suono(self):
        print(f"{self.nome} squittisce!")        
    
    def nuota(self):
        print(f"Il pesciolino {self.nome} sta nuotando nell'acquario!")

#definisco le classi di appartenenza di ogni animale        
animale_gen = Animale("Pippo", 2)
leone1 = Leone("Simba", 5)
cane1 = Cane("Milu", 3)
pesce1 = Pesce("Dory", 3)

#richiamo le classi
animale_gen.fai_suono()
leone1.caccia()
cane1.mangia()
pesce1.nuota()


#ESERCIZIO2
#Gestione fabbrica, classi Prodotto, Elettronica, Abbigliamento, Fabbrica

#classe base
class Prodotto:
    def __init__(self, nome:str, costo_produzione:float, prezzo_vendita:float):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        
    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        return profitto
        
#classi parallele         
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia:bool):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia
        
    def info(self):
        print(f"Garanzia: {self.garanzia}")    
    

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, taglia:str, materiale:str):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.taglia = taglia
        self.materiale = materiale
    
    def info(self):
        print(f"Questo capo d'abbigliamento è di taglia {self.taglia} e di materiale {self.materiale}.")
        

#classe Fabbrica
class Fabbrica():
    
    def __init__(self):
        
        #inventario vuoto
        self.inventario = {}
    
    def aggiungi_prodotto(self, articolo, quantita):
        
        #se l'articolo è già presente aumenta le quantità
        if articolo in self.inventario:
            self.inventario[articolo] += quantita
            print(f"Prodotto: {articolo.nome} - Quantità: {quantita}.")
            
        #altrimenti la quantità aggiunta sarà la quantità effettiva
        else:
            self.inventario[articolo] = quantita
            print(f"Prodotto: {articolo.nome} - Quantità: {quantita}.")
            
    def vendi_prodotto(self, articolo, quantita):
        
        #se l'articolo è presente in inventario e ha una quantità maggiore a quella richiesta
        #si calcola il profitto 
        if articolo in self.inventario and self.inventario[articolo] >= quantita:
            self.inventario[articolo] -= quantita
            profitto_tot = (articolo.calcola_profitto()) * quantita
            print(f"Prodotto venduto: {articolo.nome} - Profitto: {profitto_tot}")
        
        #altrimenti l'articolo non sarà disponibile
        else:
            print("Prodotto non disponibile")
        
    def resi_prodotto(self, articolo, quantita):
        
        #se l'articolo è presente in inventario, la quantità aumenta 
        if articolo in self.inventario:
            self.inventario[articolo] += quantita 
            print(f"Prodotto reso: {articolo.nome} - Quantità: {quantita} ")
        else:
            self.inventario[articolo] = quantita 
            print(f"Prodotto reso: {articolo.nome} - Quantità: {quantita} ")
    
    
#articoli
prodotto1 = Abbigliamento("Maglia", 7.5, 10.5, "S", "Cotone")
prodotto2 = Abbigliamento("Felpa", 12.0, 25.0, "M", "Poliestere")
prodotto3 = Abbigliamento("Jeans", 20.0, 50.0, "L", "Denim")
prodotto4 = Abbigliamento("Giacca", 35.0, 80.0, "XL", "Pelle")
prodotto5 = Elettronica("Computer gaming", 550.0, 600, True)
prodotto6 = Elettronica("Smartphone", 300.0, 499.0, True)
prodotto7 = Elettronica("Tablet", 200.0, 350.0, True)
prodotto8 = Elettronica("Cuffie Bluetooth", 30.0, 79.0, False)
prodotto9 = Elettronica("Monitor 27 pollici", 120.0, 250.0, True)

#creazione fabbrica
fabbrica =Fabbrica()

#prova simulazione 
fabbrica.aggiungi_prodotto(prodotto1, 1)
fabbrica.aggiungi_prodotto(prodotto4, 4)
fabbrica.aggiungi_prodotto(prodotto1, 10)
fabbrica.aggiungi_prodotto(prodotto2, 5)
fabbrica.aggiungi_prodotto(prodotto3, 8)
fabbrica.aggiungi_prodotto(prodotto6, 3)

fabbrica.vendi_prodotto(prodotto1, 2)   
fabbrica.vendi_prodotto(prodotto2, 1)  
fabbrica.vendi_prodotto(prodotto3, 3)  
fabbrica.vendi_prodotto(prodotto6, 2)   
fabbrica.vendi_prodotto(prodotto6, 5)

fabbrica.resi_prodotto(prodotto1, 1)
        
        