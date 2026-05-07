#GESTIONE CLIENTI
# - visualizzare articoli in inventario
# - selezionare e acquistare articoli dall'inventario
# - salvare acquisti del cliente in un file

class Cliente:
    def __init__(self):
        #dizionario registrazione/login cliente
        self.elenco_clienti = {"nome cliente": [],
                               "password utente" : []
                               }
        
        #lista acquisti clienti
        self.acquisti_cliente = []
    
    #FUNZIONE REGISTRAZIONE UTENTE    
    def registrazione(self):
        #inizializzazione dizionario vuoto per login e registrazione clienti
        input_nome = input("Inserisci nome utente: ")
        input_password = int(input("Inserisci password (4 cifre) : "))
        
        #aggiunge il nome e la password inserite nella lista del dizionario
        self.elenco_clienti["nome cliente"].append(input_nome)
        self.elenco_clienti["password utente"].append(input_password)
        
        #creazione file di testo con credenziali utenti
        with open("gestione_clienti.txt", "a") as f:
                        f.write(f"Nome utente: {input_nome} - Password: {input_password} \n")
        
        print(f"Registrazione utente {input_nome} effettuata.")
     
    #FUNZIONE ACCESSO UTENTE    
    def accesso(self):
        input_nome = input("Inserisci il nome utente: ")
        input_password = int(input("Inserisci una password da 4 cifre : "))
        
        #se il nome e è nei nomi utenti
        if input_nome in self.elenco_clienti["nome cliente"]: 
            
            #recupero l'indice del nome utente cliente
            indice_cliente = self.elenco_clienti["nome cliente"].index(input_nome)
            
            #se la password dell'indice corretto corrisponde a quella inserita
            if self.elenco_clienti["password utente"][indice_cliente] == input_password: 
                print("Accesso eseguito.")
                return True
        else:
            print("Nome utente o password errate. Riprova.")
            return False
            
    def acquista(self, inventario, admin):
       while True: 
        #richiamo visualizza articoli di inventario per mostrare le disponibilità prodotti
        comando_acquista = int(input("1. Acquista - 2. Esci // "))
        
        match comando_acquista:
            case 1: 
                inventario.visualizza_articoli()
                scelta_acquisto = input("Quale articolo vuoi acquistare? ")
        
                #se l'articolo selezionato esiste nell'inventario
                if scelta_acquisto in inventario.diz_articoli["nome articolo"]:
                    indice_articolo = inventario.diz_articoli["nome articolo"].index(scelta_acquisto)
                    quantita_acquisto = int(input("Quanti ne vuoi acquistare? "))
            
                    #se la quantità richiesta è disponibile
                    if inventario.diz_articoli["quantità articolo"][indice_articolo]>= quantita_acquisto:
                
                        #viene sottratta dalla quantità dell'inventario
                        inventario.diz_articoli["quantità articolo"][indice_articolo]-= quantita_acquisto
                
                        #calcolo prezzo
                        prezzo = inventario.diz_articoli["prezzo articolo"][indice_articolo] * quantita_acquisto

                        #lo restituisco ad admin per i guadagni
                        admin.guadagni += prezzo
                        
                        admin.report_vendite.append(f"Articolo {scelta_acquisto} - Quantità: {quantita_acquisto}")
                        
                        #aggiungo l'ordine nel file.txt
                        self.acquisti_cliente.append({"nome articolo" : scelta_acquisto, "quantità articolo" : quantita_acquisto, "prezzo totale" : prezzo})
                
                        #print prezzo ordine
                        print(f"Totale speso: {prezzo}")
                        continue
                
                    else:
                        print("Quantità non disponibile.")
                        break
                
                else:
                    print("Articolo non disponibile.")
                    break
            
            case 2:
                print("Uscita menu")
                break
           