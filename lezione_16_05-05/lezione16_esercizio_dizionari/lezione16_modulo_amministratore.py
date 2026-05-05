#GESTIONE AMMINISTRATORI
# - rapporto vendite
# - rapporto stato inventario
# - rapporto guadagni totali

class Amministratore:
    def __init__(self):
        self.admin = {"admin1": 2811}
        self.guadagni = 0
        self.report_vendite = []
    
    #accesso admin    
    def login_admin(self):
        input_admin = input("Admin: ")
        input_password = int(input("Password: "))
        
        if input_admin in self.admin and self.admin[input_admin] == input_password:
            print(f"Login {input_admin} effettuato.")
            return True
        else:
            print("Admin e/o password errate.")
            return False
    
    #stampa guadagni e vendite        
    def visualizza_report(self, inventario):
        print(f"Guadagni vendite: {self.guadagni} - Storico vendite: {self.report_vendite}")
    
    #stampa l'inventario completo
    def stato_inventario(self, inventario):
        inventario.visualizza_stato() 
    