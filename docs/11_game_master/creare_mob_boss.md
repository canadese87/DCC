# Creare Mob e Boss (Create Your Own Mobs and Bosses)

Mob e Boss sono definiti principalmente da Stat e Attack: non hanno Skill né Traumas. Un Mob o Boss si documenta in uno Stat Block (vedi la sezione *Stat Block e scaling degli encounter*).

## Principi di progettazione

- Considerare il Floor in cui compare il Mob e i tipi di encounter che sfidano il gruppo.
- Copiare le schede dei crawler e individuare modi di impiegare le loro Skill meno usate.
- Se il gruppo ha una **Resistance** o un'**Immunity** a un tipo di danno, il gruppo dovrebbe incontrare Mob con quel tipo di danno almeno una volta per Floor.
- **Spostamento di un Mob a un altro Floor**: se un Mob creato per un Floor non viene usato, può comparire in un Floor successivo; diversi valori dello Stat Block ("+F") aumentano automaticamente del nuovo Floor Number. Un Mob di Level basso sul nuovo Floor dovrebbe comparire in numero maggiore rispetto a quanto pianificato.
- **Azioni**: un Mob dispone di **1 Move Action e 1 altra Action** (tipicamente un Attack); può muoversi due volte se necessario. Un **Boss dispone di 1 Action per crawler**, anche se un crawler muore a metà scontro, e può usarla per qualsiasi cosa.

*Fonte: manuale, p. 270.*

## Procedura di creazione

Campi dello Stat Block, nell'ordine del manuale:

### Name

Ogni Mob ha un nome originale.

### Size

La taglia è relativa. Indicare il nome della taglia e il valore numerico associato sotto il nome del Mob (esempio: Large (5)). La taglia influisce sugli Attack quando c'è grande differenza di taglia tra combattenti (vedi *Additional Combat Modifiers*, pp. 84–85).

### Type

Solo descrittivo. I tipi più comuni: Beastly, Undead, Humanoid, Ooze; altri esempi: Trapezoidal, Patchwork.

### Health Bar Slots (Mob)

- Il numero di slot HB è uguale al **Level del Mob, fino a un massimo di 10**.
- Dentro ogni slot si scrive il **CON Mod** del Mob.
- Assegnare le percentuali a ciascuno slot, con **100% nello slot più a destra**: dividere 100 per il numero di slot e arrotondare al numero intero più vicino; tale valore è la percentuale di ogni slot, elencate in ordine da sinistra a destra. È ammesso arrotondare per eccesso o per difetto in modo non uniforme per chiudere a 100% sull'ultimo slot.
- Le percentuali non devono essere esatte, ma vanno comunicate ai crawler, che vedono le Health Bar sopra i Mob.

!!! example "Esempio"
    Mob di Level 6: 6 slot HB. 100 ÷ 6 = 16,66: le percentuali crescono da sinistra a destra con incrementi di 16% o 17% (sommando ogni incremento al totale), in modo da terminare con 100% a destra. Non è corretto arrotondare ogni incremento a 17%, perché si avrebbe un salto da 85% a 102%.

    Mob di Level 3 (Bad Llama): 3 slot, percentuali 33% – 67% – 100%, ciascuno slot contenente il CON Mod.

### Health Bar Slots (Boss)

I Boss usano la Tabella 50 per slot HB e punti Stat.

#### Tabella 50: Boss Severity

| Boss Tier | Neighborhood | Borough | City | Province | Country | Floor |
|---|---|---|---|---|---|---|
| Stats per Level | 3 | 4 | 5 | 6 | 8 | 10 |
| HB Slots | 10 + F | 15 + F | 20 + F | 25 + F | 30 + F | 40 + F |

!!! warning "Da verificare"
    Il manuale non specifica il valore contenuto negli slot HB dei Boss né applica esplicitamente alla riga "Stats per Level" una formula: si presume (per analogia con i Mob, che hanno 3 punti Stat per Level) che "Stats per Level" indichi i punti Stat per Level del Boss, da sommare alla base 5 per Stat. Il testo rimanda alla Tabella 50 con "Bosses work a little bit differently" e "See Table 50 for their additional stat points".

### Level

Il GM sceglie liberamente il Level, ma le seguenti indicazioni permettono ai crawler di superare lo scontro. I Floor hanno un intervallo tipico di Level dei Mob (Tabella 51).

**Boss**

- Costruire le statistiche del Boss come quelle di un Mob del Floor, ma usando la **riga successiva** della Tabella 51 (esempio: un Boss del Third Floor ha forza paragonabile a un Mob del Fifth Floor).
- **Neighborhood Boss**: estremo basso dell'intervallo.
- **Borough Boss**: metà dell'intervallo.
- **City Boss**: estremo alto dell'intervallo, oppure l'estremo basso per il Floor successivo ("the next floor down").
- **Province o Country Boss**: possono essere ancora più forti.
- Il Level di un Boss è quasi sempre superiore alla media dei crawler; i Boss non compaiono in gruppi numerosi: sono di norma unici (possono avere Mob con sé).

!!! example "Esempio"
    Sul Third Floor i Mob sono tipicamente Level 10–29. I Boss variano quindi tra Level 30 e 59 (un Floor più in alto nella Tabella 51): Neighborhood Boss nei Level bassi 30, Borough Boss nei bassi 40, City Boss nei 50, e così via.

**Mob**

- Un Mob di Level 93 può comparire in qualsiasi momento.
- Mob di Level basso possono comparire in Floor in cui sono facili: devono comparire in **grandi numeri**.
- Mob di Level uguale o superiore ai crawler: un gruppo pari al numero dei membri del party è tipico.

#### Tabella 51: Mob Level, Floor & Damage Dice

| Mob Level | Dice of Damage | Floor |
|---|---|---|
| 1–4 | 1d | 1 |
| 5–9 | 2d | 2 |
| 10–29 | 3d | 3–4 |
| 30–59 | 5d | 5–7 |
| 60–99 | 7d | 8–10 |
| 100–159 | 9d | 11–13 |
| 160–249 | 12d | 14–16 |
| 250+ | 15d | 17–18 |

### Surprise

Surprise è un Skill Check INT-Opposed (con Ambush, Stealth o Skill correlata) per sorprendere un Mob.

- Formula: **Surprise = 10 + INT Mod, seguito da +F.**
- Calcolare dopo aver definito le Stat.
- I crawler possono sorprendere solo Mob ignari della loro presenza. Se il gruppo si imbatte in un gruppo di Mob, o i Mob sono in attesa, non è possibile tentare la sorpresa.

### Evade

Evade è la Difficulty degli Attack dei crawler contro il Mob.

- Formula: **Evade = 10 + DEX Mod, seguito da +F.**
- Il "+F" viene aggiunto in gioco in base al Floor corrente.

!!! example "Esempio"
    Mob con INT Mod +2 e DEX Mod +4: Surprise 12+F; Evade 14+F.

### Move

Il valore tipico per Mob umanoidi bipedi è **20+S**; sono ammessi valori superiori o inferiori. Con le mappe di battaglia considerare il terreno: in aree aperte gli Attack a distanza infliggono molto danno prima che Mob lenti si avvicinino; in aree affollate con scarsa visibilità gli Attack in mischia sono più letali.

### Damage Resistance (DR)

- DR base del Mob = **Floor Number**.
- Mob con armatura vera (cuoio, maglia) o naturale (pelle spessa, placche): **+1 o +2 DR**.
- Mob incantatori: DR di norma **1 o 2 in meno** rispetto alla norma.
- Un Mob annunciato dal System AI come "proveniente da un altro Floor" usa come DR base quella del **suo Floor di origine**, non quello corrente (esempio: un Rage Elemental del Thirteenth Floor sul Second Floor ha ancora DR 13).
- Se il GM sposta intenzionalmente Mob tra Floor, usa il Floor Number corrente.

### Stats

- Mob: **base 1 in ogni Stat e 3 punti Stat da spendere per Level** (esempio: un Mob di Level 6 ha 18 punti da distribuire). Il GM decide la distribuzione.
- Boss: **base 5 in ogni Stat**; vedi la Tabella 50 per i punti aggiuntivi.
- Scrivere il valore di ogni Stat e il relativo Stat Mod tra parentesi.
- Indicazioni: Mob con attacchi naturali o armi traggono vantaggio da STR elevata; gli incantatori richiedono INT elevata.

### Attacks

- Mob di Level basso hanno spesso un solo Attack principale. Mob di Level superiore hanno più Attack; i Boss ne hanno di più.
- I dadi di danno determinano la letalità. Il dado standard è **d6**; il GM può variare.
- Se i crawler dominano i Mob, aumentare i numeri finché lo scontro diventa una sfida senza essere gravoso (vedi la sezione *Gestione di regole, patch e morte dei PC*).

**Regole per i dadi di danno**

- **Attack principale**: usa i dadi di danno completi della Tabella 51.
- **Altri Attack** che aggiungono solo un nuovo tipo di danno: spesso usano anch'essi il dado di danno completo (esempio: bestia di Level 11 con Bite (Piercing) e Trample (Bludgeoning) infligge 3d con entrambi).
- **Attack ad area** (Blast, Burst, Cone, Line): di norma perdono **1d** dal numero completo di dadi. Se il danno è basso, l'area ha portata e raggio ampi; se il danno è buono, l'area è più limitata. Aggiungere **Splash damage** (metà danno) permette di colpire l'intero gruppo senza usare un ampio Blast.
- **Attack con effetti extra** innescati quando il crawler perde slot HB o fallisce nettamente un Evade Check: di norma perdono anch'essi **1d**.
- **Attack che applicano automaticamente un Debuff**: non devono infliggere molto danno (spesso solo d4).
- Se i crawler non subiscono danno da Mob simili, aumentare i dadi di **un passo**.
- Se ogni Debuff o effetto aggiuntivo è subordinato a un **Major Evade Fail** o peggio, tali effetti si verificheranno raramente: per Attack a basso danno, applicare i Debuff a ogni colpo a segno o alla perdita di 1 o più slot HB. Se il danno è alto, i crawler dovranno probabilmente effettuare l'Evade.
- Nota: i crawler tendono a ritenere non conveniente effettuare l'Evade contro Attack a basso danno, a meno che ne arrivino 3 o più.

### Notes

Le note sotto gli Attack contengono: abilità aggiuntive, strategia, ordine degli Attack, effetti passivi, interattivi o innescati, e tutto ciò che riguarda l'encounter e non appartiene allo Stat Block. I Boss hanno quasi sempre note. Le Notes possono contenere **debolezze** che i crawler possono scoprire con l'azione Look for Clues.

*Fonte: manuale, p. 270–273.*

## Riepilogo delle formule

| Valore | Mob | Boss |
|---|---|---|
| Slot Health Bar | Level (max 10); ogni slot contiene il CON Mod | Tabella 50 (10+F ... 40+F, secondo il Boss Tier) |
| Punti Stat | 1 base per Stat + 3 per Level | 5 base per Stat + punti aggiuntivi della Tabella 50 |
| Surprise | 10 + INT Mod + F | non specificato separatamente |
| Evade | 10 + DEX Mod + F | non specificato separatamente |
| Move | 20+S tipico per umanoidi bipedi | non specificato separatamente |
| DR | Floor Number (+1/+2 armatura, -1/-2 incantatori) | non specificato separatamente |
| Dadi di danno (Attack principale) | Tabella 51 per Level | non specificato separatamente |
| Azioni | 1 Move Action + 1 altra Action | 1 Action per crawler |

*Fonte: manuale, p. 270–273.*
