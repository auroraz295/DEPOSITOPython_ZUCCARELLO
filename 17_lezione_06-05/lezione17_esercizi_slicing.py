#ESERCIZIO SLICING E FANCY INDEXING
import numpy as np
import csv

#crea array di 20 numeri interi casuali da 10 a 50
#np.random.randint genera numeri casuali da 10 a 50, size è la dimensione dell'array
arr1 = np.random.randint(10,51, size=(20,))
print(arr1)

#estrarre i primi 10 elementi
arr2 = arr1[:10]
print(f"Primi 10: {arr2}")

#estrarre gli ultimi 5
arr3 = arr1[-5:]
print(f"Ultimi 5: {arr3}")

#estrarre dall'indice 5 al 15 escluso
indice = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
arr4 = arr1[indice]
print(f"Numeri da indice 5 a indice 14: {arr4}")

#estrarre ogni terzo elemento
arr5 = arr1[2::3]
print(f"Ogni terzo elemento: {arr5}")

#modifica gli elementi dall'indice 5 al 10 escluso assegnando il valore 99
#seleziono tramite slicing e assegno valore

#copia dell'array per non modificare l'originale
arr_copia = arr1.copy()
arr_copia[5:10] = 99

print(f"Modifica elementi {arr_copia}")

#creo file txt
with open("file_slicing.txt", "w") as f:
    f.write(f"Array creato: {arr1} \nPrimi 10: {arr2} \nUltimi 5: {arr3} \nNumeri da indice 5 a indice 14: {arr4} \nModifica elementi valore 99: {arr_copia}")

#creo file csv
with open("file_slicing.csv", "w", newline="", encoding="utf-8") as f2:
    writer = csv.writer(f2)
    writer.writerows((arr1, arr2, arr3, arr4, arr5, arr_copia))
    
    