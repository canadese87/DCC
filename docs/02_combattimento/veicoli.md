# Veicoli (Vehicles)

## Regole generali

I veicoli sono mezzi di locomozione non autonomi. Non hanno Action: si muovono secondo la volontà del guidatore.

- Le Skill per i veicoli hanno nomi specifici. Guidare una motocicletta richiede la Skill **Chopper Pilot**. Guidare un veicolo con tre o più ruote o cingoli si chiama **Driving**. Il termine Driving è usato per entrambe le categorie.
- Il valore di Move di un veicolo corrisponde approssimativamente alle sue miglia orarie.

### Salire su un veicolo

| Situazione | Procedura |
|---|---|
| Veicolo fermo | Si usano 10 feet di Move (può essere uno Step). |
| Veicolo in movimento | Si usa una Move Action per effettuare una Stat Check di DEX con Difficulty 10 + [Move ÷ 2]. |

### Movimento e Skill Check

- Un veicolo può andare da un punto A a un punto B senza Skill Check.
- Serve una Skill Check quando si tenta una manovra spettacolare, si guida durante un combattimento o quando il fallimento ha una conseguenza.
- Il guidatore può fermarsi in qualsiasi momento. Può, ad esempio, effettuare Move, Attack, Move. Non esiste inerzia forzata: a ogni Action successiva il guidatore può mantenere lo stesso Move, rallentare o fermarsi.

**Conseguenze del fallimento.** Se il GM stabilisce che il fallimento ha conseguenze (ad esempio sfuggire a un'esplosione), si effettua una Skill Check di Driving Unopposed. Il risultato determina le prestazioni del veicolo secondo la Tabella 6.

**Mancata decelerazione.** Se il fallimento comporta l'impossibilità di fermarsi in tempo (ad esempio avvicinandosi a un dirupo, a un muro o a una strada bloccata), si effettua una Skill Check di Driving con Difficulty 10 + [Move ÷ 5].

- Success: il veicolo si ferma nel punto desiderato.
- Fail: il GM decide le conseguenze.

### Tabella 6: Risultati della Check del veicolo

| Risultato della Check | Effetto |
|---|---|
| Critical Hit | Il Move del veicolo aumenta del 50% in questo round, oppure si ottiene 1 AI Favor. |
| Amazing Success | Il veicolo dispone del Move completo in questo round. Si ottiene Advantage sulla successiva Skill Check per guidare quel veicolo. |
| Standard Success | Il veicolo dispone del Move completo in questo round. |
| Near Miss Fail | Il veicolo perde 5 feet di Move in questo round. |
| Standard Fail | Il veicolo perde metà del suo Move in questo round. |
| Major Fail | Il guidatore perde metà del proprio Move in questo round e il veicolo subisce il 10% di danno. |
| Critical Fail | Il veicolo si pianta: non può muoversi in questo round e subisce il 30% di danno. |

!!! warning "Da verificare"
    Manuale p. 72, Tabella 6: la riga Major Fail recita "You lose half of your Move" (il proprio Move), mentre le righe precedenti si riferiscono al Move del veicolo. Si tratta probabilmente del Move del veicolo, ma il testo non lo specifica.

## Uso di Skill durante il movimento

- Il guidatore effettua con Disadvantage qualsiasi Skill Check non legata alla guida, tranne l'uso di armi montate esclusive (ad esempio una lancia) o delle armi integrate nel veicolo.
- I passeggeri (chiunque non sia il guidatore) possono compiere qualsiasi Action ragionevole all'interno del veicolo senza penalità.
- Il veicolo deve terminare il proprio movimento entro la gittata di Attack di un bersaglio perché gli occupanti possano attaccarlo. Non sono possibili attacchi "al passaggio", né contro i nemici né contro gli occupanti da parte dei nemici nella situazione inversa.

## Bersagli degli attacchi

Un Attack può essere diretto a un veicolo oppure a un occupante del veicolo. I veicoli non effettuano Evade; i loro occupanti sì.

- **Attacco al veicolo**: Difficulty intrinseca 10 + [Move attuale del veicolo ÷ 5]. Se l'attacco è frontale o dal retro (head-on o trunk-on), il Move del veicolo non si include nella Difficulty.
- **Attacco a un occupante**: l'occupante può effettuare Evade con un Evade Buff pari al Move del veicolo ÷ 10, tranne per gli attacchi provenienti da direttamente davanti o dietro. Un Near Miss contro un occupante colpisce il veicolo.

## Speronamento (Ramming)

Una parte tenta di forzare una collisione; l'altra tenta di evitarla.

- Lo speronamento si risolve con una Skill Check di Driving contro l'Evade del bersaglio.
- Danno in caso di colpo: 1d6 per ogni valore di Size del veicolo e 1d6 per ogni 10 di Move (Move ÷ 10).
- Il veicolo che effettua lo speronamento subisce metà del danno e dimezza il proprio Move.
- Se il bersaglio è più grande del veicolo che effettua lo speronamento, il veicolo subisce il danno completo e il suo Move scende a 0 ft.
- Gli occupanti subiscono metà del danno subito dal proprio veicolo, ridotto dalla propria Damage Resistance (DR) e da quella del veicolo.

!!! example "Esempio"
    Un veicolo di Size 4 che si muove a Move 50 infligge 4 + 5 = 9d6 di danno al bersaglio.

## Health Bar e DR del veicolo

- Come i crawler, i veicoli hanno 10 slot di Health Bar (vedi la sezione *Salute*).
- Al posto del CON Mod, ogni slot contiene il valore di Size del veicolo (1–8).
- I veicoli hanno una DR (Tabella 7), che riduce il danno che colpisce sia gli occupanti sia il veicolo stesso.
- A 0% di Health Bar il veicolo esplode e infligge agli occupanti Xd6+F danni da Fire, dove X è la Size del veicolo e F è il numero del Floor. La DR del veicolo non protegge da questo danno.
- Si applica anche ai veicoli elettrici.

## Occupanza

- L'occupanza è il numero totale di entità (guidatore incluso) che possono stare nel veicolo.
- Il valore non cambia per piccole variazioni di Size delle entità, ma può cambiare in casi estremi.
- Le aree di carico sono all'aperto (camion) oppure in un container (autoarticolati).
- I veicoli sono tipicamente 1–2 valori di Size più grandi dei loro occupanti. Il GM può imporre complicazioni aggiuntive in caso di discrepanze estreme.

## Tabella 7: Veicoli di esempio

| Veicolo | Move | Size | DR | Occupanza |
|---|---|---|---|---|
| Skateboard | 30 | 2 | 0 | 1 |
| Bicycle | 40 | 3 | 0 | 1-2 |
| Tank | 50 | 6 | 10 | 4 |
| 18-Wheeler | 60 | 7 | 4 | 4 (+50 nel cargo) |
| Large Truck | 70 | 6 | 4 | 3 (+5 nel cargo) |
| Mid-Sized Sedan | 80 | 5 | 3 | 5–6 |
| Sportscar | 100 | 5 | 2 | 2 |
| Motorcycle | 120 | 4 | 1 | 1–2 |

!!! warning "Da verificare"
    Manuale p. 73, Tabella 7: nel testo estratto le colonne sono disallineate. Per Skateboard ("20") e Bicycle ("30") compare un solo numero, interpretato come Size 2 / DR 0 e Size 3 / DR 0. Per la Motocicletta la sequenza "4 / 1 / 1–2" è interpretata come Size 4, DR 1, occupanza 1–2. Per lo Sportscar "5 / 2 / 2" è interpretato come Size 5, DR 2, occupanza 2.

## Personalizzazione dei veicoli

Nella maggior parte delle campagne i veicoli sono un semplice mezzo di trasporto. Alcuni accessori e potenziamenti richiedono il Crafting (vedi la sezione *Crafting*); altri si acquistano già pronti. L'elenco seguente è un campione.

### Crafting di veicoli

| Tipo di potenziamento | Skill richiesta |
|---|---|
| Armor | Smithing |
| Mounted Weapons | Engineering |
| Speed Buffs | Gear Head |
| Magical Buffs | Arcane |
| Pimping Your Ride | Gear Head |

### Oggetti già pronti (Off the Shelf)

| Oggetto | Categoria | Effetto |
|---|---|---|
| Roll Cage | Armor | +1 DR |
| Nitrous Oxide | Speed Buff | Raddoppia il Move per 3 round. |
| Ram Plate | Mounted Weapon | +F danni quando si effettua Ramming. |
| Hydromancy Shock Absorbers | Magical Buff | Una volta per Floor riduce di 1 livello un Fail di una Driving Check (un Major Fail diventa Standard Fail). |
| Fuzzy Dice | Pimping Your Ride | Un reroll di una Driving Skill Check per Floor. |

*Fonte: manuale, p. 72–73.*
