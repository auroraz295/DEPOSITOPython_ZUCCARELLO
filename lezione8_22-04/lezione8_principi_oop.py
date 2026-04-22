#EREDITARIETA' CLASSI BASE

#SUPERCLASSE // classe "padre"
class Animale:
    def __init__(self, nome):
        self.nome = nome
    
    def parla(self):
        print(f"{self.nome} fa suono generico.")

#SOTTOCLASSE // classe "figlio"        
class Cane(Animale):
    def parla(self):
        print(f"{self.nome} abbaia!")
        
animale_generico = Animale("AnimaleGenerico")
cane = Cane("Fido")

animale_generico.parla()
cane.parla()

#EREDITARIETA' MULTIPLA CLASSI 

#due classi base
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
    def mostra_informazioni(self):
        print(f"Veicolo marca: {self.marca}, Modello: {self.modello}")
        
class DotazioniSpeciali:
    def __init__(self, dotazioni:list[str]):
        self.dotazioni = dotazioni
        
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {", ".join(self.dotazioni)}")
        
#classe automobile che eredita entrambe le classi

class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        #richiamo la superclasse
        #alternativa: super().__init__(self, marca, modello)
        Veicolo.__init__(self, marca, modello)                
        
        #richiamo l'altra classe
        #alternativa: self.__init__(self, dotazioni)
        DotazioniSpeciali.__init__(self, dotazioni)
        
        self.cavalli = cavalli
        
    def mostra_informazioni(self):
        
        #alternativa: Veicolo.mostra_informazioni(self) // 
        # super() non ha bisogno del (self) ed eredita la prima superclasse
        super().mostra_informazioni()      
        
        #alternativa: DotazioniSpeciali.mostra_dotazioni(self)  // 
        #self. va a prendere direttamente il mostra dotazione della classe ereditata                   
        self.mostra_dotazioni()
        
        print(f"Potenza: {self.cavalli} cavalli")
        
auto = AutomobileSportiva("Ferrari", "F8", 
                          #lista dotazioni
                          ["ABS", "Controllo trazione", "Airbag laterali"],
                          720)   

auto.mostra_informazioni()    