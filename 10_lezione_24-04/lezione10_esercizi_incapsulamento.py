#ESERCIZIO 1 
#Creare una classe ContoBancario che incapsula le informazioni di un conto e fornisce metodi
# per gestire il saldo in modo sicuro. L'obiettivo è utilizzare l'incapsulamento per 
# prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto.

#CLASSE BASE
class ContoBancario:
    
    #definizione attributi privati con __
    def __init__(self, num_titolare:str, num_saldo:float):
        self.__titolare = num_titolare
        self.__saldo = num_saldo
      
    #azione di deposito (e aumento saldo) solo se l'importo è maggiore di 0     
    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Utente: {self.__titolare} - Importo: {self.__saldo} euro")
        else:
            print("Importo non valido.")
     
    #azione di prelievo solo se il saldo è maggiore all'importo da prelevare        
    def preleva(self, importo):
        if self.__saldo >importo and importo> 0:
            self.__saldo -= importo
            print(f"Hai prelevato {importo}.")
            print(f"Utente {self.__titolare} - Importo: {self.__saldo} euro")
        else:
            print("Prelievo non disponibile.")
    
    #azione di visualizzazione saldo        
    def visualizza_saldo(self):
        print(f"Utente: {self.__titolare} - Saldo corrente: {self.__saldo} euro")
    
    #restituisce il titolare    
    def get_titolare(self):
        return self.__titolare
    
    #modifica il titolare
    def set_titolare(self, nuovo_titolare:str):
        if nuovo_titolare != " ":
            self.__titolare = nuovo_titolare
        else:
            print("Inserire un nome per il titolare valido.")
  
#SIMULAZIONE        
p = ContoBancario("Aurora", 1000.0)

p.deposita(200)
p.deposita(400)
p.preleva(150)
p.visualizza_saldo()

print(p.get_titolare())
p.set_titolare("Chiara")
print(p.get_titolare())


#ESERCIZIO 2 
#Sistema di gestione studenti
#Immagina di dover creare un sistema di gestione per una scuola che deve mantenere 
# le informazioni sugli studenti, i professori e le lezioni. Seguendo il paradigma 
# della programmazione orientata agli oggetti (OOP), dovrai implementare le classi necessarie
# usando incapsulamento, ereditarietà e polimorfismo.

#CLASSE BASE
class Persona:
    
    #attributi Persona nome ed età privati con __
    def __init__(self, nome:str, eta:int):
        self.__nome = nome
        self.__eta = eta
    
    #print di presentazione    
    def presentazione(self):
        print(f"Ciao, sono {self.__nome} e ho {self.__eta} anni.")
    
    #restituisce nome, eta e modifica entrambi     
    def get_nome(self):
        return self.__nome
        
    def get_eta(self):
        return self.__eta
    
    def set_nome(self, nome_nuovo):
        self.__nome = nome_nuovo
        
    def set_eta(self, eta_nuova):
        self.__eta = eta_nuova
        
#SOTTOCLASSI

#EREDITARIETA'
class Studente(Persona):
    
    #attributi Studente
    def __init__(self, nome, eta, voti_studente:list):
        super().__init__(nome, eta)
        self.voti_studente = voti_studente
    
    #conta quanto è lunga la lista, per ogni voto in lista accumula una somma_voti e divide per voti_tot
    def calcola_media(self):
        voti_tot = len(self.voti_studente)
        somma_voti = 0
        for voto in self.voti_studente:
            somma_voti += voto
        media_voti = somma_voti / voti_tot
        return media_voti
    
    #POLIMORFISMO
    #OVERRIDE presentazione Persona, con aggiunta di self.calcola_meda()
    def presentazione(self):
        print(f"Ciao, sono uno studente e mi chiamo {self.get_nome()}, ho {self.get_eta()} anni e ho una media di {self.calcola_media()}.")
        
#EREDITARIETA'       
class Professore(Persona):
    
    #attributi Professore
    def __init__(self, nome, eta, materia:str):
        super().__init__(nome, eta)
        self.materia = materia
    
    #POLIMORFISMO
    #OVERRIDE presentazione Persona, con aggiunta di self.materia    
    def presentazione(self):
        print(f"Ciao, sono un professore e mi chiamo {self.get_nome()}, {self.get_eta()} anni e insegno {self.materia}.")
        

#SIMULAZIONE
ps = Persona("Chiara", 30)
ps.presentazione()                   
            
st1 = Studente("Aurora", 25, [8, 6.5, 6, 8, 9])
st1.calcola_media()
st1.presentazione()

pf1 = Professore("Maria", 55, "Italiano")
pf1.presentazione()
