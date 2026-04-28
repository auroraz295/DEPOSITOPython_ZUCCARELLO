from abc import ABC, abstractmethod

# @abstrasctmethod permette di creare un metodo astratto (def muovi) 
# (è di conseguenza una classe astratta)
# che è vuoto. viene definito poi dalle classi figlie
# è come se fosse un "contenitore" astratto e vuoto da riempire in seguito 
class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass
    
class Cane(Animale):
    def muovi(self):
        print("Corro")
        
class Pesce(Animale):
    def muovi(self):
        print("Nuoto")