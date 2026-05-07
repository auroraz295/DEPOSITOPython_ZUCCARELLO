from modulo_capoprincipale import Giacca, Pantalone, Gilet 
from modulo_finitura import Cravatta, Papillon, Pochette
from modulo_gestione import GestioneSartoria

sartoria = GestioneSartoria()

#MAIN MENU
while True:
    comando = int(input("Menu: 1. Crea capo - 2. Modifica capo - 3. Elimina capo - 4. Genera dati - 5. Analisi capi // "))

    match comando :
        case 1:
            sartoria.crea_capo()
        
        case 2:
            sartoria.modifica_capo()
        
        case 3:
            sartoria.elimina_capo()
        
        case 4:
            pass
        
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
        case _:
            print("Opzione non disponibile.")