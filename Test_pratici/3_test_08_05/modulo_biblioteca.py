from modulo_libro import Libro
from modulo_gestione_file import salva_catalogo, salva_prenotati, salva_venduti

#MODULO GESTIONALE BIBLIOTECA
class Biblioteca:
    def __init__(self):
        self.__catalogo_completo = [Libro(101, "Il nome della rosa", "Giallo", "Umberto Eco", "Disponibile", 14.50),
                                    Libro(102, "1984", "Distopico", "George Orwell", "Disponibile", 12.00),
                                    Libro(103, "Dune", "Fantascienza", "Frank Herbert", "Disponibile", 18.90),
                                    Libro(104, "Assassinio sull'Orient Express", "Giallo", "Agatha Christie", "Disponibile", 9.99),
                                    Libro(105, "Lo Hobbit", "Fantasy", "J.R.R. Tolkien", "Disponibile", 15.50),
                                    Libro(106, "Il Grande Gatsby", "Classico", "F. Scott Fitzgerald", "Disponibile", 11.00),
                                    Libro(107, "Harry Potter e la Pietra Filosofale", "Fantasy", "J.K. Rowling", "Disponibile", 16.00),
                                    Libro(108, "Cronaca di una morte annunciata", "Giallo", "Gabriel García Márquez", "Disponibile", 10.50),
                                    Libro(109, "Fondazione", "Fantascienza", "Isaac Asimov", "Disponibile", 13.00),
                                    Libro(110, "Il Signore degli Anelli", "Fantasy", "J.R.R. Tolkien", "Disponibile", 25.00)
                                    ]
        
        
        self.__catalogo_prenotati = []
        self.__catalogo_venduti = []
    
    #GET LISTE CATALOGHI
    #completo
    def get_catalogo_completo(self):
        return self.__catalogo_completo
    
    #prenotati
    def get_catalogo_prenotati(self):
        return self.__catalogo_prenotati
    
    #venduti
    def get_catalogo_venduti(self):
        return self.__catalogo_venduti
    
    #FUNZIONE STAMPA LIBRI
    #visualizza tutti i libri 
    
    def stampa(self):
        #stampa lista libri
        for libro in self.__catalogo_completo:
            print(f"Codice: {libro.get_codice()} - Libro: {libro.descrizione()}") 
     
    #FUNZIONE AGGIUNTA LIBRO  
    def aggiungi(self):
        codice = int(input("Codice: "))
        nome = input("Nome: ")
        genere = input("Genere: ")
        autore = input("Autore: ")
        stato = "Disponibile"
        prezzo = float(input("Prezzo: "))
        
        #creazione oggetto libro e aggiunta al catalogo
        libro = Libro(codice, nome, genere, autore, stato, prezzo)
        self.__catalogo_completo.append(libro)

        #salvo libro in file txt
        salva_catalogo(libro)
    
        print(f"Aggiunto: {libro.descrizione()}")
        
    #FUNZIONE PRENOTAZIONE LIBRO
    def prenota(self):
        #scelta utente  
        prenotazione = int(input("Inserisci il codice libro da prenotare: "))
        
        for libro in self.__catalogo_completo:
            if prenotazione == libro.get_codice() and libro.get_stato() == "Disponibile":
                
                #cambio stato
                nuovo_stato = "Prenotato"
                libro.set_stato(nuovo_stato)
                
                #aggiunta lista prenotati
                self.__catalogo_prenotati.append(libro)
                #salva prenotati su file 
                salva_prenotati(self.__catalogo_prenotati)
            
                print(f"Libro: {libro.get_nome()} - Stato: {libro.get_stato()} ")
           
            else:
                print("Libro non diponibile per la prenotazione.")
                
    #FUNZIONE VENDITA LIBRO
    def vendi(self):
        #scelta utente 
        vendita = int(input("Inserisci il codice libro da vendere: "))
        
        for libro in self.__catalogo_completo:
            if vendita == libro.get_codice() and libro.get_stato() == "Disponibile":
                
                #cambio stato
                nuovo_stato = "Venduto"
                libro.set_stato(nuovo_stato)
                
                #aggiunta lista venduti
                self.__catalogo_venduti.append(libro)
                #salva venduti su file 
                salva_venduti(self.__catalogo_venduti)
            
                print(f"Libro: {libro.get_nome()} - Stato: {libro.get_stato()} ")
           
            else:
                print("Libro non diponibile per la vendita.")
        
    
                
        