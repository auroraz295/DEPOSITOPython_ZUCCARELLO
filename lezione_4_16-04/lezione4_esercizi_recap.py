#ESERCIZIO RECAP 

def funzione1():
    while True:
        num1 = int(input("Inserisci un numero intero positivo: "))
        #se il numero non è positivo ripeto il ciclo
        if num1 <0 or num1 == 0:
            continue 
        else:
            break
        
def funzione2():
    num2 = int(input("Inserisci un numero n per generare una lista di numeri casuali da 1 a n: "))      
    lista1 = []
    #per ogni elemento da 1 fino a n+1 (altrimenti viene escluso n)
    for i in range(1, (num2+1)):
        lista1.append(i)
    print(lista1) 
        
while True:
    recap = int(input("Quale punto dell'esercizio di recap vuoi svolgere? Da 1 a 7: "))
    
    #menu
    match recap:
        case 1: funzione1()
        case 2: funzione2()
        case 3: pass
        case 4: pass
        case 5: pass
        case 6: pass
        case 7: pass
        case _: break