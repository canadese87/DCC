# Attack Skill: regole e riepilogo

Le Attack Skill rappresentano la capacità di danneggiare, disabilitare o fermare un bersaglio, con armi, pugni o altri mezzi offensivi. Ogni arma è una Skill distinta: il nome dell'arma è anche il nome della Skill usata per impugnarla. Il Rank non si condivide tra armi dello stesso tipo.

Tutte le Attack Skill Check sono effettuate contro il valore di **Evade** del bersaglio, che stabilisce la Difficulty dell'attacco.

## Formato di una voce Attack Skill

| Campo | Contenuto |
|---|---|
| **Name** | Nome dell'Attack, riportato come intestazione. |
| **Attack Type** | Melee o Ranged. La maggior parte degli Attack è Melee, con gittata 5 ft (adiacente). La Stat Mod predefinita per il tiro per colpire è STR per i Melee e DEX per le armi Ranged. Se si usa un'altra Stat Mod per colpire, è indicata in questa riga. |
| **Range** | Distanza massima a cui l'Attack può colpire, se superiore a 5 ft. Se non è indicato alcun Range, la gittata è Melee (adiacente o entro 5 ft). |
| **AI Favor** | Le armi a basso danno concedono AI Favor al crawler che usa tale Attack per la maggioranza dei propri attacchi durante un combattimento di almeno tre round. |
| **Limitations** | Condizioni, requisiti o penalità. "Requires two hands to wield" significa che servono entrambe le mani per impugnare l'arma; non si possono tenere altri oggetti durante l'attacco. |
| **Cooldown** | Se l'arma o l'effetto ha un Cooldown, è indicato qui. Che l'attacco colpisca o manchi, il timer parte. Durante il Cooldown l'arma o l'effetto non può essere usato. |
| **Description** | Note o descrizione della Skill. Si effettua una Attack Skill Check contro il valore di Evade del bersaglio. |
| **Base Damage** | Dadi di danno inflitti con 0–4 Rank nella Skill (0 Rank = uso untrained). Al danno si aggiunge il valore della Stat Mod appropriata. Tale Mod non coincide sempre con quella della riga Attack Type e non tutte le armi aggiungono una Stat Mod. Per ultimo è indicato il tipo di danno, rilevante se il bersaglio ha Resistance, Immunity o Vulnerability a quel tipo. |
| **Effects** | Eventuali effetti diversi dal danno. |
| **Upgrades** | Bonus che si attivano ai Rank 5, 10 e 15. |

**Evade del bersaglio** = 10 + DEX + numero della Floor.

### Compilazione della scheda del personaggio

1. Scrivere le Attack Skill nella sezione "Attacks" sul fronte della scheda.
2. Compilare la casella "To Hit" con i valori "Rank + Stat Mod".
3. Compilare la casella "Damage" scrivendo i dadi come "1dX", sostituendo X con il tipo di dado indicato. La voce Base Damage indica anche la Stat Mod (se presente) da aggiungere al danno.
4. Usare l'area Effects per annotare promemoria brevi degli effetti base, degli effetti degli Upgrade e dell'AI Favor (se presente).
5. Scrivere il nome della Attack Skill nella lista "Skills", dove si possono aggiungere note e segnare la casella di avanzamento all'estrema destra quando si usa la Skill. Questo permette di tirare per la Skill Advancement (vedi la sezione *Skill Advancement*) con tutte le Skill in un unico posto.
6. Quando una Attack Skill avanza di Rank, aggiornare il Rank anche nella sezione "Attacks".

*Fonte: manuale, p. 175–176, 177.*

## Rank Damage Dice

Un bonus ai danni frequente è l'aggiunta di un **Rank damage die** al tiro di danno. Il dado dipende dal Rank corrente nella Attack Skill; talvolta altre Skill lo usano, non sempre per il danno.

- Il Rank damage die **non fa parte del danno base** dell'Attack, quindi **non viene raddoppiato** su un Critical Hit.
- Si tira il dado più vicino al proprio Rank senza superarlo. Al Rank 1 il bonus è semplicemente +1 al danno.

!!! example "Esempio"
    Con 7 Rank, il Rank damage die è 1d6, perché è il dado più vicino a 7 senza superarlo.

**Tabella 37: Rank Damage Dice Scaling**

| Skill Rank | Damage Dice |
|:--:|---|
| 1 | +1 |
| 2–3 | +1d2 |
| 4–5 | +1d4 |
| 6–7 | +1d6 |
| 8–9 | +1d8 |
| 10–11 | +1d10 |
| 12–13 | +1d12 |
| 14–15 | +1d8 e +1d6 |
| 16–17 | +2d8 |
| 18–19 | +1d10 e +1d8 |
| 20 | +2d10 |

*Fonte: manuale, p. 176.*

## Riepilogo delle Attack Skill

La colonna "Stat" indica la Stat Mod usata per colpire. "Danno" indica i dadi del Base Damage con la Stat Mod aggiunta e il tipo di danno. Le Limitations e i Cooldown sono riassunti: i dettagli completi sono nelle schede delle singole Skill.

### Animal Crawler & Pet Strike Skills

| Skill | Tipo | Stat | Range | Danno | AI Favor | Limitations / Cooldown |
|---|---|:--:|---|---|:--:|---|
| Back Claw | Melee | STR | Melee | 1d6 + STR Slashing | — | — |
| Bite | Melee | STR | Melee | 1d8 + STR Piercing | — | Il bersaglio deve avere un'appendice |
| Slice Attack | Melee | DEX | Melee | 1d4 + STR Slashing | 1 | — |

### Bashing Weapon Skills

| Skill | Tipo | Stat | Range | Danno | AI Favor | Limitations / Cooldown |
|---|---|:--:|---|---|:--:|---|
| Club | Melee | STR | Melee | 1d6 + STR Bludgeoning | — | — |
| Improvised Weapons | Melee | STR | Melee | 1d4 + STR Bludgeoning | 1 | Oggetto di peso tra 1 lb e STR lb |
| Warhammer | Melee | STR | Melee | 1d10 + STR Bludgeoning | — | Two hands |

### Edged Weapon Skills

| Skill | Tipo | Stat | Range | Danno | AI Favor | Limitations / Cooldown |
|---|---|:--:|---|---|:--:|---|
| Axe | Melee | STR | Melee | 1d6 + STR Slashing | — | — |
| Dagger | Melee | DEX | Melee | 1d4 + STR Piercing | 1 | — |
| Longsword | Melee | STR | Melee | 1d8 + STR Slashing | — | — |
| Rapier | Melee | DEX | Melee | 1d6 + DEX Piercing | — | — |

### Hand-to-Hand Combat Skills

| Skill | Tipo | Stat | Range | Danno | AI Favor | Limitations / Cooldown | Damage Effect disponibili |
|---|---|:--:|---|---|:--:|---|---|
| Foot Soldier | Melee | STR | Melee | 1d4 + STR Bludgeoning | 1 (solo senza Damage Effect) | — | Powerful Strike, Smush |
| Noggin Nocker | Melee | STR | Melee | 1d4 + CON Bludgeoning | 1 (solo senza Damage Effect) | Con Success si perde 1 Health Bar slot | Skullcracker, Powerful Strike |
| Pugilism | Melee | DEX | Melee | 1d2 + STR Bludgeoning | 2 (solo senza Damage Effect) | — | Dirty Fighting, Iron Punch, Powerful Strike |
| Unarmed Combat | Melee | STR | Melee | 1d4 + STR Bludgeoning | 1 | Non può scegliere un Damage Effect | Nessuno |
| Wrasslin' | Melee | STR | Melee | 1d4 + STR Bludgeoning | 1 (solo senza Damage Effect) | Two hands; Held Debuff su Success | Choke Out, Dirty Fighting, Toss |

### Hand-to-Hand Damage Effect Skills

| Skill | Tipo | Si applica a | Cooldown |
|---|---|---|---|
| Choke Out | Passive | Wrasslin' | — |
| Dirty Fighting | Passive | Pugilism, Wrasslin' | — |
| Iron Punch | Passive | Pugilism | — |
| Powerful Strike | Passive | Foot Soldier, Noggin Nocker, Pugilism | 30 ore |
| Skullcracker | Passive | Noggin Nocker | — |
| Smush | Passive | Foot Soldier | Una volta per round |
| Toss | Passive | Wrasslin' | — |

### Ranged Weapon Skills

| Skill | Tipo | Stat | Range | Danno | AI Favor | Limitations / Cooldown |
|---|---|:--:|---|---|:--:|---|
| Crossbow | Ranged | DEX | 50 ft | 1d8 Piercing | — | Two hands; munizioni; Cooldown una volta per round |
| Bow | Ranged | DEX | 100 ft | 1d6 + STR Piercing | — | Two hands; munizioni |
| Handgun | Ranged | DEX | 150 ft | 1d8 Piercing | — | Munizioni; ricarica dopo Major Fail o peggio |
| Javelin | Ranged | DEX | 40 ft | 1d8 + STR Piercing | — | — |
| Shotgun | Ranged | DEX | 30 ft | 1d10 Piercing | — | Two hands; munizioni; ricarica dopo Major Fail o peggio |
| Shuriken | Ranged | DEX | 30 ft | 1d4 + STR Piercing | 1 | — |
| Slingshot | Ranged | DEX | 30 ft | 1d2 + STR Bludgeoning | 2 | Two hands |

### Reach Weapon Skills

| Skill | Tipo | Stat | Range | Danno | AI Favor | Limitations / Cooldown |
|---|---|:--:|---|---|:--:|---|
| Herding Weapons | Melee | STR | 10 ft | 1d4 + STR Bludgeoning | 1 | Two hands |
| Lance | Melee | STR | 10 ft | 1d12 + STR Piercing | — | Solo da cavalcatura; incompatibile con Attack of Opportunity e Zone of Control |
| Polearm | Melee | STR | 10 ft | 1d8 + STR Piercing | — | Two hands |
| Quarterstaff | Melee | STR | 10 ft | 1d6 + STR Bludgeoning | — | Two hands |

### Esplosivi e fumo

Gli esplosivi e i fumogeni sono descritti nella sezione *Attack Skill: esplosivi e fumo*. La Skill di esplosivi non viene usata per attaccare con un esplosivo lanciato (vedi la Skill Throwing).

*Fonte: manuale, p. 177–184.*
