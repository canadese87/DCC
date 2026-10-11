# Il round di combattimento (Combat Steps)

## Step 1: Mob Action Declaration

Il GM annuncia le Action dei Mob: movimento generale, Attack o altre Action che useranno e bersagli.

- **Mob di bassa qualità**: ogni Mob ha 1 Move Action e 1 altra Action per round, di solito un Attack. Di norma divide gli Attack in modo uniforme tra i crawler a portata.
- **Mob di alta qualità** (Elites e Bosses): hanno 1 Action per crawler in ogni round, salvo diversa indicazione dello Stat Block. Mantengono questo numero di Action anche se alcuni crawler sono fuori combattimento o morti.

### Scelta del bersaglio

I Mob scelgono i bersagli in base a vari fattori:

- chi percepiscono come la minaccia maggiore;
- chi è più vicino;
- quali crawler possiedono oggetti o effetti che li dissuadono o li fanno infuriare (ad esempio Mob di classe Fairy contro un crawler con un Goblin Pass);
- in modo casuale.

## Step 2: Crawler Reaction Phase

Dopo che tutti i Mob hanno annunciato movimento, Action e bersagli, i crawler possono usare Interrupt Action per reagire prima della risoluzione delle Action dei Mob.

- Le Action spese in questa fase contano contro le 2 Action che ogni crawler ha in ogni round.
- Decidere quando spendere le Action è una parte significativa della strategia.
- Quando tutti i giocatori hanno concluso le proprie Interrupt Action, si passa allo Step 3. Può essere utile una "last call" per le Action prima di chiudere la fase.

### Interrupt Action disponibili

**Evade (Interrupt)**: la Interrupt Action più comune. Il crawler tenta di evitare gli Attack diretti contro di lui.

- Il giocatore effettua una Evade Check separata contro ogni Attack diretto al proprio crawler (3 Attack = 3 Evade Check).
- La Difficulty della Evade Check è determinata dal valore di Attack del Mob.
- Un'evasione riuscita contro un Area Attack riduce il danno del 50%.
- Un Natural 20 su una Evade Check dà Advantage sulla successiva Attack Skill Check contro quel Mob; un Amazing Success ha lo stesso effetto. Un Major Fail o un Critical Fail hanno gli effetti descritti in *Combattimento: principi generali*.

!!! warning "Da verificare"
    Manuale p. 81–82: il testo rimanda a "Step 5" per i dettagli sulla Difficulty della Evade Check, ma lo Step 5 è Clean Up e non contiene questa informazione. Il manuale in queste pagine non specifica altrimenti come si calcola il "valore di Attack" del Mob.

**Intervene (Interrupt)**: l'Interrupt più flessibile. Permette a un crawler di aiutarne un altro al costo di una Action.

- Il crawler che interviene tira 1d6 e può aggiungere il risultato alla Action di un altro crawler dopo che il risultato è stato annunciato.
- Può essere usato su qualsiasi Check d20 (escluse le Stat Check), ma è più utile per trasformare un Near Miss Fail in un Success.
- Intervene può essere usato solo in combattimento ed è utilizzabile anche durante la Crawler Action Phase.

**Catcher (Interrupt)**: richiede Rank nella Skill Passiva Catcher. Permette di incassare il colpo al posto di un alleato adiacente (usando il proprio Step per portarsi in posizione se necessario). Il crawler Catcher non può effettuare Evade contro l'Attack che sta intercettando.

**Healing (Interrupt)**: versione specializzata della Action Cast a Spell o Use a Hotlist Item per attivare una Spell o un oggetto con tratto healing.

- La guarigione si applica prima che il Mob infligga il danno.
- La Healing Action può essere usata anche come Action normale durante la Crawler Action Phase, dove permette anche di effettuare una Make a Check (ad esempio First Aid).

**Taunt (Interrupt)**: il crawler effettua una Skill Check di Taunt INT-Opposed contro un Mob; il Mob è attirato ad attaccare il crawler che usa Taunt invece del bersaglio originale. Dopo aver usato Taunt, il crawler può spendere una Action per effettuare Evade contro quegli Attack e contro gli altri.

## Step 3: Mob Action Resolution

I Mob infliggono danno ai crawler che hanno fallito l'Evade o che non l'hanno tentato nello Step 2. Si applicano anche gli altri effetti dell'Attack, come i Debuff.

1. Il GM tira i dadi di danno di ogni Attack.
2. Aggiunge lo Stat Mod appropriato al totale.
3. Applica gli eventuali effetti aggiuntivi (ad esempio Debuff).
4. I crawler applicano la propria Damage Resistance (DR) al danno dell'Attack prima di segnare il danno sulla Health Bar (vedi la sezione *Salute*).

## Step 4: Crawler Action Phase

I giocatori usano le Action rimanenti dei propri crawler.

- I crawler possono usare le proprie Action in qualsiasi ordine e anche alternarle. Non esiste iniziativa.
- I crawler possono usare entrambe le Action per Attack.

### Attack

Il crawler colpisce un Mob con pugni o calci, un'arma da mischia, un'arma a distanza o una Spell. Il crawler può cambiare l'arma in mano con un'altra della propria Hotlist come parte della Attack Action.

**Scegliere un bersaglio.** Si seleziona un bersaglio entro la gittata.

- La maggior parte delle Weapon Skill da mischia ha gittata di 5 feet. Le Weapon Skill con la keyword Reach hanno gittata di 10 feet.
- Le Weapon Skill Reach non possono attaccare attraverso spazi occupati, ma possono attaccare in diagonale attraverso l'angolo tra due spazi, purché almeno uno dei due sia libero.
- I lanciatori di Spell spendono ora i propri Mana Points per attivare la Spell.
- Le Weapon Skill a distanza elencano la gittata massima; non esiste penalità per attaccare un nemico entro quella gittata.
- Le armi a distanza e le Spell che hanno come bersaglio un nemico fuori gittata falliscono automaticamente.

**Determinare i modificatori.** Giocatore e GM stabiliscono quali modifiche si applicano alla Skill Check (se presenti): benefici dei Buff, penalità dei Debuff, modificatori per la Size del bersaglio e sfide ambientali come scarsa illuminazione o copertura (vedi *Attacchi, modificatori e danno*).

**Effettuare l'Attack.** Il giocatore tira la Weapon Skill Check.

- Formula: 1d20 + Skill Rank + Stat Mod.
- Il numero bersaglio dell'Attack è l'Evade score del Mob, pari a 10 + DEX Mod + Floor.
- Gli Stat Block di alcuni Mob possono prevedere modificatori aggiuntivi.
- Dopo il tiro, il GM determina il grado di Success del crawler e l'eventuale opportunità per un alleato di usare Intervene.
- Se l'Attack colpisce, il giocatore tira il danno in base all'Attack o alla Spell.

### Cast a Spell

- Il crawler spende una Action per lanciare una Spell non di Attack, paga il costo in Mana e segue le istruzioni della Spell.
- Non esiste un limite al numero di Spell lanciabili in combattimento, purché il crawler abbia Action e Mana sufficienti.
- I tipi di caster sono limitati dalle Spell presenti nella Hotlist. Una Spell non presente nella Hotlist non può essere lanciata finché non viene recuperata con la Action Retrieve (vedi *Non-Skill Actions*).

### Make a Check

- Molte Skill non di Attack possono essere utili in combattimento: il crawler può spendere una Action per tentare la Skill durante la battaglia.
- Se il GM richiede una Skill Check non di Attack nel corso della battaglia, in genere ciò non richiede che il crawler spenda una Action per effettuarla.

!!! warning "Da verificare"
    Manuale p. 85: il testo afferma sia che il crawler può spendere una Action per tentare una Skill non di Attack, sia che una Skill Check non di Attack richiesta dal GM di norma non richiede una Action. Non è specificato quando si applica l'una o l'altra regola.

### Look for Clues

Versione specializzata della Make a Check che serve a raccogliere informazioni su un Boss (non sui normali Mob) o sull'ambiente, a vantaggio dell'intero gruppo. Si effettua come Skill Check Unopposed di Perception, Investigation o simile.

- In caso di Success, il crawler apprende un'informazione sul Boss o sull'area utile al gruppo.
- Amazing Success o migliore fornisce indizi aggiuntivi, se disponibili.
- Se vi sono più indizi possibili, il crawler può specificare su quale aspetto della scena concentrare l'Action (il Boss, l'ambiente, altre caratteristiche). Per i Boss può essere molto specifico (arma, armatura, un oggetto indossato).
- Gli indizi possono includere vulnerabilità, Resistance, Attack da cui guardarsi, l'effetto dell'uccisione del leader di un Mob, come contrastare i Debuff inflitti dai nemici, elementi ambientali utili nello scontro e altro.
- Il GM decide quale indizio fornire. Se il GM ritiene che nessun indizio sia utile, può invece concedere a ciascun crawler Advantage sul successivo Attack o Evade, a seconda di ciò che interessava di più a chi cercava.

### Healing

Oltre alle Action Use a Hotlist Item e Cast a Spell, un crawler può usare la Action Make a Check per usare la Skill First Aid o qualsiasi altro mezzo di guarigione in questa fase (vedi anche la Interrupt Action Healing).

### Non-Skill Actions

Durante un combattimento i crawler possono eseguire Action che non richiedono una Skill Check:

- **Call a Play**: un crawler propone un'Action che un alleato compirà (ad esempio attaccare un bersaglio specifico). Il crawler tira 2d6 e tiene il risultato più alto: è il Called Play bonus. Quando un altro crawler compie l'Action proposta, il crawler che ha chiamato la mossa può aggiungere il Called Play bonus al totale della Skill Check dell'alleato. Se la Skill Check riesce già senza il bonus, il Called Play bonus si aggiunge invece al tiro di danno.
- **Intervene**: durante la Crawler Action Phase un crawler può usare anche la Action Intervene (vedi Step 2).
- **Move**: il crawler può spendere una Action per percorrere fino al proprio Move e compiere uno Step, come di consueto.
- **Retrieve**: estrae un oggetto dall'Inventory portandolo in mano o sul pavimento, oppure lo aggiunge alla Hotlist. L'oggetto non può essere usato durante la Action corrente.
- **Use a Hotlist Item**: il crawler sceglie dalla Hotlist un oggetto consumabile (ad esempio una pozione o una scroll) e lo usa, oppure ne preleva un altro. Cambiare arma è gratuito come parte della Attack Action.

## Step 5: Clean Up

In questa fase giocatori e GM:

- **Applicano gli effetti di fine round**: i crawler con Buff, Debuff, la Skill Regeneration e altri effetti li applicano ora, nell'ordine per loro più vantaggioso. Tutti i contatori avanzano.
- **Determinano la fine del combattimento**: se tutti i combattenti di una delle due parti sono sconfitti, il combattimento termina. Altrimenti continua dallo Step 1.
- Tutti i combattenti azzerano il conteggio delle Action.

## Mob contro Mob (regola per il GM)

I crawler possono trovare il modo di far attaccare i Mob tra loro o contro i Boss. Il GM può semplicemente decidere l'esito.

- Se la narrazione non indica un vincitore chiaro, si confrontano direttamente Attack ed Evade (o altre Stat pertinenti) degli NPC: vince l'NPC con il valore migliore.
- Opzionalmente (i GM non tirano le Attack Skill Check), si tira 1d12 e si usa la Tabella 8. La tabella è sbilanciata verso l'NPC più potente, ma permette talvolta la vittoria dello sfavorito.
- I Mob che attaccano altri Mob e mancano consumano comunque le proprie Action.

### Tabella 8: NPC contro NPC

| Tiro (1d12) | Effetto |
|---|---|
| 1 | L'NPC attaccante perde nettamente o manca di molto, ottenendo un Major Fail. Tutti (altri Mob, Boss e crawler) ottengono Advantage per attaccarlo fino alla fine del round, oppure un Debuff a scelta del GM. |
| 2–4 | L'NPC attaccante manca o forse perde lo scontro. |
| 5–8 | L'NPC attaccante colpisce se la sua Stat pertinente è superiore alla Stat opposta del difensore. |
| 9–11 | L'NPC attaccante colpisce e infligge danno normale, o forse vince lo scontro. |
| 12 | L'NPC attaccante ottiene un Amazing Success: infligge al difensore danno con bonus pari al doppio del Floor Number, oppure un Buff simile, oppure risulta semplicemente vincitore. |

*Fonte: manuale, p. 81–86.*
