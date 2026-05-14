import numpy as np

#NUMPY - MODULO ALGEBRA LINEARE
#matrice quadrata
arr = np.array([[1, 2], [3, 4]])

#calcolo dell'inversa della matrice
arr_inversa = np.linalg.inv(arr)

print("Inversa di arr: \n", arr_inversa)

#NORMA DI UN VETTORE
vett = np.array([3, 4])

#calcolo della norma del vettore
norma_v = np.linalg.norm(vett)

print("Norma del vettore: \n", norma_v)

#FUNZIONE NUMPY.LINALG.SOLVE - SISTEMA LINEARE DI EQUAZIONI AX=BAX = BAX=B
A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])

#risoluzione sistema di equazioni Ax=B
x = np.linalg.solve(A, B)

print("Soluzione x: ", x)

#FUNZIONE NUMPY.FFT.FFT - TRASFORMATA DI FOURIER DISCRETA - frequenze segnali

#segnale
t = np.linspace(0, 1, 400)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

#calcolo trasformata di fourier
fft_sig = np.fft.fft(sig)

#frequenze associate
freqs = np.fft.fftfreq(len(fft_sig))

print("Trasformata di Fourier: ", fft_sig)
print("Frequenze associate: ", freqs)

#BROADCASTING
arr2 = np.array([1, 2, 3, 4])
scalar = 10

#broadcasting aggiunge lo scalare a ogni elemento dell'array
result = arr2 + scalar
print(result)