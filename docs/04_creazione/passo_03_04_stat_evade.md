---
tags:
  - Creazione personaggio
  - Tabelle
---

# Passi 3–4: Stat ed Evade

## Passo 3: scelta delle Stat

Tutte le creature, crawler compresi, hanno cinque Stat. Ciascuna misura la capacità in una categoria.

| Stat | Abbreviazione | Descrizione |
|---|---|---|
| Strength | STR | Potenza fisica. Base del combattimento fisico e delle Skill basate sulla forza. |
| Intelligence | INT | Intelligenza e conoscenza. Base delle Skill che usano ingegno e saggezza. Determina il Mana disponibile per lanciare Spell. |
| Constitution | CON | Robustezza e resistenza fisica. Base delle Skill di resistenza fisica e mentale. Determina la Health. |
| Dexterity | DEX | Agilità e coordinazione. Base delle Skill che dipendono da velocità e agilità. Migliora la capacità di Evade gli attacchi. |
| Charisma | CHA | Presenza personale. Base delle Skill di persuasione e coercizione. Necessario per attrarre gli spettatori del World Dungeon. |

Ogni Stat ha un punteggio. Un Human tipico ha punteggi tra 2 e 6. Il punteggio minimo è 1.

### Metodi di determinazione

Le Stat iniziali si determinano con uno dei due metodi seguenti.

**Standard Array**: assegnare i punteggi 2, 3, 4, 5 e 6 alle cinque Stat, scegliendo liberamente. Ogni numero si usa una sola volta.

!!! example "Esempio"
    Crawler orientato all'intelletto: Strength 2, Intelligence 6, Constitution 3, Dexterity 5, Charisma 4.

**Leaving it to Chance** (tiro casuale): partendo da Strength e procedendo lungo l'elenco delle Stat (Strength, Intelligence, Constitution, Dexterity, Charisma), tirare 1d6 per ciascuna Stat, ritirando ogni 1. Il risultato è il punteggio della Stat. Non sono ammessi ripetizione dei tiri né scambi tra Stat.

### Registrazione

- Scrivere i punteggi nei campi corrispondenti della scheda.
- Scrivere lo stesso punteggio sia nel valore "Enhanced" sia nel valore "Unenhanced". Il potenziamento delle Stat è trattato più avanti nel manuale.

### Stat Mod

Ogni Stat ha un ==Stat Mod== (Mod). Il valore della Stat misura la capacità complessiva; il Mod determina l'effetto sulle Skill Check.

Lo Stat Mod si basa sul valore **Enhanced** della Stat (Tabella 20).

**Tabella 20: Stat Mods**

| Valore Stat | Stat Mod |
|---|---|
| 1–2 | +1 |
| 3–5 | +2 |
| 6–9 | +3 |
| 10–19 | +4 |
| 20–49 | +5 |
| 50–99 | +6 |
| 100–149 | +7 |
| 150–199 | +8 |
| 200–299 | +9 |
| 300+ | +10 |

Regole:

- Quando il testo usa l'abbreviazione maiuscola della Stat (ad esempio CON), si riferisce allo Stat Mod.
- Aggiornare lo Stat Mod ogni volta che il valore della Stat raggiunge un intervallo superiore.
- Lo Stat Mod si somma ai tiri di ogni Skill che usa Stat.

### Completamento della scheda

1. Completare la colonna "Stat & Mod" nella sezione "Skills", scrivendo il valore come "+X". Esempio: se una Skill usa il Charisma Modifier +2, si scrive "CHA +2".
2. Completare i valori "Stat Mod" nelle colonne "To Hit" e "Damage" della sezione "Attacks" per ogni arma. Se la Skill di arma non è ancora stata consultata nel Capitolo 4, consultarla ora: la Skill di arma indica il danno base e lo Stat Mod (se presente) da sommare.
3. Scrivere il valore dei dadi di danno nel formato "1dX" (vedi manuale p. 55 per i dadi), sostituendo X con il tipo di dado indicato nella descrizione.
4. Il tipo di danno indicato nella voce dell'arma si può scrivere nella colonna "Effects" o nel riquadro "Damage".

!!! example "Esempio"
    Unarmed Combat di un Human (manuale p. 179): colonna "Damage" "1d4 + STR", colonna "Effects" "Bludgeoning". Slice Attack di un animale (manuale p. 177): colonna "Damage" "1d4 + STR", colonna "Effects" "Slashing".

## Passo 4: determinazione dell'Evade

==Evade== è una Action usata per evitare gli attacchi. È un **Interrupt**: può essere usata anche quando non è il proprio turno di agire.

- Se non si usa l'Action Evade, i nemici infliggono danno automaticamente.
- Spendendo una Action per Evade, si può tirare separatamente contro ciascun attacco in arrivo.
- La riga "Evade" della scheda (sotto la Health Bar) serve a determinare il totale di Evade nel tiro.
- Evade non è una Skill e non ha Rank. Nella Evade Check si somma solo il DEX Mod.
- Scrivere il DEX Mod nel primo riquadro della riga Evade.

*Fonte: manuale, p. 109–111.*
