#METODO SPECIALE __STR__ E __REPR__
class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        
    def __str__(self):
        return f"{self.titolo} scritto da {self.autore}"
    
    def __repr__(self):
        return f"Libro(titolo[self]: {self.titolo} - Autore(titolo[self]): {self.autore})"
    
l1 = Libro("Il Signore degli Anelli", "Tolkien")

print(l1)

#METODO __LEN__
class Squadra:
    def __init__(self, giocatori):
        self.giocatori = giocatori
    
    def __len__(self):
        return len(self.giocatori)
    
team = Squadra(["Marco", "Anna", "Luca"])

print(len(team))

#METODO __EQ__
class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
    
    def __eq__(self, altro:object):
        return self.nome == altro.nome and self.prezzo == altro.prezzo
    
p1 = Prodotto("Penna", 2)
p2 = Prodotto("Penna", 2)

print(p1 == p2)

#METODO __GETATTRIBUTE__
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def __getattribute__(self, attributo):
        print(f"Sto accedendo all'attributo: {attributo}")
        return super().__getattribute__(attributo)
    
p = Persona("Aurora", 25)
print(p.nome)
print(p.eta)