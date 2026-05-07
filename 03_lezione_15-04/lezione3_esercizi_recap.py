#1. Utilizzo di if
#Scrivi un sistema che prendee in input un numero e stampa "Pari" se il numero 
#è pari, "Dispari" se il numero è dispari.

#2. Utilizzo di while e range
#Scrivi un sistema che predne in input un numero intero positivo n e stampa tutti i numeri
#da n a 0 (compreso), decrementando di 1. Deve potersi ripetere all'infinito.

#3. Utilizzo di for
#Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di ciascun numero della lista

#4. Utilizzo di if, while e for insieme
#Scrivi un sistema che prende in input una lista di numeri interi che precedenemente è stata
#valorizzata dall'utente. Il sistema deve: 
#utilizzare un ciclo for per trovare il numero massimo nella lista
#utilizzare un ciclo while pper contare quanti numeri sono presenti nella lista
#utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota, altrimenti
#stampare il numero massimo trovato e il numero di elementi nella lista. 

recap = int(input("Scegli l'esercizio da ripetere tra: 1. Condizione if 2. Ciclo while e range 3. Ciclo for 4. Condizioni e cicli if, while, for:"))

#creo menu 
match recap:
    
    #esercizio1
    case 1: 
        numero1 = int(input("Scrivi un numero per vedere se è Pari o Dispari: "))
        
        #se il numero scelto diviso per 2 fa 0, restituisce pari
        if numero1 %2 == 0: 
            print(f"Il numero {numero1} è Pari!")
        else:
            print(f"Il numero {numero1} è Dispari!") 
            
    #esercizio2
    case 2: 
        while recap: 
            numero2 = int(input("Inserisci un numero positivo: "))   
            
            #dal numero scelto, fa un conto alla rovescia dalla cifra più grande a 0
            for i in range(numero2, -1, -1):  
                print(i) 
             
    #esercizio3            
    case 3:  
        controllo = True
        
        #finché la condizione è vera, esegue questo blocco di codice
        while controllo: 
            
            #dato che input restituisce direttamente una stringa, e split fa in modo che restituisce una lista, è come se l'input fosse direttamente la lista
            lista = input("Inserisci una lista di numeri per calcolare il quadrato di ciascuno. Separa ogni numero con una virgola ").split(",")
            
            #per ogni numero presente in lista, calcola e stampa il quadrato, convertendolo prima in int
            for i in lista: 
                print(f"Il quadrato di {i} è:", (int(i) ** 2))
            controllo = False

    #esercizio4
    case 4:  
        
        #ciclo for numero massimo
        controllo = True
        numeri = []
         
        while controllo:
            
            #creo la lista direttamente dall'input
            numeri = input("Inserisci una lista di numeri per vedere il numero massimo trovato. Separa i numeri con una virgola ")
            
            #se la lista è vuota
            if len(numeri) == 0:
                print("La lista è vuota!!")
                
                #interrompo il ciclo
                controllo = False
                
            else:       
                
                #separo i numeri dalla virgola
                numeri = numeri.split(",") 
                #seleziono il primo numero della lista e lo converto in int per confrontarlo con gli altri numeri
                massimo = int(numeri[0])
            
                #ogni numero della lista lo converto in int (l'input restituisce una listta di stringhe)
                for numero in numeri:
                    numero = int(numero)
                
                    #se il numero è maggiore del numero precedente, lo sostituisce nella variabile
                    if numero > massimo:
                        massimo = numero
            
                #ciclo while per lunghezza lista
                contatore = 0 
                while contatore < len(numeri):
                    contatore += 1           
                    
                #dopo aver concluso il ciclo for stampa l'ultimo numero massimo trovato        
                print(f"Il numero massimo della tua lista è {massimo}!")
            
                #dopo aver contato gli elementi della lista stampa il risultato
                print(f"Il numero di elementi della tua lista è {contatore}!")
                
                #interrompo il ciclo
                controllo = False   
