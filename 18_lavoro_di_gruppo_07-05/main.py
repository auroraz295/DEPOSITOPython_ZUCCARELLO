from modulo_capoprincipale import Giacca, Pantalone, Gilet
from modulo_finitura import Cravatta, Papillon, Pochette
from modulo_gestione import GestioneSartoria
from modulo_vendite_random import Vendite_Random

sartoria = GestioneSartoria()
venditore_random = Vendite_Random(sartoria.get_lista_capi(), sartoria.get_lista_rifiniture())

#MAIN MENU
while True:
    comando = int(input("Menu: 1. Crea capo - 2. Modifica capo - 3. Elimina capo - 4. Genera dati - 5. Analisi capi - 6. Esci // "))

    match comando :
        # Crea capo
        case 1:
            sartoria.crea_capo()

        # Modifica capo
        case 2:
            sartoria.modifica_capo()

        # Elimina capo
        case 3:
            sartoria.elimina_capo()

        # Genera dati casuali
        case 4:
            venditore_random.creazione_casuale()

        # Analisi capi
        case 5:
            tipo_analisi = int(input("Scegli il tipo di analisi: 1. Analisi di tutti i capi - 2. Analisi per tipo - 3. Analisi per tipo per personalizzazione //  "))

            match tipo_analisi:
                case 1:
                    sartoria.analisi_tutti()

                case 2:
                    sartoria.analisi_tipo()

                case 3:
                    sartoria.analisi_dettagli()

                case _:
                    print("Opzione non disponibile.")
                    continue

        # Esci
        case 6:
            print("Grazie per aver utilizzato il programma!")
            break

        # Scelta non valida
        case _:
            print("Opzione non disponibile.")
            continue