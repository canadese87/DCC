# Buff, Debuff e Injury (Buffs & Debuffs)

I crawler ottengono o subiscono spesso effetti di stato che cambiano il loro rendimento. Si chiamano rispettivamente **Buff** e **Debuff**.

- I Buff rendono i crawler più forti, veloci, resistenti o comunque più difficili da uccidere.
- I Debuff fanno l'opposto e sono di norma applicati come effetto collaterale del subire danno.

## Buff

I Buff sono effetti positivi che conferiscono un beneficio a un crawler. Sono di solito concessi da pozioni, Spell ed equipaggiamento. Se un Buff ha una durata e/o un cooldown, deve essere attivato per ottenerne gli effetti. I Buff sono di due tipi: Internal Buff ed External Buff.

### Internal Buff

Un Internal Buff influisce sul crawler senza interferire con gli altri. I più comuni aumentano Stat o Skill.

- I Buff concessi da Skill Upgrade, Race e Class sono permanenti finché si ha accesso alla loro fonte.
- I benefici dell'equipaggiamento (ad esempio un bonus a Evade dalla Skill Rapier) si applicano solo mentre si impugna quell'equipaggiamento.

Esempi di Internal Buff:

| Buff | Effetto |
|---|---|
| Anti-Piercing | La DR di un'armatura con questa qualità si applica contro il danno Armor-Piercing. |
| Good Sleep | +Floor Number a tutte le Stat del crawler per 30 ore. |
| Invisible | Una creatura Invisible non può essere presa di mira da nulla che richieda la vista; anche il suo equipaggiamento è nascosto. Ottiene anche i benefici degli Unseen Attackers (vedi *Attacchi, modificatori e danno*). |
| Iron Skin Potion | Raddoppia la DR del crawler per 30 minuti. |
| Recovery Buff | Ripristina il crawler alla piena Health (una volta ogni 5 ore). |
| Replenish Buff | Ottiene Mana pari a INT ogni 10 minuti. |
| Restore Buff | Ripristina il crawler al pieno Mana (una volta ogni 5 ore). |
| Rooted in Place | Non può essere spinto, tirato, fatto scivolare o spostato con la forza in altro modo. |
| Sticky Feet | Concede al crawler un Climb Movement per un numero di minuti pari alla propria DEX. |

### External Buff

Mentre i Buff normali si applicano sempre, gli External Buff si attivano quando si verifica un particolare trigger.

- Quando il trigger si verifica, il giocatore può scegliere se il Buff si attiva o no (utile quando l'effetto ha un cooldown).
- Attivare un External Buff in generale non richiede una Action. Alcuni effetti potenti possono richiedere una Action specifica, risolta come un Interrupt.

Esempi di External Buff:

| Buff | Effetto |
|---|---|
| Damage Reflection | Quando un crawler perde un numero specifico di slot di Health Bar, l'attaccante perde 1 slot di HB. Alcune versioni possono dirigere il danno altrove. |
| Resistances & Immunities | Quando un crawler subisce un tipo di danno, può attivare questo External Buff per ridurre istantaneamente il danno. |
| Safe Fall | Quando un crawler cade da una distanza uguale o superiore a una soglia, questo External Buff si attiva per impedire il danno Bludgeoning da caduta; il crawler atterra in posa da supereroe. |

### Regola del Tre (The Rule of Three)

- Un crawler può avere al massimo tre External Buff attivi contemporaneamente.
- Se ha accesso a più di tre External Buff, il giocatore sceglie quali tre sono attivi all'inizio della giornata di crawling e li annota nella sezione External Buffs della scheda del personaggio.
- Di norma si scelgono i Buff più utili fino alla fine del successivo Long Rest.
- Se un crawler ottiene un nuovo External Buff durante la giornata, può cambiare quali External Buff ha attivi durante uno Short Rest.

## Debuff

I Debuff sono effetti negativi sulla creatura che li subisce: limitano le opzioni, applicano Disadvantage alle Check o infliggono danno continuo finché il Debuff non termina.

- Non esiste un limite al numero di Debuff che possono agire contemporaneamente su una creatura.
- Una creatura non può subire lo stesso Debuff più di una volta contemporaneamente, a meno che la voce del Debuff indichi "Stackable". Quando una creatura ha Debuff Stackable, tutti applicano il proprio effetto in modo cumulativo.

### Debuff su Mob o NPC

I Debuff applicati a Mob o NPC hanno gli stessi effetti che hanno sui crawler. Poiché però il GM non tira Check d20, si comportano diversamente. Il GM applica i seguenti cambiamenti quando un Debuff concede una delle penalità elencate.

| Penalità del Debuff | Effetto su Mob o NPC |
|---|---|
| Danno | Il danno del Debuff si applica alla fine di ogni round. |
| Disadvantage | La Difficulty dell'Action, dello Stat Mod o di una funzione simile del Mob è ridotta di 5 quando un crawler effettua una Check contro di esso. Nel caso di un Attack, il crawler ottiene una Evade Check gratuita contro l'Action svantaggiata. Se fallisce quella Check gratuita, può comunque spendere un'Action per effettuare Evade come di consueto e riprovare. |
| Penalità Skill −X | La Difficulty del Mob è ridotta di X. |

### Durata dei Debuff

- Tutti i Debuff hanno una durata: il tempo o le condizioni che devono verificarsi prima che il Debuff termini.
- Alcune Action, oggetti o abilità possono porre fine a un Debuff in anticipo (ad esempio rotolarsi a terra o buttarsi in acqua per spegnere un fuoco).
- Il GM può stabilire che un Debuff termini in anticipo se le circostanze cambiano.
- Se un Debuff infligge a un crawler un danno che lo porterebbe a 0% di HB, il crawler può effettuare una Stat Check di CON con Difficulty 10 + Floor alla fine del round. Questa Stat Check non richiede una Action ma avviene automaticamente prima del danno fatale. In caso di Success, il Debuff termina e il crawler evita il danno.

### Debuff che infliggono danno

- Quando un Debuff danneggia un crawler, il danno si applica alla fine di ogni round di combattimento.
- Il danno dei Debuff ignora la DR, ma le altre Resistance e Immunity si applicano comunque.

### Tabella 11: Debuff

La tabella riporta nome, effetto e durata predefinita dei Debuff.

| Debuff | Effetto | Durata |
|---|---|---|
| Blinded | Tutte le Skill Check che richiedono la vista si tirano con Disadvantage. | Fino alla fine del round successivo. |
| Blood Trail | Si subiscono 1d6+F alla fine di ogni round. Stackable. | Fino a quando non viene curato con una benda o una Skill Check di First Aid. |
| Burned | Si subiscono 1d10+F danni da Fire alla fine di ogni round. | Fino alla fine del combattimento o 5 minuti. Come Action, la vittima può effettuare una Stat Check di DEX per spegnere le fiamme. |
| Drowning | Si subiscono 1d6+F danni alla fine di ogni round. | Finché la testa non è fuori dall'acqua. |
| Dying | Si è a 0% di HB. Il CON Mod indica quanti round restano prima di morire. Si sottrae 1 da questo conto alla rovescia alla fine di ogni round. Inoltre, ogni volta che un crawler Dying subirebbe danno da qualsiasi fonte, sottrae invece 1 dal conto alla rovescia. | Finché non si muore o non si recupera almeno 1 slot di HB. |
| Enraged | Si è in uno stato di furia estrema e incontrollata. Si possono compiere solo Attack e Move Action. | Fino alla fine di 2 round o 20 secondi. |
| Fatigued | Penalità di −1 a tutte le Check e Move dimezzato. Stackable. | Fino alla fine di un Long Rest. |
| Held | Si è tenuti attivamente. Non si possono usare Move Action né compiere uno Step, ma si può ancora torcere il corpo per effettuare Evade. Gli Attack contro un nemico Held si effettuano con Advantage. | Finché non si viene rilasciati da ciò che tiene o non ci si libera. Si effettua una Skill Check di Escape Artist STR-Opposed; se non si è tenuti fisicamente, è Unopposed. |
| Long-Term Major Injury | Penalità di −5 a tutte le Check. | Fino alla fine di un Full Day's Rest. |
| Long-Term Minor Injury | Penalità di −2 a tutte le Check. | Fino alla fine di un Long Rest. |
| Major Injury | Penalità di −5 a tutte le Check. Ottenere un Major Injury una seconda volta lo trasforma in Long-Term Major Injury. | Fino alla fine di un Long Rest. |
| Minor Injury | Penalità di −2 a tutte le Check. Ottenere un Minor Injury una seconda volta lo trasforma in Long-Term Minor Injury. | Fino alla fine di uno Short Rest. |
| Muted | Non si può parlare né lanciare Spell. | Fino alla fine del combattimento o 5 minuti. |
| Poisoned | Si subiscono 1d8+F danni da Poison alla fine di ogni round. Stackable. | Finché non viene trattato con un antidoto. |
| Paralyzed | Non si può compiere alcuna Action. | Fino alla fine del round successivo. |
| Queasy | Se la prossima Action richiede un tiro, viene effettuata con Disadvantage. | Alla fine della prossima Action compiuta. |
| Sepsis | Si è Staggered (vedi Staggered) e si subiscono 1d10+F danni da Poison alla fine di ogni round. | Come Staggered; il danno continua finché non si viene curati. |
| Shit-Faced | Tutte le Check si effettuano con Disadvantage. | Fino alla fine di 10 minuti. |
| Shocked | Si perde la prossima Action. | Una volta che si è rinunciato a quell'Action. |
| Sore as Shit | Penalità di −1 a tutti i tiri. | Fino alla fine di 1 ora. |
| Staggered | La prossima Action compiuta non può essere un Move; se è un Attack, la Check si effettua con Disadvantage. Non si può compiere uno Step di 10 ft con la prossima Action. | Alla fine della prossima Action compiuta. |
| Stiff Legs | Non si possono compiere Step di 10 ft. | Fino alla fine del combattimento o 5 minuti. |
| Stunned | Si ottiene Disadvantage sulla prossima Check. | Una volta effettuata una Check. |
| Take Down | Si cade prone. Mentre si è prone, tutti gli Attack contro di sé si effettuano con Advantage. | Si usa lo Step di 10 ft per rialzarsi. |
| Terrified | Non si possono compiere Move Action né Step di 10 ft. Tutti gli Attack si effettuano con Disadvantage. | Fino alla fine del round successivo, oppure finché non si subisce danno di almeno 1 slot di HB. |
| The Taint | Non si può essere curati. | Fino alla fine del combattimento o 5 minuti. |
| Woozy | Non si può aggiungere il DEX Mod alle Attack Check o alle Evade Check. | Fino alla fine del round successivo. |

!!! note "Note sulla tabella"
    "F" indica il numero del Floor corrente. I nomi Shit-Faced e Sore as Shit sono i nomi ufficiali dei Debuff. Per Blood Trail e Drowning il tipo di danno non è specificato nella tabella.

!!! warning "Da verificare"
    Manuale p. 97, Tabella 11: nel testo estratto le righe sono interlacciate e le celle di Effetto e Durata sono state riassociate ai nomi in base all'ordine e al contenuto (ad esempio "Until the end of a full day of rest" a Long-Term Major Injury, in coerenza con la sezione Injuries a p. 96). Nell'effetto di Sepsis la durata "As Staggered, and the damage continues until you're healed" è interpretata come "come Staggered; il danno continua finché non si viene curati".

## Injuries

Le Injury sono un tipo specifico di Debuff ottenuto tramite danni significativi, come un grave fallimento nell'evitare un Attack, l'effetto di un Attack particolarmente potente o violento di un Mob, e altri sforzi catastrofici.

- Esistono due tipi principali di Injury: normali e di lungo periodo (long-term).
- Il modo più comune in cui una Injury passa da semplice a long-term è subire più volte la stessa gravità di Injury. Ad esempio, se un crawler subisce un Minor Injury e ne subisce un altro, diventa un Long-Term Minor Injury.
- Tutte le Injury si curano più comunemente con il riposo in una saferoom.

| Injury | Effetto | Recupero |
|---|---|---|
| Minor Injury | −2 a tutte le Check. | Il Minor Injury normale dura fino alla fine di uno Short Rest. |
| Long-Term Minor Injury | −2 a tutte le Check. | Richiede un Long Rest per il recupero completo. |
| Major Injury | −5 a tutte le Check. | Il Major Injury normale richiede un Long Rest. |
| Long-Term Major Injury | −5 a tutte le Check. | Richiede 30 ore complete di riposo per il recupero completo (Full Day's Rest; vedi *Riposo* nella sezione *Salute*). |

La magia particolarmente potente reperibile ai Floor più avanzati o nelle loot box di alto tier può aiutare i crawler a recuperare più in fretta dalle Injury; tale magia è rara nei primi Floor.

*Fonte: manuale, p. 95–97.*
