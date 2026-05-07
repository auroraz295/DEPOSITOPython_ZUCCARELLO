# Funzione per salvare il catalogo su file
def salva_catalogo(lista_catalogo):

    with open("catalogo.txt", "w", encoding="utf-8") as f:
        for item in lista_catalogo:
            f.write(f"{item}\n")