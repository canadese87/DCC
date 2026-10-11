# Inventory del Crawler (Crawler Inventory)

## Inventory

Ogni crawler dispone di un Inventory per gli oggetti portati con sé e per quelli trovati nel dungeon. Quasi qualsiasi oggetto può essere conservato nell'Inventory.

### Aggiungere e rimuovere oggetti

- **Aggiungere**: il crawler raccoglie l'oggetto; se l'oggetto è pesante, lo mantiene in mano per circa 4 secondi, dopodiché diventa idoneo all'inserimento nell'Inventory. Gli oggetti ottenuti saccheggiando cadaveri (loot) possono essere aggiunti automaticamente all'Inventory.
- **Rimuovere o usare**: il crawler seleziona l'oggetto scorrendo l'interfaccia mentale. Per usare un oggetto è sufficiente pensarlo: l'oggetto compare.
- L'oro è registrato nell'Inventory e occupa un solo slot (vedi *Gold* in *Achievement e Loot Box*).

### Hotlist

- La Hotlist è un insieme limitato di slot in cui collocare oggetti o Spell specifici per un uso più rapido.
- Consente di evitare la ricerca nell'intero Inventory.
- I consumabili possono dover essere collocati nella Hotlist per essere utilizzabili immediatamente.

### Eccezioni per i quadrupedi (Quadruped Exceptions)

- I crawler quadrupedi o di altre Race prive della capacità fisica di raccogliere oggetti usano un'interfaccia separata per aggiungere oggetti all'Inventory.
- Il crawler si avvicina all'oggetto e il sistema indica se può essere aggiunto all'Inventory, in base a Strength e altri fattori.
- L'uso degli oggetti funziona in modo analogo: il sistema consente ai quadrupedi di usare oggetti senza tenerli fisicamente in mano, con limitazioni appropriate.

### Interface Lockout

Il sistema disabilita automaticamente Inventory, Hotlist e armi in determinate circostanze:

- in presenza di un Dungeon Admin;
- quando il crawler entra in una production trailer;
- quando il crawler viene rimosso dal dungeon per qualsiasi altro motivo (l'accesso può essere limitato).

*Fonte: manuale, p. 19–20.*
