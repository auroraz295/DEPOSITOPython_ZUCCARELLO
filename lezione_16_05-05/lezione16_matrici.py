#MATRICI
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#accesso all'elemento della matrice, riga 0 (prima riga) e colonna 1 (seconda colonna)
elemento = matrice [0][1]

#iterare sugli elementi della matrice
for riga in matrice:
    for elemento in riga:
        print(elemento)
