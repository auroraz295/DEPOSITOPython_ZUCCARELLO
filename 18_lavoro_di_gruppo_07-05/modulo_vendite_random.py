from modulo_capoprincipale import Giacca, Pantalone, Gilet
from modulo_finitura import Cravatta, Papillon, Pochette
from modulo_gestore_file import salva_catalogo

import random

# Creo classe Vendite Random
class Vendite_Random:

    def __init__(self, lista_capi, lista_rifiniture):
        self._catalogo_capi = lista_capi
        self._catalogo_rifiniture = lista_rifiniture

        # Lista per scelta degli oggetti
        self._lista_capo_principale = [
            "Giacca",
            "Pantalone",
            "Gilet"
        ]

        # Lista per scelta degli oggetti
        self._lista_finitura = [
            "Cravatta",
            "Papillon",
            "Pochette"
        ]

        # Lista per scelta casuale della taglia
        self._lista_taglie =[
            "S",
            "M",
            "L",
            "XL",
            "XXL"
        ]

        # Lista per scelta casuale del colore
        self._lista_colori = [
            "Nero",
            "Bianco",
            "Blu",
            "Rosso"
        ]

        # Lista per scelta casuale del tessuto
        self._lista_tessuti = [
            "Lana",
            "Cotone",
            "Seta"
        ]

        # Lista per scelta casuale del tipo di taglio
        self._lista_tipo_taglio = [
            "skinny",
            "wide",
            "slim"
        ]

        # Lista per scelta casuale della larghezza della cravatta
        self._lista_larghezze = [
            5,
            7,
            9
        ]

        # Lista per scelta casuale del tipo di chiusura del papillon
        self._lista_tipo_chiusura = [
            "a clip",
            "a nodo"
        ]

        # Prezzi base per i capi principali e le finiture
        self._prezzo_giacca = 40.0
        self._prezzo_pantalone = 30.0
        self._prezzo_gilet = 25.0

        self._prezzo_cravatta = 15.0
        self._prezzo_papillon = 15.0
        self._prezzo_pochette = 10.0

        # Codice progressivo per identificare univocamente ogni capo/finitura
        self._codice = 0

    # Metodo per generare caratteristiche casuali per i capi principali
    def random_caratteristiche_capo_principale(self):
        # Generazione casuale delle caratteristiche
        self._codice += 1
        tessuto = random.choice(self._lista_tessuti)
        colore = random.choice(self._lista_colori)
        taglia = random.choice(self._lista_taglie)
        tipo_taglio = random.choice(self._lista_tipo_taglio)
        numero_bottoni = random.randint(1, 3)
        è_reversibile = random.choice([True, False])

        return self._codice, tessuto, colore, taglia, tipo_taglio, numero_bottoni, è_reversibile

    # Metodo per generare caratteristiche casuali per le finiture
    def random_caratteristiche_finitura(self):
        # Generazione casuale delle caratteristiche
        self._codice += 1
        tessuto = random.choice(self._lista_tessuti)
        colore = random.choice(self._lista_colori)
        larghezza = random.choice(self._lista_larghezze)
        tipo_chiusura = random.choice(self._lista_tipo_chiusura)
        ha_piega_decorativa = random.choice([True, False])

        return self._codice, tessuto, colore, larghezza, tipo_chiusura, ha_piega_decorativa

    # Metodo per creare capi e finiture casuali e aggiungerli al catalogo
    def creazione_casuale(self):

        while True:

            scelta = input("Cosa desidera acquistare?"
                        "\n1. Capo Principale"
                        "\n2. Finitura"
                        "\n3. Esci"
                        "\n\n> "
                        )

            match scelta:

                # Creazione casuale di un capo principale o di una finitura in base alla scelta dell'utente
                case "1":
                    codice, tessuto, colore, taglia, tipo_taglio, numero_bottoni, è_reversibile = self.random_caratteristiche_capo_principale()
                    capo_principale_scelto = random.choice(self._lista_capo_principale)

                    if capo_principale_scelto == "Giacca":
                        capo_principale = Giacca(codice, "Giacca", tessuto, colore, taglia, self._prezzo_giacca, numero_bottoni)
                        print(f"Hai scelto: {capo_principale._nome} - Costo totale: {capo_principale.costo()}€")
                        self._catalogo_capi.append(capo_principale)

                    elif capo_principale_scelto == "Pantalone":
                        capo_principale = Pantalone(codice, "Pantalone", tessuto, colore, taglia, self._prezzo_pantalone, tipo_taglio)
                        print(f"Hai scelto: {capo_principale._nome} - Costo totale: {capo_principale.costo()}€")
                        self._catalogo_capi.append(capo_principale)

                    elif capo_principale_scelto == "Gilet":
                        capo_principale = Gilet(codice, "Gilet", tessuto, colore, taglia, self._prezzo_gilet, è_reversibile)
                        print(f"Hai scelto: {capo_principale._nome} - Costo totale: {capo_principale.costo()}€")
                        self._catalogo_capi.append(capo_principale)

                # Creazione casuale di una finitura in base alla scelta dell'utente
                case "2":
                    codice, tessuto, colore, larghezza, tipo_chiusura, ha_piega_decorativa = self.random_caratteristiche_finitura()
                    finitura_scelta = random.choice(self._lista_finitura)

                    if finitura_scelta == "Cravatta":
                        finitura = Cravatta(codice, "Cravatta", tessuto, colore, self._prezzo_cravatta, larghezza)
                        print(f"Hai scelto: {finitura._nome} - Costo totale: {finitura.costo()}€")
                        self._catalogo_rifiniture.append(finitura)

                    elif finitura_scelta == "Papillon":
                        finitura = Papillon(codice, "Papillon", tessuto, colore, self._prezzo_papillon, tipo_chiusura)
                        print(f"Hai scelto: {finitura._nome} - Costo totale: {finitura.costo()}€")
                        self._catalogo_rifiniture.append(finitura)

                    elif finitura_scelta == "Pochette":
                        finitura = Pochette(codice, "Pochette", tessuto, colore, self._prezzo_pochette, ha_piega_decorativa)
                        print(f"Hai scelto: {finitura._nome} - Costo totale: {finitura.costo()}€")
                        self._catalogo_rifiniture.append(finitura)

                # Esci e salva il catalogo su file
                case "3":
                    lista_catalogo = self._catalogo_capi + self._catalogo_rifiniture
                    salva_catalogo(lista_catalogo)
                    print("Grazie per aver acquistato!")
                    break

                # Scelta non valida
                case _:
                    print("Scelta non valida. Riprova.")
                    continue