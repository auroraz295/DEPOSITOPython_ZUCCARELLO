#ESERCIZIO 1
#creare una classe base MetodoPagamento e diverse classi derivate che rappresentano
#diversi metodi di pagamento. Questo scenario permetterà di vedere il polimorfismo in
#azione, permettendo alle diverse sottoclassi di implementare i loro specifici
#comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe
#base.
import random 

#SUPERCLASSI
class Utente:
    def __init__(self):
        self.nome = input("Inserisci il tuo nome: ")
        self.importo_da_pagare = random.randint(1,100)
        print(f"Hai un credito di {self.importo_da_pagare} euro.")
        
    #metto un get che mi servirà per recuperare l'importo    
    def get_importo(self):
        return self.importo_da_pagare
    
class MetodoPagamento:
    def effettua_pagamento(self, importo):
        print(f"Hai pagato {importo} euro.")

#SOTTOCLASSI      
#per ogni funzione effettua_pagamento si arrotonda l'importo da pagare e si printa
#si sovrascrive ogni print con l'override 
#polimorfismo: le funzioni hanno lo stesso nome ma comportamenti diversi
 
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        importo_scontato = round(importo * 1.03, 2)
        print(f"Hai pagato {importo_scontato} euro con un tasso del 3%.")
        
class Paypal(MetodoPagamento):
     def effettua_pagamento(self, importo): 
        importo_scontato = round(importo * 1.05,2)
        print(f"Hai pagato {importo_scontato} euro con un tasso del 5%.")

class BonificoBancario(MetodoPagamento):
     def effettua_pagamento(self, importo):
        importo_scontato = round(importo * 1.02,2)
        print(f"Hai pagato {importo_scontato} euro con un tasso del 2%.")

#MAIN    
#funzione paga, che prende come parametri l'importo scelto e il metodo scelto
#grazie al polimorfismo prende l'oggetto che è MetodoPagamento ed esegue la funzione giusta
class GestorePagamenti():
    def paga(self, metodo:MetodoPagamento, importo):
        metodo.effettua_pagamento(importo)
        
        
#SIMULAZIONE
gestione = GestorePagamenti()

metodo_scelto1 = CartaDiCredito()
metodo_scelto2 = Paypal()
metodo_scelto3 = BonificoBancario() 
metodo_scelto4 = MetodoPagamento()

utente1 = Utente()
importo1 = utente1.get_importo()

comando = int(input("Con quale metodo vuoi pagare? 1. Standard - 2. Carta di credito: tasso - 3. Paypal: tasso 5% - 4. Bonifico bancario: tasso 2% "))
match comando: 
    case 1:
        gestione.paga(metodo_scelto4, importo1)
        
    case 2:
        gestione.paga(metodo_scelto1, importo1)

    case 3:
        gestione.paga(metodo_scelto2, importo1)

    case 4:
        gestione.paga(metodo_scelto3, importo1)


#ESERCIZIO2 

#CLASSE BASE - posto
class Posto:
    def __init__(self, numero:int, fila:str):
        self._numero = numero 
        self._fila = fila
        self._occupato = False 
        
    #PRENOTAZIONE
    #se l'inizializzazione è False non si può prenotare, 
    #altrimenti è prenotabile e poi lo stato occupato diventa True
    def prenota(self):
        if self._occupato == True:
            print("Ci dispiace, il posto non è prenotabile.")
        else:
            self._occupato = True
            print(f"Il posto numero {self._numero} della fila {self._fila} è stato prenotato.")
    
    #se il posto è occupato cambia l'inizializzazione da false a true per renderlo libero
    def libera(self):
        if self._occupato == True:
            self._occupato = False
            print(f"Il posto numero {self._numero} della fila {self._fila} è stato liberato.")
        else:
            print("Il posto non era stato prenotato. ")
      
    #restituisce informazioni su numero, fila e stato occupato      
    def get_info_numero(self):
        return self._numero
    
    def get_info_fila(self):
        return self._fila 
    
    def get_info_occupato(self):
        return self._occupato 
    
#CLASSI DERIVATE

#POSTO VIP
class PostoVIP(Posto):
    def __init__(self, numero, fila):
        super().__init__(numero, fila)
        
        #lista di servizi extra in più
        servizi_extra = ["Accesso al lounge", "Servizio in posto", "Cena inclusa"]
        self.__servizi_extra = servizi_extra
    
    #se il posto è occcupato non è prenotabile, altrimenti si possono scegliere dei servizi extra
    def prenota(self):
        if self._occupato == True:
            print("Ci dispiace, il posto non è prenotabile.")
        else:
            self._occupato = True
            print(f"Il posto VIP numero {self._numero} della fila {self._fila} è stato prenotato.")
            
            #menu per la scelta dei servizi_extra
            while True:
                comando_posto_vip = int(input("Attivazione servizi extra: 1. Accesso al lounge 2. Servizio in posto 3. Cena inclusa - "))
                match comando_posto_vip:
                    
                    case 1:
                        print(f"Servizio extra {self.__servizi_extra[0]} aggiunto alla prenotazione.")
                        break
                    case 2:
                        print(f"Servizio extra {self.__servizi_extra[1]} aggiunto alla prenotazione.")
                        break
                    case 3:
                        print(f"Servizio extra {self.__servizi_extra[2]} aggiunto alla prenotazione.")
                        break
                    case _:
                        print("Opzione non disponibile.")
                        break
    
#POSTO STANDARD 
class PostoStandard(Posto):
    def __init__(self, numero, fila):
        super().__init__(numero, fila)
        
        self._costo = 7.50
    
    def prenota(self):
        if self._occupato == True:
            print("Ci dispiace, il posto non è prenotabile.")
        else:
            #c'è un costo aggiuntivo, si chiede all'utente se si è sicuri di comprare il biglietto
            comando_posto_standard = input(f"Comprare il biglietto online ha un costo aggiuntivo di {self._costo} euro. Procedere? SI / NO ")
            match comando_posto_standard:
                case "SI":
                    self._occupato = True
                    print(f"Il posto Standard numero {self._numero} della fila {self._fila} è stato prenotato.")
                
                case "NO":
                    print("Tornare al menu principale.")

#CLASSE TEATRO 
class Teatro:
    def __init__(self):
        posti = []
        self._posti = posti
        
    #aggiunge l'oggetto posto alla lista
    def aggiungi_posto(self, posto:Posto):
        self._posto = posto 
        self._posti.append(posto)
    
    #cerca il posto nella lista e chiama il metodo prenota
    def prenota_posto(self, numero, fila):
        for p in self._posti:
            if p.get_info_numero() == numero and p.get_info_fila() == fila:
                p.prenota()
                break
        else:
            print("Il posto non esiste.")
     
    #cerca il posto nella lista e se lo trova chiama il metodo libera       
    def libera_posto(self, numero, fila):
        for p in self._posti:
            if p.get_info_numero() == numero and p.get_info_fila() == fila:
                p.libera()
                break
        else:
            print("Il posto non esiste.")  
    
    #per ogni oggetto nella lista, se lo stato è occupato allora stampa le informazioni
    def stampa_posti_occupati(self):
        trovato = False
        for p in self._posti:
            if p.get_info_occupato() == True:
                print(f"Numero: {p.get_info_numero()} - Fila: {p.get_info_fila()}")
                trovato = True
        if trovato == False:
            print("Non ci sono posti occupati.")

#creo teatro
prova_teatro = Teatro()

prova_teatro.aggiungi_posto(PostoStandard(1, "A"))
prova_teatro.aggiungi_posto(PostoStandard(2, "A"))
prova_teatro.aggiungi_posto(PostoVIP(10, "VIP"))

# MAIN 
while True:
    comando = input("Vuoi accedere al teatro? SI / NO - ")
    match comando: 
        case "SI":
            comando2 = int(input("A quale servizio vuoi accedere? 1. Prenota posto 2. Libera posto 3. Stampa posti occupati - "))
            match comando2:
                
                #prenota posto
                case 1:
                    num = int(input("Inserisci il numero posto: "))
                    fila = input("Inserisci la fila: ")
                    prova_teatro.prenota_posto(num, fila)
                
                #libera posto        
                case 2:
                    num = int(input("Inserisci il numero posto: "))
                    fila = input("Inserisci la fila: ")
                    prova_teatro.libera_posto(num, fila)
                
                #stampa posti occupati
                case 3:
                    prova_teatro.stampa_posti_occupati()
                
                case _:
                    print("Opzione non disponibile.")     
                      
        case "NO":
            break
        
        case _: 
            print("Opzione non disponibile.")
            