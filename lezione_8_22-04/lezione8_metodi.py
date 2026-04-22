#METODO STATICO
class Calcolatrice:
    @staticmethod
    def somma(a,b):
        return a+b
    
risultato = Calcolatrice.somma(5,3)

print(risultato)

#METODO DECORATO
class Contatore:
    numero_istanze = 0 
    def __init__(self):
        Contatore.numero_istanze += 1
        
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")

c1 = Contatore()
c2 = Contatore()
c3 = Contatore()

#si preferisce chiamare la classe Contatore e non l'oggetto c1, c2 o c3, perché è un
#metodo legato alla classe
Contatore.mostra_numero_istanze()

#ALTRO ESEMPIO USO @CLASSMETHOD
class Persona:
    def __init__(self, nome: str, eta: int):
        self.nome = nome 
        self.eta = eta 
        
    #se ci serve prendere informazioni da un excel o csv, anziché prendere ogni volta la stringa e scomporla,
    # con classmethod costruisce l'oggetto e prende la stringa     
    @classmethod
    def init_from_string(cls, s: str):   
        nome, eta = s.split(",")                  #si scompone la stringa in arrivo
        
        #cls è il riferimento alla classe Persona
        return cls(nome, int(eta))
    
p = Persona.init_from_string("Mario,30")
print(p.nome, p.eta)

#in questo caso @classmethod è stato utilizzato per scomporre una stringa, definendo l'oggetto persona 
#e scomponendo la stringa (data in input), così da avere nome ed età
