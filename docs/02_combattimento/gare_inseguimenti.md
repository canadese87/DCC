---
tags:
  - Combattimento
  - Veicoli
  - Da verificare
  - Tabelle
---

# Gare e inseguimenti (Racing & Chasing)

Le gare e gli inseguimenti risolvono un conflitto tramite la velocità invece che con il combattimento.

- **Racing**: tutti i partecipanti cercano di raggiungere un punto fisso; conta l'ordine di arrivo.
- **Chasing**: l'obiettivo si sposta.
- Queste prove, in generale, non usano le regole delle Party Skill Check.
- Alcuni crawler possono usare veicoli, che consentono un Move molto maggiore (vedi Tabella 7 nella sezione *Veicoli*).

## Gara (Racing)

Una gara si risolve in una serie di Skill Check chiamate **legs** (tratte). Una leg può rappresentare tempo, ostacoli o diverse centinaia di giri di pista.

- La Skill per la gara, o per ciascuna leg, è di norma determinata dal tipo di movimento: Running per un inseguimento a piedi, una combinazione di Chopper Pilot e Driving per una gara di veicoli.
- Il GM può accettare una Skill diversa proposta dai giocatori (ad esempio Flying o Dive Bomb).
- La maggior parte delle gare e degli inseguimenti ha tre legs; il GM può usarne quante vuole.
- I partecipanti dedicano tutte le Action alla gara. Il GM può consentire un'altra Action al prezzo di abbandonare completamente la gara.

### Modificatori e valori

| Elemento | Regola |
|---|---|
| Move Rate Modifier | Ogni partecipante aggiunge il proprio Move ÷ 10 (arrotondato per difetto) a tutte le Skill Check di movimento della gara. Move 20 (valore predefinito) = +2; Move 45 = +4. |
| NPC Racers | NPC e Mob non tirano. In ogni leg ottengono un valore fisso: 10 + Stat Mod + Floor Number + Move Rate Modifier. |

### Svolgimento di una leg

1. Ogni partecipante effettua una Skill Check adatta alla leg e aggiunge il proprio Move Rate Modifier.
2. I risultati si confrontano dal più alto al più basso. Il risultato più alto ottiene il 1° posto, poi 2°, 3° e così via.
3. In caso di parità, vince il piazzamento chi ha il Move base più alto. Se la parità persiste, i partecipanti condividono il piazzamento.
4. Si registra il piazzamento di ogni partecipante dopo ogni leg.

### Vittoria

- Dopo l'ultima leg si sommano i piazzamenti di ogni partecipante in tutte le legs. Vince chi ha il totale più basso.
- In caso di parità sul totale più basso, vince chi ha il miglior piazzamento nell'ultima leg.
- Se la parità persiste, resta una parità.

!!! example "Esempio"
    Tre partecipanti con Move 20 (Move Mod +2), Move 30 (+3, NPC con DEX +5 su Floor 5) e Move 45 (+4). L'NPC ottiene automaticamente 10 + 5 + 5 + 3 = 23 a ogni leg. Piazzamenti: il primo partecipante 1 + 3 + 1 = 5; il terzo 3 + 1 + 2 = 6; l'NPC 2 + 2 + 3 = 7. Vince il primo partecipante (totale più basso). Nella leg 3 il primo partecipante ha speso un AI Favor per ripetere il tiro.

## Inseguimento (Chasing)

In un inseguimento chi insegue (**chaser**) cerca di raggiungere la preda (**quarry**). Il traguardo si sposta e non esiste piazzamento.

### Struttura

- Il GM stabilisce il numero di legs in base alla distanza iniziale tra la preda e gli inseguitori, alla distanza che la preda deve percorrere e alla complessità del terreno.
- Un inseguimento in un'area aperta o in un corridoio libero può avere tre legs. Un inseguimento in un bazar, su un ponte o in un circo può avere cinque o più legs.
- La Skill da usare in ogni leg è decisa dal GM. Variare le Skill richieste (Running, Jumping, Climbing, Swimming, Skill di navigazione come individuare scorciatoie, o altre) rende l'inseguimento più dinamico. Ogni leg può usare una Skill diversa.

### Risoluzione di una leg

Ogni chaser effettua una Opposed Skill Check, aggiungendo il proprio Move Rate Modifier. La preda si oppone con lo Stat Mod usato nella Skill Check (ad esempio una Skill Check di Running è contrastata dal DEX Mod della preda).

| Risultato | Ground |
|---|---|
| Amazing Success o migliore | +2 Ground. Il GM può invece concedere +1 Ground e un bonus alternativo, ad esempio la possibilità di effettuare Intervene per un alleato anche se non è un combattimento tradizionale. |
| Standard Success | +1 Ground |
| Near Miss Fail | 0 Ground |
| Standard Fail | −1 Ground |
| Major Fail | −2 Ground |
| Critical Fail | L'inseguimento termina per quel chaser (ad esempio perché ha urtato un muro o è finito in una sostanza viscosa). |

### Totale di Ground e conclusione

- Il Ground si registra come totale progressivo attraverso le legs.
- Se il totale raggiunge +4 o più in qualsiasi momento, il chaser ha raggiunto la preda in anticipo.
- Se il totale scende a −4 o meno, la preda è sfuggita e il chaser esce dall'inseguimento.
- Gli altri chaser proseguono fino all'ultima leg o finché non rimane nessun inseguitore.
- Dopo l'ultima leg, ogni chaser ancora in gioco confronta il proprio totale. Un totale positivo da 1 a 3 significa che la preda è stata raggiunta. Un totale di 0 o meno significa che la preda è fuggita.
- Per stabilire chi raggiunge la preda per primo, vince il personaggio con il totale di Ground più alto, usando il Move come spareggio. In caso di disputa decide il GM.

!!! note "Valori degli NPC"
    Gli NPC usano il valore fisso 10 + Stat Mod + Floor Number + Move Rate Modifier (vedi *Gara*). Nell'esempio del manuale la preda (Move 30, +3 Move Mod, STR +4, DEX +5, Floor 5) ottiene 22 con una Skill basata su STR e 23 con una Skill basata su DEX.

!!! warning "Da verificare"
    Manuale p. 75–76, esempio di inseguimento: (1) un chaser NPC con risultato fisso 19 contro 23 è definito "Near Miss" e ottiene 0 Ground, benché la differenza (4) rientri nello Standard Fail (3–9, −1 Ground). (2) Un chaser con 12 contro 22 (differenza 10, Major Fail, −2 Ground) perde 1 Ground. Le regole sopra riportate seguono le definizioni della tabella dei risultati; il manuale non spiega le discrepanze dell'esempio.

*Fonte: manuale, p. 73–76.*
