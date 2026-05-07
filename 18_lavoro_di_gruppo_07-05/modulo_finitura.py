# Classe genitore
class Finitura:

    # Attributi
    def __init__(self, codice: int, nome: str, materiale: str, colore: str, prezzo: float):
        self._codice = codice
        self._nome = nome
        self._materiale = materiale
        self._colore = colore
        self._prezzo = prezzo

    # Metodi
    def costo(self):
        return self._prezzo
    
    # Getter codice
    def get_codice(self): 
        return self._codice
    
    # Getter e setter nome
    def get_nome(self): 
        return self._nome
    def set_nome(self, nuovo_nome): 
        self._nome = nuovo_nome
        return self._nome

    # Getter e setter tessuto
    def get_tessuto(self): 
        return self._nome
    def set_tessuto(self, nuovo_tessuto): 
        self._tessuto = nuovo_tessuto
        return self._tessuto
    
    # Getter e setter colore
    def get_colore(self): 
        return self._colore
    def set_colore(self, nuovo_colore): 
        self._colore = nuovo_colore
        return self._colore

    # Getter e setter taglia
    def get_taglia(self): 
        return self._taglia
    def set_taglia(self, nuovo_taglia): 
        self._taglia = nuovo_taglia
        return self._taglia

    # Getter e setter prezzo
    def get_prezzo(self): 
        return self._prezzo
    def set_prezzo(self, nuovo_prezzo): 
        self._prezzo = nuovo_prezzo
        return self._prezzo

# Classi figlie
class Cravatta(Finitura):
    # Attributi
    def __init__(self, codice: int, nome: str, materiale: str, colore: str, prezzo: float, larghezza: int):
        super().__init__(codice, nome, materiale, colore, prezzo)
        self._larghezza = larghezza

    def costo(self):
        costo_per_larghezza = 2.0
        self._costo_totale = self._prezzo + (self._larghezza * costo_per_larghezza)
        return self._costo_totale
    
    # Getter e setter larghezza
    def get_larghezza(self): 
        return self._larghezza
    def set_larghezza(self, nuova_larghezza): 
        self._larghezza = nuova_larghezza
        return self._larghezza
    

class Papillon(Finitura):
    # Attributi
    def __init__(self, codice: int, nome: str, materiale: str, colore: str, prezzo: float, tipo_chiusura: str):
        super().__init__(codice, nome, materiale, colore, prezzo)
        self._tipo_chiusura = tipo_chiusura

    def costo(self):
        if self._tipo_chiusura == "a clip":
            costo_per_tipo_chiusura = 5.0
            self._costo_totale = self._prezzo + costo_per_tipo_chiusura
            return self._costo_totale
        elif self._tipo_chiusura == "a nodo":
            costo_per_tipo_chiusura = 7.0
            self._costo_totale = self._prezzo + costo_per_tipo_chiusura
            return self._costo_totale
        else:
            return self._prezzo
        
    # Getter e setter tipo_chiusura
    def get_tipo_chiusura(self): 
        return self._tipo_chiusura
    def set_tipo_chiusura(self, nuova_chiusura): 
        self._tipo_chiusura = nuova_chiusura
        return self._tipo_chiusura


class Pochette(Finitura):
    # Attributi
    def __init__(self, codice: int, nome: str, materiale: str, colore: str, prezzo: float, piega_decorativa: bool):
        super().__init__(codice, nome, materiale, colore, prezzo)
        self._piega_decorativa = piega_decorativa

    def costo(self):
        if self._piega_decorativa:
            costo_piega = 3.0
            self._costo_totale = self._prezzo + costo_piega
            return self._costo_totale
        else:
            return self._prezzo
        
    # Getter e setter piega_decorativa
    def get_piega_decorativa(self): 
        return self._piega_decorativa
    def set_piega_decorativa(self, nuova_piega_decorativa): 
        self._piega_decorativa = nuova_piega_decorativa
        return self._piega_decorativa