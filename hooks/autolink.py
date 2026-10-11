"""Collegamenti automatici tra le pagine della documentazione.

Per ogni pagina, la prima occorrenza di un nome di Spell, Skill, Class, Race,
divinità o Debuff viene trasformata in un link alla relativa scheda.
I file sorgente non vengono modificati: i link sono generati a ogni build.
"""

import logging
import posixpath
import re
from pathlib import Path

from markdown.extensions.toc import slugify

log = logging.getLogger("mkdocs.hooks.autolink")

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"

# (glob relativo a docs/, livello dei titoli che contengono i nomi)
SOURCES = [
    ("09_spell_loot/spell_[a-z]_*.md", 2),
    ("08_skill/utility_skill_[a-z]_*.md", 3),
    ("08_skill/attack_armi_mischia.md", 3),
    ("08_skill/attack_hand_to_hand.md", 3),
    ("08_skill/attack_distanza_reach.md", 3),
    ("06_classi/arcanist.md", 2),
    ("06_classi/barbarian.md", 2),
    ("06_classi/bard.md", 2),
    ("06_classi/cleric.md", 2),
    ("06_classi/druid.md", 2),
    ("06_classi/fighter.md", 2),
    ("06_classi/mage.md", 2),
    ("06_classi/monk.md", 2),
    ("06_classi/paladin.md", 2),
    ("06_classi/rogue.md", 2),
    ("05_razze/earth_based_*.md", 2),
    ("05_razze/alien_races.md", 2),
    ("07_divinita_avanzamento/profili_divinita.md", 2),
]

# Titoli che non sono nomi di singole voci.
SKIP_HEADING = re.compile(
    r"^(Regole|Riepilogo|Compilazione|Tabella|Class ammesse|Esplosivi)|Skills?$"
)

# Nomi troppo generici: compaiono nel testo con altri significati.
GENERIC = {
    "Heal", "Hole", "Ping", "Torch", "Web", "Fear", "Shield", "Taunt", "Catcher",
    "Human", "Cat", "Bite", "Club", "Bow", "Axe", "Toss", "Balance", "Aiming",
    "Lore", "Running", "Hide", "Salvage", "Fabricate", "Smush", "Charm",
}

# Debuff della Tabella 11 (escluse le voci troppo comuni nel testo).
DEBUFF_PAGE = "02_combattimento/buff_debuff.md"
DEBUFF_ANCHOR = "tabella-11-debuff"
DEBUFFS = [
    "Blinded", "Blood Trail", "Enraged", "Fatigued", "Paralyzed", "Poisoned",
    "Queasy", "Sepsis", "Shocked", "Staggered", "Stunned", "Terrified",
    "Woozy", "Stiff Legs", "Take Down", "The Taint", "Shit-Faced",
    "Major Injury", "Minor Injury", "Long-Term Major Injury", "Long-Term Minor Injury",
]

EXCLUDED_PAGES = {"index.md", "tags.md"}

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
TABLE_SEP = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
PROTECTED = re.compile(
    r"(`[^`]*`|!?\[[^\]]*\]\([^)]*\)|<[^>]*>|\{:[^}]*\}|\{\s*[.#][^}]*\})"
)
ID_COUNT = re.compile(r"^(.*)_([0-9]+)$")

_index = None      # nome -> (src_uri, anchor)
_regex = None


def _clean(text):
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[*_`]", "", text).strip()


def _unique(ident, used):
    while ident in used or not ident:
        m = ID_COUNT.match(ident)
        ident = "%s_%d" % (m.group(1), int(m.group(2)) + 1) if m else ident + "_1"
    used.add(ident)
    return ident


def _headings(text):
    """Restituisce (livello, testo, id) per ogni titolo, con id univoci come in mkdocs."""
    used, out, in_fence = set(), [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING.match(line)
        if m:
            title = _clean(m.group(2))
            out.append((len(m.group(1)), title, _unique(slugify(title, "-"), used)))
    return out


def _names(title):
    """Nomi (principale e alternativi) ricavabili da un titolo."""
    names = []
    main = re.split(r"\s+\(", title, maxsplit=1)[0].strip()
    names.append(main)
    if "(" in title:
        inner = title[title.index("(") + 1:title.rindex(")")] if ")" in title else ""
        for part in inner.split(","):
            part = part.strip()
            if part and part[0].isupper() and part.upper() != part:
                names.append(part)
    if "," in main:  # es. "Dwarf, Classic" -> "Dwarf Classic"
        names.append(main.replace(",", ""))
    return names


def _build_index():
    global _index, _regex
    found = {}
    for pattern, level in SOURCES:
        for path in sorted(DOCS_DIR.glob(pattern)):
            uri = path.relative_to(DOCS_DIR).as_posix()
            for lvl, title, ident in _headings(path.read_text(encoding="utf-8")):
                if lvl != level or SKIP_HEADING.search(title):
                    continue
                for name in _names(title):
                    if len(name) < 4 or name in GENERIC:
                        continue
                    found.setdefault(name, set()).add((uri, ident))
    for name in DEBUFFS:
        found.setdefault(name, set()).add((DEBUFF_PAGE, DEBUFF_ANCHOR))

    index, dropped = {}, []
    for name, targets in found.items():
        if len(targets) == 1:
            index[name] = next(iter(targets))
        else:
            dropped.append(name)
    if dropped:
        log.info("autolink: nomi ambigui ignorati: %s", ", ".join(sorted(dropped)))
    _index = index
    terms = sorted(index, key=len, reverse=True)
    _regex = re.compile(
        r"(?<![\w'’-])(?:" + "|".join(re.escape(t) for t in terms) + r")(?!\w)"
    )
    log.info("autolink: %d termini indicizzati", len(index))


def on_page_markdown(markdown, page, config, files):
    uri = page.file.src_uri
    if uri in EXCLUDED_PAGES:
        return markdown
    if _index is None:
        _build_index()

    base = posixpath.dirname(uri)
    linked = set()

    def replace(match):
        name = match.group(0)
        target, anchor = _index[name]
        if target == uri or name in linked:
            return name
        linked.add(name)
        rel = posixpath.relpath(target, base or ".")
        return "[%s](%s#%s){ .dcc-auto }" % (name, rel, anchor)

    def process(segment):
        return _regex.sub(replace, segment)

    out, in_fence = [], False
    for line in markdown.split("\n"):
        if FENCE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        stripped = line.lstrip()
        if (
            in_fence
            or stripped.startswith(("#", "!!!", "???", "*[", "---"))
            or TABLE_SEP.match(line)
        ):
            out.append(line)
            continue
        parts = PROTECTED.split(line)
        # gli indici dispari sono i segmenti protetti (separatore con gruppo di cattura)
        for i in range(0, len(parts), 2):
            parts[i] = process(parts[i])
        out.append("".join(parts))
    return "\n".join(out)
