#SCOPE VARIABILI
#SCOPE GLOBALE
numero = 10

def funzione_esterna():
    #SCOPE LOCALE
    numero = 5 
    print(f"Numero dentro funzione_esterna (locale): {numero}")
    
    def funzione_interna():
        #SCOPE NON LOCAL
        #prende la variabile della funzione sopra e poi lo modifica 
        nonlocal numero
        numero = 3 
        print(f"Numero dentro funzioneinterna (nonlocal): {numero}")
        
    funzione_interna()
    
print(f"Numero nel main (globale): {numero}")
funzione_esterna()
print(f"Numero nel main dopo chiamata (globale non cambiato): {numero}")