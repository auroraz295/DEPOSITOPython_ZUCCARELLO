#MAIN
from modulo_libro import Libro
from modulo_biblioteca import Biblioteca
from modulo_analisi import analisi_generi, analisi_totale
from modulo_gestione_file import salva_catalogo, salva_prenotati, salva_venduti

biblioteca = Biblioteca()

def chiusura():
    while True:
        exit = input("Torna indietro - ENTER // ")
        if exit == "":
            break
        else:
            print("Operazione non eseguibile.")
            

while True:
    
    comando = int(input("Menu - 1. Catalogo libri - 2. Prenota libro - 3. Vendi libro - 4. Aggiungi libro - 5. Analisi catalogo // "))
    match comando:
        
        #stampa catalogo libri
        case 1:
            biblioteca.stampa()
            
            #chiusura/torna indietro menu
            chiusura()
        
        #prenota libro
        case 2:
            biblioteca.prenota()
            
            #chiusura/torna indietro menu
            chiusura()
            
        #vendi libro
        case 3:
            biblioteca.vendi()
            
            #chiusura/torna indietro menu
            chiusura()
        
        #aggiungi libro
        case 4:
            biblioteca.aggiungi()
            
            #chiusura/torna indietro menu
            chiusura()
        
        #analisi catalogo
        case 5:
            scelta_analisi = int(input("Analisi: 1. Analisi completa - 2. Analisi generi // "))
            if scelta_analisi == 1:
                analisi_totale(biblioteca)
                
                #chiusura/torna indietro menu
                chiusura()
            elif scelta_analisi == 2:
                analisi_generi(biblioteca)
                
                #chiusura/torna indietro menu
                chiusura()
    
        #case default
        case _:
            print("Operazione non eseguibile.")
            
            
            