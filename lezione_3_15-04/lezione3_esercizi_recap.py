#1. Utilizzo di if
#Scrivi un sistema che prendee in input un numero e stampa "Pari" se il numero 
#è pari, "Dispari" se il numero è dispari.

#2. Utilizzo di while e range
#Scrivi un sistema che predne in input un numero intero positivo n e stampa tutti i numeri
#da n a 0 (compreso), decrementando di 1. Deve potersi ripetere all'infinito.

#3. Utilizzo di for
#Scrivi un sistema che prednne in input una lista di numeri e stampa il quadrato di ciascun numero della lista

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
    case 1: #esercizio1
        numero1 = int(input("Scrivi un numero per vedere se è Pari o Dispari: "))
        if numero1 %2 == 0: #se il numero scelto diviso per 2 fa 0, restituisce pari
            print(f"Il numero {numero1} è Pari!")
        else:
            print(f"Il numero {numero1} è Dispari!") 
    case 2: #essercizio2
        while recap: 
            numero2 = int(input("Inserisci un numero positivo: "))   
            for i in range(numero2, -1, -1): #dal numero scelto, fa un conto alla rovescia dalla cifra più grande a 0 
                print(i) 
    case 3:  
        controllo = True
        
        while controllo: #finché la condizione è vera, esegue questo blocco di codice
            quadrati = [] #lista vuota iniziale 
            numero3 = int(input("Inserisci una lista di numeri per calcolare il quadrato di ciascuno. "))
            quadrati.append(numero3) #aggiungo il numero scelto dall'utente alla lista
            controllore = input("Hai finito la tua lista?") #se l'utente ha finito la sua lista si esegue il quadrato dei numeri
            if controllore == "si":
                for quadrato in quadrati: #per ogni numero presente in lista, calcola e stampa il quadrato
                    print(f"Il quadrato di {quadrato} è:", (quadrato ** 2))
                controllo = False

""" PARTE DA RIVEDERE E COMPLETARE
    case 4:  
        controllo = True
        numeri = []
        while controllo:
            numero4 = int(input("Inserisci una lista di numeri per vedere il numero massimo trovato: "))
            check = input("Hai finito la tua lista?")
            if check == "si":
                max = 0
                for numero in numeri:
                    if numero > max:
                        max = numero 
                print(f"Il numero massimo della tua lista è {max}")
                controllo = False  """