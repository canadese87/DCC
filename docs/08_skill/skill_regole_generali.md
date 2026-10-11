# Skill: regole generali (Skills)

Le Skill sono la base del sistema di gioco. Il crawler effettua una ==Skill Check== per compiere la maggior parte delle azioni e ottiene Upgrade aumentando il Rank delle Skill.

## Formato di una voce Skill

Ogni voce Skill segue lo stesso formato:

- **Intestazione**: il nome della Skill.
- **Parole chiave**: sotto l'intestazione sono elencate la Stat Mod che si aggiunge alla Skill Check (se presente) e le eventuali caratteristiche speciali della Skill (per esempio Passive, Interrupt, Limitations).
- **Descrizione**: spiega l'effetto della Skill. Può contenere ulteriori parole chiave, come "AI Favor" e "Limitations", che variano in base al tipo di Skill.
- **Upgrades**: i benefici ottenuti ai Rank superiori.

*Fonte: manuale, p. 173.*

## Skill Check

Le Skill Check sono **Opposed** oppure **Unopposed**, in base a ciò contro cui il crawler agisce (vedi la sezione *Skill Check*).

- **Opposed**: la Check è effettuata contro un antagonista specifico. La Difficulty tiene conto della Stat Mod dell'antagonista.
- **Unopposed**: la Check è effettuata contro elementi privi di Stat block, come oggetti o ambiente.

Procedura:

1. Tira 1d20.
2. Aggiungi il Rank nella Skill.
3. Aggiungi la Stat Mod associata.
4. Se il totale è pari o superiore alla Difficulty della Check, l'esito è almeno uno Standard Success. Se il totale supera significativamente la Difficulty, possono applicarsi effetti migliori.

Il GM stabilisce la Difficulty della Check e deve conoscere il tipo esatto di Skill Check effettuata. Non comunica la Difficulty al giocatore, ma solo l'esito.

La descrizione di una Skill riporta gli effetti di uno Standard Success. Sono possibili altri esiti oltre allo Standard Success (vedi la sezione *Degrees of Success and Failure*).

??? note "Skill Check Unopposed che diventano Opposed"
    Una Check indicata come Unopposed può, a discrezione del GM, diventare Opposed se qualcosa si oppone attivamente al crawler.

*Fonte: manuale, p. 173, 184.*

## Skill Passive (Passive Skills)

- Le Passive Skill **non richiedono una Skill Check** per ottenerne gli effetti.
- Poiché non si effettua una Skill Check, una Passive Skill non può essere segnata per una Skill Advancement Check (vedi la sezione *Skill Advancement*). Ogni voce Passive descrive come aumentarne il Rank, tipicamente tramite equipaggiamento magico e addestramento; alcune prevedono altri metodi.
- Usare una Passive Skill richiede in genere un'Action, come per ogni altro tipo di Skill. Alcune si attivano insieme ad altre Skill senza costo di Action aggiuntivo, come gli Hand-to-Hand Damage Effects.
- Una Passive Skill non può essere usata con 0 Rank (untrained).
- Il modo più semplice per ottenere Rank in una Passive Skill è una pozione, una scroll o un oggetto. Possono essere ottenute anche da alcuni benefici di Race e Class, a partire dalla Third Floor.

*Fonte: manuale, p. 173.*

## Upgrade delle Skill

Con l'aumento del Rank, le Skill concedono bonus aggiuntivi ai **Rank 5, 10 e 15**.

- Gli Upgrade delle Attack Skill aggiungono in genere dadi di danno extra al danno base dell'effetto. Questi dadi si applicano sempre, anche quando altre parti dell'Upgrade sono situazionali.
- Quando un Upgrade aumenta la gittata o la durata, rimuove una limitazione o simile, **sostituisce** l'effetto base invece di aggiungersi a esso.
- Tutti gli altri tipi di Upgrade si **sommano**. Gli Upgrade additivi usano di norma il segno più (+).

*Fonte: manuale, p. 173–174.*

## Creazione di Skill personalizzate

Il manuale fornisce uno schema per creare qualunque Skill. Una Skill o Spell contrassegnata da un asterisco di equipaggiamento (gear) è una **Custom Skill** non presente nel manuale e richiede l'uso di questo schema.

### Linee guida

- Il modo più semplice è riutilizzare una Skill esistente cambiandone solo il nome e l'ambientazione narrativa, mantenendo la stessa struttura meccanica. Esempio: *Dumpster Diving* può diventare *Search* o *Scrounging*.
- Si possono combinare effetti e Upgrade di Skill diverse. Una Skill *Crochet* può avere un Upgrade personalizzato che funziona come l'Upgrade di una Utility Skill, oppure può usare l'Upgrade al Rank 5 della Skill *Dagger*.
- Un nuovo effetto o Upgrade può essere inventato seguendo il criterio: **più è di nicchia, più può essere forte**.
- Se una Skill risulta troppo forte o troppo debole, il GM può modificarla in seguito.
- In gioco può applicarsi più di una Skill a una situazione. Poiché le Skill migliorano con l'uso, il crawler può scegliere di usare una Skill più debole o meno adatta per farle guadagnare esperienza.
- Le Skill inventate devono in genere avere un campo d'azione ristretto e **non devono sostituire o superare** le Skill esistenti né Action come Evade.
- Una Skill simile a Evade dovrebbe essere utile solo contro un certo tipo di attacco (per esempio Edged Weapons o Ranged Weapons) oppure avere uno svantaggio significativo che ne renda l'uso situazionale.
- Le Evade Check non usano i Rank. Qualunque elemento che aggiunga Rank a una Skill Check che permette di evitare un tipo di attacco risulterebbe immediatamente superiore a Evade, e non è consentito.

!!! example "Esempio: Custom Skill (Needle)"
    Il giocatore crea la Skill *Needle* (Stat: Dexterity): copre l'uso di aghi per creare oggetti o come armi, e applicazioni periferiche (passare attraverso uno spazio stretto, creare oggetti di tessuto, riparare una vela, combattere con ferri da maglia).

    | Rank | Upgrade |
    |:--:|---|
    | 5 | +1d4 base damage |
    | 10 | Scelta di un oggetto di specialità (needlework). Advantage quando si crea quell'oggetto mundane. |
    | 15 | +1d4 base damage. Gli attacchi contro la schiena di un nemico infliggono ×2 danni. |

    Il Rank 5 è l'Upgrade standard delle armi. Il Rank 15 è quello della Skill *Dagger*. Il Rank 10 è un Upgrade di Crafting.

??? example "Esempio: Custom Skill (Yarn Wrangler)"
    Skill *Yarn Wrangler* (Dexterity), basata su *Fabricate* e *Ropework*: permette di creare o recuperare filato e materiali affini e di legare bersagli.

    | Rank | Upgrade |
    |:--:|---|
    | 5 | La Skill può essere usata anche come Attack, con gittata 10 ft vs Evade del bersaglio. Con Success il bersaglio ottiene il Held Debuff. |
    | 10 | Scelta di un oggetto di specialità (yarn-craft). Advantage quando si crea quell'oggetto mundane. |
    | 15 | La gittata dell'Attack è pari al valore di Strength (minimo 15). |

    Poiché l'Upgrade del Rank 10 di *Needle* e quello di *Yarn Wrangler* si sovrappongono, il giocatore sceglie una sola delle due Skill o ne riprogetta una.

??? example "Esempio: Custom Skill orientata al combattimento (Samurai Blade Clap)"
    Skill *Samurai Blade Clap* (Dexterity): si effettua una Skill Check quando si è attaccati da un'arma Edged melee. Con Success il crawler evita i danni e gli effetti dell'attacco. Il GM la considera di utilità molto ristretta e difficile da addestrare.

    | Rank | Upgrade |
    |:--:|---|
    | 5 | La Skill è utilizzabile anche contro armi Ranged se il proiettile ha un filo (per esempio frecce o shuriken). Il proiettile può essere messo nell'Inventory come parte della stessa Action. |
    | 10 | Con Amazing Success o migliore, l'attaccante melee è disarmato. |
    | 15 | +5 DR contro le armi Edged che si tenta di bloccare. |

*Fonte: manuale, p. 174–175.*
