---
tags:
  - Combattimento
  - Tabelle
---

# Attacchi, modificatori e danno (Attacks, Modifiers, Damage)

## Tipi di Attack

| Tipo | Stat per colpire | Stat per il danno | Note |
|---|---|---|---|
| Melee Attack | STR | STR | Gli Attack da mischia usano per lo più STR sia per colpire sia per il danno. |
| Ranged Attack (fisico) | DEX | Alcuni applicano STR; altri non hanno bonus al danno | Subisce Disadvantage se effettuato entro la portata da mischia di un nemico. |
| Spell Attack | INT | INT (per lo più) | Gli Spell Attack a distanza subiscono Disadvantage se effettuati entro la portata da mischia di un nemico. |

## Area of Effect Attacks (Area Attack)

Attack come la Spell Fireball o la Skill Goblin Dynamite (uso di esplosivi) infliggono danno su un'area ampia. Le qualità di Area Attack sono elencate nella voce della Attack Skill.

### Risoluzione

1. L'attaccante effettua un singolo tiro di Attack contro un nemico a sua scelta entro la gittata, come di consueto.
2. Se l'Attack ha Success, l'attaccante tira il danno una sola volta e applica il danno completo a tutte le creature nell'area interessata (crawler e Mob, compreso il bersaglio dell'Attack). Resistance e DR riducono il danno come di consueto.
3. Se l'Attack fallisce, la maggior parte degli Attack ha avuto un malfunzionamento e nessuna creatura subisce danno, a meno di un Critical Fail che colpisce il bersaglio sbagliato.
4. Eccezione: gli Area Attack come Throwing e Fireball che fanno riferimento alla Figure 3 (p. 200 del manuale) hanno comunque effetto in caso di Fail: l'Attack atterra da qualche parte e infligge danno a ciò che si trova vicino al nuovo punto di impatto.

### Splash

Alcuni Area Attack hanno un'area Splash: un raggio dall'esplosione iniziale che infligge metà del danno alle creature al suo interno. Chi si trova nell'area Splash applica DR e altri effetti normalmente.

### Evade contro Area Attack

- Una creatura colpita da un Area Attack può effettuare Evade (se spende una Action) e può avere modificatori situazionali dovuti a copertura, elevazione e altro.
- Una vittima che effettua Evade con successo riduce il danno del 50%.
- Un Evade riuscito nell'area Splash riduce il danno di un ulteriore 50%, quindi viene applicato solo il 25% del danno.
- Il danno è arrotondato per difetto come di consueto.
- Compiere uno Step durante una Evade Check (o qualsiasi Interrupt) non è abbastanza rapido per sfuggire a un'esplosione: non si può uscire semplicemente dall'area interessata.

### Fuoco amico

Gli Area Attack colpiscono tutte le creature nell'area, anche gli alleati.

### Tipi di area (Area of Effect Types)

| Tipo | Descrizione |
|---|---|
| Blast | Si estende in tutte le direzioni dal bersaglio (o dal punto in cui è atterrato l'esplosivo) fino alla distanza indicata (vedi la nota sul Blast sotto). |
| Burst | Si estende in tutte le direzioni dal lanciatore fino alla distanza indicata. |
| Line | Si estende dal lanciatore, larga 5 feet, fino alla distanza indicata. |
| Cone | Si estende dal lanciatore in un arco di 60 gradi fino alla distanza indicata. |
| +Splash | Si estende oltre l'area a danno pieno e infligge metà del danno entro la distanza di Splash. Di solito si aggiunge ad altri tipi di area e si estende allo stesso modo. Alcuni Attack hanno solo un effetto Splash: il bersaglio subisce il danno pieno, tutti gli altri nell'area Splash subiscono metà del danno. |

!!! example "Esempio"
    Un "20ft Cone +10ft Splash" è lungo 30 feet. Le vittime nei primi 20 feet subiscono il danno pieno; quelle negli ultimi 10 feet (area Splash) subiscono metà del danno.

**Nota sul Blast**: su una mappa di battaglia, il bersaglio o il punto di impatto di un "10ft Blast radius" è l'origine dell'effetto. Da quello spazio di 5 ft × 5 ft il Blast si estende di due spazi in ogni direzione. Se non si tiene traccia della posizione esatta di crawler, Mob e altri NPC, il GM stabilisce in modo ragionevole chi è coinvolto in un Area Attack.

La Figure 2 del manuale illustra i tipi di area (Blast da bersaglio, Burst da lanciatore, Line, Cone e le relative aree Splash); non è riprodotta qui.

## Modificatori di Attack

Diverse situazioni possono alterare l'Evade score di un bersaglio o modificare altrimenti l'Attack.

### Cover

- Gli oggetti possono frapporsi agli Attack a distanza superiore alla mischia: tali Attack si effettuano con Disadvantage.
- Gli Attack in mischia non sono influenzati dalla cover.
- Esempi di cover: casse, terreno, automobili, muretti.
- Se l'Attack manca, la cover può essere distrutta, in base alla sua solidità e alla forza dell'attaccante.

### Modificatori ambientali

- Attaccare bersagli in Cover, Darkness, Severe Weather, Shifting Ground o altre condizioni penalizzanti comporta Disadvantage.
- Chi beneficia dell'aiuto dell'ambiente (ad esempio attaccando da una posizione elevata) tira con Advantage.

### Size

- Un crawler tira le Attack Skill Check con Advantage se il bersaglio è di 4 o più classi di Size più grande.
- Un crawler tira le Attack Skill Check con Disadvantage se attacca un bersaglio di 4 o più classi di Size più piccolo.
- Quando una creatura più grande colpisce una più piccola con un Melee Attack effettuato con Disadvantage a causa di questo modificatore, aggiunge il proprio valore di Size al danno.

#### Tabella 9: Size delle creature

| Size | Nome | Esempi di creature |
|---|---|---|
| 1 | Tiny | Scatterer, Rat |
| 2 | Small | Cat, Raccoon |
| 3 | Petite | Goblin, Boar |
| 4 | Medium | Human, Wolf |
| 5 | Large | Horse, Mantaur |
| 6 | Huge | Elephant, Rhino |
| 7 | Colossal | Dinosaur, Dragon |
| 8 | Gargantuan | Kaiju |

### Unseen Attackers

- Le creature ottengono Advantage sulle Attack Skill Check contro bersagli che non possono vederle (ad esempio un crawler nascosto, invisibile o dall'altra parte di una nube di fumo).
- Le creature subiscono Disadvantage sulle Attack Skill Check contro bersagli che non possono vedere.

## Danno (Damage)

Quando un crawler colpisce con un Attack infligge danno.

- Il danno parte dal dado di danno base determinato dalla Skill, più lo Stat Mod appropriato. Ranks più alti conferiscono dadi di danno base aggiuntivi (vedi le voci delle Attack Skill nella sezione *Skill*). Alcuni Attack aggiungono effetti speciali oltre a questi dadi.
- **Unarmed Attack**: infliggono basso danno intrinseco ma permettono al combattente di aggiungere 1 Damage Effect all'Attack (ad esempio Powerful Strike, Iron Punch e altri). Se l'Attack colpisce, si tirano i dadi di danno dell'Attack e poi si applica il Damage Effect scelto.
- Dopo aver calcolato il danno totale, il GM applica l'eventuale DR e poi segna la Health Bar del Mob.
- Per le Critical Hit (Natural 20) e l'Amazing Success vedi *Combattimento: principi generali*.

!!! example "Esempio: Critical Hit"
    Una Warhammer Skill Rank 10 infligge 1d10+STR, più 2d10 per l'Upgrade al Rank 10. Con un Natural 20 i dadi raddoppiano a 6d10+STR (lo Stat Mod si aggiunge una sola volta).

*Fonte: manuale, p. 83–85.*
