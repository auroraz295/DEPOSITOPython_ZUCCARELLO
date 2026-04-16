#1. Indovina il numero

import random 

def indovina():
    #random genera un numero casuale float, poi convertito in int, da 1 a 100 inclusi
    num_cas = int(random.uniform(1,100))
   
    while True:
        #input iniziale
        tent1 = int(input("Facciamo un gioco: indovina un numero da 1 a 100! "))
        
        #se il numero è diverso dal numero casuale
        if tent1 != num_cas:
            #restituisce una stampa se è più alto o più basso
            if tent1<num_cas:
                print("Mi dispiace, il numero da indovinare è più alto!")
            if tent1>num_cas:
                print("Mi dispiace, il numero da indovinare è più basso!")
            
            #tentativo 2
            tent2 = input("Vuoi riprovare?")
            if tent2 == "si":
                #esegue il codice dall'inizio
                continue
            else:
                #termina il gioco
                print("Gioco terminato.")
                break
            
        #se il numero è esatto printa la frase e termina il gioco    
        elif tent1 == num_cas:
            print(f"Hai indovinato! Il numero era {num_cas}!")
            break
            
indovina()

#2. Sequenza di Fibonacci fino al numero N