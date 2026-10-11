# Tempo e Azioni (Time, Actions)

## Tempo (Time)

All'inizio di ogni Floor il System AI stabilisce il tempo che precede il **collasso della Floor**. Al collasso, l'intera Floor viene distrutta e i crawler che non sono scesi alla Floor successiva tramite una stairwell muoiono. Oltre a questa pressione narrativa, il gioco divide il tempo per i giocatori e le loro Actions.

### Tempo di gioco (Game Time)

Il gioco suddivide il tempo in segmenti narrativi:

- **Actions**: in una scena strutturata, come un combattimento, ogni crawler ha **due Actions**. Le Actions possono essere divise, consentendo ai crawler di collaborare.
- **Rounds**: in una scena strutturata un round contiene tutte le Actions, sia dei Mobs sia dei crawler. Ogni round dura **10 secondi**.
- **Scenes**: una scena può essere libera o strutturata e comprende tutte le Actions compiute in una determinata area.
    - In combattimento una scena è l'insieme di tutti i round e a volte è chiamata **encounter**.
    - Fuori dal combattimento, il tempo trascorso in un luogo (ad esempio una conversazione in una saferoom o l'attraversamento di una palude pericolosa) è una scena.

### Durata delle Floor

Il GM può personalizzare il tempo per Floor. In generale:

| Floor | Durata |
|---|---|
| Third Floor | 8 giorni |
| Fourth Floor | 10 giorni |
| Fifth Floor | 15 giorni |

Un giorno nel dungeon dura **30 ore**.

### Dungeon Floor Clock

- I crawler dispongono di un tempo limitato su ogni Floor per raggiungere la stairwell verso la Floor successiva. Se non ci riescono, vengono distrutti insieme al resto della Floor.
- Giocatori e GM non devono tenere traccia del tempo al minuto, ma in genere è importante tenere traccia di ore e giorni.
- Il tempo che precede il collasso della Floor è annunciato all'inizio di ogni Floor e ogni crawler ha accesso al timer.
- Il tempo può essere fatto scorrere o rallentare in base a quanto i giocatori vogliono trattenersi sulla Floor.

### Cooldowns

Alcune Skills e magic items hanno periodi di **cooldown** che limitano la frequenza di utilizzo. Esempi:

| Cooldown | Significato |
|---|---|
| **Once per Round** | Non si possono spendere entrambe le Actions del round in questa attività. |
| **Once per Scene** | Una volta durante uno scontro o una visita a un locale. |
| **Once per X Hours** | Le più comuni sono 1 e 5 ore. Un'ora è simile a girovagare per una città; cinque ore equivalgono a ripulire un Neighborhood dai Mobs. |
| **Once per Day** | Una volta per giorno di dungeon di 30 ore. |
| **Once per X Days** | Una volta ogni X giorni da 30 ore; si azzera al passaggio a una nuova Floor. |
| **Once per Floor** | Una volta per Floor; si azzera all'ingresso in una nuova Floor. |

*Fonte: manuale, p. 63.*

## Azioni (Actions)

Quando un crawler fa qualcosa di diverso dal parlare, compie una **Action**.

- **Fuori dal combattimento**: i crawler possono compiere Actions in qualsiasi ordine, e il GM narra il risultato di ciascuna.
- **In combattimento o in altra scena strutturata**: ogni crawler compie **due Actions per round**. I crawler possono collaborare e compiere le Actions in qualsiasi ordine per raggiungere gli obiettivi.
- I Mobs agiscono per primi, a meno che i crawler li sorprendano.
- Alcune Actions sono contrassegnate come **Interrupt** e hanno usi speciali in una scena di combattimento. Per Interrupt e fasi vedi la sezione *Combattimento* (p. 79).
- Le Actions specifiche del combattimento sono trattate a p. 81.
- Skills, oggetti e altre fonti possono conferire nuove Actions oltre a quelle di base.

### Tracciamento delle Actions

Ogni giocatore usa segnalini, monete, carte da gioco o dolciumi per tenere traccia del numero di Actions che possiede, mostrandoli a tutti i giocatori e in particolare al GM.

### Step

Ogni volta che un crawler compie una Action può anche compiere uno **Step**, che per impostazione predefinita è un movimento fino a **10 feet**. Lo Step non è una Action a sé. Vedi la sezione *Esplorazione dell'ambiente* per le regole di movimento.

### Niente Actions trattenute o attesa

- Un giocatore può attendere di usare le proprie Actions dopo che un altro crawler ha agito.
- Altrimenti, un giocatore **non può trattenere (hold) un'Action né prepararsi per il round successivo**.

### Tabella 3: Actions

| Action | Sommario |
|---|---|
| **Make a Check** | Effettuare uno Skill Check o uno Stat Check per fare ciò che si vuole nella scena. |
| **Cast a Spell** | Scegliere uno Spell o uno scroll nella Hotlist e tirare uno Spell Check se è un Attacco. Se è uno Spell non da scroll, si spende Mana per lanciarlo. |
| **Move** | Muoversi fino al valore di Move del crawler (predefinito 20 feet). |
| **Help** | Aiutare un altro crawler con il suo Skill Check non di combattimento, aggiungendo **1d2** (senza Skill Rank) o **1d6** (con Skill Rank) **prima** del tiro. |
| **Use a Hotlist Item** | Usare un oggetto consumabile preparato o predisporre un altro Hotlist Item. Per la Hotlist del crawler vedi p. 98. |
| **Retrieve** | Spostare un oggetto dall'Inventory del crawler alla Hotlist o alla mano. |

### Tabella 4: Actions specifiche del combattimento

| Action | Sommario |
|---|---|
| **Attack** | Usare una Skill, uno Spell o un altro effetto che richiede uno Skill Check di Attacco contro un bersaglio, tirando i danni in caso di Success. Estrarre o cambiare un'arma da una Hotlist è gratuito come parte di questa Action. |
| **Call a Play** | Pianificare un'Action, dando a un alleato un bonus quando la compie. |
| **Catcher** (Interrupt) | Subire un colpo per un alleato. |
| **Evade** (Interrupt) | Tentare di evitare gli Attacchi contro il proprio crawler in questo round. |
| **Heal** (tipicamente un Interrupt) | Usare uno Spell o un oggetto per curare. Può essere usata anche come Action non Interrupt dentro o fuori dal combattimento. |
| **Intervene** (Interrupt) | Aiutare un altro crawler con il suo Skill Check, aggiungendo **1d6 dopo** il suo tiro. |
| **Look for Clues** | In un incontro con un Boss, ottenere informazioni su un nemico o sull'ambiente. |
| **Taunt** (Interrupt) | Proteggere un alleato reindirizzando su di sé gli Attacchi di un Mob. |

!!! warning "Da verificare"
    Pagina 64 del manuale: le Tabelle 3 e 4 sono interlacciate nel testo estratto; le colonne "Action" e "Sommario" sono state ricostruite per ordine di lettura e corrispondenza di contenuto. Il valore di Move predefinito (20 feet, Tabella 3) e lo Step (10 feet) sono due valori distinti, riportati entrambi come nel manuale.

*Fonte: manuale, p. 64.*
