#FUNZIONI GESTIONE FILE

#salva i libri contenuti nel catalogo completo
def salva_catalogo(catalogo_libri):
    with open("catalogo_completo_biblioteca.txt", "w", encoding="utf-8") as f:
        for libro in catalogo_libri:
            f.write(f"{libro} \n")

#aggiunge nel file txt i libri prenotati
def salva_prenotati(catalogo_libri):
    with open("catalogo_prenotati.txt", "a", encoding="utf-8") as f:
        for libro in catalogo_libri:
            f.write(f"{libro}\n")

#aggiunge nel file txt i libri venduti
def salva_venduti(catalogo_libri):
     with open("catalogo_venduti.txt", "a", encoding="utf-8") as f:
        for libro in catalogo_libri:
            f.write(f"{libro}\n")