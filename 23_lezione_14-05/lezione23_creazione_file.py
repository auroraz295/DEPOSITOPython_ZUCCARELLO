import pandas as pd

#Creazione di un DataFrame da un dizionario
data = {'nome': ['Alice', 'Bob'], 'età': [25, 30]}
df = pd.DataFrame(data)

#Caricamento di un DataFrame da un file CSV
df_csv = pd.read_csv('data.csv')

#Lettura DataFrame da file CSV
#Percorso del file CSV
file_path = 'vendite.csv'

#Caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)

#le prime righe del DataFrame per confermare 
print(df.head())