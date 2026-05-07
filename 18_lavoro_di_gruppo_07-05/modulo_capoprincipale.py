#CLASSE BASE CAPI PRINCIPALI

class CapoPrincipale:
    
    #definizione attributi protetti
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
    
    #GET E SET ATTRIBUTI
    #codice
    def get_codice(self): 
        return self._codice
    
    #nome
    def get_nome(self): 
        return self._nome
    
    def set_nome(self, nuovo_nome): 
        self._nome = nuovo_nome
        return self._nome

    #tessuto
    def get_tessuto(self): 
        return self._tessuto
    
    def set_tessuto(self, nuovo_tessuto): 
        self._tessuto = nuovo_tessuto
        return self._tessuto
    
    #colore
    def get_colore(self): 
        return self._colore
    
    def set_colore(self, nuovo_colore): 
        self._colore = nuovo_colore
        return self._colore

    #taglia
    def get_taglia(self): 
        return self._taglia
    
    def set_taglia(self, nuovo_taglia): 
        self._taglia = nuovo_taglia
        return self._taglia

    #prezzo
    def get_prezzo(self): 
        return self._prezzo
    
    def set_prezzo(self, nuovo_prezzo): 
        self._prezzo = nuovo_prezzo
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
    
    #GET E SET CARATTERISTICHE
    def get_numerobottoni(self):
        return self._numerobottoni
    
    def set_numerobottoni(self, nuovi_bottoni):
        self._numerobottoni = nuovi_bottoni
        return self._numerobottoni
        

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
            
    #GET E SET CARATTERISTICHE
    def get_tipo_taglio(self):
        return self._tipo_taglio
    
    def set_tipo_taglio(self, nuovo_tipo):
        self._tipo_taglio = nuovo_tipo
        return self._tipo_taglio
            

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
            return self._prezzo  
        
    #GET E SET CARATTERISTICHE
    def get_reversibile(self):
        return self._reversibile
    
    def set_reversibile(self, nuovo_reversibile):
        self._reversibile = nuovo_reversibile
        return self._reversibile