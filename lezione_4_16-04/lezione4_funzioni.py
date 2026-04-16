#FUNZIONE
#def nome funzione(parametro): 

#funzione senza return con un parametro
def saluta(nome):
    print(f"Ciao, {nome}.")
    
#funzione richiamata    
saluta("Aurora")

#funzione senza return con due o infiniti parametri
def somma(a, b):
    risultato = a + b 
    print(f"La somma è: {risultato}")
    
#funzione richiamata 
somma(5, 3)

#funzione con RETURN
def quadrato(numero):
    return numero * numero

risultato = quadrato(4)
print(risultato)

#TIPI DI PARAMETRI
#posizionali: ordine esatto / keyword: qualsiasi ordine / default: specificano valore predefinito

#nome è posizionale, messaggio è default
def saluta(nome:str, messaggio="Ciao"):
    print(f"{messaggio} {nome}!")
    
saluta("Mario")
saluta("Luigi", messaggio="Buongiorno")

#FUNZIONE GENERATORE
def fibonacci(n):
    a,b = 0, 1
    
    while a < n:
        yield a
        a, b = b, a + b
        
#DECORATORE
def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao!")

saluta()