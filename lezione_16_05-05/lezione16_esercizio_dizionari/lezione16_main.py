#MAIN

#importo moduli 
from lezione16_modulo_clienti import Cliente
from lezione16_modulo_inventario import Inventario
from lezione16_modulo_amministratore import Amministratore

#creazione oggetti
gestione_clienti = Cliente()
inventario = Inventario()
admin = Amministratore()

while True:
    comando = int(input("Menù: 1. Registrazione Cliente - 2. Accesso Cliente - 3. Accesso Admin // "))
    match comando:
        case 1:
            gestione_clienti.registrazione()
            continue
        
        case 2:
            cliente = gestione_clienti.accesso()
            if cliente:
                print("Acquista articoli")
                gestione_clienti.acquista(inventario, admin)
                
        case 3:
            if admin.login_admin():
                while True:
                    comando_admin = int(input("1. Visualizza rapporto vendite - 2. Visualizza stato inventario - 3. Aggiungi articoli inventario - 4. Modifica articoli - 5. Rimuovi articoli // "))
                    match comando_admin:
                        case 1:
                            admin.visualizza_report(inventario)
                            continue
                        
                        case 2:
                            inventario.visualizza_stato()
                            continue
                    
                        case 3: 
                            inventario.aggiungi_articoli()
                            pass
                    
                        case 4:
                            inventario.modifica_articoli()
                            continue
                    
                        case 5:
                            inventario.rimuovi_articoli()
                            continue
                    
                        case _:
                            print("Operazione non disponibile.")
                            continue
             
        case _:
            print("Operazione non disponibile.")
            continue
        
        