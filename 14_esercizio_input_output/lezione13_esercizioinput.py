#GESTORE FILE RICEVUTA DI ACQUISTO E ORDINE

#CLASSE UTENTE
class Utente:
    def __init__(self, nome):
        self.nome = nome
     
p1 = Utente("Aurora")        
 
ricevuta = open("ricevuta_acquisto.txt", "w")
ricevuta.close()


#MAIN
while True:
    
    
    comando = int(input(f"Ciao {p1.nome}, scegli cosa acquistare: 1. Libri - 2. Videogiochi - 3. Giocattoli -  "))
    match comando:
        
        #libri
        case 1:
            scelta_libri = int(input("Acquista: 1. The Host - 2. Harry Potter e il Prigioniero di Azkaban - 3. Divergent - "))
            match scelta_libri:
                case 1:
                    with open("ricevuta_acquisto.txt", "a") as f:
                        f.write("The Host, ")
                        
                    scelta_continue = input("Vuoi continuare ad acquistare? SI / NO -  ")
                    match scelta_continue:
                        case "SI":
                            continue
                        case "NO":
                            pass 
                        
                    
                case 2:
                    with open("ricevuta_acquisto.txt", "a") as f:
                        f.write("Harry Potter e il Prigioniero di Azkaban, ")
                        
                    scelta_continue = input("Vuoi continuare ad acquistare? SI / NO -  ")
                    match scelta_continue:
                        case "SI":
                            continue
                        case "NO":
                            pass 
                    
                case 3:
                    with open("ricevuta_acquisto.txt", "a") as f:
                        f.write("Divergent, ")
                        
                    scelta_continue = input("Vuoi continuare ad acquistare? SI / NO -  ")
                    match scelta_continue:
                        case "SI":
                            continue
                        case "NO":
                            pass 
                
                case _:
                    print("Opzione non eseguibile. ")
                    continue
        
        #videogiochi   
        case 2:
            scelta_videogiochi = int(input("Acquista: 1. The Last of Us - 2. Watch Dogs 2  - 3. Marvel's Spiderman - "))
            match scelta_videogiochi:
                case 1:
                    with open("ricevuta_acquisto.txt", "a") as f:
                        f.write("The Last of Us, ")
                        
                    scelta_continue = input("Vuoi continuare ad acquistare? SI / NO -  ")
                    match scelta_continue:
                        case "SI":
                            continue
                        case "NO":
                            pass 
                
                case 2:
                    with open("ricevuta_acquisto.txt", "a") as f:
                        f.write("Watch Dogs 2, ")
                        
                    scelta_continue = input("Vuoi continuare ad acquistare? SI / NO -  ")
                    match scelta_continue:
                        case "SI":
                            continue
                        case "NO":
                            pass 
                
                case 3:
                    with open("ricevuta_acquisto.txt", "a") as f:
                        f.write("Marvel's Spiderman, ")
                        
                    scelta_continue = input("Vuoi continuare ad acquistare? SI / NO -  ")
                    match scelta_continue:
                        case "SI":
                            continue
                        case "NO":
                            pass 
       
       
        #giocattoli
        case 3:
            scelta_giocattoli = int(input("Acquista: 1. Barbie Fairytopia - 2. Peluche XL Winnie The Pooh  - 3. Set bambole Winx - "))
            match scelta_giocattoli:
                case 1:
                    with open("ricevuta_acquisto.txt", "a") as f:
                        f.write("Barbie Fairytopia, ")
                        
                    scelta_continue = input("Vuoi continuare ad acquistare? SI / NO -  ")
                    match scelta_continue:
                        case "SI":
                            continue
                        case "NO":
                            pass 
                
                case 2:
                    with open("ricevuta_acquisto.txt", "a") as f:
                        f.write("Peluche XL Winnie The Pooh, ")
                        
                    scelta_continue = input("Vuoi continuare ad acquistare? SI / NO -  ")
                    match scelta_continue:
                        case "SI":
                            continue
                        case "NO":
                            pass 
                
                case 3:
                    with open("ricevuta_acquisto.txt", "a") as f:
                        f.write("Set bambole Winx, ")
                        
                    scelta_continue = input("Vuoi continuare ad acquistare? SI / NO -  ")
                    match scelta_continue:
                        case "SI":
                            continue
                        case "NO":
                            pass 
       
    
        #case default
        case _:
            pass 

    comando2 = int(input("1. Stampa ricevuta di acquisto - 2. Stampa ricevuta di ordine -  "))
    match comando2:
        
        #ricevuta acquisto
        case 1:
            lista_articoli = []
            with open("ricevuta_acquisto.txt", "r") as f:
                for riga in f:
                    articolo = riga.strip(", ")
                    lista_articoli.append(articolo)
                
            for a in lista_articoli:
                print(a)        
            break
            
        
        #ricevuta ordine
        case 2:
            with open("ricevuta_acquisto.txt", "r") as f:
                for riga in f:
                    print(riga.strip(", "))
            break
        
        case _:
            print("Opzione non eseguibile.")
            continue