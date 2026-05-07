#@PROPERTY E @PROPERTY.SETTER
class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self._voto = voto 
        
    @property
    def voto(self):
        print("Voto getter")
        return self._voto
        
    @voto.setter
    def voto(self, nuovo_voto):
        if 0 <= nuovo_voto <= 30:
            self._voto = nuovo_voto
        else:
            print("Voto non valido")
            
#voto, nonostante sia una funzione, viene utilizzata come attributo 
#quindi come s.voto e non voto()            
            
s = Studente("Aurora", 28)
print(s.voto)

s.voto = 24
print(s.voto)