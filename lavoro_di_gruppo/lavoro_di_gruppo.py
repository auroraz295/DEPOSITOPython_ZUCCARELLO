#GESTIONE OFFICINA ELETTRODOMESTICI

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
        self.__bonus_capacita = {self.stima_costo_base()} + 25
        self.__bonus_giri = {self.stima_costo_base()} + 40

        
        #condizioni per il bonus
        if self.__capacita_kg <= 10:
            
            if self.__giri_centrifuga <=30:
                print(f"Costo base manutenzione: {self.stima_costo_base()}") 
            elif self.__giri_centrifuga > 30:
                print(f"Costo base manutenzione: {self.__bonus_capacita}") 
            
        elif self.__capacita_kg > 10 or self.__giri_centrifuga > 30:
            self.costo_aggiornato = {self.stima_costo_base()} + self.__bonus_capacita + self.__bonus_giri
            print(f"Costo base manutenzione: {self.costo_aggiornato}")
        
        else:
            print("Costo base non disponibile.")
        
    
