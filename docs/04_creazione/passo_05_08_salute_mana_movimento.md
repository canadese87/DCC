---
tags:
  - Creazione personaggio
  - Tabelle
---

# Passi 5–8: Health, Mana, Hotlist, Move, AI Favor, Size

## Passo 5: Health Bar

- Il totale di ==Health== è pari al **CON Mod × 10**.
- Il danno subito non viene sottratto direttamente dal punteggio di Health: si perde Health solo quando il danno supera determinate soglie (vedi sezione *Combattimento*, manuale p. 93).
- La ==Health Bar== ha 10 slot, ciascuno pari al 10% della Health totale.
- Scrivere il CON Mod in ogni slot della Health Bar.

*Fonte: manuale, p. 111.*

## Passo 6: Mana e Spell iniziali

### Mana

- Il ==Mana== è la risorsa spesa per lanciare Spell.
- All'ingresso nel World Dungeon il crawler ottiene Mana Points pari al valore **Enhanced** della Stat Intelligence (il valore effettivo, non lo Stat Mod).
- Scrivere il valore Enhanced di Intelligence nel riquadro "Max Mana", a destra dei punteggi di Intelligence. Aggiornare "Max Mana" ogni volta che il punteggio cambia.
- Ogni lancio di una Spell costa il Mana indicato nella descrizione della Spell. Annotare il costo nella Hotlist o negli effetti di attacco.
- Dopo la spesa, registrare il nuovo totale nel campo "Current", a destra di "Max Mana". Non cancellare mai "Max Mana": non cambia con il lancio di Spell.
- Il Mana attuale non può essere ripristinato oltre il valore di Max Mana.
- Lanciare una Spell richiede la spesa di una Action.

### Spell Heal

Tutti i crawler iniziano con la Spell **Heal** (manuale p. 206).

**Heal (Interrupt)**

| Voce | Valore |
|---|---|
| Rank | 1 (massimo) |
| Costo in Mana | 2 |
| Effetto | Cura 2 slot della Health Bar (20% della Health) |
| Bersaglio | Solo il lanciatore |
| Tipo | Interrupt |

- Heal è un Interrupt: può essere lanciata in qualsiasi momento, non solo nel proprio turno di combattimento.
- Si può scrivere Heal e la sua descrizione in uno dei riquadri della sezione "Hotlist" della scheda. Si può rimuoverla in seguito per fare spazio a Spell migliori.
- Per salute e recupero della Health vedi manuale p. 93.

### Hotlist

Ogni crawler ha una ==Hotlist== di **10 slot**. In essa si possono collocare Spell, pozioni, scroll, armi secondarie e oggetti vari per accedervi rapidamente.

- Fuori dal combattimento, oppure spendendo una Action in combattimento, qualsiasi oggetto della Hotlist appare istantaneamente in una mano libera, pronto all'uso nello stesso momento o nella stessa Action. In alternativa può apparire a terra davanti al crawler.
- Per cambiare arma: l'arma impugnata passa temporaneamente nella Hotlist mentre la nuova arma esce, e si tira l'attacco con la nuova arma. Il cambio e l'attacco costano una sola Action.
- Se l'arma deve essere prelevata dall'Inventory anziché dalla Hotlist, servono due Action: un'azione di Inventory per spostare l'arma dall'Inventory alla Hotlist, poi la Action per cambiare arma e attaccare.
- Gli oggetti nella Hotlist non conferiscono benefici aggiuntivi: sono solo facilmente accessibili. Quando un oggetto torna in uno slot della Hotlist, i suoi benefici si disattivano.
- Dopo un cambio, verificare se Stat Mod o Skill risultano modificati. Non occorre cancellare dalla scheda l'equipaggiamento standard, a meno che il cambio duri più di un singolo combattimento.
- In un singolo slot della Hotlist si possono collocare fino a **999 esemplari** dello stesso oggetto per nome.

*Fonte: manuale, p. 111–112.*

## Passo 7: Move e Step

- Il crawler si muove di **20 piedi** con una Move action in combattimento (vedi sezione *Movimento*, manuale p. 69). Questo valore può cambiare con la scelta di una diversa Race alla Third Floor, oppure per oggetti, maledizioni o decisione del System AI.
- Scrivere "20" nel riquadro "Move" della scheda, sulla stessa riga di "Evade" sotto la Health Bar.
- Il crawler ha anche uno **Step di 10 piedi**. Ogni volta che spende una Action in combattimento, può eseguire uno Step e muoversi di 10 piedi.
- Di conseguenza una Move action consente di muoversi di 30 piedi in totale (20 di Move più 10 di Step). Si può inoltre attaccare e muoversi di 10 piedi al costo di una singola Action.
- Scrivere "10" nel riquadro "Step", a destra di "Move".

*Fonte: manuale, p. 112.*

## Passo 8: AI Favor e Size

### AI Favor

L'==AI Favor== è una risorsa del crawler.

- Un crawler Human scrive "1" nel riquadro "AI Favor" della scheda (sotto i riquadri "Move" e "Step").
- Un crawler animale ha speso il proprio AI Favor iniziale: non ottiene AI Favor iniziale.

**Uso**: si può spendere 1 punto di AI Favor per:

- una volta per Check, ritirare un d20 prima che il GM annunci il risultato. Non si può spendere AI Favor per ritirare un Natural 1 (Critical Fail automatico);
- una volta per round, ottenere una Action extra non di Attack in combattimento.

**Ottenere AI Favor**: si ottiene AI Favor aggiuntivo compiendo gesti eroici, sopravvivendo ad atti avventati, ostacolando gli showrunner o soddisfacendo le preferenze del System AI. I requisiti specifici sono stabiliti dal GM.

### Size

- Scrivere la Size nel riquadro a destra di "AI Favor".
- Gli Human sono tipicamente "Medium (4)".
- Gli animali possono avere Size da 2 a 4 (Tabella 21).
- La Size influenza gli attacchi contro nemici molto più grandi o più piccoli (vedi sezione *Size*, manuale p. 85).

**Tabella 21: Animal Crawler Size**

| Size | Nome | Esempio di creatura |
|---|---|---|
| 1 | Tiny | Scatterer, Rat |
| 2 | Small | Cat, Raccoon |
| 3 | Petite | Dog, Boar |
| 4 | Medium | Chimpanzee, Wolf |
| 5 | Large | Horse, Mantaur |

!!! note "Nota"
    Il testo indica per gli animali un intervallo di Size da 2 a 4, mentre la Tabella 21 elenca anche le Size 1 e 5.

### Popularity

Il crawler iniziale non ha Popularity. La scheda (pagina 2) ha un riquadro per essa: lasciarlo vuoto. Un crawler di Third Floor o successiva ottiene Popularity (vedi sezione *Popularity*, manuale p. 279 e sezione *Creazione di un crawler di Third Floor e oltre*).

*Fonte: manuale, p. 112.*
