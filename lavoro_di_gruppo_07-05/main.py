#MAIN

from modulo_capoprincipale import Giacca, Pantalone, Gilet 
from modulo_finitura import Cravatta, Papillon, Pochette

#lista catalogo capi
catalogo = []

#inserimento vendite randomico 


#FUNZIONE CREA CAPO
def crea_capo(self):
    scelta_capo = int(input("Cosa vuoi creare? 1. Giacca - 2. Pantalone - 3. Gilet - 4- Cravatta - 5. Papillon - 6. Pochette // "))
    codice = int(input("Inserisci codice: "))
    nome = codice
    tessuto = input("Inserisci tessuto: ")
    taglia = input("Inserisci taglia: ")
    colore = input("Inserisci colore: ")
    prezzo = float(input("Inserisci prezzo: "))
    
    #GIACCA
    if scelta_capo == 1: 
        n_bottoni = int(input("Numero bottoni giacca: "))
        catalogo.append(Giacca(codice, nome, tessuto, taglia, colore, prezzo, n_bottoni))
        
    
    #PANTALONE    
    elif scelta_capo == 2:
        tipo_taglio = int(input("Tipo taglio: 1. Skinny - 2. Wide - 3. Slim // "))
        catalogo.append(Pantalone(codice, nome, tessuto, taglia, colore, prezzo, tipo_taglio))
    
    #GILET
    elif scelta_capo == 3:
        reversibile = input("Reversibile: SI / NO")
        if reversibile == "SI":
            reversibile = True
            catalogo.append(Gilet(codice, nome, tessuto, taglia, colore, prezzo, reversibile))
        else:
            reversibile = False
            catalogo.append(Gilet(codice, nome, tessuto, taglia, colore, prezzo, reversibile))
    
    #CRAVATTA
    elif scelta_capo == 4:
        larghezza = int(input("Larghezza cravatta: "))
        catalogo.append(Cravatta(codice, nome, tessuto, colore, prezzo, larghezza))


    #PAPILLON
    elif scelta_capo == 5:
        tipo_chiusura = int(input("Tipo chiusura: 1. A clip - 2. A nodo // "))
        if tipo_chiusura == 1:
            pass
        
        if tipo_chiusura == 2:
            pass
    
    
    #POCHETTE
    elif scelta_capo == 6:
        pass


#FUNZIONE MODIFICA CAPO
def modifica_capo(self):
    pass


#FUNZIONE ELIMINA CAPO 
def elimina_capo(self):
    pass


#menu
comando = int(input("Menu: 1. Crea capo - 2. Modifica capo - 3. Elimina capo - 4. Genera dati // "))

match comando :
    case 1:
        pass
    
    case 2:
        pass
    
    case 3:
        pass
    
    case 4:
        pass
    
    case _:
        print("Opzione non disponibile ")