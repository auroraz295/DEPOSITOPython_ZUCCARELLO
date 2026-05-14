#ESERCIZIO 1 
#CREA ARRAY utilizzando arange e verifica il tipo di dato e la forma
import numpy as np

#creo array
arr = np.arange(10,50, 1)
print("Tipo di dato array: ", arr.dtype)

#cambio con tipo di dato float
#.astype cambia il tipo di dato
arr = arr.astype(float)
print("Tipo di dato array: ", arr.dtype)

#stampo forma
print("Forma array: ", arr.shape)

#ESERCIZIO 2
#crea array di 20 numeri interi casuali da 10 a 50
#np.random.randint genera numeri casuali da 10 a 50, size è la dimensione dell'array
arr1 = np.random.randint(10, 50, size=(20,))
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

#ESERCIZIO 3 
# creo matrice 6x6
matrice_originale = np.random.randint(1, 101, size=(6, 6))
print(matrice_originale)

#sottomatrice 4x4
sotto_matrice = matrice_originale[1:5, 1:5]
print(sotto_matrice)

#inverto righe
matrice_invertita = sotto_matrice[::-1]
print(matrice_invertita)

#diagonale
diagonale = np.diag(matrice_invertita)
print(diagonale)

#sostituzione elementi multipli di 3 con il valore -1
matrice_modificata = matrice_invertita.copy()
matrice_modificata[matrice_modificata % 3 == 0] = -1
print(matrice_modificata)
