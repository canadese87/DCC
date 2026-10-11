---
tags:
  - Dungeon
  - Da verificare
  - Tabelle
---

# Interfaccia del Crawler (The Crawler Interface)

## Ingresso nel World Dungeon

- Il World Dungeon è strutturato su 18 Level (Floor).
- Il primo Floor si apre circa 18 secondi dopo la fine dell'annuncio iniziale. Quando gli ingressi si chiudono, non è più possibile entrare.
- Una volta entrato, il crawler non può uscire finché non ha completato tutti i 18 Floor oppure non soddisfa altri requisiti specifici.
- Per accedere al Floor successivo il crawler deve trovare una stairwell. Se non la trova prima del collasso del Floor, viene eliminato insieme al Floor stesso (vedi *Countdown Timer* più sotto e le sezioni sui singoli Floor).
- Le Tutorial Guild sono distribuite nei Floor da uno a tre secondo l'annuncio iniziale.

!!! warning "Da verificare"
    L'annuncio iniziale (p. 15) indica le Tutorial Guild sui Floor da uno a tre. La sezione sui Tutorial Levels (p. 24) afferma che dal Third Floor non esistono più Tutorial Guild. Le due indicazioni sono in contrasto.

Un crawler conserva tutti i sensi normali all'ingresso (possono cambiare durante la Race Selection al Third Floor) e ottiene nuove funzioni percettive tramite l'enhancement zone, la più importante delle quali è l'Heads-Up Display (HUD). Tutti gli organismi provenienti da mondi con Primal Engine possiedono l'hardware necessario.

*Fonte: manuale, p. 15–16.*

## Heads-Up Display (HUD)

L'HUD appare nel campo visivo del crawler. Include sempre:

- **Mana Bar**: mostra il Mana corrente (riserve magiche).
- **Health Bar**: mostra il livello di danno subito (quanto il crawler è vicino alla morte).
- Finestre e schermate per Stat, Inventory, tooltip e messaggi di sistema.

I messaggi di sistema compaiono automaticamente in occasione di annunci, notifiche e achievement. Per impostazione predefinita compaiono al centro del campo visivo finché non vengono minimizzati.

Il crawler può modificare le impostazioni dell'HUD: ingrandire o ridurre le finestre, aggiungere o rimuovere elementi (ad esempio il View Counter) e personalizzarne la disposizione.

L'HUD si controlla con mente e attenzione. È disponibile un'opzione di tastiera virtuale per scrivere mentalmente i messaggi.

### Tabella 1: HUD

| Elemento HUD | Indicazione | Note |
|---|---|---|
| Health Bar | Livello di danno del crawler | Diminuisce da destra a sinistra. Verde dal 100% al 66%; giallo dal 66% al 33%; rosso dal 33% allo 0%. |
| Overhead Map | Mappa di un Neighborhood, Borough, ecc. | Spesso ottenibile come loot dai Boss. Alcune Skill danno maggiore accesso alle mappe. |
| Punto verde | Il crawler stesso | |
| Punto blu | Altri crawler (controllati da giocatori o dal GM) | |
| Punto rosso | NPC ostili, come Mob e Boss | |
| Punto bianco | NPC non ostili | |
| Punto viola | Non-crawler o non residenti del dungeon (come Hunter o altri turisti) | |
| Punto arancione | Pet e Familiar | |
| Punto bianco con X verde | Minion (o Mercenary) | |
| X nera | Cadaveri | Un cadavere diventa una X nera. Passandoci sopra con l'attenzione, se si è abbastanza vicini, viene indicato di chi si tratta; altrimenti l'identità resta ignota. |
| Croce al posto del punto | Elite | |
| Stella al posto del punto | NPC importanti | |
| Stella animata (rotante, pulsante) al posto del punto | Divinità (God) | |
| Quadrato bianco al posto del punto | Stairs | |
| Teschio sopra la testa del crawler | Il crawler ha ucciso un crawler | Un teschio per ogni crawler ucciso. |
| Teschio dorato sopra la testa del crawler | Il crawler ha ucciso un crawler della leaderboard | Un teschio dorato per ogni crawler della leaderboard ucciso. |
| Stella sopra la testa del crawler | Il crawler ha ucciso un Boss | |

!!! warning "Da verificare"
    La tabella originale (p. 17) è stata ricostruita da un layout a colonne interlacciate. L'associazione tra simboli (Croce, Stella, Stella animata, Quadrato bianco) e indicazioni (Elite, NPC importanti, God, Stairs) segue l'ordine di lettura. Gli Elite sono descritti a p. 32 come marcati con una croce nera.

### Minimap

- La minimap occupa la maggior parte dello spazio dell'HUD.
- All'inizio della maggior parte dei Floor la mappa è vuota e si riempie con l'esplorazione.
- Mob e punti di riferimento importanti appaiono in colori e forme diversi (vedi Tabella 1).
- La minimap non è un radar. Mob invisibili, nascosti o stealth possono non comparire finché il crawler non è loro addosso.
- Il crawler può ingrandire o ridurre la minimap mentalmente.
- La minimap standard mostra un quarto di miglio quadrato attorno al crawler.
- Se il crawler ha già ottenuto informazioni su un Mob oppure possiede un potenziamento di mappa specifico del Floor (ad esempio Neighborhood Map o Field Guide), possono essere già visibili sezioni più ampie della mappa, oppure i nomi di Mob e crawler compaiono sopra i simboli corrispondenti.
- **Expanding The Map**: la fog of war che oscura parte di un Floor si rimuove sconfiggendo un Boss e raccogliendo la mappa dal suo cadavere. La mappa è un drop persistente: ogni crawler che partecipa ottiene una mappa.

### Health Menu

- Mostra la Health complessiva come percentuale fino al 100%.
- Mostra i Buff e i Debuff attivi.
- Un danno sufficientemente grave comporta uno stato di injured.
- Mostra il Mana, necessario per lanciare Spell.

### Messaging System

- L'HUD funge da hub di comunicazione non verbale.
- Il crawler può inviare messaggi ai membri del proprio party in qualsiasi momento con il pensiero; i messaggi compaiono sull'HUD del destinatario.
- Per inviare messaggi ad altri crawler è necessario collegarsi con essi con un fist bump.
- Il destinatario può non vedere il messaggio finché non è in condizione di farlo (ad esempio durante un combattimento o mentre dorme).
- Se il messaggio proviene da un crawler morto, il sistema lo segnala.
- Se il crawler destinatario si trova in un luogo anomalo, il sistema mostra il messaggio "crawler unavailable".

### Dati su crawler e creature

- Osservando un altro crawler o una creatura, l'HUD mostra informazioni come il Level.
- Dal Third Floor sono visibili anche Race e Class di un crawler.
- Accanto al nome del crawler compaiono stelle, una per ogni Boss ucciso.
- Accanto al nome compaiono teschi, uno per ogni crawler ucciso. Il teschio diventa dorato se la vittima era un crawler tra i primi dieci della classifica.
- Esaminando una creatura si ottengono nome e Level, oltre a un breve commento descrittivo.

### Translation System

L'HUD converte automaticamente tutte le lingue in Syndicate Standard.

### Countdown Timer

- Ogni Floor è disponibile per un tempo limitato, al termine del quale collassa (tutti i crawler ancora presenti muoiono).
- L'HUD mostra sempre il timer del conto alla rovescia fino al collasso del Floor.
- Per evitare il collasso il crawler deve raggiungere una stairwell verso il Floor successivo.

### Combat Systems

- L'HUD mostra il danno inflitto ai nemici.
- Mostra i Buff, i bonus e i Debuff applicati al bersaglio.

### Scratch Pad

L'interfaccia include un blocco note in cui il crawler può scrivere appunti.

*Fonte: manuale, p. 16–19.*

## Quest

L'HUD tiene traccia delle Quest, gli obiettivi da completare nel dungeon. Ogni Quest assegna esperienza, ricompense e loot.

- Le Quest "ufficiali" non sono disponibili prima del Third Floor.
- **Individual Quest**: progettate per crawler che giocano da soli. Sono completabili senza assistenza esterna, ma abbastanza impegnative da poter causare la morte in caso di fallimento.
- **Group Quest**: Quest per l'intero party. Hanno scala e difficoltà maggiori rispetto alle Individual Quest, con ricompense proporzionalmente maggiori.
- Le ricompense delle Quest sono in genere Quest Box (vedi *Achievement e Loot Box*).

*Fonte: manuale, p. 20–21.*
