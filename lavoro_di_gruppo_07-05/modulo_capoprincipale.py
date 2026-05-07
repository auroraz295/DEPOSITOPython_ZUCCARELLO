#CLASSE BASE CAPI PRINCIPALI

class CapoPrincipale:
    
    #definizione atrtibuti protetti
    def __init__(self, codice:int, nome:str, tessuto:str, colore:str, taglia:str, prezzo:float):
        self._codice = codice
        self._nome = nome
        self._tessuto = tessuto
        self._colore = colore
        self._taglia = taglia 
        self._prezzo = prezzo
    
    #FUNZIONE COSTO   
    def costo(self):
        return self._prezzo
    
#CLASSI FIGLIE

class Giacca(CapoPrincipale):
    
    #definizione e ereditarietà attributi
    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo, numerobottoni:int):
        super().__init__(codice, nome, tessuto, colore, taglia, prezzo)
        
        self._numerobottoni = numerobottoni

    #FUNZIONE COSTO   
    #per ogni bottone, costo aggiuntivo
    def costo(self):
        bonus_bottoni = 2.50
        self.costo_totale = (bonus_bottoni * self._numerobottoni) + self._prezzo
        
        return self._costo_totale
        

class Pantalone(CapoPrincipale):
    #definizione e ereditarietà attributi
    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo, tipotaglio:str):
        super().__init__(codice, nome, tessuto, colore, taglia, prezzo)

        self._tipotaglio = tipotaglio

    #FUNZIONE COSTO 
    #tre tagli di pantaloni, ad ognuna un costo diverso  
    def costo(self):
        tipo_skinny = 10.50
        tipo_wide = 16.50
        tipo_slim = 12
        
        if self._tipotaglio == "skinny":
            self._costo_totale = tipo_skinny + self._prezzo
            
            return self._costo_totale
            
        elif self._tipotaglio == "wide":
            self._costo_totale = tipo_wide + self._prezzo
            
            return self._costo_totale
            
        elif self._tipotaglio == "slim":
            self._costo_totale = tipo_slim + self._prezzo

            return self._costo_totale
            
            

class Gilet(CapoPrincipale):
    #definizione e ereditarietà attributi
    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo, reversibile:bool):
        super().__init__(codice, nome, tessuto, colore, taglia, prezzo)
        
        self._reversibile = reversibile
        
    #FUNZIONE COSTO   
    #se è reversibile, costo aggiuntivo
    def costo(self):
        bonus_reversibile = 21
        
        if self._reversibile:
            self._costo_totale = bonus_reversibile + self._prezzo
            
            return self._costo_totale
        
        else:
            return self._costo_totale   