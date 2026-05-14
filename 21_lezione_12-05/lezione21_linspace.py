import numpy as np

#LINSPACE - genera array di numeri equidistanti tra un valore iniziale e uno finale
#lo stop è incluso
arr = np.linspace(0, 1, 5)
print(arr)


#RANDOM - array numeri casuali
random_arr = np.random.rand(3, 3)
print(random_arr)

#creo matrice
matrice = np.random.randint(10, 100, size=(5, 5))
print(matrice)

#SUM, MEAN, STD
arr1 = np.array([1, 2, 3, 4, 5])

sum = np.sum(arr1)
mean = np.mean(arr1)
std = np.std(arr1)

print("Somma:", sum)
print("Media:", mean)
print("Deviazione standard:", std)