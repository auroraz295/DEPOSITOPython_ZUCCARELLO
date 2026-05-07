# Classe genitore
class Finitura:

    # Attributi
    def __init__(self, codice: int, nome: str, materiale: str, colore: str, prezzo: float):
        self.__codice = codice
        self._nome = nome
        self._materiale = materiale
        self._colore = colore
        self._prezzo = prezzo

    # Getter del codice
    def get_codice(self):
        return self.__codice

    # Metodi
    def costo(self):
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