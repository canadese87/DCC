---
tags:
  - Game Master
  - Mob e Boss
  - Encounter
  - Da verificare
  - Tabelle
---

# Stat Block e scaling degli encounter

## Stat Block di Mob e Boss

Ogni Mob, Boss o altro NPC dispone di uno **Stat Block**: elenco in formato abbreviato di meccaniche, valori principali e Attack. Lo Stat Block è riservato al GM (salvo quando si vuole usare il Taunt sui giocatori). Tutti gli Stat Block seguono lo stesso formato.

### Esempio di Stat Block (Bad Llama)

```text
Bad Llama
Mob; Large (5), Mutated

Health Bar:  [2] [2] [2]
              33%  67%  100%

Level 3
Surprise 11+F     STR 3 (+2)
Evade 13+F        INT 1 (+1)
Move 20+S         CON 3 (+2)
DR 2              DEX 6 (+3)
                  CHA 1 (+1)

Lava Spit: 13+F to hit, 1d8+3 Fire, 30ft range.
  On an Evade Major Fail or worse, the target gains the Burning Debuff.

Notes: Bad Reflux - Attacks can target the lava pouch in the Llama's throat
during rounds when it uses Lava Spit, but this adds +2 to the Llama's Evade.
The pouch ruptures if such an Attack deals damage, killing the Llama and
setting its corpse aflame.
```

### Lettura dello Stat Block

| Riga | Contenuto |
|---|---|
| Top Lines | Nome, tipo e taglia (Size) della creatura. |
| Riga della Health Bar | La Health Bar (HB) della creatura: quando subisce danno, il GM può comunicare ai giocatori la percentuale di Health rimanente. Il GM la tiene su carta (numeri, calcoli o semplici caselle HB). |
| Middle Lines | Level, Surprise, Evade, Move, DR e Stat con relativi Stat Mod. Si somma il **Floor Number** attuale ai valori contrassegnati "+F". |
| Attacks | Il valore "to hit" è la Difficulty degli Evade Check dei crawler, seguito da dadi di danno, tipo di danno e gittata. Alcuni Attack hanno effetti aggiuntivi (in corsivo sotto l'Attack), spesso quando il crawler fallisce nettamente l'Evade, ma anche in altre situazioni. |
| Notes | Note speciali sulla creatura. |

Regole di lettura:

- **Surprise**: è la Difficulty degli Skill Check di Stealth e Ambush dei crawler (di fatto un Check INT-Opposed già calcolato).
- **Damage Resistance (DR)**: si sottrae da ogni valore di danno subito dalla creatura.
- **Effetti di Fail**: gli effetti di fallimento specifici dell'Attack si aggiungono alla regola del **Major Fail** ("danno aggiuntivo pari al Floor Number") e del **Critical Fail** ("danno doppio").

!!! note "Verifica del calcolo (Bad Llama)"
    Level 3: 3 punti Stat per Level = 9 punti, più base 1 in ognuna delle 5 Stat (5): totale 14. Valori presentati: STR 3 + INT 1 + CON 3 + DEX 6 + CHA 1 = 14. Surprise 11 = 10 + INT Mod (+1). Evade 13 = 10 + DEX Mod (+3). Health Bar con 3 slot (Level 3), ciascuno con CON Mod (2).

!!! warning "Da verificare"
    Il manuale non definisce il significato del suffisso "+S" nel valore di Move ("20+S"). Il testo (p. 271) indica "20+S" come Move tipico dei Mob umanoidi bipedi.

*Fonte: manuale, p. 267–268.*

## Scaling degli encounter

Il numero di Mob di partenza è determinato dal numero di membri del gruppo. La Tabella 49 fornisce il numero di Mob per ciascun livello di potenza avversaria.

### Tabella 49: Adversary Power

| Dimensione del gruppo | Weak (50%) | Moderate (100%) | Strong (150%) | Overwhelming (200%) |
|---|---|---|---|---|
| 2 | 1 | 2 | 3 | 4+ |
| 3 | 2 | 3 | 5 | 6+ |
| 4 | 2 | 4 | 6 | 8+ |
| 5 | 3 | 5 | 8 | 10+ |
| 6 | 3 | 6 | 9 | 12+ |
| 7 | 4 | 7 | 11 | 14+ |

!!! warning "Da verificare"
    Il testo estratto della tabella (p. 268) è confuso; la tabella è ricostruita sulla base delle percentuali indicate (Weak 50%, Moderate 100%, Strong 150%, Overwhelming 200%, arrotondate per eccesso) e coincide con la sequenza dei numeri leggibili nel testo (2-3-4 / 5-6-7 gruppi; Weak 1-2-2 e 3-3-4; Strong 3-5-6 e 8-9-11; Overwhelming 4+/6+/8+ e 10+/12+/14+). Il manuale non indica gruppi di 1 giocatore o di più di 7.

### Livelli di potenza

- **Weak**: utili ai margini di un Neighborhood o come complicazione per un gruppo indebolito. Il combattimento è rapido, ma può essere complicato da ambiente o trappole; può essere saltato o riassunto in un montage (come nel grinding).
- **Moderate**: combattimento tipico. I crawler non dovrebbero avere difficoltà, ma consumeranno probabilmente risorse.
- **Strong**: il gruppo dovrebbe faticare ma non essere in grave pericolo. Più i Mob superano numericamente i crawler, maggiore è il pericolo.
- **Overwhelming**: può comportare il rischio di morte dei personaggi e imporre scelte difficili; il gruppo può preferire la fuga.

La forza di un gruppo di Mob dipende in larga misura dal loro numero, perché più nemici infliggono più colpi ai PC (esempio: un gruppo Weak di Goblin è in inferiorità numerica di due a uno rispetto ai PC; un gruppo Overwhelming li supera di due a uno o più).

### Adattamenti

- I valori della tabella vanno regolati in base all'esperienza di gioco: giocatori tattici o gruppi con ottimo loot possono far sembrare Moderate un gruppo Strong.
- Il numero di Mob può essere modificato in corsa: rinforzi, un gruppo rivale di Mob, intervento di altri crawler. Un Mob può anche raccogliere l'arma di un crawler caduto e fuggire invece di ucciderlo; il gruppo può poi curarsi e recuperare l'oggetto.

*Fonte: manuale, p. 268.*
