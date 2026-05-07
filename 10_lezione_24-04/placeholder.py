
voti_studente = [8, 4, 6, 7, 9]
voti_tot = len(voti_studente)

somma_voti = 0
for voto in voti_studente:
    somma_voti += voto
    media_voti = somma_voti / voti_tot
print(f"Studente: Aurora - Media: {media_voti}") 