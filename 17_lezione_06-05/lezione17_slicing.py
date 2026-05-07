#INDEXING E SLICING
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#INDEXING
print(arr[0])

#SLICING
print(arr[1:3])

#BOOLEAN INDEXING
print(arr[arr>2])

arr2 = np.array ([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

#SLICING SULLE RIGHE
print(arr2[1:3])

#SLICING SULLE COLONNE
print(arr2[:, 1:3])

#SLICING MISTO
print(arr2[1:3, 1:3])

#ESEMPI SLICING
#slicing con passo
print(arr[1:8:2])

#omissione start e stop
print(arr[:5])
print(arr[5:])

#indici negativi
print(arr[-5:])
print(arr[:-5])

#FANCY INDEXING
arr3 = np.array([10, 20, 30, 40, 50])

#utilizzo array di indici
indices = np.array([1,3])
print(arr3[indices])

#utilizzo lista di indici (meglio di no)
indices = [0, 2, 4]
print(arr3[indices])