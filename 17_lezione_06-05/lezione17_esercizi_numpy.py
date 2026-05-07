#CREA ARRAY utilizzando arange e verifica il tipo di dato e la forma
import numpy as np
import csv

#creo array
arr = np.arange(10,50, 1)
print("Tipo di dato array: ", arr.dtype)

#cambio con tipo di dato float
#.astype cambia il tipo di dato
arr = arr.astype(float)
print("Tipo di dato array: ", arr.dtype)

#stampo forma
print("Forma array: ", arr.shape)

#salvo su file txt
with open("prova_numpy.txt", "w") as f:
    f.write(f"Array: {arr} - Tipo di dato: {arr.dtype} - Forma: {arr.shape} ")
    
