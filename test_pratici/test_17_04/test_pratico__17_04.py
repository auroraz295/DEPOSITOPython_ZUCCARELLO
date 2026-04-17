#PRIMO PUNTO - LOGIN E REGISTRAZIONE

#liste per gli account
nomiutenti = []
pswutenti = []

#lista per i numeri
lista_addendi = []
lista_risultati = []

#FUNZIONE REGISTRAZIONE
def registrazione():
    while True:
        nome = input("Inserisci il tuo nome: ")
        
        #se il nome esiste già nella lista, riprovare con un nuovo nome
        if nome in nomiutenti:
            print("Spiacente! Nome già utilizzato. Riprova la registrazione con un nuovo nome utente")    
            continue
        
        #altrimenti prosegue la registrazione utente chiedendo la password
        else:
            nomiutenti.append(nome)
            psw = input("Inserisci una password di 4 cifre: ") 
            pswutenti.append(psw)
            print("Registrazione effettuata con successo!")
            break

#FUNZIONE ACCESSO
def accesso():
    while True:
        nome2 = input("Inserisci il nome con cui vuoi accedere: ")
        #se il nome non è già nella lista, quindi non è registrato, non si può accedere
        if nome2 not in nomiutenti:
            print("Mi dispiace, non sei registrato. ")
            return False
        
        #altrimenti si prosegue con l'accesso e l'inserimento password
        else:
            psw2 = input("Inserisci la tua password: ")
            
            #se la password non è presente in lista, è sbagliata e si deve ritentare l'accesso
            if psw2 not in pswutenti:
                print("Mi dispiace, password sbagliata.")
            else:
                print("Accesso effettuato con successo!")
                
                #faccio restituire vero in modo tale da avere un controllo che faccia accedere alla calcolatrice e alla stampa solo chi ha effettuato l'accesso
                return True
            
#FUNZIONE NUMERI           
def numeri():
    num_addendi= int(input("Su quanti numeri vuoi effettuare l'operazione? "))
    
    lista_operazione = []
    #finché la lista di numeri è minore del numero totale di numeri su cui fare l'operazione
    while len(lista_operazione)< num_addendi:
       
        #chiederà x volte di inserire il numero per quanto inserito in num_addendi
        addendo = int(input("Inserisci il numero: "))
        
        #ogni numero viene aggiunto alla lista per poter fare l'operazione
        lista_operazione.append(addendo)
        
        #ogni numero viene aggiunto alla lista per poter stampare tutti gli addendi
        lista_addendi.append(addendo)
    return lista_operazione
  
#FUNZIONE ADDIZIONE        
def addizione(lista_operazione):
    
    #contatore somma a zero inizialmente
    risultato_somm = 0
    
    #per ogni numero nella lista, somma
    for i in lista_operazione:
        risultato_somm += i
        
    #salvo il risultato in una lista    
    lista_risultati.append(risultato_somm)    
    print(f"Il risultato della tua addizione è: {risultato_somm}") 
    return risultato_somm  
 
#FUNZIONE SOTTRAZIONE            
def sottrazione(lista_operazione):
    
    #prendo il primo numero, altrimenti verranno sottrazioni negative
    risultato_sott = lista_operazione[0]
    for i in lista_operazione[1:]:
        risultato_sott -= i 
        
    #salvo il risultato in una lista    
    lista_risultati.append(risultato_sott)      
    print(f"Il risultato della tua sottrazione è {risultato_sott}")
    return risultato_sott

#FUNZIONE MOLTIPLICAZIONE
def moltiplicazione(lista_operazione):
    
    #prendo il primo numero della lista, non potevo iniziare il contatore con 0 o tutti i risultati sarebbero stati 0
    risultato_mol = lista_operazione[0]
    
    #seleziono dal secondo numero in poi o viene il risultato falsato
    for i in lista_operazione[1:]:
        risultato_mol = risultato_mol * i 
        
    #salvo il risultato in una lista    
    lista_risultati.append(risultato_mol)      
    print(f"Il risultato della tua moltiplicazione è {risultato_mol}")
    return risultato_mol

#FUNZIONE DIVISIONE
def divisione(lista_operazione):
    
    #anche qui preferisco prendere il primo numero della lista
    risultato_div = lista_operazione[0]
    
    #prendo il secondo dalla lista
    for i in lista_operazione[1:]:
        if i == 0:
            print("Errore. Impossibile dividere per zero!")
        else:    
            risultato_div = risultato_div/i
        
    #salvo il risultato in una lista    
    lista_risultati.append(risultato_div)      
    print(f"Il risultato della tua divisione è: {risultato_div}")
    return risultato_div

#FUNZIONE POTENZA
def potenza():
    
    #chiedo di inserire solo due numeri per la potenza
    num1 = int(input("Inserisci il numero su cui effettuare una potenza: ")) 
    num2 = int(input("Inserisci la base su cui elevare il tuo numero: ")) 
    risultato_pot = num1 ** num2
    
    #salvo il risultato in una lista    
    lista_risultati.append(risultato_pot)  
    print(f"Il risultato della tua potenza è {risultato_pot}")      
    return risultato_pot

#FUNZIONE ALTRO, nel caso in cui nel menu si digiti altri caratteri
def altro():
    print("Azione non eseguibile")
  
#FUNZIONE ADDENDI, deve restituire la stampa degli addendi scelti - DA COMPLETARE
def addendi():
    print(f"Gli addendi che hai utilizzato nelle operazioni sono: {lista_addendi}")
    pass
    
#FUNZIONE RISULTATI, deve restituire la stampa di tutti i risultati ottenuti - DA COMPLETARE    
def risultati():  
    print(f"I risultati ottenuti nelle tue operazioni sono: {lista_risultati} ")  
    pass

#MENU CALCOLATRICE, ogni operazione è una funzione            
def calcolatrice():
    operazione = int(input("Quale operazione vuoi eseguire? 1. Addizione 2. Sottrazione 3. Moltiplicazione 4. Divisione 5. Potenza "))   
    match operazione:
        
        case 1: addizione(numeri())
        
        case 2: sottrazione(numeri()) 
        
        case 3: moltiplicazione(numeri())
        
        case 4: divisione(numeri())
        
        case 5: potenza()
            
        case _: altro()

#MENU STAMPA
def stampa():
    scelta = int(input("Cosa vuoi stampare? 1. Addendi 2.Risultati - "))
    match scelta:
        
        case 1: addendi()
        
        case 2 : risultati()
        
        case _: altro()



#MENU COMPLETO           
while True:
    #imposto inanzitutto il login falso
    login = False
    menu1 = int(input("Vuoi registrarti o accedere con il tuo account? 1. Registrazione 2. Accesso - "))
    
    match menu1:
        
        case 1: registrazione()
            
        case 2: login = accesso()
        
        case _: altro()
    
    #solo chi ha avuto accesso all'account può eseguire le operazioni
    if login == True:
        
        #faccio iterare questo menu solo 5 volte e poi richiederà il login
        for i in range(5):
         
            menu2 = int(input("Vuoi usare la calcolatrice o stampare i dati? 1. Calcolatrice 2.Stampa dati - "))  
    
            match menu2:
                case 1: calcolatrice()
            
                case 2: stampa()  
            
                case _: altro()
                
           