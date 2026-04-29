#GESTIONE OFFICINA ELETTRODOMESTICI

#CLASSE BASE - ELETTRODOMESTICO
class Elettrodomestico():
    def __init__(self, marca:str, modello:str, anno_acquisto:int, guasto:str):
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto
     
    #METODI   
    def descrizione(self):
        print(f"Marca: {self.get_marca()} - Modello: {self.get_modello()} - Anno acquisto: {self.get_anno_acquisto()} - Guasto: {self.get_guasto()}")
    
    def stima_costo_base(self):
        return 100
        
    #GET E SET MARCA ELETTRODOMESTICO    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, nuova_marca):
        self.__marca = nuova_marca
        return self.__marca
    
    #GET E SET MODELLO ELETTRODOMESTICO
    def get_modello(self):
        return self.__modello
    
    def set_modello(self, nuovo_modello):
        self._modello = nuovo_modello
        return self.__modello
    
    #GET E SET ANNO ACQUISTO ELETTRODOMESTICO
    def get_anno_acquisto(self):
        return self.__anno_acquisto
    
    def set_anno_acquisto(self, nuovo_anno_acquisto):
        if nuovo_anno_acquisto <= 2026:
            self.__anno_acquisto = nuovo_anno_acquisto
            return self.__anno_acquisto
        else:
            print("Anno acquisto non valido.")
    
    #GET E SET GUASTO ELETTRODOMESTICO
    def get_guasto(self):
        return self.__guasto
    
    def set_guasto(self, nuovo_guasto):
        self.__guasto = nuovo_guasto
        return self.__guasto
         

#CLASSI DERIVATE 
#LAVATRICE
class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg:int, giri_centrifuga:int):
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        self.__capacita_kg = capacita_kg
        self.__giri_centrifuga = giri_centrifuga
     
    #METODO STIMA COSTO   
    def stima_costo_base(self):
        
        self.__costo_base = super().stima_costo_base()
        
        #bonus attributi aggiuntivi
        self.__bonus_capacita = 25
        self.__bonus_giri =  40

        
        #condizioni per il bonus
        if self.__capacita_kg <= 10:
            
            if self.__giri_centrifuga <=30:
                return self.__costo_base 
            else:
                return self.__costo_base + self.__bonus_giri
        
        elif self.__capacita_kg > 10:

            if self.__giri_centrifuga <=30:
                return self.__costo_base + self.__bonus_capacita
            else:
                return self.__costo_base + self.__bonus_capacita + self.__bonus_giri
            
        else:
            return 0
            
 
#CLASSE FRIGORIFERO         
class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, litri:int, ha_freezer:bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        self.__litri = litri
        self.__ha_freezer = ha_freezer
     
    #METODO STIMA COSTO     
    def stima_costo_base(self):
        
        self.__costo_base = super().stima_costo_base()
        
        #bonus attributi aggiuntivi
        self.__bonus_litri = 50
        self.__bonus_freezer =  75

        
        #condizioni per il bonus
        if self.__litri <= 10:
            
            if self.__ha_freezer == False:
                return self.__costo_base
            else:
                return self.__costo_base + self.__bonus_freezer
        
        elif self.__litri > 10:

            if self.__ha_freezer == True:
                return self.__costo_base + self.__bonus_litri + self.__bonus_freezer
            else:
                return self.__costo_base + self.__bonus_litri
            
        else:
            return 0 


#CLASSE FORNO 
class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, alimentazione, ventilato):
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        self.__alimentazione = alimentazione #elettrico o gas
        self.__ventilato = ventilato
    
    #METODO STIMA COSTO     
    def stima_costo_base(self):
        
        self.__costo_base = super().stima_costo_base()
        
        #bonus attributi aggiuntivi
        self.__bonus_tipo_forno = 100
        self.__bonus_ventilazione =  25

        
        #condizioni per il bonus
        if self.__alimentazione == "elettrico":
            
            if self.__ventilato == False:
                return self.__costo_base + self.__bonus_ventilazione 
            else:
                return self.__costo_base
        
        elif self.__alimentazione == "gas":

            if self.__ventilato == True:
                return self.__costo_base + self.__bonus_tipo_forno + self.__bonus_ventilazione
            else:
                return self.__costo_base + self.__bonus_tipo_forno
            
        else:
            return 0    
         
            
#CLASSE TICKET            
class TicketRiparazione:
    def __init__(self, id_ticket:int, elettrodomestico:Elettrodomestico):
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico
        self.__stato = "Aperto"
        self.__note = []
    
    #METODI AGGIUNGI NOTA - CALCOLA PREVENTIVO  
    def aggiungi_nota(self, testo):
        self.__note.append(testo)
        
    def calcola_preventivo(self):
        return self.__elettrodomestico.stima_costo_base()
        
    #GET TICKET
    def get_ticket(self):
        return self.__id_ticket
        
    #GET E SET STATO
    def get_stato(self):
        return self.__stato
    
    def set_stato(self, nuovo_stato):
        self.__stato = nuovo_stato
        return self.__stato
     
    #GET E SET _NOTE 
    def get_note(self):
        return self.__note
    
    def set_note(self, nuove_note):
        self.__note = nuove_note
        return self.__note
    
    #GET CLASS NAME
    #__elettrodomestico permette di accedere all'elettrodomestico inserito in ticket 
    def get_tipo(self):
        return self.__elettrodomestico.__class__.__name__
    
    #GET OGGETTO 
    #restituisce l'oggetto elettrodomestico 
    def get_oggetto(self):
        return self.__elettrodomestico
 
#CLASSE OFFICINA        
class Officina:
    def __init__(self, nome:str):
        self.nome = nome
        self.tickets =  []
    
    #METODI AGGIUNGI/CHIUDI/STAMPA/TOTALE TICKET     
    def aggiungi_ticket(self, ticket:TicketRiparazione):
        self.tickets.append(ticket)
    
    def chiudi_ticket(self, id_ticket):
        for t in self.tickets:
            if t.get_ticket() == id_ticket:
                nuovo_stato = "Chiuso"
                t.set_stato(nuovo_stato)
                print(f"Il ticket {id_ticket} è stato chiuso.")

    def stampa_ticket_aperti(self):
        for t in self.tickets:
            if t.get_stato() == "Aperto":
                print(f"ID: {t.get_ticket()} - Tipo elettrodomestico: {t.get_tipo()} - Stato: {t.get_stato()}")
    
    def totale_preventivi(self):
        somma_preventivi = 0 
        for t in self.tickets:
            preventivo = t.calcola_preventivo()
            somma_preventivi += preventivo
        print(f"Totale preventivi: {somma_preventivi}")
    
    #METODO STATISTICHE PER TIPO
    def statistiche_per_tipo(self):
        
        #inizializzazione somme 
        somma_forno = 0 
        somma_lav = 0
        somma_frigo = 0
        
        for t in self.tickets:
            
            #ricavo oggetto
            oggetto = t.get_oggetto()
            
            #confronto oggetti 
            if type(oggetto) == Forno:
                somma_forno += 1
                
            elif type(oggetto) == Lavatrice:
                somma_lav += 1 
                
            elif type(oggetto) == Frigorifero:
                somma_frigo +=1
        
        print(f"Numero di lavatrici in riparazione: {somma_lav} - Numero di frigoriferi in riparazione: {somma_frigo} - Numero di forni in riparazione: {somma_forno} ")
                
        
 
#SIMULAZIONE  

#CREAZIONE ELETTRODOMESTICI    
l1 = Lavatrice("Samsung", "EcoBubble", 2022, "Pompa scarico bloccata", 9, 1400)
l2 = Lavatrice("LG", "AI Direct Drive", 2023, "Cuscinetti rumorosi", 12, 1600)

f1 = Frigorifero("Bosch", "Serie 6", 2021, "Non raffredda", 350, True)
f2 = Frigorifero("Whirlpool", "Total No Frost", 2020, "Guarnizione rotta", 8, False) 

o1 = Forno("Smeg", "Victoria", 2019, "Resistenza bruciata", "elettrico", True)
o2 = Forno("Candy", "Pop Evo", 2024, "Vetro rotto", "gas", False)

#CREAZIONE TICKET 
t1 = TicketRiparazione(101, l1)
t2 = TicketRiparazione(102, l2)
t3 = TicketRiparazione(103, f1)
t4 = TicketRiparazione(104, f2)
t5 = TicketRiparazione(105, o1)
t6 = TicketRiparazione(106, o2)

#CREAZIONE OFFICINA
officina = Officina("Bruno&Zuccarello Riparazioni")

#AGGIUNGI TICKET
officina.aggiungi_ticket(t1)
officina.aggiungi_ticket(t2)
officina.aggiungi_ticket(t3)
officina.aggiungi_ticket(t4)
officina.aggiungi_ticket(t5)
officina.aggiungi_ticket(t6)

#PROVE METODI
#stampa ticket aperti
officina.stampa_ticket_aperti()

#cambio stato ticket
t3.set_stato("In lavorazione")
print(t3.get_stato())

#chiusura ticket 
officina.chiudi_ticket(101)
officina.stampa_ticket_aperti()

#totale preventivi
officina.totale_preventivi()

#statistiche per tipo
officina.statistiche_per_tipo()