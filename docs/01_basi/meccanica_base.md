---
tags:
  - Regole base
  - Check
  - Tabelle
---

# Meccanica base: i Check (The Core Mechanic)

Quando un crawler tenta di influire sulla situazione in cui si trova e emergono possibilità interessanti o pericolose, si effettua un **Check**.

## Procedura di un Check

1. **Determinare la sfida (Challenge)**: giocatori e GM discutono la sfida e il costo del Failure, in modo che sia chiaro a tutti cosa è in gioco.
2. **Determinare l'approccio (Stats e Skills)**: ogni giocatore sceglie narrativamente il proprio approccio; questo determina quali regole lo supportano.
    - Se il crawler possiede la Skill appropriata, la Skill determina anche quale Stat Mod si applica.
    - In alternativa si individua quale delle Five Core Stats riguarda la sfida e poi quale Skill (se presente) applica meglio quella Stat.
    - In alcuni casi la sola Stat è il modo più adatto di verificare il risultato (vedi *Stat Check*).
    - Stabilite Stat e Skill, si applicano lo Stat Mod e i Rank della Skill: modificano il tiro di d20.
3. **Applicare benefici e penalità**: oltre a Stats e Skills possono agire effetti che conferiscono benefici situazionali (**Buffs**) o penalità situazionali (**Debuffs**). Il beneficio più comune è **Advantage**, la penalità più comune è **Disadvantage**.
4. **Tirare il d20**: il giocatore tira un d20 e aggiunge il risultato ai modificatori determinati ai passi precedenti.
5. **Confrontare il totale con la Difficulty**: se il totale del Check **eguaglia o supera** la Difficulty stabilita dal GM, il crawler ha successo. Se è inferiore, fallisce.
6. **Determinare il grado di Successo o Fallimento**: oltre a Success o Failure, il crawler può riuscire con effetti positivi aggiuntivi o fallire con conseguenze durature (vedi *Gradi di Successo e Fallimento*).

## Check senza Skill Rank

Un giocatore può tentare un Check di una Skill di tipo Attack o Utility anche se il crawler non è addestrato in quella Skill, ma deve tirare con **Disadvantage**: si tirano 2d20, si usa il risultato più basso e si aggiunge lo Stat Mod appropriato. **Non si aggiungono Rank**, perché il crawler non ne possiede.

- Sulla Third Floor e sulle Floor inferiori è possibile tentare di usare le Skills senza addestramento. Questo non fa ottenere nuove Skills, a differenza delle Tutorial Floors (vedi lo Starter Set).
- Le nuove Skills si ottengono tramite: equipaggiamento con bonus a Skill; una lucky potion; visita a una Guild e pagamento per ottenere una nuova Skill a Rank 1; i benefici di Race e Class.
- **Spells**: un crawler non può tentare uno Spell senza Rank nello Spell, a meno che sia uno scroll.
- **Skills Passive**: non richiedono Skill Check, non possono essere tentate senza addestramento e non ricevono advancement marks (p. 169) con l'uso normale. Si ottengono tramite mezzi magici oppure, sulla Third Floor, tramite la scelta di Race o Class.
- Alcune Race e Class comportano svantaggi (ad esempio Hobgoblin).

## Stat Check

Un **Stat Check** si basa solo sul valore della Stat, senza una Skill. Funziona come un normale Check ma **salta il passo 2**.

Esempi di Stat Check con Difficulty indicative:

| Stat | Uso | Difficulty |
|---|---|---|
| Strength | Forzare una porta bloccata | 10 + Floor Number |
| Intelligence | Riconoscere un'illusione | 10 + Rank dello Spell di illusione |
| Constitution | Evitare gli effetti dell'alcol | 10 + Floor Number |
| Dexterity | Dondolarsi su un lampadario | 10 + Floor Number |
| Charisma | Evitare di essere ammaliati o affascinati | 10 + CHA di chi tenta di manipolare |

- Gli Stat Check possono essere usati anche per compiti normali svolti sotto pressione, quando il Failure ha conseguenze.
- **Gli altri crawler non possono aiutare con gli Stat Check.**
- Uno Stat Check è usato quando il crawler si affida solo alle Stats per resistere a un effetto dell'ambiente o dei Mobs.

## Determinare la Difficulty

La Difficulty è il numero che il crawler deve eguagliare o superare con il tiro di d20 più tutti i modificatori e i Buffs.

- La Difficulty parte da una base di **10**, modificata dal numero della **Floor** su cui si trova il crawler, poi modificata in base al fatto che il Check sia **Opposed** o **Unopposed**.
- Il GM non tira d20 contro i crawler: la Difficulty sostituisce il tiro contrapposto, per tutti gli Skill Check.
- Si determina se il Check è Opposed o Unopposed **prima** che il crawler lo effettui.
- Le formule seguenti sono indicative: il GM può assegnare una Difficulty a propria scelta se ha più senso delle formule.

### Tabella riepilogativa

| Tipo di Check | Difficulty |
|---|---|
| Opposed | 10 + Stat Mod rilevante dell'antagonista + Floor Number |
| Unopposed | 10 + (Floor Number × 2) |
| Stat Check | 10 + Floor Number |

### Opposed Check

Un Check Opposed è quello in cui qualcuno o qualcosa si oppone al crawler (un Mob, un Boss, un altro crawler, ecc.).

**Difficulty = 10 + Stat Mod rilevante dell'antagonista + Floor Number**

- Lo Stat Mod può essere sostituito da un Rank di Spell, da una size class o da qualunque forza contro cui il crawler si trova.
- Il GM non tira per "opporsi" ai tiri del crawler.
- Esempi: Check sociali per influenzare NPC e combattimento, dove una Skill del crawler è contrapposta direttamente a un antagonista.

### Unopposed Check

Un Check Unopposed non è diretto contro un antagonista ed è basato sulla profondità del crawler nel World Dungeon.

**Difficulty = 10 + (Floor Number × 2)**

- Esempi: Climbing, Dumpster-Diving, Endurance e la maggior parte delle altre Skills usate per sopravvivere nel World Dungeon.
- Se il crawler non interferisce con nessuno nel fare il Skill Check, il Check è Unopposed.

### Stat Check (Difficulty)

Poiché i crawler non aggiungono i Rank di Skill a questi Check, la Difficulty è più bassa:

**Difficulty = 10 + Floor Number**

## Party Skill Check

Quando l'intero party deve cooperare a una singola Action (ad esempio superare di nascosto un posto di guardia, scendere insieme da una scogliera), si usa un Party Skill Check:

- Ogni giocatore effettua un Skill Check per il proprio crawler e lo confronta con la Difficulty.
- Se **metà o più** dei membri del party ha successo nel proprio Skill Check individuale, il party ha successo.
- I crawler non possono aiutarsi tra loro (non si applica l'azione Help), perché eseguono tutti la Skill insieme.
- Con un **Amazing Success** o superiore, un Check fallito di un membro del party diventa un Success. Con un **Major Fail** o peggio, il Check riuscito di un altro membro diventa un Failure (vedi *Gradi di Successo e Fallimento*).

## Escalating Check

Alcune Difficulty non sono un numero singolo ma più valori crescenti (ad esempio 12, 17 e 22 invece di solo 17). Le Difficulty più basse producono comunque risultati, quelle più alte producono risultati migliori.

- Si presentano spesso nella raccolta di informazioni o nelle attività di gruppo.
- Il tiro più alto ottiene il risultato migliore; chi ha ottenuto un Success ottiene spesso qualcosa.
- Quando un singolo crawler effettua un Escalating Check, ottiene il **miglior risultato raggiunto più tutti i risultati con Difficulty inferiore**.

## Advantage e Disadvantage

Quando una regola indica di tirare con Advantage o Disadvantage, si riferisce sempre al tiro del d20 in un Check.

- **Advantage**: si tira un d20 extra e si tiene il risultato **più alto**.
- **Disadvantage**: si tira un d20 extra e si tiene il risultato **più basso**.
- Se si hanno sia Advantage sia Disadvantage, si annullano a vicenda e si tira normalmente.
- Più istanze di Advantage o di Disadvantage **non si cumulano**: si tira sempre un solo d20 extra.
- Se si hanno due fonti di Advantage e una di Disadvantage, un Advantage annulla il Disadvantage e rimane **Advantage**.

### Advantage e Disadvantage dei Mobs

Il GM non tira il d20, quindi l'effetto per i Mobs è diverso:

- **Mob con Advantage**: la Difficulty dell'Action, dell'Evade o di un'altra qualità rilevante del Mob **aumenta di 5**.
- **Mob con Disadvantage**: la Difficulty dell'Action, dell'Evade o di un'altra qualità rilevante del Mob **diminuisce di 5**.
- Nel caso di un'Attack Action, i crawler bersaglio ottengono un **Evade Check gratuito** contro l'Attacco con Disadvantage. Se falliscono questo Evade Check gratuito, il crawler può spendere un'Action per Evade e tirare di nuovo il Check (e tirare contro gli ulteriori Attacchi come di norma).

## Gradi di Successo e Fallimento (Degrees of Success & Failure)

Il Success si determina confrontando il risultato finale del tiro con la Difficulty: se è uguale o superiore c'è Success, altrimenti Failure.

- Il GM determina di quanto il risultato ha superato o mancato la Difficulty.
- Il GM annuncia il **grado** di Success o Failure ma **non** l'entità esatta, tranne per il risultato **Near Miss**.
- Un risultato uguale alla Difficulty è un "Success by 0".
- I **Critical Hit** e i **Critical Fail** non attivano anche i risultati di Success o Failure di 10 o più: il crawler ottiene solo il singolo grado più alto di Success o Failure.
- Nel combattimento i gradi di Success e Failure hanno meccaniche aggiuntive (vedi la sezione *Combattimento*, p. 79).

### Success

Raggiungere o superare la Difficulty è un Success e indica in genere un progresso verso l'obiettivo.

| Condizione | Grado | Effetto |
|---|---|---|
| Natural 20 (20 sul dado, senza modificatori) | **Critical Hit** | Si ottiene il miglior risultato possibile; il crawler esegue l'Action alla perfezione. |
| Success by 10 or more | **Amazing Success** | L'Action ha più impatto del normale: ad esempio compiere il compito più rapidamente, impressionare gli NPC vicini, usare meno materiale o effetto simile. |
| Success by 0–9 | **Standard Success** | Il risultato di Success di base. |

### Failure

Un risultato inferiore alla Difficulty o al valore obiettivo è un Failure. Il GM decide l'esito in base al grado di Failure e alla situazione.

| Condizione | Grado | Effetto |
|---|---|---|
| Fail by 1–2 | **Near Miss Fail** | Fallimento per un soffio. |
| Fail by 3–9 | **Standard Fail** | Failure normale. Per mantenere il ritmo, il GM può consentire di fallire in avanti (*fail forward*), cioè riuscire con una conseguenza. |
| Fail by 10 or more | **Major Fail** | Il Failure comporta una conseguenza, ad esempio rompere uno strumento comune, mettersi in imbarazzo o perdere troppo tempo mentre il timer di collasso della Floor si avvicina. |
| Natural 1 (1 sul dado, senza modificatori) | **Critical Fail** | Il peggior risultato possibile. Le conseguenze possono includere colpire un alleato invece di un nemico, rompere un'arma o uno strumento importante, o ottenere un Debuff. |

## Ripetere un Check (Checking Again)

Per alcune Actions fuori dal combattimento può avere senso ritentare. Quando è possibile, si considera di saltare del tutto il tiro, a meno che i tentativi aggiuntivi comportino una conseguenza interessante.

- Quando un crawler ottiene un **Major Fail** o un **Critical Fail**, **non può tentare di nuovo quella Skill nella stessa scena**.
- Con una Skill di Rank alto (circa **8–10 o superiore**) i Check riescono spesso. Il crawler può esibirsi davanti alle telecamere per aumentare la Popularity (p. 279), ottenere AI Favor o attirare l'attenzione di Sponsor (p. 284) attuali o potenziali. In questo caso il Check si tira con **Disadvantage**. Vedi *Playing to the Cameras* (p. 280).

## Fallire in avanti (Failing Forward)

Un tiro fallito non deve bloccare l'avanzamento della storia.

- Se esistono altre vie per avere Success (convincere la guardia, combattere, passare di nascosto), non c'è problema.
- Se non ci sono altre opzioni, si può far fallire in avanti: il Failure del tiro non è un Failure assoluto, ma il Success è accompagnato da complicazioni o conseguenze pesanti.

Conseguenze possibili di un cattivo tiro che non sono un Failure totale:

- una traccia che altri possono seguire;
- un oggetto viene usato o consumato;
- scoperta da parte di un Mob o altro avversario;
- perdita di AI Favor;
- perdita di Health;
- perdita di tempo.

## AI Favor

I crawler ottengono **AI Favor** compiendo azioni eroiche, azzardate, che sfidano gli showrunner o che assecondano il System AI in qualche modo.

I giocatori possono spendere AI Favor per:

- **Una volta per Check**: ritirare un d20 prima che il GM annunci il risultato, **tranne in caso di Natural 1**.
- **Una volta per round**: ottenere un'Action extra **non di Attacco** per il crawler in combattimento.

## Esempio di Check

!!! example "Esempio"
    La crawler Keisha deve risolvere un enigma di tracciati (Intelligence). Il GM chiede un Check di Investigation; Keisha non possiede la Skill. La giocatrice propone invece di usare la Skill Engineering (Rank 5). Il GM accetta e concede Advantage, perché Keisha possiede un oggetto utile (diagrammi tecnici).

    Tiro: 4 e 16. Con Advantage si tiene 16. Totale: 16 + 2 (INT) + 5 (Rank Engineering) = **23**, Success.

    Il grado di risultato modifica l'esito: Standard Success rivela il percorso più evidente; Amazing Success o superiore può rivelare ulteriori percorsi; Failure comporta perdita di tempo; Major Fail può far credere che l'unica linea utile non arriverà in tempo; Critical Fail può impedire di trovare il percorso o danneggiare l'intero programma delle linee.

    Punti illustrati: la Stat è spesso il primo elemento determinato; il giocatore può proporre una Skill alternativa narrando come si applica; se non è richiesta una Skill specifica non si applica Disadvantage per la sua assenza; il GM decide bonus e penalità (qui Advantage per l'oggetto appropriato).

*Fonte: manuale, p. 58–62.*
