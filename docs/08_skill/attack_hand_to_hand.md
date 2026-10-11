# Attack Skill: Hand-to-Hand

## Regole generali Hand-to-Hand

- Quando si attacca con una Attack Skill hand-to-hand la cui descrizione indica che si può scegliere un Damage Effect, si sceglie **un** Damage Effect disponibile **prima** di effettuare la Attack Skill Check.
- Se l'Attack colpisce, si tirano prima i dadi del base damage e poi si applica il Damage Effect scelto.
- Se per la maggioranza degli attacchi hand-to-hand di un combattimento di almeno tre round non si usa alcun Damage Effect, il crawler ottiene l'AI Favor indicato nella voce della Skill.

*Fonte: manuale, p. 179.*

## Hand-to-Hand Combat Skills

### Foot Soldier

- **Tipo**: Melee Attack
- **Stat per colpire**: STR
- **AI Favor**: 1 (solo se non si usa un Damage Effect)
- **Damage Effect**: Powerful Strike o Smush (facoltativo), scelto prima del tiro per colpire.
- **Base Damage**: 1d4 + STR Bludgeoning

| Rank | Upgrade |
|:--:|---|
| 5 | +1d4 base damage |
| 10 | +1d4 base damage |
| 15 | +1d4 base damage. Il bersaglio ottiene il Sore as Shit Debuff. |

### Noggin Nocker

- **Tipo**: Melee Attack
- **Stat per colpire**: STR
- **AI Favor**: 1 (solo se non si usa un Damage Effect)
- **Limitations**: con Success, il crawler perde 1 Health Bar slot.
- **Damage Effect**: Skullcracker o Powerful Strike (facoltativo), scelto prima del tiro per colpire.
- **Base Damage**: 1d4 + CON Bludgeoning

| Rank | Upgrade |
|:--:|---|
| 5 | +1d4 base damage. Il crawler non subisce danno dal proprio Attack. |
| 10 | +1d4 base damage. Aggiungere 1 Rank damage die. |
| 15 | +1d4 base damage. Il bersaglio ottiene il Woozy Debuff. |

### Pugilism

- **Tipo**: Melee Attack
- **Stat per colpire**: DEX
- **AI Favor**: 2 (solo se non si usa un Damage Effect)
- **Damage Effect**: Dirty Fighting, Iron Punch o Powerful Strike (facoltativo), scelto prima del tiro per colpire.
- **Base Damage**: 1d2 + STR Bludgeoning

| Rank | Upgrade |
|:--:|---|
| 5 | +2d2 base damage |
| 10 | +1d2 base damage |
| 15 | +1d2 base damage. Si può effettuare un Attack extra gratuito con Disadvantage. |

!!! warning "Da verificare"
    Manuale, p. 179 (Pugilism, Rank 5): l'Upgrade riporta "+2d2 base damage", mentre gli altri Upgrade della Skill aggiungono 1d2. Riportato come stampato.

### Unarmed Combat

- **Tipo**: Melee Attack
- **Stat per colpire**: STR
- **AI Favor**: 1
- **Limitations**: non può scegliere un Damage Effect. Ogni crawler possiede questa Skill dall'inizio.
- **Descrizione**: raggruppa tutti i colpi senza arma.
- **Base Damage**: 1d4 + STR Bludgeoning

| Rank | Upgrade |
|:--:|---|
| 5 | +1d4 base damage |
| 10 | +1d4 base damage |
| 15 | +2d4 base damage |

### Wrasslin'

- **Tipo**: Melee Attack
- **Stat per colpire**: STR
- **AI Favor**: 1 (solo se non si usa un Damage Effect)
- **Limitations**: richiede due mani per essere impugnato.
- **Damage Effect**: Choke Out, Dirty Fighting o Toss (facoltativo), scelto prima del tiro per colpire.
- **Effetto**: con Success, il bersaglio ottiene il Held Debuff.
    - Un bersaglio Held resta Held finché non spende un'Action per tentare di liberarsi (i Mob possono usare la loro Move Action).
    - Per impedire la fuga, il crawler deve usare un'Action come Interrupt e superare una Wrasslin' STR-Opposed Skill Check.
- **Base Damage**: 1d4 + STR Bludgeoning

| Rank | Upgrade |
|:--:|---|
| 5 | Il Held Debuff può essere mantenuto senza costo di Action, ma la Skill Check per impedire la fuga è effettuata con Disadvantage. |
| 10 | +1d4 base damage |
| 15 | +1d4 base damage |

*Fonte: manuale, p. 179.*

## Hand-to-Hand Damage Effect Skills

Gli Hand-to-Hand Damage Effect sono un tipo speciale di Passive Skill che si aggiunge a determinate Skill hand-to-hand per potenziare o modificare l'attacco.

- Se l'attacco ha Success, si applica anche il Damage Effect scelto.
- Se l'attacco è un Fail, il Damage Effect non ha alcun effetto ma entra comunque in Cooldown (se previsto).
- Quando si effettua un Attack che aggiunge un Damage Effect, si pone un segno per la Skill Advancement successiva (vedi la sezione *Skill Advancement*) **o** nella Attack Skill **o** nel Damage Effect, non in entrambi.

### Choke Out

- **Tipo**: Damage Effect di Wrasslin', Passive
- **Effetto**: se il bersaglio è al 10% di Health Bar o meno, si infligge ×2 il danno totale.

| Rank | Upgrade |
|:--:|---|
| 5 | Choke Out si attiva al 20% di Health Bar o meno. |
| 10 | Choke Out si attiva al 40% di Health Bar o meno e infligge ×4 il danno totale. |
| 15 | Choke Out si attiva all'80% di Health Bar o meno e infligge ×8 il danno totale. |

### Dirty Fighting

- **Tipo**: Damage Effect di Pugilism o Wrasslin', Passive
- **Effetto**: si applica il Woozy Debuff al bersaglio.
- **Limitations**: se la Attack Skill Check è un Critical Fail, il crawler perde 1 Popularity.

| Rank | Upgrade |
|:--:|---|
| 5 | Si applica anche il The Taint Debuff al bersaglio. |
| 10 | Si applica anche il Blinded Debuff al bersaglio. Non si perde più Popularity sui Critical Fail. |
| 15 | Si applica anche immediatamente un Minor Injury Debuff al bersaglio. |

### Iron Punch

- **Tipo**: Damage Effect di Pugilism, Passive
- **Effetto**: +1d2 base damage.

| Rank | Upgrade |
|:--:|---|
| 5 | Aggiungere 1 Rank damage die. |
| 10 | Si può scegliere che il bersaglio ottenga lo Stunned Debuff invece di tirare il danno. |
| 15 | Aggiungere 1 Rank damage die. Il bersaglio ottiene lo Stunned Debuff. |

### Powerful Strike

- **Tipo**: Damage Effect di Foot Soldier, Noggin Nocker o Pugilism, Passive
- **Cooldown**: 30 ore
- **Effetto**: si moltiplica il risultato dei dadi di base damage per il Rank in questa Skill, poi si aggiungono modificatori e buff.

| Rank | Upgrade |
|:--:|---|
| 5 | Il Cooldown è 10 ore. |
| 10 | Il Cooldown è 5 ore. |
| 15 | Il Cooldown è 2 ore. |

### Skullcracker

- **Tipo**: Damage Effect di Noggin Nocker, Passive
- **Effetto**: se il bersaglio è della stessa taglia del crawler, +1d4 base damage.

| Rank | Upgrade |
|:--:|---|
| 5 | +1d4 base damage se il bersaglio è della stessa taglia del crawler. |
| 10 | Se il bersaglio è della stessa taglia del crawler, aggiungere 1 Rank damage die; il bersaglio ottiene lo Stunned Debuff. |
| 15 | Se il bersaglio è della stessa taglia del crawler, aggiungere 1 Rank damage die; il bersaglio ottiene il Blood Trail Debuff. |

### Smush

- **Tipo**: Damage Effect di Foot Soldier, Passive
- **Limitations**: applicabile solo a bersagli al 20% di Health Bar o meno.
- **Cooldown**: una volta per round.
- **Effetto**: si infligge ×2 il danno totale.

| Rank | Upgrade |
|:--:|---|
| 5 | Smush si attiva al 30% di Health Bar o meno e infligge ×3 il danno totale. |
| 10 | La Skill non ha Cooldown. |
| 15 | Smush si attiva al 40% di Health Bar o meno e infligge ×4 il danno totale. |

### Toss

- **Tipo**: Damage Effect di Wrasslin', Passive
- **Effetto**: si infligge +1d8 base damage + STR Bludgeoning, si pone fine al Held Debuff e si lancia il bersaglio di 5 ft ogni cinque Rank (minimo 5 ft) posseduti in questa Skill.
- **Limitations**: si possono lanciare (Toss) solo nemici di taglia inferiore a quella del crawler.

| Rank | Upgrade |
|:--:|---|
| 5 | Si possono lanciare nemici fino alla propria taglia o inferiori. |
| 10 | Si possono lanciare nemici di una taglia superiore alla propria o inferiori. |
| 15 | +1d8 base damage. Si possono lanciare nemici di due taglie superiori alla propria o inferiori. |

### Riepilogo dei Damage Effect per Skill

| Attack Skill | Damage Effect selezionabili |
|---|---|
| Foot Soldier | Powerful Strike, Smush |
| Noggin Nocker | Skullcracker, Powerful Strike |
| Pugilism | Dirty Fighting, Iron Punch, Powerful Strike |
| Unarmed Combat | Nessuno |
| Wrasslin' | Choke Out, Dirty Fighting, Toss |

*Fonte: manuale, p. 180–181.*
