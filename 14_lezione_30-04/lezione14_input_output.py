#APERTURA LETTURA SCRITTURA DI UN FILE 

#APERTURA
file = open("file.txt", "r")

#LETTURA
#READ, legge l'intero contenuto
contenuto = file.read()
#READLINE, legge una singola riga 
riga = file.readline()

print(contenuto)
print(riga)

#SCRITTURA
#apertura in modalità scrittura w 
file = open("file.txt", "w")

#sovrascrittura
file.write("Esempio scrittura su file.")
file.close

file = open("file.txt", "r")
file = file.read()

print(file)