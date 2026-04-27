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
    #se l'inizializzazione è false non si può prenotare, 
    #altrimenti è prenotabile
    def prenota(self):
        if self._occupato == False:
            print("Ci dispiace, il posto non è prenotabile.")
        else:
            print(f"Il posto numero {self._numero} della fila {self._fila} è stato prenotato.")
    
    #se il posto è occupato cambia l'inizializzazione da false a true per renderlo libero
    def libera(self):
        if self._occupato == False:
            _occupato = True
            print(f"Il posto numero {self._numero} della fila {self._fila} è stato liberato.")
        else:
            print("Il posto non era stato prenotato. ")
      
    #restituisce informazioni su numero, fila e stato occupato      
    def get_info(self):
        return self._numero and self._fila and self._occupato 
    
#CLASSI DERIVATE

#POSTO VIP
class PostoVIP(Posto):
    def __init__(self, servizi_extra:list):
        super().__init__(self._numero, self._fila)
        
        #lista di servizi extra in più
        servizi_extra = ["Accesso al lounge", "Servizio in posto", "Cena inclusa"]
        self.__servizi_extra = servizi_extra
    
    #se il posto è occcupato non è prenotabile, altrimenti si possono scegliere dei servizi extra
    def prenota(self):
        if self._occupato == False:
            print("Ci dispiace, il posto non è prenotabile.")
        else:
            print(f"Il posto numero {self._numero} della fila {self._fila} è stato prenotato.")
            while True:
                comando_posto_vip = int(input("Attivazione servizi extra: 1. Accesso al lounge 2. Servizio in posto 3. Cena inclusa"))
                match comando_posto_vip:
                    
                    #SERVIZI EXTRA DA DEFINIRE
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case _:
                        print("Opzione non disponibile.")
    
#POSTO STANDARD - DA DEFINIRE
class PostoStandard(Posto):
    def __init__(self, costo):
        super().__init__(self._numero, self._fila)
        self.__costo = costo
    
    def prenota(self):
        pass
    
#CLASSE TEATRO - DA DEFNIRE
class Teatro:
    def __init__(self, posti:list):
        self._posti = posti
        
    def aggiungi_posto(self, posto):
        pass
    
    def prenota_posto(self, numero, fila):
        pass
    
    def stampa_posti_occupati(self):
        pass
        
    


# MAIN - DA DEFINIRE
while True:
    comando = input("Vuoi accedere al teatro? SI / NO - ")
    match comando: 
        case "SI":
            comando2 = int(input("A quale servizio vuoi accedere? 1. Prenota posto 2. Libera posto - "))
            match comando2:
                case 1:
                    comando3 = int(input("1. Prenotazione Posto Standard 2. Prenotazione Posto VIP - "))
                    match comando3:
                        
                        case 1:
                            pass
                        
                        case 2:
                            pass
                        
                case 2:
                    pass
                
                case _:
                    print("Opzione non disponibile.")
                
                
                
        case "NO":
            break
        
        case _: 
            print("Opzione non disponibile.")
            