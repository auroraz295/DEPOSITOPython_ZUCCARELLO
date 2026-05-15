import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#GRAFICO A LINEE
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure()

plt.plot(x,y)
plt.title("Grafico a linee")
plt.xlabel("X")
plt.ylabel("Y")

#plt.show()

#GRAFICO A BARRE
categorie = ["A", "B", "C", "D", "E"]
valori = [3, 7, 2, 5, 8]

plt.figure()

plt.bar(categorie, valori)
plt.title("Grafico a barre")
plt.xlabel("Categorie")
plt.ylabel("Valori")

#plt.show()

#ISTOGRAMMA
data = np.random.randn(1000)

plt.figure()

plt.hist(data, bins=30)
plt.title("Istogramma")
plt.xlabel("Valori")
plt.ylabel("Frequenza")

#plt.show()

#SCATTER PLOT
x1 = np.random.rand(50)
y1 = np.random.rand(50)

plt.figure()

plt.scatter(x1, y1)
plt.title("Scatter plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()

#SE PLT.SHOW() E' MESSO ALLA FINE, MOSTRERA' TUTTI I GRAFICI INSIEME
#SE E' MESSO DOPO OGNI GRAFICO, LI VISUALIZZA SEPARATAMENTE