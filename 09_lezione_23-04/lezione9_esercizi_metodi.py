#ESERCIZIO 

#CLASSE BASE
class UnitaMilitare:
    def __init__(self, nome:str, numero_soldati:int):
        self.nome = nome
        self.numero_soldati = numero_soldati
    
    #3 metodi    
    def muovi(self):
        print(f"L'unità {self.nome} si sta muovendo.")
    
    def attacca(self):
        print(f"L'unità {self.nome} sta attaccando.")
    
    def ritira(self):
        print(f"L'unità {self.nome} si è ritirata.")
        
    #METODI SPECIALI
    #__str__ restituisce questa stringa se si usa print
    def __str__(self):
        return f"Unità {self.nome} ha {self.numero_soldati} soldati."
    
    #__repr__ rappresentazione tecnica 
    def __repr__(self):
        return f"UnitaMilitare(nome:{self.nome} - numero_soldati:{self.numero_soldati})"
    
    #__eq__ se due unità hanno sia stesso nome che stesso numero di soldati, sono la stessa unità
    def __eq__(self, altro):
        if not isinstance(altro, UnitaMilitare):
            return False
        return self.nome == altro.nome and self.numero_soldati == altro.numero_soldati
    
    #__getattribute__ è come un controllo di ogni accesso
    #si attiva "spesso" nel codice perché quando si vanno a cercare le informazioni si passa da questa classe
    def __getattribute__(self, attributo):
        print(f"Sto accedendo all'attributo: {attributo}")
        return super().__getattribute__(attributo)
        
#CLASSI DERIVATE 
#tutte le classi ereditano da UnitaMilitare e aggiungono un metodo ciascuno
class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        
    def costruisci_trincea(self):
        print(f"L'unità {self.nome} ha costruito difese temporanee.")
        
class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        
    def calibra_artiglieria(self):
        print(f"L'unità {self.nome} sta calibrando i pezzi di artiglieria per la precisione.")
        
class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        
    def esplora_terreno(self):
        print(f"L'unità {self.nome} sta esplorando l'area per raccogliere informazioni sul nemico.")
        
class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        
    def rifornisci_unita(self):
        print(f"L'unità {self.nome} sta gestendo il rifornimento e la manutenzione.")
        
class Ricognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        
    def conduci_ricognizione(self):
        print(f"L'unità {self.nome} sta conducendo missioni di sorveglianza.") 

#---------------------------------------------------------------

#la classe controllo è come se fosse il main script, anche se è una classe ma è una parte "divisa"
#rispetto alle classi. 

#CLASSE CONTROLLO
class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    
    #lista vuota per contenere le unità
    def __init__(self): 
        self.unita_registrate = []
     
    #se un'unità non esiste la aggiunge alla lista   
    def registra_unita(self, unita):
        if unita.nome not in self.unita_registrate:
            self.unita_registrate.append(unita)
            print(f"Unità {unita.nome} aggiunta al registro.")   
    
    #stampa i nomi delle unità        
    def mostra_unita(self):
        lista_nomi = []
        for nome in self.unita_registrate:
            lista_nomi.append(nome)
        print(f"Le unità registrate sono: {lista_nomi}")    
            
    
    #per ogni nome nella lista, controlla se il nome di cui si cercano dettagli esiste nella lista
    #se esiste, stampa i dettagli 
    #ripescate da ClassiMilitari con __str__    
    def dettagli_unita(self, nome):
        nome_trovato = False
        for unita in self.unita_registrate:
            if unita.nome == nome:
                print(f"{unita}")
                nome_trovato = True
                break
        if not nome_trovato:
            print("Unità non esistente")    
    
    #METODI SPECIALI
    #__len__ permette di usare len e conta le unità presenti nella lista
    def __len__(self):
        return len(self.unita_registrate)
    
#SIMULAZIONE
#creazione unità    
u1 = Fanteria("Alpha-1", 150)    
u2 = Artiglieria("Bombarda", 40)
u3 = Cavalleria("Fulmine", 80)

#azioni unità
u1.costruisci_trincea()
u2.calibra_artiglieria()
u3.esplora_terreno()

#funzionamento metodi __str__ e __repr__
print(u1)
print(repr(u2))

#creazione controllo militare
comando = ControlloMilitare()

#registrazione unità
comando.registra_unita(u1)
comando.registra_unita(u2)
comando.registra_unita(u3)

#"lunghezza" unità 
print(f"Registro: {len(comando)} unità.")

#dettagli unità
comando.mostra_unita()
comando.dettagli_unita("Fulmine")
comando.dettagli_unita("Prova")