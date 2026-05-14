#ESERCIZIO 1
import numpy as np
import os

#crea array di 12 numeri equidistanti
arr1 = np.linspace(0, 1, 12)

#cambia forma a una matrice 3x4
matrice = arr1.reshape(3,4)

#genera matrice 3x4 numeri casuali
matrice_random = np.random.rand(3,4)

#calcola somma di entrambe le matrici
somma_matrice = np.sum(matrice)
somma_matrice_random = np.sum(matrice_random)

print(arr1)

print(matrice)
print(somma_matrice)

print(matrice_random)
print(somma_matrice_random)

#ESERCIZIO 2

def esercizio():
    
    #gestione file txt
    modalita = ""
    while modalita not in ["w", "a"]:
        scelta = int(input("1. Sovrascrivere il file TXT - 2. Aggiungere i dati // "))
        if scelta == 1:
            modalita = "w"
        elif scelta == 2:
            modalita = "a"
        else:
            print("Opzione non eseguibile. ")
    
    while True:
        
        #creazione array linspace
        array_lin = np.linspace(0, 10, 50)
        
        #creazione array casuale
        array_ran = np.random.random(50)
        
        #somma elementi array
        array_somm = array_lin + array_ran
        
        #calcolo somma
        somma = np.sum(array_somm)
        
        #somma elementi maggiori di 5 
        somma_maggiori5 = np.sum(array_somm[array_somm>5])
        
        #print
        print("Array con linspace: ", array_lin)
        print("Array random: ", array_ran)
        print("Nuovo array: ", array_somm)
        
        print("Somma totale elementi array: ", somma)
        print("Somma elementi array >5: ", somma_maggiori5)
        
        #salvataggio file
        with open("esercizio_numpy.txt", modalita, encoding="utf-8") as f:
            f.write(f"Array con linspace: {array_lin} \n")
            f.write(f"Array random: {array_ran} \n")
            f.write(f"Array nuovo: {array_somm} \n")
            f.write(f"Somma totale: {somma} \n")
            f.write(f"Somma elementi >5: {somma_maggiori5} \n")
            
        ripeti = int(input("1. Esegui ancora - 2. Chiudi // "))
        if ripeti == 2:
            break
        
        
esercizio()