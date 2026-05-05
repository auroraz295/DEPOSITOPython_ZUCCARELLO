#DIZIONARI
#tipo dict, definito da {}, modificabile e ordinato
studente = {
    "nome": "Alice",
    "età": 20,
    "sesso": "Femmina"
}

print(studente["nome"])
print(studente["età"])

#MOFDIFICABILITA'
studente["età"] = 21
print(studente)

#aggiungi coppia chiave-valore
studente["città"] = "Roma"
print(studente)

#METODI DIZIONARI
print(studente.keys())
print(studente.values())