""" #1. Creare una serie di condizioni una dentro l’altra che a fronte di un input
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

accounts = ["Auri", "Gloria", "Diego"]
psw = [1332, 6455, 9152]
id = [1, 2, 3]
accesso = int(input("Preferisci accedere(1) o registrarti(2)"))

if accesso == 2:
    nome = input("Inserisci il tuo nome: ")
    password = input("Inserisci la tua password di 4 cifre: ")
    id = 1
    accounts.append(nome)
    psw.append(password)
    print("Ti sei registrato con successo!")
    print(f"Nome utente:{nome}")
    print(f"Password: {password}")
    print(f"ID: {id}")     
else:
    accesso2 = input("Scegli l'account con cui accedere: ")
    psw2 = int(input("Digita la password da 4 cifre:"))
    if accesso2 in accounts:
        print("Accesso effettuato!")
      
#4. Scrivi un programma che chieda all'utente la sua età. Se l'età è
#inferiore a 18 anni, il programma dovrebbe stampare "Mi dispiace, non puoi
#vedere questo film". Altrimenti, dovrebbe stampare "Puoi vedere questo film".

eta = int(input("Quanti anni hai? "))

#condizione da rispettare 
if eta <18:
    print("Mi dispiace, non puoi vedere questo film.")
else:
    print("Puoi vedere questo film.")
"""   
    
#5.Scrivi un programma che chieda all'utente di inserire due
#numeri e un'operazione da eseguire tra addizione (+), sottrazione (-),
#moltiplicazione (*) e divisione (/). Il programma dovrebbe poi eseguire
#l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere
#per zero, il programma dovrebbe stampare "Errore: Divisione per zero". 
#Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione
#non valida".

#input per ottenere i due numeri su cui eseguire l'oeprazione
num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

operazione = input("Scegli l'operazione da eseguire: ")

#menu operazioni; per ogni operazione un caso e una print 
#nella divisione c'è una specifica in cui non si può dividere se il secondo numero è 0

match operazione:
    case "addizione":
        print("Il risultato dell'addizione è:", (num1 + num2))
    case "sottrazione":
        print("Il risultato della sottrazione è:", (num1 - num2))  
    case "moltiplicazione":
        print("Il risultato della moltiplicazione è:", (num1 * num2))
    case "divisione":
        if num2 == 0:
            print("Errore: Divisione per zero.")       
        else:
            print("Il risultato della divisione è:", (num1/num2))
    case _:
        print("Operazione non valida.")        