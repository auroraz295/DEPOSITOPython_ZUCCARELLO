#1. Creare una serie di condizioni una dentro l’altra che a fronte di un input
# per ogni if decidano se farti passare o no ( 3 livelli, fate un paragone con == )

#chiedo il numero all'utente e lo converto in int
richiesta = int(input("Scegli un numero: "))

#prima condizione
if richiesta >0:
    print("Il tuo numero è maggiore di 0.")
    #seconda condizione
    if richiesta >10:
        print("Il tuo numero è anche maggiore di 10.")
        #terza condizione
        if richiesta == 50: 
            print("Il numero che hai scelto è proprio il 50!")
            
#2. Andare a creare un if con vari elif e un else finale che gestisca un
# menu per la selezione di un crud basilare (aggiungi modifica elimina)
lista = [1, 2, 3, 4, 5, 6]
richiesta2 = int(input("Scegli se vuoi aggiungere(1), eliminare(2) o modificare(3): "))
print(f"La lista è {lista}")

#richiesta 1, aggiunge un elemento alla fine
if richiesta2 == 1:
    aggiungi = int(input("Che numero vuoi aggiungere? "))
    lista.append(aggiungi)
    print(lista)
    
#richiesta 2, rimuove un elemento    
elif richiesta2 == 2:
    rimuovi = int(input("Quale numero vuoi rimuovere? "))
    lista.remove(rimuovi)
    print(lista)
    
#richiesta 3, inserisce un elemento in una posizione   
elif richiesta2 == 3:
    modifica = int(input("Quale numero vuoi modificare? ")) 
    posizione = int(input("In che posizione vuoi inserirlo? "))   
    lista.insert(posizione, modifica)
    print(lista)
else: 
    lista.sort()
    print(lista)
    
#3. Creare un if con else semplice, dentro l’if inserire una struttura di creazione di dati (nome, password, id dato dal sistema a crescere) 
# e nell’else il controllo automatico la dove è presente l’account nel sistema e solo se si passa dall’else concludere lo script

accesso = int(input("Preferisci accedere(1) o registrarti(2)"))

if accesso == 2:
    nome = input("Inserisci il tuo nome: ")
    password = input("Inserisci la tua password: ")
    id = 1
    print("Ti sei registrato con successo!")
    print(f"Nome utente:{nome}")
    print(f"Password: {password}")
    print(f"ID: {id}")
    if accesso == 1:
        accesso2 = input("Scegli l'account con cui accedere: ")
        if accesso2 == nome:
                print("Accesso effettuato!")
        
    else:
        print("Accesso negato")
        
#DA RIVEDERE ESERCIZIO 3