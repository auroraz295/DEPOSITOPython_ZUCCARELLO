#TEST PRATICO 08-05
#sistema che permetta di leggere file txt/csv e stampi i risultati, permettendo di
#modificarli, aggiungerli, eliminarli
#il menu deve poter analizzare i dati

#MODULO LIBRO

#CLASSE BASE LIBRO
class Libro:
    def __init__(self, codice:int, nome:str, genere:str, autore:str, stato:str, prezzo:float):
        self.__codice = codice
        self.__nome = nome
        self.__genere = genere
        self.__autore = autore
        self.__stato = stato
        self.__prezzo = prezzo
        
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
    
    #stato
    def get_stato(self):
        return self.__stato
    
    def set_stato(self, nuovo_stato):
        self.__stato = nuovo_stato
        return self.__stato
    
    #prezzo
    def get_prezzo(self):
        return self.__prezzo
    
    def set_prezzo(self, nuovo_prezzo):
        self.__prezzo = nuovo_prezzo
        return self.__prezzo
        
    #FUNZIONE DESCRIZIONE LIBRO
    def descrizione(self):
        print(f"Libro: {self.__nome} - Genere: {self.__genere} - Autore: {self.__autore} - Stato: {self.__stato} - Prezzo: {self.__prezzo}")
        
        