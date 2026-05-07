#INCAPSULAMENTO

#ATTRIBUTO PRIVATO
class Computer:
    def __init__(self, nome_proc):
        self.__processore = nome_proc       
        
    def get_processore(self):
        return self.__processore
    
    def set_processore(self, processore):
        self.__processore = processore
        
pc = Computer("Intel i5")

print(pc.get_processore())
pc.set_processore("AMD Ryzen 5")
print(pc.get_processore())

#ATTRIBUTO PROTETTO
#non è una regola reale ma è una convenzione
#si utilizza per avere il codice più pulito e sicuro

class Animale:
    def __init__(self, nome:str, eta:int):
        
        #così non è più modificabile dall'esterno
        self._nome = nome        
        self.eta = eta
    
    #funzione verso generico
    def fai_suono(self):
            print(f"{self._nome} fa un verso generico!")
            
    def get_nome(self):
        return self._nome
                 
class Leone(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        
    def fai_suono(self):
        print(f"{self._nome} ruggisce!")
    
    def caccia(self):
        print(f"Il leone {self._nome} sta cacciando una preda!")

class Cane(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        
    def fai_suono(self):
        print(f"{self._nome} abbaia!")    
            
    def mangia(self):
        print(f"Il cane {self._nome} sta rosicchiando un osso!")

class Pesce(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        
    def fai_suono(self):
        print(f"{self._nome} squittisce!")        
    
    def nuota(self):
        print(f"Il pesciolino {self._nome} sta nuotando nell'acquario!")
        
animale_gen = Animale("Pippo", 2)
leone1 = Leone("Simba", 5)
cane1 = Cane("Milu", 3)
pesce1 = Pesce("Dory", 3)

animale_gen.fai_suono()
leone1.caccia()
cane1.mangia()
pesce1.nuota()

print(animale_gen.get_nome())
print(leone1.get_nome())
print(cane1.get_nome())


#VARIABILI O METODI PRIVATI
class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"
    
    def __metodo_privato(self):
        return "Questo è un metodo privato."
    
obj = MiaClasse()

#dà errore
#print(obj.__variabile_privata)

#stampa, ma non è buona prassi
print(obj._MiaClasse__variabile_privata)

#VARIABILI O METODI PROTETTI
class ClasseBase:
    def __init__(self):
        self._variabile_protetta = "Sono protetta"
        
class SottoClasse(ClasseBase):
    def __init__(self):
        super().__init__()
        print(self._variabile_protetta)
        
obj2 = SottoClasse()

#accesso da fuori la classe, non consigliato ma possibile
print(obj2._variabile_protetta)