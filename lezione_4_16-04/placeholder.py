#PROVE CODICE
def funzione2():
    num2 = int(input("Inserisci un numero n per generare una lista di numeri casuali da 1 a n: "))      
    lista1 = []
    for i in range(1, (num2+1)):
        lista1.append(i)
    print(lista1)

#RIVEDERE DA QUI
#prova con una lista già predefinita
def funzione3():    
    numeri = [1, 2, 3, 4, 5, 6]
    #per ogni numero nella lista
    for numero in numeri:
        #se il numero è pari
        if numero % 2 == 0:
            #somma prende il numero
            somma = numero 
            #tengo la somma e parto da capo prendendo un altro numero della lista
            yield somma
            #sommo i due numeri
            nuova_somma = somma + numero
    print(f"La somma è {nuova_somma}") 
                
    
        
        

recap = int(input("Quale punto dell'esercizio di recap vuoi svolgere? Da 1 a 7: "))
    
match recap:
        
    case 3: funzione3()
   
