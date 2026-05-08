#TEST PRATICO 08-05
#sistema che permetta di leggere file txt/csv e stampi i risultati, permettendo di
#modificarli, aggiungerli, eliminarli
#il menu deve poter analizzare i dati

#MODULO LIBRO

#CLASSE BASE LIBRO
class Libro:
    def __init__(self, codice:int, nome:str, genere:str, autore:str, prezzo:float, stato:str):
        self.__codice = codice
        self.__nome = nome
        self.__genere = genere
        self.__autore = autore
        self.__prezzo = prezzo
        self.__stato = stato
    
        
    #GETTER E SETTER ATTRIBUTI
    
    #codice
    def get_codice(self):
        return self.__codice
    
    def set_codice(self, nuovo_codice):
        self.__codice = nuovo_codice
        return self.__codice
    
    #nome
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nuovo_nome):
        self.__nome = nuovo_nome
        return self.__nome
    
    #genere
    def get_genere(self):
        return self.__genere
    
    def set_genere(self, nuovo_genere):
        self.__genere = nuovo_genere
        return self.__genere
    
    #autore
    def get_autore(self):
        return self.__autore
    
    def set_autore(self, nuovo_autore):
        self.__autore = nuovo_autore
        return self.__autore
    
    #prezzo
    def get_prezzo(self):
        return self.__prezzo
    
    def set_prezzo(self, nuovo_prezzo):
        self.__prezzo = nuovo_prezzo
        return self.__prezzo
    
    #stato
    def get_stato(self):
        return self.__stato
    
    def set_stato(self, nuovo_stato):
        self.__stato = nuovo_stato
        return self.__stato
    
    #METODO SPECIALE STR
    def __str__(self):
        return f"{self.get_codice()}, {self.get_nome()}, {self.get_genere()}, {self.get_autore()}, {self.get_prezzo()}, {self.get_stato()}"
        
    #FUNZIONE DESCRIZIONE LIBRO
    def descrizione(self):
        print(f"Codice: {self.__codice} - Libro: {self.__nome} - Genere: {self.__genere} - Autore: {self.__autore} - Prezzo: {self.__prezzo} - Stato: {self.__stato}")
        
        