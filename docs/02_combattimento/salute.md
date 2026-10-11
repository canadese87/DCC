---
tags:
  - Combattimento
  - Salute
  - Da verificare
  - Tabelle
---

# Salute (Health Menu)

L'Health Menu di ogni personaggio è accessibile ogni volta che può accedere al proprio HUD. Indica gli stati attivi (Buff, Debuff e Injury). Nel gioco l'Health Menu comprende: Health Bar, Mana, Buff & Debuff e Injuries.

## Health Bar (HB)

- Ogni creatura ha una Health Bar (HB), che tiene traccia della salute disponibile. Il valore di ogni slot è determinato dal CON Mod.
- La HB dei crawler è composta da 10 slot. Le singole creature possono avere meno slot (ad esempio i Mob comuni) o più slot (Boss, Elite e alcuni NPC).

## Tipi di danno (Damage Types)

Ogni istanza di danno ha di solito un tipo: Bludgeoning, Piercing o Slashing per il danno fisico; Acid, Ice, Fire e altri per quello elementale. I tipi di danno non hanno di per sé un effetto specifico, ma sono richiamati da altri effetti come Resistance, Vulnerability e Immunity.

### Tabella 10: Tipi di danno e rarità

| Tipo di danno | Rarità |
|---|---|
| Acid | Uncommon |
| Bludgeoning | Common |
| Electric | Uncommon |
| Fire | Common |
| Force | Uncommon |
| Holy | Uncommon |
| Ice | Uncommon |
| Necrotic | Uncommon |
| Piercing | Common |
| Poison | Common |
| Psychic | Uncommon |
| Slashing | Common |
| Sonic | Uncommon |

## Resistenze, Vulnerability e Immunity

Il danno si modifica nell'ordine seguente.

1. **Damage Resistance (DR)**: quando un bersaglio subisce danno, il totale è ridotto prima di tutto dalla sua DR. Il danno restante, se presente, si applica alla Health Bar.
2. **Elemental Resistance**: vedi sotto.
3. **Damage Vulnerability**.
4. **Damage Immunity**.

### Tipi di Resistance

- **Damage Resistance (DR)**: resistenza contro tutti i tipi di danno.
- **Elemental Resistance**: una creatura con resistenza a un tipo elementale (ad esempio Fire Resistance) subisce metà del danno di quel tipo ogni volta che lo subisce.
- DR ed Elemental Resistance si ottengono tramite Armor (naturale o indossata), Magic e Buff.

### Damage Vulnerability

- Dopo l'applicazione della Resistance si applica l'eventuale Damage Vulnerability.
- Le creature possono avere Vulnerability a tipi specifici di danno (ad esempio un Fire Elemental è vulnerabile al danno Ice).
- Una creatura subisce il doppio del danno quando è vulnerabile a quel tipo di danno.

### Damage Immunity

- Infine si calcola la Damage Immunity. Le creature possono avere Immunity a tipi specifici di danno (ad esempio un Fire Elemental è immune al danno Fire).
- Una creatura riduce a zero qualsiasi danno di un tipo a cui è immune.
- Un'Immunity ignora anche eventuali effetti aggiuntivi derivanti da quel danno, come i Debuff.

### Tipi di danno multipli

- Alcuni attacchi hanno più tipi di danno (ad esempio Fire e Force con la Spell Magic Missile a Rank 10+). Il danno si divide in parti uguali tra i tipi.
- Resistance, Vulnerability o Immunity a uno dei tipi si applicano solo alla parte di danno di quel tipo.

!!! example "Esempio"
    Un crawler con Immunity a Fire contro una Spell Magic Missile da 20 danni subisce comunque 10 danni Force.

!!! warning "Da verificare"
    Manuale p. 92 (esempio di combattimento): l'ordine citato per gli effetti dopo la DR è "Resistance, Immunity e Vulnerability", mentre la sezione Health Menu (p. 93) indica Resistance, poi Vulnerability, poi Immunity. L'ordine seguito qui è quello della sezione Health Menu. Poiché l'Immunity azzera il danno, il risultato non cambia.

## Applicare il danno alla Health Bar

Dopo aver applicato DR, Elemental Resistance, Vulnerability e Immunity, il danno restante si applica alla Health Bar.

- Se il danno restante è inferiore al valore di uno slot di HB, la vittima non subisce danno.
- Se è superiore, si somma il valore degli slot della HB finché il totale è pari al danno. Il danno che non raggiunge il valore di uno slot è perso.

!!! example "Esempio"
    Con una Health Bar di 10 slot da 4 ciascuno, un crawler subisce 22 danni. 22 è maggiore di 4: si segna uno slot e restano 18 danni. Si ripete la procedura per 5 slot in totale; restano 2 danni, inferiori a 4, che vengono ignorati. L'Attack fa perdere 5 slot di HB e la HB mostra il 50% rimanente.

!!! warning "Da verificare"
    Manuale p. 94: il testo dice di sommare gli slot "finché il totale è uguale o maggiore del danno", mentre l'esempio (22 danni, slot da 4) rimuove 5 slot (totale 20) e non 6 (totale 24). La regola qui riportata segue l'esempio: si rimuovono solo gli slot interamente coperti dal danno.

### Segnare la HB sulla scheda

- Per segnare uno slot di HB si riempie o si segna a matita il triangolo nell'angolo in alto a destra dello slot. Non si deve barrare il CON Mod, altrimenti lo si cancellerebbe insieme al segno di danno.
- Si segnano gli slot da verde a rosso (da destra a sinistra).
- Per i danni successivi non si contano gli slot già segnati.

## 0% Health Bar e Dying

Se un crawler perde l'ultimo slot di HB, ottiene il Debuff Dying e deve essere curato ad almeno il 10% per sopravvivere.

- Mentre è Dying, un crawler non può compiere Action, muoversi, parlare né usare il proprio HUD.
- Rimane Dying per un numero di round pari al proprio CON, dopodiché muore.
- Ogni volta che un crawler Dying subirebbe danno, e durante il Combat Step 5: Clean Up, si sottrae 1 dal numero di round che gli restano da Dying.
- I Mob muoiono istantaneamente a 0% di HB. I crawler GMC muoiono con la stessa lentezza dei crawler dei giocatori.

!!! warning "Da verificare"
    Manuale pp. 87, 91, 94, 97: la durata di Dying è indicata come "CON" (pp. 91, 94) oppure come "CON Mod" (p. 87 e Tabella 11, p. 97). Il testo non chiarisce quale dei due valori sia corretto.

### Action e guarigione da 0%

- Quando la HB di un crawler scende a 0%, il crawler non può usare le Action rimanenti finché non viene curato.
- Se un altro crawler lo cura durante lo Step 4 dello stesso round, può usare subito le Action che gli restavano.

## Guarigione (Healing)

- I crawler possono guarire con la magia (ad esempio la Spell Heal, che ogni crawler impara entrando nel World Dungeon), con pozioni e altri oggetti, e riposando o curandosi.
- A differenza del danno, la guarigione avviene sempre per slot. Ad esempio la Spell Heal recupera il 20% della HB, cioè due slot.
- Per guarire uno slot si cancellano gli slot persi da rosso a verde, fermandosi al 100%.
- Spell e oggetti indicano esplicitamente quanti slot di HB o quale percentuale ripristinano.

### Riposo (Resting)

Riposando in una saferoom i crawler rigenerano Health Bar e Mana senza usare Mana né oggetti. Il riposo può avvenire dormendo nella stanza privata della saferoom, oppure con attività come rilassarsi, mangiare, conversare e guardare il recap show, ma senza lavoro manuale più faticoso di un'attività tranquilla.

| Tipo di riposo | Durata | Effetto |
|---|---|---|
| Short Rest | 2 ore | Recupera 5 slot di HB. Rigenera anche metà del Mana totale (arrotondato per difetto): con 15 INT recupera 7 Mana. |
| Long Rest | 8 ore | HB e Mana tornano al massimo. Rimuove tutte le istanze del Debuff Fatigued. |
| Full Day's Rest | 30 ore | Necessario per recuperare dalle Injury di lungo periodo (vedi *Injuries* in *Buff e Debuff*). Recupera anche tutta la HB e tutto il Mana. |

### Recupero fuori dal combattimento

Per ogni ora completa trascorsa fuori dal combattimento o da altre situazioni di stress, un crawler recupera 1 slot di HB e 5 Mana.

### Altre forme di guarigione

Oltre a oggetti e Spell, Skill e Buff presenti nell'equipaggiamento possono aiutare a recuperare Health e Mana, come la Skill Regeneration e il Recovery Buff (vedi *Buff e Debuff*).

## Mana

- Il Mana è l'energia usata per lanciare le Spell. I crawler vi accedono tramite l'Health Menu.
- I crawler recuperano Mana riposando, consumando il Mana Toast disponibile in alcune saferoom, consumando Mana Potion e in altri modi.
- Per il lancio delle Spell e il Mana vedi le sezioni *Spell* e *Mana*.

*Fonte: manuale, p. 93–96.*
