# Crafting: incantamento e Skill Check

## Incantare oggetti (Enchanting Items)

Un oggetto può ricevere proprietà magiche quali: Skill bonuses, Stat buffs, triggered effects (inclusi gli effetti "On an Amazing Success" sulle armi), Resistances, Immunities, Damage Reflection e altro.

- Lo stesso identico enchantment **non** può essere applicato più di una volta a un oggetto. Esempio: dopo +1 Strength, l'oggetto non può ricevere un secondo buff di Strength.
- Non esiste un "+1 Longsword". Si aggiungono a una Longsword un **+1 Longsword Skill Rank** e un **+1 damage bonus**. Sono due enchantment distinti, creati e tirati separatamente.

### Rischi dell'over-enchanting

Il rischio riguarda ogni metodo di enchantment.

- Quando si applica **qualsiasi enchantment, con qualsiasi metodo**, a un oggetto che ha già **3 o più enchantment**, si tira **1d10**.
- Con un risultato di **5 o meno** l'oggetto si rompe in modo permanente.
- Gli oggetti distrutti da over-enchanting **non possono essere riparati**.
- Ogni enchantment conta come uno, indipendentemente dal livello di bonus. Un buff di +3 Strength conta come un solo enchantment.

### Altri metodi di enchantment

Il World Dungeon offre vari metodi per migliorare gli oggetti; sono tutti non comuni. Quelli più frequenti sono i seguenti.

**Scroll of Upgrade**: applica **un** enchantment a un oggetto attualmente equipaggiato; va applicato durante la scena in corso. Uno Scroll of Upgrade da platinum box può fornire due enchantment. Il livello tipico è un Bonus Level pari al Floor Number corrente (vedi Tabella 46).

!!! example "Esempio"
    Uno Scroll of Upgrade al Third Floor concede un enchantment di Bonus Level 3: +3 Strength, +3 damage oppure +3 Skill.

Gli enchantment più comuni sono i triggered effects "Amazing Success" sulle armi, abbreviati nelle note dell'arma come "AS: EFFECT". Regole:

- aggiungono danno extra, Debuff o altro effetto;
- è ammesso **un solo** trigger di questo tipo per arma;
- si sommano al bonus "+F damage" generato da ogni Amazing Success;
- un Critical Hit **non** attiva tale effetto.

Altri esempi di upgrade per armi sono nella Tabella 26 (p. 116 del manuale).

**Sharpening Stone**: si trova di norma nelle Platinum loot box e di norma è utilizzabile solo su "spiky weapons".

- Ha breve durata: va applicata subito e viene poi distrutta.
- Un'arma migliorata con una Sharpening Stone **raddoppia lo Stat Mod per il danno** su un'arma da taglio o appuntita e aggiunge **+1 danno ogni 10 Level** del possessore.

**Upgrade Patch**: rara; si trova nelle loot box di tier Gold.

- Migliora un capo di abbigliamento.
- Le patch sono oggetti **Fleeting**: se la patch viene rimossa, il bonus si perde.

**Bang Bro Spell**: questa Spell (p. 203 del manuale) crea un enchantment temporaneo su un oggetto.

### Bonus selezionabili

Chi incanta sceglie il beneficio desiderato tra: Stats, Non-Spell Skills, Buffs, Triggered Effects, Resistances, Immunities, Movement e Bonus Damage. Il beneficio si applica a un oggetto con cui lo stile di crafting interagisce.

- Per un bonus numerico (a Skill, Stat, DR o bonus damage) il valore del bonus determina gran parte della difficoltà della Skill Check di crafting.
- Se l'enchantment comporta qualcosa di più dell'aggiunta di numeri, il suo bonus level va discusso con il GM.
- Se l'enchantment risulta troppo debole o troppo potente, il Dungeon può intervenire per correggerlo.

#### Tabella 46: Bonus Level Examples

| Bonus | Esempi |
|---|---|
| +1 | Stick of Dynamite che infligge 1d6 Bludgeoning senza Area of Effect |
| +2 | Standard Healing Potion; Standard Mana Potion; Damage Reflection 8:1* |
| +3 | Poison Antidote Potion; Anti-Piercing Benefit (su abbigliamento con DR); Resistance a UNCOMMON DAMAGE TYPE; +5ft Move |
| +4 | Damage Reflection 5:1*; Good Healing Potion; Good Mana Refill Potion; Armor-Piercing |
| +5 | Restore Buff (full Mana, con cooldown); Resistance a COMMON DAMAGE TYPE; +10ft Move |
| +6 | Immunity a UNCOMMON DAMAGE TYPE; Rank Damage Die come damage bonus su un'arma; Gold Standard Healing Potion |
| +7 | Recovery Buff (cura tutti gli slot della Health Bar, con cooldown); +15ft Move |
| +8 | Damage Reflection 3:1*; Supreme Healing Potion |
| +9 | Immunity a COMMON DAMAGE TYPE; +20ft Move |
| +10 | Mordecai's Special Brew |

\*Damage Reflection: se il bersaglio perde in un solo colpo un numero di slot della Health Bar maggiore o uguale al primo numero, l'attaccante perde 1 slot della Health Bar.

!!! warning "Da verificare"
    Manuale p. 224. Le celle della Tabella 46 sono separate nel testo estratto; l'assegnazione degli esempi ai livelli di bonus è ricostruita per ordine di lettura e coerenza interna (es. Move +5ft ogni 2 livelli da +3; 1d6 = +1 e 3d6 = +3 secondo la formula di DC).

*Fonte: manuale, p. 223–224.*

## Tempo di crafting

- Ogni bonus level applicato richiede **1 ora per livello**. Esempio: un bonus +3 richiede 3 ore.
- Il lavoro può essere distribuito su più giorni, salvo diversa indicazione del blueprint.
- Le table attachment possono ridurre il tempo; lo fanno anche alcuni Rank Upgrade.
- Alcune potion possono essere prodotte in grandi lotti: ogni potion aggiuntiva richiede **+1 minuto per bonus level**, ma tutti gli ingredienti devono essere disponibili. Vedi la sezione *Alchemy*.

*Fonte: manuale, p. 224–225.*

## Skill Check di crafting

Quando è pronto, il crawler effettua una **Unopposed Skill Check** con la Skill richiesta dall'oggetto. **Aggiunge il tier del crafting table** al tiro.

- I materiali vengono consumati sia in caso di successo sia di fallimento. Skill e risultati come Salvage possono permettere di recuperare alcuni ingredienti.
- La Difficulty dipende dal bonus level e dal tipo di enchantment. Il **tipo** di enchantment è il fattore principale.

### Difficulty per tipo di enchantment

| Tipo di enchantment | Difficulty |
|---|---|
| Stats | 10 + [Bonus x2] |
| Non-Passive Skills e Spells | 10 + [Bonus x4] |
| DR, Passive Skills e Spells | 10 + [Bonus x6] |
| Qualsiasi categoria non coperta sopra | 10 + [Bonus x4] |

!!! example "Esempio"
    - +2 Dexterity a un pugnale: 10 + (2 x 2) = 14.
    - Scroll of Fireball Rank 2: 10 + (2 x 4) = 18.
    - Potion di +2 Dodge (Passive Skill): 10 + (2 x 6) = 22.
    - Stick of dynamite 3d6: 10 + (3 x 4) = 22.

### Esito

- **Successo**: l'oggetto è perfetto e dura per tutta la vita del crawler.
- **Fallimento**: si determina di quanto è fallita la prova e si consulta la Tabella 47.
- **Critical Fail**: l'oggetto si rompe, ma può essere riparato (vedi *Repair*, p. 197 del manuale). Gli ingredienti dell'enchantment possono comunque essere recuperati con Salvage.

### Salvaging

Il margine di fallimento determina quante materie prime si recuperano. Più i materiali sono robusti, più è probabile recuperarli. Il GM assegna penalità e bonus di conseguenza. Gli ingredienti misti e liquidi di norma non sono recuperabili.

#### Tabella 47: Salvaging

| Fallito di | Risultato |
|---|---|
| 10+ | Non resta nulla da recuperare.* |
| 3–9 | Si recupera metà delle materie prime.* |
| 1–2 | Le materie prime sono interamente recuperate. |

\*Se ne può recuperare di più con la Skill Salvage (p. 198 del manuale).

*Fonte: manuale, p. 225.*
