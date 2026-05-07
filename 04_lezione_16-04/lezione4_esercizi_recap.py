#ESERCIZIO RECAP 
import random

def funzione1():
    while True:
        num1 = int(input("Inserisci un numero intero positivo: "))
        #se il numero non è positivo ripeto il ciclo
        if num1 <0 or num1 == 0:
            continue 
        else:
            break
        
def funzione2():
    num2 = int(input("Inserisci un numero n per generare una lista di numeri casuali da 1 a n: "))      
    lista1 = []
    #per ogni x volte (determinate dal numero scelto)
    for i in range(1, (num2+1)):
        #crea un numero casuale da 1 a n e aggiungilo alla lista
        num_cas = random.randint(1, num2)
        lista1.append(num_cas)
    print(lista1)
    return lista1

def funzione3(lista1):    
    #contatore somma 
    somma = 0
    #per ogni numero nella lista
    for numero in lista1:
        #se il numero è pari
        if numero % 2 == 0:
            #somma prende il numero
            somma += numero 
    print(f"La somma è {somma}") 
        
def funzione4(lista1):
    lista2 = []
    for numero in lista1:
        #se il numero in lista diviso per 2 è diverso da zero, sarà dispari
        if numero % 2 != 0:
            #aggiunge il numero ad una nuova lista con solo i num dispari
            lista2.append(numero)
    print(f"La tua lista con numeri dispari è {lista2}.") 
    
    #aggiungo un parametro di default
    #se riceve un num_primo bene, se nessuno gliela specifica allora usa None (vuoto)
    
    #in questo modo quando chiamo la funzione 5 per l'esercizio case 5 funziona correttamente, 
    #ma se richiamo la funzione 5 per l'esercizio case 6 accetta lo stesso la funzione con il parametro dato (la lista di numeri primi)
def funzione5(n=None):
    if n == None: 
        num_primo = int(input("Inserisci un numero per scoprire se è primo o no: "))  
    else:
        #serve per la funzione 6, quando gli passiamo la lista di numeri primi
        num_primo = n
        
    if num_primo < 2:
        print("Devi inserire un numero maggiore di 1.")
        return False
         
    for i in range(2, num_primo):
        if num_primo % i == 0:
            #solo nel caso in cui il numero è dato dall'input, si stampa la frase
            if n == None:
                print(f"Mi dispiace! {num_primo} NON è un numero primo.")
            return False     
     
    if n == None:
        print(f"Bravo! {num_primo} è un numero primo.") 
    return True 

def funzione6(lista1):
    #creo nuova lista per i numeri primi
    lista3 = []
    for numero in lista1:
        #rubo la funzione 5 così da non ripetere il codice e verificare direttamente se un numero è primo
        if funzione5(numero) == True:
            #aggiungo ogni numero primo alla lista
            lista3.append(numero)
    print(f"Ecco la tua lista di soli numeri primi! {lista3}")   
       
       
def funzione7(lista1):
    somma2 = 0
    #faccio la somma con ogni numero della lista
    for numero in lista1:
        somma2 += numero
    print(f"La somma totale della lista è {somma2}")      
    
    #se il numero totale risponde al True della funzione5 è numero primo 
    if funzione5(somma2) == True:
        print("La somma della lista è un numero primo.")  
    else:
        print("La somma della lista NON è un numero primo.")      
        
             
while True:
    recap = int(input("Quale punto dell'esercizio di recap vuoi svolgere? Da 1 a 7: "))
    
    #menu
    match recap:
        case 1: funzione1()
        case 2: funzione2()
        case 3: funzione3(funzione2())
        case 4: funzione4(funzione2())
        case 5: funzione5()
        case 6: funzione6(funzione2())
        case 7: funzione7(funzione2())
        case _: break