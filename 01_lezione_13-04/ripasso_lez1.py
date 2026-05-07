#TIPI VARIABILI

var1 = "ciao"
var2 = 34
var3 = 2.5
var4 = False

print(f"{var1} è di tipo {type(var1)}")
print(f"{var2} è di tipo {type(var2)}")
print(f"{var3} è di tipo {type(var3)}")
print(f"{var4} è di tipo {type(var4)}")

#ASSEGNAZIONE MULTIPLE
#più valori in una stessa variabile
a, b, c = 4, 11, 7
print(a,b,c)

#stesso valore in più variabili
e = f = g = 13
print(e, f, g)

#VARIABILI DINAMICHE
nome = "Aurora"
print(nome)

nome = "Claudia"
print(nome)

#OPERAZIONI VARIABILI
a = 24
b = 3

print(f"Addizione: {a+b}, Sottrazione: {a-b}, Moltiplicazione: {a*b}, Divisione: {a/b}")
print(f"Divisione intera: {a//b}, Modulo: {a%b}, Potenza: {a**b}")

#CASTING (conversione tipi di dato)
numero = "23"
print(f"Variabile: {numero}, tipo {type(numero)}")

numero = int(numero)
print(f"Variabile: {numero}, tipo {type(numero)}")

#COSTANTI (nome variabile maiuscolo)

PI_GRECO = 3.14159

#VARIABILI GLOBALI (scope)
#esterno
x = 44 

def esempio_scope():
    x = 1
    print(f"Scope interno: {x}")
    
esempio_scope()    
print(f"Scope esterno: {x}")    

#GLOBAL
contatore = 0 

def incrementa():
    global contatore
    contatore += 1

incrementa()
incrementa()
incrementa()

print(f"Contatore globale: {contatore}")

#global permette di usare la variabile fuori dallo scope della funzione, anziché crearne una nuova 
#permette anche di modificare fuori la funzione la variabile 
#stampando la variabile fuori, il risultato è 3 e non 0
