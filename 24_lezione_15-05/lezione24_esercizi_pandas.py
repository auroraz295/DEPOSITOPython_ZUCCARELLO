#ESERCIZIO SLIDE 275 - 276 - 277
import numpy as np
import pandas as pd

#DATI DA CREARE

#DATAFRAME ISCRITTI
iscritti = { 'nome': ['Marco Rossi', 'Giulia Bianchi', 'Luca Verdi', 'Elena Neri', 'Marco Rossi', 'Sara Viola', 
                      'Antonio Gallo', 'Chiara Sala', 'Paolo Moretti', 'Marta Riva', 'Roberto Ferri'],
             'eta' : [16, 32, 45, 19, 51, 28, 55, np.nan, 17, 31, 22],
             'citta' : ['Milano', 'Roma', 'Napoli', 'Torino', 'Milano', 'Firenze', 
                        'Bari', 'Bologna', 'Palermo', 'Genova', 'Venezia'],
             'tipo_abbonamento' : ['Base', 'Premium', 'Family', 'Base', 'Base', 'Premium',
                                   'Family', 'Base', 'Premium', 'Family', 'Base']
            }

df_iscritti = pd.DataFrame(iscritti)

#DATAFRAME PRESENZE
presenze = { 'data' : ['2026-05-10', '2026-05-10', '2026-05-10', '2026-05-10', '2026-05-10',
                        '2026-05-12', '2026-05-12', '2026-05-12', '2026-05-12', '2026-05-12',
                        '2026-05-15', '2026-05-15', '2026-05-15', '2026-05-15', '2026-05-15'],
             'corso' : ['Yoga', 'Crossfit', 'Nuoto', 'Pilates', 'Yoga',
                        'Nuoto', 'Crossfit', 'Pilates', 'Yoga', 'Nuoto',
                        'Crossfit', 'Yoga', 'Pilates', 'Nuoto', 'Crossfit'],
             'citta' : ['Milano', 'Roma', 'Napoli', 'Milano', 'Roma',
                        'Napoli', 'Milano', 'Roma', 'Napoli', 'Milano',
                        'Roma', 'Napoli', 'Milano', 'Roma', 'Napoli'],
             'partecipanti' : [12, 25, 18, 10, 15, 20, 22, 14, 11, 19, 30, 13, 16, 21, 28],
            }

df_presenze = pd.DataFrame(presenze)

#DATAFRAME COSTI ABBONAMENTO
costi_abbonamento = { 'tipo_abbonamento' : ['Base', 'Premium', 'Family'],
                      'costo_mensile' : [39.90, 59.90, 89.90]
                    }

df_costi = pd.DataFrame(costi_abbonamento)

#1. INTRODUZIONE
#stampa iscritti originali
print("\nDataframe iscritti originale")
print(df_iscritti)

#filtra iscritti con età maggiore di 25
filtro_eta = df_iscritti[df_iscritti['eta'] >25]

print("\nDataframe con filtro di età > 25")
print(filtro_eta)

#colonna attivo (true/false) se l'abbonamento è premium o no
df_iscritti["Attivo"] = df_iscritti["tipo_abbonamento"] == "Premium"

#check dataframe
print("\nDataframe con colonna Attivo")
print(df_iscritti)

#2. PULIZIA DATI
#rimuovi duplicati 
df_iscritti = df_iscritti.drop_duplicates()

print("\nDataframe senza duplicati")
print(df_iscritti)

#se età mancante, sostituisci con la media
df_iscritti.fillna({"eta": df_iscritti["eta"].mean()}, inplace=True)

#3. APPLY CON FUNZIONE PERSONALIZZATA 
#crea funzione fascia_eta - <18 junior, >=18 e <=44 adulto, >=45 senior

def fascia_eta(eta):
    if (eta < 18) :
        return "Junior"
    elif (eta > 18 and eta <= 44): 
        return "Adulto"
    elif (eta>= 45):
        return "Senior"
    else:
        return " - "
    
#creo nuova colonna con apply
df_iscritti["fascia_eta"] = df_iscritti["eta"].apply(fascia_eta)

#check con nuova colonna
print(df_iscritti)

#4. ANALISI PRESENZE
#ordina il dataframe presenze per citta e poi per partecipanti
df_ordine_citta = df_presenze.sort_values(by="citta")
df_ordine_partecipanti = df_presenze.sort_values(by="partecipanti")

print("\nDataframe presenze ordinato per città")
print(df_ordine_citta)

print("\nDataframe ordinato per partecipanti")
print(df_ordine_partecipanti)

#groupby per corso con somma totale partecipanti
group_corso = df_presenze.groupby('corso')["partecipanti"].sum()

print("\nGroup by per corso")
print(group_corso)

#groupby per citta con media partecipanti
group_citta = df_presenze.groupby('citta')["partecipanti"].mean()

print("\nGroup by per citta")
print(group_citta)

#crea pivot table 
pivot_table = df_presenze.pivot_table(values="partecipanti", index="corso", columns="citta", aggfunc="mean")

print("\nPivot table dataframe presenze")
print(pivot_table)

#5. MULTIINDEX 
#crea un nuovo dataframe 

sedi = { 'nome': ['Marco Rossi', 'Giulia Bianchi', 'Luca Verdi', 'Elena Neri', 'Marco Rossi', 'Sara Viola',
                  'Antonio Gallo', 'Chiara Sala', 'Paolo Moretti', 'Marta Riva', 'Roberto Ferri'],
             'eta' : [16, 32, 45, 19, 51, 28, 55, np.nan, 17, 31, 22],
             'citta' : ['Milano', 'Roma', 'Napoli', 'Torino', 'Milano', 'Firenze',
                        'Bari', 'Bologna', 'Palermo', 'Genova', 'Venezia'],
             'tipo_abbonamento' : ['Base', 'Premium', 'Family', 'Base', 'Base', 'Premium',
                                   'Family', 'Base', 'Premium', 'Family', 'Base'],
             'sede': ['Nord', 'Centro', 'Sud', 'Nord', 'Nord', 'Centro', 
                      'Sud', 'Nord', 'Sud', 'Nord', 'Nord'],
             'anno': [2024, 2025, 2024, 2024, 2025, 2024,
                      2025, 2024, 2025, 2024, 2025],
        }

df_sedi = pd.DataFrame(sedi)

#imposta multiindex su sede e anno
df_multi = df_sedi.set_index(["sede", "anno"])

print("\nMulti index per sede e anno")
print(df_multi)

#filtro loc per tutte le righe di una sede
righe_nord = df_multi.loc["Nord"]
righe_centro = df_multi.loc["Centro"]
righe_sud = df_multi.loc["Sud"]

print("\nTutte le righe per la sede Nord")
print(righe_nord)

print("\nTutte le righe per la sede Centro")
print(righe_centro)

print("\nTutte le righe per la sede Sud")
print(righe_sud)

#filtro loc per valore iscritti di una sede in un anno specifico
filtro_sede_anno = df_multi.loc[("Nord", 2024)]

print("\nIscritti sede nord anno 2024")
print(filtro_sede_anno)

#5. MERGE
#fai merge tra iscritti e costi abbonamento su tipo abbonamento
df_merge = pd.merge(df_iscritti, df_costi, on="tipo_abbonamento")
df_merge["costo_annuale"] = df_merge["costo_mensile"] * 12

print("\nMerge con colonna costo annuale aggiunta")
print(df_merge)

#OUTPUT FINALE
#salva in csv: iscritti_puliti, report_presenze_pivot, iscritti_con_costi

df_iscritti.to_csv("iscritti_puliti.csv", encoding="utf-8")
pivot_table.to_csv("report_presenze_pivot.csv", encoding="utf-8")
df_merge.to_csv("iscritti_con_costi.csv", encoding="utf-8")