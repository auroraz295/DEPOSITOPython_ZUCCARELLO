#1. Chiedi all'utente di inserire un numero. Il programma dovrebbe fare un conto 
#alla rovescia a partire da quel numero fino a zero, stampando ogni numero e chiedere
#se si vuole ripetere o no.

richiesta = int(input("Inserisci un numero: "))

#per ogni numero da quello scelto, alla rovescia (-1)
for i in range(richiesta, -1, -1):
    print(i)

#secondo input per continuare il ciclo o no
conferma = input("Vuoi ripetere? ")
if conferma == "si":
    richiesta2 = int(input("Inserisci un altro numero: "))
    for i in range(richiesta, -1, -1):
        print(i)
    
    
#2. Chiedi all'utente di inserire un numero. Il programma dovrebbe controllare se
#il numero inserito è primo/pari o no. Se è primo, lo salva e stampa "Il numero è primo."
#Altrimenti, stampa "Il numero non è primo." Si ferma quando ha 5 numeri primi.

lista = []

#definisco un ciclo while per far fermare il codice solo quando ha salvato 5 numeri pari
while len(lista) <5 :
    numero = int(input("Inserisci un numero: "))
    
    #se il numero è pari, salva dentro la lista e ripete il ciclo
    if numero % 2 == 0:
        lista.append(numero)
        print(f" Il numero {numero} è pari.")
    else: 
        print("Il numero non è pari.")
    print (lista)
    
