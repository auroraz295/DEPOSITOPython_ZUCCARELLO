#GESTIONE OFFICINA ELETTRODOMESTICI

#importo collezione abc per l'astrazione
from abc import ABC, abstractmethod

#CLASSE BASE - ELETTRODOMESTICO
class Elettrodomestico():
    def __init__(self, marca:str, modello:str, anno_acquisto:int, guasto:str):
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto
     
    #METODI   
    def descrizione(self):
        print(f"Marca: {self.get_marca()} - Modello: {self.get_modello()} - Anno acquisto: {self.get_anno_acquisto()} - Guasto: {self.get_guasto()}")
    
    def stima_costo_base(self):
        self.__costo_base = 100
        return self.__costo_base
        
    #GET E SET MARCA ELETTRODOMESTICO    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, nuova_marca):
        self.__marca = nuova_marca
        return self.__marca
    
    #GET E SET MODELLO ELETTRODOMESTICO
    def get_modello(self):
        return self.__modello
    
    def set_modello(self, nuovo_modello):
        self._modello = nuovo_modello
        return self.__modello
    
    #GET E SET ANNO ACQUISTO ELETTRODOMESTICO
    def get_anno_acquisto(self):
        return self.__anno_acquisto
    
    def set_anno_acquisto(self, nuovo_anno_acquisto):
        if nuovo_anno_acquisto <= 2026:
            self.__anno_acquisto = nuovo_anno_acquisto
            return self.__anno_acquisto
        else:
            print("Anno acquisto non valido.")
    
    #GET E SET GUASTO ELETTRODOMESTICO
    def get_guasto(self):
        return self.__guasto
    
    def set_guasto(self, nuovo_guasto):
        self.__guasto = nuovo_guasto
        return self.__guasto
         

#CLASSI DERIVATE 
#LAVATRICE
class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg:int, giri_centrifuga:int):
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        self.__capacita_kg = capacita_kg
        self.__giri_centrifuga = giri_centrifuga
     
    #METODO STIMA COSTO   
    def stima_costo_base(self):
        
        #bonus attributi aggiuntivi
        self.__bonus_capacita = 25
        self.__bonus_giri =  40

        
        #condizioni per il bonus
        if self.__capacita_kg <= 10:
            
            if self.__giri_centrifuga <=30:
                print(f"Costo base manutenzione: {self.stima_costo_base()}") 
            else:
                print(f"Costo base manutenzione: {self.stima_costo_base() + self.__bonus_giri}") 
        
        elif self.__capacita_kg > 10:

            if self.__giri_centrifuga <=30:
                print(f"Costo base manutenzione: {self.stima_costo_base() + self.__bonus_capacita}") 
            else:
                print(f"Costo base manutenzione: {self.stima_costo_base() + self.__bonus_capacita + self.__bonus_giri}") 
            
        else:
            print("Costo base non disponibile.")
 
#CLASSE FRIGORIFERO         
class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, litri:int, ha_freezer:bool):
        super().init(marca, modello, anno_acquisto, guasto)
        
        self.__litri = litri
        self.__ha_freezer = ha_freezer
        
    def stima_costo_base(self):
        
        #bonus attributi aggiuntivi
        self.__bonus_litri = 50
        self.__bonus_freezer =  75

        
        #condizioni per il bonus
        if self.__litri <= 10:
            
            if self.__ha_freezer == False:
                print(f"Costo base manutenzione: {self.stima_costo_base()}") 
            else:
                print(f"Costo base manutenzione: {self.stima_costo_base() + self.__bonus_freezer}") 
        
        elif self.__litri > 10:

            if self.__ha_freezer == True:
                print(f"Costo base manutenzione: {self.stima_costo_base() + self.__bonus_litri + self.__bonus_freezer}") 
            else:
                print(f"Costo base manutenzione: {self.stima_costo_base() + self.__bonus_litri}") 
            
        else:
            print("Costo base non disponibile.")    

#CLASSE FORNO 
class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, alimentazione, ventilato):
        super().init(marca, modello, anno_acquisto, guasto)
        
        self.__alimentazione = alimentazione #"elettrico" o "gas"
        self.__ventilato = ventilato