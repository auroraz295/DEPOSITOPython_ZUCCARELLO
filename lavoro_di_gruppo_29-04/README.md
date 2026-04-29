## Sistema Gestione Officina Elettrodomestici

Questo progetto implementa un sistema di gestione per un'officina di riparazioni, sviluppato in Python utilizzando il paradigma della Programmazione a Oggetti (OOP). Il software permette di gestire il ciclo di vita delle riparazioni, dalla creazione dei ticket al calcolo dei preventivi personalizzati.

###  🚀 Funzionalità Principali

<h4>Gestione Multicategoria:</h4> Supporto specifico per Lavatrici, Frigoriferi e Forni con attributi tecnici dedicati.

<h4>Calcolo Preventivi Dinamico:</h4> Ogni categoria di elettrodomestico ha una propria logica di calcolo dei costi basata su specifiche tecniche (es. capacità di carico, presenza freezer, tipo di alimentazione).

<h4>Sistema di Ticketing:</h4> Gestione completa dello stato delle riparazioni (Aperto, In Lavorazione, Chiuso) e tracciamento delle note tecniche.

<h4> Reportistica Officina:</h4> Generazione automatica di statistiche sui tipi di apparecchi in riparazione e calcolo del fatturato totale dei preventivi.

###  🛠️ Concetti OOP Applicati

<h4>Incapsulamento:</h4> Tutti gli attributi critici sono privati (__nome) e accessibili solo tramite metodi Getter e Setter per garantire la protezione dei dati.

<h4>Ereditarietà:</h4> Utilizzo di una classe base Elettrodomestico da cui derivano le classi specializzate.

<h4>Polimorfismo:</h4> Override del metodo stima_costo_base() nelle classi derivate per adattare il comportamento del calcolo costi a ogni specifico modello.

<h4>Introspezione:</h4> Uso dei metodi type() e __class__.__name__ per identificare dinamicamente le tipologie di oggetti gestiti dal sistema.

###  💻 Come testarlo

Il file contiene già una sezione di simulazione finale che:

Crea un parco macchine di test.

Apre i ticket di riparazione.

Simula il cambio di stato e la chiusura dei lavori.

Stampa il riepilogo finanziario e statistico dell'officina.

### Autori

Sviluppato da: <a href ="https://github.com/auroraz295"> Aurora Zuccarello</a> & <a href="https://github.com/sasabru/DepositoPython_Bruno"> Salvatore Bruno</a>

