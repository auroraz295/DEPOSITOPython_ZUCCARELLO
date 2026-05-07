#NUMPY - Numerical Python
import numpy as np

#creazione array unidimensionale
arr1 = np.array([1, 2, 3, 4, 5])

#creazione array bidimensionale
arr2 = np.array([[1, 2, 3] , [4, 5, 6]])

#ALCUNI METODI ARRAY

#np.zeros() crea array con zeri
#np.ones() crea array con uno
#np.arange() segue range con start, step, stop

#SHAPE - prima righe, poi colonne 
print("Forma array: ", arr1.shape)
print("Forma array2: ", arr2.shape)

#NDIM
print("Dimensioni dell'array: ", arr1.ndim)

#DTYPE
print("Tipo di dati: ", arr1.dtype)

#ARANGE()
arr3 = np.arange(10)
print(arr3)

#RESHAPE()
reshape_arr = arr3.reshape((5,2))
print(reshape_arr)

#SIZE
print("Numero di elementi: ", arr1.size)

#SUM()
print("Somma degli elementi: ", arr1.sum())

#MEAN()
print("Media degli elementi: ", arr1.mean())

#MAX() - valore massimo
print("Valore massimo: ", arr1.max())

#ARGMAX() - posizione del valore massimo
print("Indice del valore massimo: ", arr1.argmax())
