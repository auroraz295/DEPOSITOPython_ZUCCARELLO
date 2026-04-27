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


