import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#ESERCIZIO 1 
#Genera un DataFrame pandas con una colonna temperature (30 valori casuali) e calcola:
# temperatura massima, temperatura minima , temperatura media, mediana delle temperature

#dataframe 30 temperature casuali
np.random.seed(28)
df = pd.DataFrame({"temperatura": np.random.uniform(5, 40, 30)})

min = df['temperatura'].min()
max = df['temperatura'].max()
media = df['temperatura'].mean()
mediana = df['temperatura'].median()

print(df)

#temperature
print(f"Temperatura minima: {min}")
print(f"Temperatura massima: {max}")
print(f"Temperatura media: {media}")
print(f"Mediana temperatura: {mediana}")

#line plot temperature con linea orizzontale della media
plt.figure()
plt.plot(df['temperatura'])
plt.axhline(media)

#grafico a barre con seaborn
plt.figure()
sns.histplot(data=df, kde=True)

plt.show()

#ESERCIZIO 2 
#Crea un DataFrame con colonne altezza, peso ed età.
#Applica la normalizzazione min-max ad altezza e peso (scala i valori tra 0 e 1), lasciando età invariata.

dati = { "altezza" : [175, 162, 188, 170, 155, 180],
         "peso" : [70, 55, 85, 68, 50, 78],
         "eta" : [25, 34, 41, 19, 52, 28]
        }

df2 = pd.DataFrame(dati)

df_copia = df2.copy()

#normalizzazione
for colonna in ["altezza", "peso"]:
   df_copia[colonna] = (df2[colonna] - df2[colonna].min()) / (df2[colonna].max() - df2[colonna].min())

#grafico a barre 
#griglia subplot
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

#grafico dati originali
axes[0].barh(df2["altezza"], df2["peso"])
axes[0].set_title('Grafico dati originali')

#grafico dati normalizzati
axes[1].bar(df_copia["altezza"], df_copia["peso"])
axes[1].set_title('Grafico dati normalizzati')

plt.tight_layout()  # regola automaticamente lo spazio tra i grafici
plt.show()

#grafico scatter
plt.figure()
plt.scatter(df_copia["altezza"], df_copia["peso"])

plt.show()

