import pandas as pd

#MULTI INDEX
data_multi = {'Paese': ['Italia', 'Italia', 'Francia', 'Francia'],
              'Anno': [2023, 2024, 2023, 2024],
              'Vendite': [120, 135, 110, 118]
            }

df_multi = pd.DataFrame(data_multi)

#Creo un indice gerarchico con Paese e Anno
df_multi = df_multi.set_index(['Paese', 'Anno'])

print("\nDataFrame con MultiIndex:")
print(df_multi)

#SELETTORE LOC - FILTRO
#Seleziono tutte le righe per Italia
print("\nTutte le righe per Italia (loc):")
print(df_multi.loc['Italia'])

#Seleziono il valore specifico per Francia nel 2024
print("\nValore Vendite per Francia, 2024 (loc):")
print(df_multi.loc[('Francia', 2024), 'Vendite'])