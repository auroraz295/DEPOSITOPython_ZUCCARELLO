import pandas as pd
import numpy as np

#DataFrame esempio, inclusi valori mancanti e duplicati
data = { 'Nome': ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', None],
         'Età': [25, 30, 22, 30, np.nan, 25, 29],
         'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma']
         }

df = pd.DataFrame(data)

#Stampa del DataFrame originale
print("DataFrame Originale:")
print(df)

#Rimozione dei duplicati
df = df.drop_duplicates()

#Gestione dei dati mancanti
#Rimozione delle righe dove almeno un elemento è mancante
df_cleaned = df.dropna()

#possiamo sostituire dati mancanti con valore di default
# //old versions
#df['Età'].fillna(df['Età'].mean(), inplace=True)

#// newer versions
df.fillna({'Eta': df['Eta'].mean()}, inplace=True)

#Stampa del DataFrame pulito
print("\nDataFrame dopo la pulizia:")
print(df_cleaned)

#Stampa del DataFrame con dati mancanti sostituiti
print("\nDataFrame con dati mancanti sostituiti:")
print(df)

#------------------

#ESPLORAZIONE E PULIZIA
#Visualizzazione delle statistiche descrittive
print(df.describe())

#Rimozione dei valori mancanti
df_clean = df.dropna()

#SELEZIONE E FILTRAGGIO
#Selezione di una colonna
ages = df['età']

#Filtraggio basato su una condizione
adults = df[df['età'] >= 18]

#MANIPOLAZIONE DEI DATI
#Ordinamento dei dati per età
df_sorted = df.sort_values(by='età')


#Unione di due DataFrame
merged_df = pd.merge(df, df_csv, on='nome')

#TRASFORMAZIONI
#Applicazione di una funzione a una colonna
df['età_doppia'] = df['età'].apply(lambda x: x * 2)