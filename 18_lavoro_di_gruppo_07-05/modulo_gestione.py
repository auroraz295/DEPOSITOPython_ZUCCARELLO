from modulo_capoprincipale import Giacca, Pantalone, Gilet 
from modulo_finitura import Cravatta, Papillon, Pochette

#GESTIONE SARTORIA
class GestioneSartoria: 
    def __init__(self):
        
        #lista catalogo capi
        self._catalogo_capi = []
        self._catalogo_rifiniture = []
        
        
    #GET LISTE
    def get_lista_capi(self):
        return self._catalogo_capi
    
    def get_lista_rifiniture(self):
        return self._catalogo_rifiniture

    #FUNZIONE CREA CAPO
    def crea_capo(self):
        scelta_capo = int(input("Cosa vuoi creare? 1. Giacca - 2. Pantalone - 3. Gilet - 4. Cravatta - 5. Papillon - 6. Pochette // "))
        codice = int(input("Inserisci codice: "))
        nome = codice
        tessuto = input("Inserisci tessuto/materiale: ")
        colore = input("Inserisci colore: ")
        prezzo = float(input("Inserisci prezzo: "))
        
        #GIACCA
        if scelta_capo == 1: 
            taglia = input("Inserisci taglia: ")
            n_bottoni = int(input("Numero bottoni giacca: "))
            self._catalogo_capi.append(Giacca(codice, nome, tessuto, colore, taglia, prezzo, n_bottoni))
        
        #PANTALONE    
        elif scelta_capo == 2:
            taglia = input("Inserisci taglia: ")
            tipo_taglio = int(input("Tipo taglio: 1. Skinny - 2. Wide - 3. Slim // "))
            
            if tipo_taglio == 1:
                tipo_taglio = "Skinny"
                self._catalogo_capi.append(Pantalone(codice, nome, tessuto, colore, taglia, prezzo, tipo_taglio))
                
            elif tipo_taglio == 2:
                tipo_taglio = "Wide"
                self._catalogo_capi.append(Pantalone(codice, nome, tessuto, colore, taglia, prezzo, tipo_taglio))
                
            elif tipo_taglio == 3:
                tipo_taglio = "Slim"
                self._catalogo_capi.append(Pantalone(codice, nome, tessuto, colore, taglia, prezzo, tipo_taglio))
            else:
                print("Tipo di taglio non disponibile.")  
        
        #GILET
        elif scelta_capo == 3:
            taglia = input("Inserisci taglia: ")
            reversibile = input("Reversibile: SI / NO - ")
            
            if reversibile == "SI":
                reversibile = True
                self._catalogo_capi.append(Gilet(codice, nome, tessuto, colore, taglia, prezzo, reversibile))
            else:
                reversibile = False
                self._catalogo_capi.append(Gilet(codice, nome, tessuto, colore, taglia, prezzo, reversibile))
        
        #CRAVATTA
        elif scelta_capo == 4:
            larghezza = int(input("Larghezza cravatta: "))
            self._catalogo_rifiniture.append(Cravatta(codice, nome, tessuto, colore, prezzo, larghezza))


        #PAPILLON
        elif scelta_capo == 5:
            tipo_chiusura = int(input("Tipo chiusura: 1. A clip - 2. A nodo // "))
            
            if tipo_chiusura == 1:
                tipo_chiusura = "a clip"
                self._catalogo_rifiniture.append(Papillon(codice, nome, tessuto, colore, prezzo, tipo_chiusura))
            
            if tipo_chiusura == 2:
                tipo_chiusura = "a nodo"
                self._catalogo_rifiniture.append(Papillon(codice, nome, tessuto, colore, prezzo, tipo_chiusura))
        
        
        #POCHETTE
        elif scelta_capo == 6:
            piega_decorativa = input("piega_decorativa: SI / NO - ")
            
            if piega_decorativa == "SI":
                piega_decorativa = True
                self._catalogo_rifiniture.append(Pochette(codice, nome, tessuto, colore, prezzo, piega_decorativa))
            else:
                piega_decorativa = False
                self._catalogo_rifiniture.append(Pochette(codice, nome, tessuto, colore, prezzo, piega_decorativa))


    #FUNZIONE MODIFICA CAPO
    def modifica_capo(self):
        codice_da_cercare = int(input("Inserisci il codice dell'articolo da modificare: "))
        catalogo_completo = self._catalogo_capi + self._catalogo_rifiniture
        
        for elemento in catalogo_completo:
            if elemento.get_codice() == codice_da_cercare:
                scelta_modifica = int(input("Cosa vuoi modificare? 1. Nome - 2. Tessuto - 3. Taglia - 4. Colore - 5. Prezzo - 6. Altre caratteristiche // "))
                
                #set nome
                if scelta_modifica == 1:
                    nuovo_nome = input("Inserisci il nuovo nome: ")
                    elemento.set_nome(nuovo_nome)
                
                #set tessuto
                elif scelta_modifica == 2:
                    nuovo_tessuto = input("Inserisci il nuovo tessuto: ")
                    elemento.set_tessuto(nuovo_tessuto)
                
                #set taglia
                elif scelta_modifica == 3:
                    nuova_taglia = input("Inserisci la nuova taglia: ")
                    elemento.set_taglia(nuova_taglia)
                
                #set colore
                elif scelta_modifica == 4:
                    nuovo_colore = input("Inserisci il nuovo colore: ")
                    elemento.set_colore(nuovo_colore)
                
                #set prezzo
                elif scelta_modifica == 5:
                    nuovo_prezzo = float(input("Inserisci il nuovo prezzo: "))
                    elemento.set_prezzo(nuovo_prezzo)
                
                #set caratteristiche speciali    
                elif scelta_modifica == 6: 
                    scelta_caratteristiche = int(input("Quale caratteristica vuoi modificare? 1. Giacca: Numero bottoni - 2. Pantaloni: Tipo taglio - 3. Gilet: Reversibilità - 4. Cravatta: Larghezza - 5. Papillon: Chiusura - 6. Pochette: Piega decorativa // "))
                   
                    #set bottoni giacca
                    if scelta_caratteristiche == 1:
                        nuovi_bottoni = input("Inserisci il nuovo numero bottoni: ")
                        elemento.set_numerobottoni(nuovi_bottoni)
                    
                    #set tipo taglio pantaloni
                    if scelta_caratteristiche == 2:
                        nuovo_tipo = input("Inserisci il nuovo tipo: ")
                        elemento.set_tipo_taglio(nuovo_tipo)
                    
                    #set reversibilità gilet
                    if scelta_caratteristiche == 3:
                        nuovo_reversibile = input("Inserisci la reversabilità: SI/NO - ")
                        
                        if nuovo_reversibile == "SI":
                            nuovo_reversibile = True
                            elemento.set_reversibile(nuovo_reversibile)
                            
                        elif nuovo_reversibile == "NO":
                            nuovo_reversibile = False
                            elemento.set_reversibile(nuovo_reversibile)
                            
                        else:
                            print("Modifica non eseguibile.")
                    
                    #set larghezza cravatta        
                    if scelta_caratteristiche == 4:
                        nuova_larghezza = int(input("Inserisci la nuova larghezza: "))
                        elemento.set_larghezza(nuova_larghezza)
                    
                    #set chiusura papillon
                    if scelta_caratteristiche == 5:
                        nuova_chiusura = int(input("Inserisci la nuova chiusura: 1. A clip - 2. A nodo // "))
                        
                        if nuova_chiusura == 1:
                            nuova_chiusura = "a clip"
                            elemento.set_tipo_chiusura(nuova_chiusura)

                        elif nuova_chiusura == 2:
                            nuova_chiusura = "a nodo"
                            elemento.set_tipo_chiusura(nuova_chiusura)
                            
                        else:
                            print("Modifica non eseguibile.")
                    
                    #set piega decorativa pochette
                    if scelta_caratteristiche == 6:
                        nuova_piega_decorativa = input("Inserisci la piega decorativa: SI/NO - ")
                        
                        if nuova_piega_decorativa == "SI":
                            nuova_piega_decorativa = True
                            elemento.set_piega_decorativa(nuova_piega_decorativa)
                            
                        elif nuova_piega_decorativa == "NO":
                            nuova_piega_decorativa = False
                            elemento.set_piega_decorativa(nuova_piega_decorativa)
                            
                        else:
                            print("Modifica non eseguibile.")
                    
                else:
                    print("Modifica non eseguibile.")

    #FUNZIONE ELIMINA CAPO 
    def elimina_capo(self):
        articolo_da_cercare = int(input("Cosa vuoi eliminare? 1. Capo principale - 2. Componente di rifinitura // "))
        
        #elimina capo principale
        if articolo_da_cercare == 1:
            codice_da_cercare = int(input("Inserisci il codice dell'articolo da modificare: "))
    
            for elemento in self._catalogo_capi:
                if elemento.get_codice() == codice_da_cercare:
                    self._catalogo_capi.remove(elemento)
                    print("Articolo eliminato.")
                else:
                    print("Articolo non trovato.")
        
        
        #elimina componente rifinitura            
        elif articolo_da_cercare == 2:
            codice_da_cercare = int(input("Inserisci il codice dell'articolo da modificare: "))
    
            for elemento in self._catalogo_rifiniture:
                if elemento.get_codice() == codice_da_cercare:
                    self._catalogo_capi.remove(elemento)
                    print(f"Articolo eliminato.")
                else:
                    print("Articolo non trovato.")
                    
            
    #FUNZIONI DI ANALISI
    #print di tutti i capi
    def analisi_tutti(self):
        for c in self._catalogo_capi:
            print(f"Codice: {c.get_codice()} - Capo: {c.get_nome()} - Colore: {c.get_colore()} - Costo Totale: {c.costo()}€")
        for r in self._catalogo_rifiniture:
            print(f"Codice: {c.get_codice()} - Rifinitura: {r.get_nome()} - Colore: {r.get_colore()} - Costo Totale: {r.costo()}€")

    #print numero capi e rifiniture in totale
    def analisi_tipo(self):
        print(f"Totale Capi Principali: {len(self._catalogo_capi)}")
        print(f"Totale Rifiniture: {len(self._catalogo_rifiniture)}")
     
    #print capi e rifiniture specifici
    def analisi_dettagli(self):
        
        #inizializzatori capi
        giacche = 0
        pantaloni = 0
        gilet = 0
        
        #inizializzatori rifiniture
        cravatte = 0
        papillon = 0
        pochette = 0
        
        for c in self._catalogo_capi:
            if isinstance(c, Giacca):
                giacche += 1
            elif isinstance(c, Pantalone):
                pantaloni += 1
            elif isinstance(c, Gilet):
                gilet += 1
        
        for r in self._catalogo_rifiniture:
            if isinstance(r, Cravatta):
                cravatte += 1
            elif isinstance(r, Papillon):
                papillon += 1
            elif isinstance(r, Pochette):
                pochette += 1
        
        #print analisi
        print(f"Giacche: {giacche} - Pantaloni: {pantaloni} - Gilet: {gilet} - Cravatte: {cravatte} - Papillon: {papillon} - Pochette: {pochette}")

