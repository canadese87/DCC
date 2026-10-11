# Equipaggiamento (Equipment)

## Inventory

L'Inventory del crawler si consulta tramite l'HUD. Gli oggetti sono categorizzati con le informazioni chiave. Gli oggetti nell'Inventory sono privi di peso: non esistono regole di ingombro.

- Fuori dal combattimento, un oggetto può essere prelevato dall'Inventory alla velocità del pensiero, comparendo nella mano del crawler, nella sua Hotlist o sul pavimento davanti a lui.
- Per trasferire un oggetto a un altro crawler o a un mercato, il crawler di norma lo rimuove dall'Inventory per consegnarlo. I mercati gestiscono i trasferimenti direttamente verso l'Inventory del crawler.

### Limiti dell'Inventory

| Limite | Regola |
|---|---|
| Living Creatures | Una creatura vivente messa nell'Inventory muore. I trasportini magici per animali permettono agli animali domestici di restarvi temporaneamente. |
| Too Heavy | Il crawler deve sollevare fisicamente un oggetto per 4 secondi, senza aiuto, per poterlo mettere nell'Inventory (vedi *Sollevare pesi*). |
| Loose Liquids | I liquidi vanno prima messi in un contenitore. |
| Active Volatile Items | Un esplosivo attivo (acceso, che brucia, che ticchetta o con miccia) a meno di 3 secondi dalla detonazione non può normalmente essere messo nell'Inventory. Tre secondi bastano per lanciarlo. |
| Items in Zero Zones or Outside the Dungeon | I crawler di norma non possono raccogliere e riporre oggetti nell'Inventory mentre si trovano nelle strutture di produzione degli show di intervista o al CrawlCon. Tutto ciò che possono portare in mano o indossare (e far passare dalle guardie) può essere riportato nel dungeon. |

### Sollevare pesi (Lifting Weight)

- Il limite principale all'inserimento di oggetti nell'Inventory è la capacità di sollevarli.
- Un crawler può sollevare fino al proprio punteggio di Strength × 15 in libbre (pounds).
- I crawler animali non devono nemmeno toccare gli oggetti per metterli nell'Inventory, ma hanno lo stesso massimale di sollevamento.

## Hotlist

Spell e oggetti che il crawler deve avere a portata di mano possono essere riposti nella Hotlist, una parte speciale dell'Inventory per l'accesso rapido.

- Di default la Hotlist contiene 10 slot per oggetti, Spell e qualsiasi altra cosa il crawler voglia avere a disposizione rapidamente.
- Un crawler può spendere una Action per attivare qualcosa dalla Hotlist (vedi *Azioni*).
- Se la Hotlist è piena, il crawler deve rimuovere o sostituire una voce per aggiungerne un'altra.
- Un crawler può scambiare un oggetto in mano con quello nella Hotlist come parte della Action Use a Hotlist Item.
- Se un crawler sostituisce l'arma attualmente equipaggiata con un'altra arma della Hotlist, lo scambio è gratuito come parte della Attack Action.

## Gear Slots

I crawler sono limitati nella quantità di equipaggiamento che possono indossare o da cui possono trarre beneficio. Il limite è imposto dalla suddivisione dell'equipaggiamento in Gear Slot.

- Ogni Gear Slot può contenere al massimo un capo di abbigliamento, tranne lo slot Accessories, che può contenere fino a 10 oggetti.
- Solo gli oggetti in questi slot conferiscono bonus di qualunque tipo. Gli oggetti nell'Inventory non conferiscono bonus.
- Ogni oggetto equipaggiabile specifica quale Gear Slot occupa.

!!! example "Esempio"
    Un crawler possiede quattro elmi, ciascuno con un bonus diverso. Può indossarne solo uno, e si applicano solo i suoi bonus; gli altri restano nell'Inventory.

| Gear Slot | Contenuto tipico |
|---|---|
| Head | Oggetti indossati sulla testa o sul collo, come elmi, bandane e cappelli. |
| Torso | Camicie, bluse, giacche e corazze. |
| Arms | Bracciali e gomitiere. |
| Legs | Pantaloni, jeans, gonne, kilt e boxer. |
| Feet | Scarpe, sandali, stivali e calze. |
| Hands/Holding | Si possono sia indossare guanti (o simili) sia impugnare oggetti. Un oggetto per mano e un paio di guanti. Se si porta uno Shield, questo occupa uno slot Holding. Se un'arma ha "Limitation: Two-Handed", non si può impugnare altro. |
| Accessories | Anelli, amuleti, spille, tatuaggi, patch, piercing e altri oggetti che non rientrano chiaramente in un altro slot. Cinture e mantelli sono accessori, ma un crawler può averne al massimo uno di ciascun tipo. |

## Ricchezza (Wealth)

- La ricchezza è tracciata nell'Inventory in monete d'oro (gold), che occupano tutte un solo slot dell'Inventory.
- Queste monete sono accettate quasi ovunque nel World Dungeon, anche se alcuni mercanti preferiscono barattare oggetti.

## Miscellaneous Junk (Misc. Junk)

La maggior parte degli oggetti comuni è considerata Miscellaneous Junk, reperibile quasi ovunque nel dungeon, anziché essere descritta oggetto per oggetto.

- È utile per il Crafting (vedi *Crafting*).
- Un crawler che ha bisogno di un oggetto innocuo (ad esempio una grattugia) può spendere 1 punto di Misc. Junk per trovarne uno nel proprio Inventory.
- Il Misc. Junk si vende a qualsiasi mercante a un prezzo non negoziabile di 1 gold ciascuno.
- Alcuni mercanti lo vendono a 2 gold ciascuno. Il prezzo è negoziabile solo per acquisti in grandi quantità.

## Regole specifiche per oggetti (Item Rules)

### Potions

Le pozioni sono oggetti monouso che creano un effetto magico quando vengono consumate.

- Se un crawler ha una pozione nella Hotlist, può ottenerne l'effetto senza berla fisicamente, purché sia cosciente e non impedito, non Dying o in condizioni simili. Se vuole, può anche materializzarla in mano e berla nello stesso istante.
- In combattimento, si deve spendere una Action per "bere" una pozione o per versarla in bocca a un membro del gruppo vicino.
- Le pozioni di guarigione di ogni tipo possono essere consumate anche come Interrupt.
- Fuori dal combattimento basta un momento libero per consumarla.
- Un crawler non può consumare più di una pozione ogni due round (una ogni round alterno) in combattimento. Tentare di farlo provoca Potion Sickness, che infligge il Debuff Poison (nella Tabella 11: Poisoned) e dura 15 secondi.

### Scrolls

Le scroll permettono di lanciare una Spell particolare una sola volta.

- Le Spell di una scroll hanno un Rank fisso, determinato quando la scroll viene scritta su speciale carta di lino.
- Il lanciatore non paga Mana per lanciare la Spell e non può cambiare il Rank della Spell lanciata.
- Dopo l'uso, la scroll si trasforma in polvere e non può essere riutilizzata.
- Convenzione di nome: Scroll of *Nome della Spell* (Rank X), ad esempio "Scroll of Bang Bro (Rank 3)". Usare una Scroll of Bang Bro lancia la Spell come se il crawler la lanciasse da sé.
- Le scroll sono una ricompensa comune nelle loot box. I crawler con la Skill Calligraphy possono iniziare a produrne al Fourth Floor, quando ottengono accesso agli spazi personali.

### Spellbooks

- Quando si legge uno spellbook, questo concede al lettore una singola Spell a un Rank predefinito, poi scompare e non può essere riutilizzato.
- Esempio: leggere uno spellbook di Hole concede quella Spell al crawler che lo legge.
- A seconda del libro, la Skill del crawler con la nuova Spell va tipicamente da Rank 1 a 5. Per generare casualmente il Skill Rank si tira 1d6−1, con Rank minimo 1.

### Pets e Pet Carriers

- Gli animali domestici portati nel dungeon che non assumono un Enhanced Pet Biscuit che permetta loro di funzionare come crawler affrontano gravi pericoli nel World Dungeon.
- Per le regole sugli animali domestici vedi il Capitolo 4 (sezione *Pets*).

*Fonte: manuale, p. 98–99.*
