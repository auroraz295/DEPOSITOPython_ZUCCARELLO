#GESTIONE INVENTARIO
# - aggiungere nuovi articoli
# - rimuovere o aggiornare articoli

class Inventario:
    def __init__(self):
        self.diz_articoli = {"nome articolo": ["Pizza", "Coca Cola", "Patatine"],
                             "prezzo articolo": [7.50, 4.00, 3.50],
                             "quantità articolo": [20, 50, 30]
                            }
                             
    #STAMPA INVENTARIO   
    def visualizza_articoli(self):
        print(self.diz_articoli["nome articolo"])
        
    def visualizza_stato(self):
        
        #per ogni elemento del dizionario, stampo nome, prezzo e quantità
        for i in range(len(self.diz_articoli["nome articolo"])):
            nome = self.diz_articoli["nome articolo"][i]
            prezzo = self.diz_articoli["prezzo articolo"][i]
            quantità = self.diz_articoli["quantità articolo"][i]
            print(f"Articolo: {nome} - Prezzo: {prezzo} - Quantità: {quantità}")
    
    #AGGIUNGI ARTICOLO
    def aggiungi_articoli(self):
        nome_articolo = input("Inserisci il nome articolo: ")
        prezzo_articolo = float(input("Inserisci il prezzo: "))
        quantita_articolo = int(input("Inserisci la quantità: "))
        
        #aggiungo l'articolo, il prezzo e la quantità nelle liste del dizionario
        self.diz_articoli["nome articolo"].append(nome_articolo)
        self.diz_articoli["prezzo articolo"].append(prezzo_articolo)
        self.diz_articoli["quantità articolo"].append(quantita_articolo)
        
        #stampo l'articolo aggiunto
        print(f"Aggiunto {nome_articolo} - Prezzo: {prezzo_articolo} - Quantità: {quantita_articolo}")
    
    #MODIFICA ARTICOLI 
    def modifica_articoli(self):
        self.diz_articoli.get("nome articolo")
        modifica_articolo = input("Quale articolo vuoi modificare? ")
        
        #se l'articolo è nel dizionario
        if modifica_articolo in self.diz_articoli.get("nome articolo"):
            
            #recupero l'indice di quell'articolo
            indice_articolo = self.diz_articoli["nome articolo"].index(modifica_articolo)
            
            modifica2 = input("Vuoi modificare la quantità o il prezzo? ")
            if modifica2 == "quantità":
                quantita = int(input("Inserisci la nuova quantità: "))
                
                #modifica la quantita dell'indice corretto
                self.diz_articoli["quantità articolo"][indice_articolo] = quantita
                
            elif modifica2 == "prezzo":
                prezzo = int(input("Inserisci il nuovo prezzo: "))
                
                #modifica il prezzo dell'indice corretto
                self.diz_articoli["prezzo articolo"][indice_articolo] = prezzo
            else: 
                print("Opzione non disponibile.")
        else:
            print("L'articolo scelto non è modificabile.")
    
    #RIMUOVI ARTICOLI        
    def rimuovi_articoli(self):
        self.diz_articoli.get("nome articolo")
        rimuovi_articolo = input("Quale articolo vuoi rimuovere? ")
        
        #se l'articolo è presente nel dizionario
        if rimuovi_articolo in self.diz_articoli.get("nome articolo"):
            
            #trova l'indice dell'articolo
            indice_articolo = self.diz_articoli["nome articolo"].index(rimuovi_articolo)
            
            #POP - rimuove l'elemento in base all'indice
            self.diz_articoli["nome articolo"].pop(indice_articolo)
            self.diz_articoli["prezzo articolo"].pop(indice_articolo)
            self.diz_articoli["quantità articolo"].pop(indice_articolo)
                 