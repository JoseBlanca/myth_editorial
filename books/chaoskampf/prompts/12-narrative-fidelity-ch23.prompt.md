# Stage 12 of 19: narrative-fidelity
# Book: chaoskampf
# Generated: 2026-04-30T05:56:45Z

---

# Governing file: scope.md

```
# Scope: Chaoskampf Across Cultures

## Book type
**Cross-cultural comparison.** Unlike the other books in this project (one-culture-per-book), this book's subject is a *motif family* — the combat-with-chaos myth — traced across ~15 ancient traditions. The comparison is the point, not a capstone. The `comparative` stage of the pipeline is therefore the engine of the book rather than the final chapter.

## Subject definition
"Chaoskampf" here means: a narrative in which a sovereign or would-be sovereign deity (or heroic champion) defeats a serpentine / monstrous adversary, and that combat does one or more of the following order-making kinds of work:
1. **Cosmogonic** — the cosmos is established from or after the combat (e.g., Marduk/Tiamat, Ninurta/Asag, Gonggong).
2. **Kingship / sovereignty** — the victor's rule over gods and/or humans is established (Baal/Yamm, Zeus/Typhon, Indra/Vṛtra).
3. **Cyclical maintenance** — the combat is re-enacted, preserving an order that is always under threat (Ra/Apep, Illuyanka in the *purulli* festival).
4. **Eschatological** — the combat closes cosmic time (Thor/Jörmungandr at Ragnarök, Rev 12, Frashokereti).

This working definition is operational, not doctrinal. The book will explicitly flag that the category "Chaoskampf" is contested in current scholarship (see §"Terminological position" below).

## Terminological position
The term *Chaoskampf* was coined by Hermann Gunkel (*Schöpfung und Chaos in Urzeit und Endzeit*, 1895). It has been critiqued in successive waves, most consequentially in:
- *Creation and Chaos: A Reconsideration of Hermann Gunkel's Chaoskampf Hypothesis*, ed. JoAnn Scurlock & Richard Beal (Eisenbrauns, 2013).
- Debra Scoggins Ballentine, *The Conflict Myth and the Biblical Tradition* (OUP, 2015), who argues "chaos" is the wrong word — adversaries are better read as agents of an alternative divine power structure.

The book will include a **dedicated introductory chapter** titled provisionally "What Chaoskampf is, and why the word is contested." The term is retained because it is what readers will search for and what scholars still (if uneasily) use, but the book acknowledges the critique and adopts "combat myth" as an interchangeable term where precision matters.

## Period
- Earliest in-scope primary source: Sumerian *Lugal-e* (Ninurta vs. Asag), Old Babylonian copies of Ur III originals — c. 2000 BCE.
- Latest in-scope primary source: Zoroastrian *Bundahišn*, late Sasanian / early Islamic redaction — c. 8th–9th c. CE.
- Secondary (scholarly) literature is contemporary (1895–present).

Post-medieval reworkings (Milton's Satan, Tolkien's Smaug, etc.) are explicitly **out of scope as primary material** but may appear briefly in the concluding chapter as reception history.

## Languages of primary sources
Sumerian, Akkadian, Hurrian, Hittite, Ugaritic, Biblical Hebrew, Koine Greek, Classical Greek, Latin, Vedic Sanskrit, Classical Sanskrit, Avestan, Middle Persian (Pahlavi), Old Egyptian (and later Egyptian through Demotic), Old Norse (Eddic + skaldic), Old English, Classical Nahuatl, Quechua, Classical Chinese, Old Japanese (*man'yōgana*), Classical Armenian, Old Church Slavonic / later East Slavic, Old Irish, Middle Welsh, Old Finnish (Kalevala-era runes), and oral-tradition records in Nyanga, Soninke, Visayan/Bikol, and Mapudungun.

The book is **translation-mediated**. The author does not read most of these languages. The source-whitelist strategy (see §"Source strategy") requires two things for each language: (1) a single scholar-standard translation that will be cited first, and (2) at least one secondary-scholarship cross-check. Where a translation is disputed, the chapter will flag the variant and footnote both readings.

## In-scope catalog

**CORE (15 stories)** — full chapters, each treating the primary text(s), the combat narrative in plain-English retelling, and the scholarly debate. See `catalog.yaml` for the complete list with key scholars.

**RELATED (~30 stories)** — shorter treatments. See `catalog.yaml`. Two options for format (see DECIDE_SCOPE.md §1):
- (A) Each gets an abbreviated chapter (2–5 pages).
- (B) Grouped into "family" chapters by tradition or subtype (e.g., "Greek dragon-slayings after Zeus-Typhon"; "Indo-European reflexes of Watkins's *HERO SLAY SERPENT*"; "Mesopotamian minor combats").

**PROVISIONAL / Methodological** — Rainbow Serpent as the dedicated critique case; Yu the Great as a sidebar contrasting hydraulic-ordering with combat-ordering.

**CONTRASTIVE / Inversion** — dedicated chapters for:
- **The inversion (Bida)** — where slaying the serpent *destroys* prosperity rather than establishing it.
- **The refusal (Nanabozho / Mishipeshu)** — where area specialists explicitly reject the chaos-vs-order mapping, and the Thunderer / Underwater-manitouk dialectic is necessary rather than adversarial.

**EXCLUDED** — see `catalog.yaml` §"exclude".

## Inclusion / exclusion criteria (the operational test)
A story is in CORE if it meets **all** of:
1. The adversary is a serpentine / monstrous figure.
2. The combat is explicitly attested in a primary source (not a modern reconstruction alone).
3. The combat does cosmogonic, kingship, cyclical, or eschatological order-making work as identified by *area specialists*, not only by pattern-matching comparativists.
4. The scholarly corpus treating it is robust enough that we can cite multiple independent area-specialist readings.

A story is RELATED if it meets (1)–(2) but (3) is weaker, or if (3) holds only under a comparativist reading that area specialists qualify. Apollo/Python and Susanoo/Orochi were moved here for this reason.

A story is PROVISIONAL / CRITIQUE if area specialists explicitly reject the chaoskampf framing (Rainbow Serpent, Yu/Xiangliu), or if the combat is absent or inverted (Nanabozho, Bida handled in dedicated chapters with the right framing).

## Appropriation protocol
Given scholarly warnings about forcing Near Eastern / Indo-European templates onto non-Eurasian traditions (explicitly flagged for Rainbow Serpent, Nanabozho, Mwindo in the research notes), every RELATED chapter on a non-Eurasian tradition must:
1. Cite at least two area specialists **by name** in the first factual pass.
2. Record any specialist objection to the chaoskampf framing in an `[APPROPRIATION-FLAG:]` marker, which the `comparative` chapter must address rather than paper over.
3. Open with the tradition's own framing (*maʿat*/*isfet*, *vṛ-*/"obstruction," *wak'a* succession, etc.) before invoking the comparative category.

## Excluded adjacent motifs (contamination risks)
A cross-cultural book does not exclude neighboring *cultures* (that would defeat its purpose); it excludes *adjacent motifs* that readers and lazy comparativists conflate with chaoskampf. The book explicitly excludes:
1. **Dismemberment cosmogonies without combat** (Ymir, Puruṣa, Pangu, arguably Cipactli) — these are order-making but not combat-order-making. Cipactli is kept in RELATED precisely to mark this boundary, not ignore it.
2. **Hero-initiation monster fights** (Fionn vs. Aillen, most of Herakles's non-Hydra labours outside the serpent-combat corpus) — order-making for the hero, not for the cosmos.
3. **Inter-species enmity / folkloric monsters** (Garuḍa vs. nāgas, Welsh Afanc, Sedna) — no cosmogonic or sovereignty function.
4. **Trickster-demiurge tales without serpent-adversary** (Māui fishing the land).
5. **Storm-god theophanies without a dragon combat** (most Yoruba Ṣàngó material, Korean foundation myths).
6. **Post-medieval literary reworkings** as primary sources (see §"Period").

## Reconstruction policy
Because every chapter is a different tradition with a different textual situation, reconstruction is handled **per chapter** in the brief, not book-globally. The governing principles are:
1. **No cross-tradition reconstruction.** A gap in the *Hymiskviða* may not be filled from the *Baal Cycle*, even if structurally analogous.
2. **In-tradition reconstruction** must specify the donor source and period-proximity tolerance (e.g., "any Rigvedic hymn; never post-Vedic").
3. All reconstructions carry `[RECONSTRUCTION:]` markers naming the donor source.
4. For fragmentary cases (*Marduk vs. Labbu*, *Song of Hedammu*, some vishap material), the chapter explicitly states the fragmentary status and presents both the securely attested material and the reconstructed narrative separately.

## Variant presentation policy
- When one variant dominates a tradition's scholarly corpus (e.g., Snorri's version of the Thor fishing episode), it is presented in the body with minor variants in footnotes.
- When variants are roughly co-equal within a tradition (the two Illuyanka versions on the same tablet group; the Homeric Hymn vs. Ovidian Apollo/Python), they are presented side by side with source attributions.
- Cross-tradition comparison is never performed inline in a story-chapter; it is confined to the `comparative` material (see §"Comparative pipeline shape").

## Book structure (locked 2026-04-23)

### Part I — story chapters, geographic clusters
Part I is organised geographically, in a sequence that respects the known Near-Eastern → Mediterranean transmission chain (West, Burkert, López-Ruiz) and then moves outward. Within each cluster, CORE stories get full chapters; closely related RELATED stories are bundled into "family" chapters rather than spun out as individual mini-chapters.

Provisional geographic clusters:
1. Mesopotamia — Ninurta/Asag, Ninurta/Anzû, Marduk/Tiamat (full chapters each); family chapter on minor Mesopotamian combats (Marduk/Labbu).
2. Anatolia & Levant — Kumarbi Cycle / Ullikummi, Illuyanka, Baal/Yamm-Lotan (full chapters each).
3. Hebrew Bible & Early Christianity — Yahweh vs. Leviathan/Rahab (full); Revelation 12 Red Dragon (full); family chapter on Christian reception (St. George / Michael lineage, Ogden 2021).
4. Greece & Rome — Zeus vs. Typhon (full); family chapter "Greek dragon-combats after Zeus-Typhon" (Apollo/Python, Herakles/Hydra-Ladon-Geryon, Perseus/Ketos, Kadmos, Bellerophon, Cacus).
5. Iran — Thraētaona vs. Aži Dahāka (full); Frashokereti as its eschatological pendant.
6. India — Indra vs. Vṛtra (full); family chapter on Vedic and post-Vedic reflexes (Trita Āptya; Krishna/Kāliya as bhakti reworking).
7. Egypt — Ra vs. Apep (full); shorter treatment of Horus vs. Seth as the debated adjacent case.
8. Norse, Germanic, and IE reflexes — Thor vs. Jörmungandr (full); family chapter "Indo-European reflexes of HERO SLAY SERPENT" (Sigurd/Fáfnir, Beowulf, Lugh/Balor, Welsh Red vs. White Dragon, Batraz, Vahagn/Vishaps); family chapter on Slavic-Baltic combat (Perun/Veles reconstruction, Dobrynya byliny).
9. East Asia — Gonggong (full); family chapter on other Chinese combats (Hou Yi); Susanoo vs. Orochi (full chapter, with explicit framing that the chaoskampf label is applied from outside, per Naumann / Isomae / Como). Yu the Great appears as a sidebar contrasting hydraulic-ordering with combat-ordering, not as a chaoskampf.
10. Americas — Huitzilopochtli / Coatepec (full); family chapter on other Mesoamerican combats (Cipactli as dismemberment-boundary; Quetzalcoatl vs. Tezcatlipoca); Andean Pariacaca vs. amaru; Mapuche Kai-Kai vs. Tren-Tren.
11. Africa — Bida and the founding of Wagadu (full chapter; the inversion anchor); Mwindo vs. Kirimu (contrastive case: the hero is punished for the killing).
12. Southeast Asia & Oceania — Bakunawa. (Rainbow Serpent is held for the Part II critique chapter, not placed geographically.)
13. Finnic — Väinämöinen vs. Iku-Turso (RELATED transformed-variant chapter).
14. North America (contrastive) — Nanabozho and Mishipeshu: the refusal — the chapter where area specialists (Hallowell, Johnston, T. Smith, Vizenor) are foregrounded and the chaoskampf framing is explicitly declined.

### Part II — thematic comparative chapters
Part II is where the comparative work happens. Load-bearing (confirmed):
- **C1. Combat as cosmogony** — Marduk, Ninurta/Asag, Gonggong, Huitzilopochtli.
- **C2. Combat as sovereignty** — Baal/Yamm, Zeus/Typhon, Indra/Vṛtra, Thraētaona, Kumarbi/Ullikummi, Ninurta/Anzû.
- **C3. Cyclical maintenance** — Ra/Apep, Illuyanka.
- **C4. Eschatological displacement** — Thor/Jörmungandr, Rev 12, Frashokereti.

Recommended additional comparative chapters (confirmed at scope-lock):
- **C5. The Indo-European HERO SLAY SERPENT formula** — Watkins's argument from Indra through Sigurd to Beowulf.
- **C6. The Near Eastern → Mediterranean transmission** — West / Burkert / López-Ruiz: Kumarbi → Hesiod; Baal/Yamm → Typhonomachy.
- **C7. The inversion problem** — Bida anchor; the ambiguous status of Sigurd's slaying.
- **C8. The refusal and the appropriation problem** — Nanabozho, Mwindo, Rainbow Serpent, and how not to flatten traditions into chaoskampf.

### Front matter, back matter, and appendices
- **Pre-chapter (00A-introduction)**: "What Chaoskampf is, and why the word is contested." Front-loaded framing of the category, Gunkel's 1895 thesis, the 20th/21st-century critiques (Scurlock & Beal, Ballentine), and the book's operational definition (§"Subject definition").
- **Methods sidebar** between Part I and Part II: tier-ranking method, appropriation protocol, area-specialist citation policy.
- **Reception coda** (final chapter, ~20–25 pages): traces the afterlife of the imagery in Milton's Satan, Christian iconography of St. Michael / St. George, Tolkien's dragons (and the 1936 Beowulf essay), modern kaiju (Godzilla and the Orochi lineage), and the continuing use of "chaos vs. order" rhetoric in contemporary religious interpretation. Explicitly *not* classified as chaoskampf; this is reception, not primary material.
- **Adversaries + champions appendix** (replaces the single-culture "character appendix"): one entry per monster (Tiamat, Yamm, Lôtan, Leviathan, Rahab, Vṛtra, Aži Dahāka, Apep, Jörmungandr, Typhon, Illuyanka, Ullikummi, Hedammu, the Red Dragon, Coyolxauhqui, etc.) plus one entry per champion. This is load-bearing because the cross-cultural comparisons happen across *figures*, not plots.
- **Bibliography**: preliminary estimate 150–250 entries.

### Terminology default (locked)
Headings and catalog use "Chaoskampf" (reader expectation, search-term coverage). Body prose uses "combat myth" as the default, reserving "Chaoskampf" for quotations, discussions of Gunkel's term, and the Part I and Part II passages where the specificity matters. This lets the book engage the Ballentine critique substantively rather than tokenistically.

### Deferred decisions
- Spanish edition (deferred at scope-lock; no effect on Part I/II work, but glossary-lock will need to re-check if/when this is decided).
- Cover image (deferred; decide before `format-finalize`).

## Book register
Asimov-style retelling. Narrative prose in the body. Citations in AsciiDoc footnotes. Inferences, lacunae, reconstructions, appropriation warnings, and variants flagged inline with explicit markers. Plain-English register — no unexplained technical terms on first use; every ancient-language term glossed at first occurrence and collected in the glossary.

## Meta
- Book slug: `chaoskampf`
- Version: scope v1 — draft of 2026-04-23
- Author: Jose Blanca
- Open questions before scope-lock closes: see `DECIDE_SCOPE.md`
```

---

# Governing file: sources.yaml

```
# Source registry for the Chaoskampf book.
# This file is a SEED: the comparative-scholarship backbone + the anchor critical edition for each CORE story.
# Per-story additional sources (more translations, specialist monographs, journal articles) will accrue at chapter-briefs time.
# All entries below are drawn from the research notes in books/chaoskampf/research/ — no guessed citations.

meta:
  stage: scope-lock
  version: v1-seed
  date: 2026-04-23
  note: "Seeded from DECISION_REPORT + the seven research notes. Additional per-story sources will be added at chapter-briefs."

registry:
  # ── Digital primary corpora ─────────────────────────────────────────

  - id: etcsl
    source_tier: primary-translation
    in_scope: true
    author: "Black, Jeremy; Cunningham, Graham; Flückiger-Hawker, Esther; Robson, Eleanor; Zólyomi, Gábor"
    title: "The Electronic Text Corpus of Sumerian Literature"
    year: 1998
    full_citation: "Black, J.A., Cunningham, G., Flückiger-Hawker, E., Robson, E., and Zólyomi, G., *The Electronic Text Corpus of Sumerian Literature* (https://etcsl.orinst.ox.ac.uk/), Oxford, 1998–2006."
    short_citation: "ETCSL"
    identifier_type: stable-url
    identifier_value: "https://etcsl.orinst.ox.ac.uk/"
    access_url: "https://etcsl.orinst.ox.ac.uk/"
    notes: "Standard digital corpus of transliterated and translated Sumerian literary texts. Primary reference for Ninurta/Asag (Lugal-e, ETCSL 1.6.2) and the Sumerian background of Ninurta/Anzû."

  # ── Comparative / theoretical spine ─────────────────────────────────

  - id: gunkel-1895
    source_tier: secondary
    in_scope: true
    author: "Gunkel, Hermann"
    title: "Schöpfung und Chaos in Urzeit und Endzeit"
    year: 1895
    full_citation: "Gunkel, H., *Schöpfung und Chaos in Urzeit und Endzeit: Eine religionsgeschichtliche Untersuchung über Gen 1 und Ap Joh 12* (Göttingen: Vandenhoeck & Ruprecht, 1895)."
    short_citation: "Gunkel 1895"
    identifier_type: stable-url
    identifier_value: "https://archive.org/details/schpfungundchao00gunkgoog"
    notes: "Coined the term Chaoskampf. Retain as historical anchor even where later scholarship has superseded the framing."

  - id: fontenrose-1959
    source_tier: secondary
    in_scope: true
    author: "Fontenrose, Joseph"
    title: "Python: A Study of Delphic Myth and Its Origins"
    year: 1959
    full_citation: "Fontenrose, J., *Python: A Study of Delphic Myth and Its Origins* (Berkeley: University of California Press, 1959)."
    short_citation: "Fontenrose 1959"
    identifier_type: ISBN
    identifier_value: "9780520040915"
    notes: "Foundational comparative treatment of dragon-combat, including the Apollo/Python cult-foundation argument."

  - id: wakeman-1973
    source_tier: secondary
    in_scope: true
    author: "Wakeman, Mary K."
    title: "God's Battle with the Monster: A Study in Biblical Imagery"
    year: 1973
    full_citation: "Wakeman, M.K., *God's Battle with the Monster: A Study in Biblical Imagery* (Leiden: Brill, 1973)."
    short_citation: "Wakeman 1973"
    identifier_type: ISBN
    identifier_value: "9789004037526"
    notes: "Core comparative treatment linking Mesopotamian combat-myth to Hebrew Bible imagery."

  - id: day-1985
    source_tier: secondary
    in_scope: true
    author: "Day, John"
    title: "God's Conflict with the Dragon and the Sea: Echoes of a Canaanite Myth in the Old Testament"
    year: 1985
    full_citation: "Day, J., *God's Conflict with the Dragon and the Sea: Echoes of a Canaanite Myth in the Old Testament* (Cambridge: Cambridge University Press, 1985)."
    short_citation: "Day 1985"
    identifier_type: ISBN
    identifier_value: "9781532692659"
    notes: "Canonical monograph on the Leviathan/Rahab corpus and its Ugaritic background."

  - id: forsyth-1987
    source_tier: secondary
    in_scope: true
    author: "Forsyth, Neil"
    title: "The Old Enemy: Satan and the Combat Myth"
    year: 1987
    full_citation: "Forsyth, N., *The Old Enemy: Satan and the Combat Myth* (Princeton: Princeton University Press, 1987)."
    short_citation: "Forsyth 1987"
    identifier_type: ISBN
    identifier_value: "9780691014746"
    notes: "Traces the combat myth from Sumer through Judeo-Christian apocalyptic. Full catalog-level treatment."

  - id: burkert-1992
    source_tier: secondary
    in_scope: true
    author: "Burkert, Walter"
    title: "The Orientalizing Revolution: Near Eastern Influence on Greek Culture in the Early Archaic Age"
    year: 1992
    full_citation: "Burkert, W., *The Orientalizing Revolution: Near Eastern Influence on Greek Culture in the Early Archaic Age*, trans. M.E. Pinder and W. Burkert (Cambridge, MA: Harvard University Press, 1992)."
    short_citation: "Burkert 1992"
    identifier_type: ISBN
    identifier_value: "9780674643642"
    notes: "Key for the Near-Eastern-to-Greek transmission of combat myth."

  - id: watkins-1995
    source_tier: secondary
    in_scope: true
    author: "Watkins, Calvert"
    title: "How to Kill a Dragon: Aspects of Indo-European Poetics"
    year: 1995
    full_citation: "Watkins, C., *How to Kill a Dragon: Aspects of Indo-European Poetics* (New York: Oxford University Press, 1995)."
    short_citation: "Watkins 1995"
    identifier_type: ISBN
    identifier_value: "9780195085952"
    notes: "The 'HERO SLAY SERPENT' formula. Anchor for all IE entries (Indra, Thraētaona, Illuyanka, Thor, Sigurd, Beowulf, Zeus)."

  - id: tolkien-1936-monsters
    source_tier: secondary
    in_scope: true
    author: "Tolkien, J.R.R."
    title: "Beowulf: The Monsters and the Critics"
    year: 1936
    container_title: "Proceedings of the British Academy"
    full_citation: "Tolkien, J.R.R., 'Beowulf: The Monsters and the Critics', *Proceedings of the British Academy* 22 (1936): 245–295; reprinted in *The Monsters and the Critics and Other Essays*, ed. Christopher Tolkien (London: George Allen & Unwin, 1983): 5–48."
    short_citation: "Tolkien 1936"
    identifier_type: stable-url
    identifier_value: "https://www.britac.ac.uk/pubs/proc/files/22p245.pdf"
    notes: "British Academy lecture (delivered 25 November 1936); the load-bearing critical move that re-established the mythic register of the *Beowulf* monsters within twentieth-century Old English scholarship. Cited in Ch19 (Beowulf sub-section); literary-critical afterlife deferred to Ch42 (reception coda)."

  - id: west-1997
    source_tier: secondary
    in_scope: true
    author: "West, M.L."
    title: "The East Face of Helicon: West Asiatic Elements in Greek Poetry and Myth"
    year: 1997
    full_citation: "West, M.L., *The East Face of Helicon: West Asiatic Elements in Greek Poetry and Myth* (Oxford: Clarendon Press, 1997)."
    short_citation: "West 1997"
    identifier_type: ISBN
    identifier_value: "9780198150428"
    notes: "Greek-Near Eastern interface. Central for Zeus-Typhon, Kumarbi-Ullikummi."

  - id: west-2007
    source_tier: secondary
    in_scope: true
    author: "West, M.L."
    title: "Indo-European Poetry and Myth"
    year: 2007
    full_citation: "West, M.L., *Indo-European Poetry and Myth* (Oxford: Oxford University Press, 2007)."
    short_citation: "West 2007"
    identifier_type: ISBN
    identifier_value: "9780199280759"
    notes: "Comparative IE. Chapter 6 ('Storm and Stream') places Thor with the IE storm-god/water-dragon complex."

  - id: scurlock-beal-2013
    source_tier: secondary
    in_scope: true
    author: "Scurlock, JoAnn; Beal, Richard (eds.)"
    title: "Creation and Chaos: A Reconsideration of Hermann Gunkel's Chaoskampf Hypothesis"
    year: 2013
    full_citation: "Scurlock, J. and Beal, R. (eds.), *Creation and Chaos: A Reconsideration of Hermann Gunkel's Chaoskampf Hypothesis* (Winona Lake: Eisenbrauns, 2013)."
    short_citation: "Scurlock & Beal 2013"
    identifier_type: ISBN
    identifier_value: "9781575062792"
    notes: "Direct reassessment of Gunkel. Essential for the book's terminological framing."

  - id: ogden-2013
    source_tier: secondary
    in_scope: true
    author: "Ogden, Daniel"
    title: "Drakōn: Dragon Myth and Serpent Cult in the Greek and Roman Worlds"
    year: 2013
    full_citation: "Ogden, D., *Drakōn: Dragon Myth and Serpent Cult in the Greek and Roman Worlds* (Oxford: Oxford University Press, 2013)."
    short_citation: "Ogden 2013"
    identifier_type: ISBN
    identifier_value: "9780199557325"
    notes: "Current Greek/Roman survey. Classifies drakontes and their adversaries."

  - id: ballentine-2015
    source_tier: secondary
    in_scope: true
    author: "Ballentine, Debra Scoggins"
    title: "The Conflict Myth and the Biblical Tradition"
    year: 2015
    full_citation: "Ballentine, D.S., *The Conflict Myth and the Biblical Tradition* (New York: Oxford University Press, 2015)."
    short_citation: "Ballentine 2015"
    identifier_type: ISBN
    identifier_value: "9780199370252"
    notes: "Argues 'chaos' is the wrong word. Central dissenting position the book must engage."

  - id: lincoln-2012
    source_tier: secondary
    in_scope: true
    author: "Lincoln, Bruce"
    title: "Gods and Demons, Priests and Scholars: Critical Explorations in the History of Religions"
    year: 2012
    full_citation: "Lincoln, B., *Gods and Demons, Priests and Scholars: Critical Explorations in the History of Religions* (Chicago: University of Chicago Press, 2012)."
    short_citation: "Lincoln 2012"
    identifier_type: ISBN
    identifier_value: "9780226481876"
    notes: "Treats combat myths as political-ideological."

  - id: witzel-2012
    source_tier: comparative
    in_scope: true
    author: "Witzel, Michael"
    title: "The Origins of the World's Mythologies"
    year: 2012
    full_citation: "Witzel, M., *The Origins of the World's Mythologies* (New York: Oxford University Press, 2012)."
    short_citation: "Witzel 2012"
    identifier_type: ISBN
    identifier_value: "9780199812851"
    notes: "Use with caution — the 'Laurasian' macro-scheme is controversial. Cited where it engages specific stories, not as framework."

  # ── Critical-edition anchor per CORE story ──────────────────────────

  - id: vandijk-1983-lugale
    source_tier: primary-translation
    in_scope: true
    author: "van Dijk, J.J.A."
    title: "LUGAL UD ME-LÁM-bi NIR-ĜÁL: Le récit épique et didactique des Travaux de Ninurta, du Déluge et de la Nouvelle Création"
    year: 1983
    full_citation: "van Dijk, J.J.A., *LUGAL UD ME-LÁM-bi NIR-ĜÁL: Le récit épique et didactique des Travaux de Ninurta, du Déluge et de la Nouvelle Création*, 2 vols. (Leiden: Brill, 1983)."
    short_citation: "van Dijk 1983"
    identifier_type: ISBN
    identifier_value: "9789004069169"
    notes: "Standard critical edition of Lugal-e. Anchor for the Ninurta/Asag chapter."

  - id: annus-2001-anzu
    source_tier: primary-translation
    in_scope: true
    author: "Annus, Amar"
    title: "The Standard Babylonian Epic of Anzu: Introduction, Cuneiform Text, Transliteration, Score, Glossary, Indices and Sign List"
    year: 2001
    full_citation: "Annus, A., *The Standard Babylonian Epic of Anzu* (State Archives of Assyria Cuneiform Texts 3, Helsinki: Neo-Assyrian Text Corpus Project, 2001)."
    short_citation: "Annus 2001"
    identifier_type: ISBN
    identifier_value: "9789514590511"
    notes: "Anchor for Ninurta/Anzû. Verify format before final citation — SAACT series numbering."

  - id: lambert-2013
    source_tier: primary-translation
    in_scope: true
    author: "Lambert, W.G."
    title: "Babylonian Creation Myths"
    year: 2013
    full_citation: "Lambert, W.G., *Babylonian Creation Myths*, Mesopotamian Civilizations 16 (Winona Lake: Eisenbrauns, 2013)."
    short_citation: "Lambert 2013"
    identifier_type: ISBN
    identifier_value: "9781575062471"
    notes: "Definitive critical edition of Enūma Eliš and related material. Anchor for Marduk/Tiamat."

  - id: foster-2005
    source_tier: primary-translation
    in_scope: true
    author: "Foster, Benjamin R."
    title: "Before the Muses: An Anthology of Akkadian Literature"
    year: 2005
    full_citation: "Foster, B.R., *Before the Muses: An Anthology of Akkadian Literature*, 3rd ed. (Bethesda: CDL Press, 2005)."
    short_citation: "Foster 2005"
    identifier_type: ISBN
    identifier_value: "9781883053765"
    notes: "Standard English anthology. Used for Enūma Eliš, Anzu, Atrahasis, Labbu."

  - id: hoffner-1998
    source_tier: primary-translation
    in_scope: true
    author: "Hoffner, Harry A. Jr."
    title: "Hittite Myths"
    year: 1998
    full_citation: "Hoffner, H.A., *Hittite Myths*, 2nd ed., SBL Writings from the Ancient World 2 (Atlanta: Society of Biblical Literature, 1998)."
    short_citation: "Hoffner 1998"
    identifier_type: ISBN
    identifier_value: "9780788504884"
    notes: "Anchor for Illuyanka and the Kumarbi Cycle (Song of Ullikummi, Song of Hedammu, Kingship in Heaven)."

  - id: beckman-1982-illuyanka
    source_tier: secondary
    in_scope: true
    author: "Beckman, Gary"
    title: "The Anatolian Myth of Illuyanka"
    year: 1982
    container_title: "Journal of the Ancient Near Eastern Society"
    full_citation: "Beckman, G., 'The Anatolian Myth of Illuyanka', *Journal of the Ancient Near Eastern Society* 14 (1982): 11–25."
    short_citation: "Beckman 1982"
    identifier_type: stable-url
    identifier_value: "https://janes.scholasticahq.com/"
    notes: "Standard philological edition and translation of Illuyanka."

  - id: smith-1994-baal-i
    source_tier: primary-translation
    in_scope: true
    author: "Smith, Mark S."
    title: "The Ugaritic Baal Cycle, Volume I: Introduction with Text, Translation and Commentary of KTU 1.1–1.2"
    year: 1994
    full_citation: "Smith, M.S., *The Ugaritic Baal Cycle, Volume I: Introduction with Text, Translation and Commentary of KTU 1.1–1.2* (Leiden: Brill, 1994)."
    short_citation: "Smith 1994"
    identifier_type: ISBN
    identifier_value: "9789004099951"
    notes: "Baal-Yamm arc. Anchor for the Baal chapter."

  - id: smith-pitard-2009-baal-ii
    source_tier: primary-translation
    in_scope: true
    author: "Smith, Mark S.; Pitard, Wayne T."
    title: "The Ugaritic Baal Cycle, Volume II: Introduction with Text, Translation and Commentary of KTU/CAT 1.3–1.4"
    year: 2009
    full_citation: "Smith, M.S. and Pitard, W.T., *The Ugaritic Baal Cycle, Volume II: Introduction with Text, Translation and Commentary of KTU/CAT 1.3–1.4* (Leiden: Brill, 2009)."
    short_citation: "Smith & Pitard 2009"
    identifier_type: ISBN
    identifier_value: "9789004153486"
    notes: "Palace-building cycle. Second half of the Baal anchor."

  - id: west-1966-theogony
    source_tier: primary-translation
    in_scope: true
    author: "West, M.L. (ed.)"
    title: "Hesiod: Theogony"
    year: 1966
    full_citation: "West, M.L. (ed.), *Hesiod: Theogony* (Oxford: Clarendon Press, 1966)."
    short_citation: "West 1966"
    identifier_type: ISBN
    identifier_value: "9780198141693"
    notes: "Critical edition with commentary. Anchor for Zeus/Typhon."

  - id: jamison-brereton-2014
    source_tier: primary-translation
    in_scope: true
    author: "Jamison, Stephanie; Brereton, Joel"
    title: "The Rigveda: The Earliest Religious Poetry of India"
    year: 2014
    full_citation: "Jamison, S.W. and Brereton, J.P., *The Rigveda: The Earliest Religious Poetry of India*, 3 vols. (New York: Oxford University Press, 2014)."
    short_citation: "Jamison & Brereton 2014"
    identifier_type: ISBN
    identifier_value: "9780199370184"
    notes: "Current scholarly-standard English Rigveda. Anchor for Indra/Vṛtra and Trita Āptya."

  - id: tagare-bhagavata
    source_tier: primary-translation
    in_scope: true
    author: "Tagare, Ganesh Vasudeo"
    title: "The Bhāgavata Purāṇa, Translated and Annotated"
    year: 1976-1979
    full_citation: "Tagare, G.V., *The Bhāgavata Purāṇa, Translated and Annotated*, 5 vols., Ancient Indian Tradition and Mythology series 7–11 (Delhi: Motilal Banarsidass, 1976–1978)."
    short_citation: "Tagare 1976–78"
    identifier_type: series
    identifier_value: "Ancient Indian Tradition and Mythology 7–11"
    notes: "Standard scholarly English translation of the Bhāgavata Purāṇa. Anchor for the Krishna-Kāliya episode (book 10 chs. 15–17) in Ch15."

  - id: benveniste-renou-1934
    source_tier: secondary
    in_scope: true
    author: "Benveniste, Émile; Renou, Louis"
    title: "Vṛtra et Vṛθragna: Étude de mythologie indo-iranienne"
    year: 1934
    full_citation: "Benveniste, É. and Renou, L., *Vṛtra et Vṛθragna: Étude de mythologie indo-iranienne*, Cahiers de la Société Asiatique 3 (Paris: Imprimerie Nationale, 1934)."
    short_citation: "Benveniste & Renou 1934"
    identifier_type: stable-url
    identifier_value: "https://gallica.bnf.fr/"
    notes: "Foundational Indo-Iranian comparative study. Essential for Indra/Vṛtra and Thraētaona/Aži Dahāka."

  - id: faulkner-1972-bod
    source_tier: primary-translation
    in_scope: true
    author: "Faulkner, Raymond O."
    title: "The Ancient Egyptian Book of the Dead"
    year: 1972
    full_citation: "Faulkner, R.O., *The Ancient Egyptian Book of the Dead*, rev. ed., ed. Carol Andrews (London: British Museum, 1985; orig. 1972)."
    short_citation: "Faulkner 1972 (rev. 1985)"
    identifier_type: ISBN
    identifier_value: "9780292704251"
    notes: "Standard English Book of the Dead including Apep-slaying spells."

  - id: faulkner-1936-bremner-rhind
    source_tier: primary-translation
    in_scope: true
    author: "Faulkner, Raymond O."
    title: "The Bremner-Rhind Papyrus I–IV"
    year: 1936
    full_citation: "Faulkner, R.O., 'The Bremner-Rhind Papyrus I–IV', *Journal of Egyptian Archaeology* 22 (1936): 121–140; 23 (1937): 10–16, 166–185; 24 (1938): 41–53."
    short_citation: "Faulkner 1936–38 (JEA 22–24)"
    identifier_type: jstor-collection
    identifier_value: "JEA 22, 23, 24"
    notes: "Faulkner's four-part philological edition of Papyrus BM EA 10188 (Bremner-Rhind) — the *Book of Overthrowing Apep* — published as articles in JEA across 1936–38. Distinct from Faulkner's 1972 Book of the Dead translation. Anchor for Ch16 ritual-embedding section."

  - id: te-velde-1967
    source_tier: secondary
    in_scope: true
    author: "te Velde, Herman"
    title: "Seth, God of Confusion: A Study of His Role in Egyptian Mythology and Religion"
    year: 1967
    full_citation: "te Velde, H., *Seth, God of Confusion: A Study of His Role in Egyptian Mythology and Religion*, 2nd ed. (Leiden: Brill, 1977; orig. 1967)."
    short_citation: "te Velde 1967"
    identifier_type: ISBN
    identifier_value: "9789004054028"
    notes: "Core study of Seth as Apep-slayer and as ambivalent figure. Anchors both Ra/Apep and Horus/Seth."

  - id: assmann-2001-search
    source_tier: secondary
    in_scope: true
    author: "Assmann, Jan"
    title: "The Search for God in Ancient Egypt"
    year: 2001
    full_citation: "Assmann, J., *The Search for God in Ancient Egypt*, trans. David Lorton (Ithaca: Cornell University Press, 2001)."
    short_citation: "Assmann 2001"
    identifier_type: ISBN
    identifier_value: "9780801487293"
    notes: "maʿat vs. isfet framework. Central to Ra/Apep chapter."

  - id: yarbro-collins-1976
    source_tier: secondary
    in_scope: true
    author: "Yarbro Collins, Adela"
    title: "The Combat Myth in the Book of Revelation"
    year: 1976
    full_citation: "Yarbro Collins, A., *The Combat Myth in the Book of Revelation*, Harvard Dissertations in Religion 9 (Missoula: Scholars Press, 1976)."
    short_citation: "Yarbro Collins 1976"
    identifier_type: ISBN
    identifier_value: "9780891300571"
    notes: "Central study of Rev 12. Traces the NT eschatologisation of the Hebrew Bible combat tradition."

  - id: aune-revelation
    source_tier: secondary
    in_scope: true
    author: "Aune, David E."
    title: "Revelation"
    year: 1997
    full_citation: "Aune, D.E., *Revelation*, Word Biblical Commentary 52A–C, 3 vols. (Dallas: Word Books / Nashville: Nelson, 1997–1998)."
    short_citation: "Aune 1997–98"
    identifier_type: ISBN
    identifier_value: "9780849902512"
    notes: "Standard historical-critical commentary including the Rev 12 dragon passage."

  - id: larrington-poetic-edda
    source_tier: primary-translation
    in_scope: true
    author: "Larrington, Carolyne"
    title: "The Poetic Edda"
    year: 2014
    full_citation: "Larrington, C. (trans.), *The Poetic Edda*, rev. ed. (Oxford: Oxford University Press, 2014)."
    short_citation: "Larrington 2014"
    identifier_type: ISBN
    identifier_value: "9780199675340"
    notes: "Working translation. For philological anchor use Dronke or Neckel/Kuhn as cross-check."

  - id: faulkes-snorri
    source_tier: primary-translation
    in_scope: true
    author: "Faulkes, Anthony (ed. and trans.)"
    title: "Edda (by Snorri Sturluson)"
    year: 1987
    full_citation: "Sturluson, S., *Edda*, trans. A. Faulkes (London: Dent / Everyman, 1987; Viking Society for Northern Research ed. 2005)."
    short_citation: "Faulkes 1987"
    identifier_type: ISBN
    identifier_value: "9780460876162"
    notes: "Standard English Prose Edda. Anchor for Thor/Jörmungandr."

  - id: lewis-2006-flood
    source_tier: secondary
    in_scope: true
    author: "Lewis, Mark Edward"
    title: "The Flood Myths of Early China"
    year: 2006
    full_citation: "Lewis, M.E., *The Flood Myths of Early China* (Albany: SUNY Press, 2006)."
    short_citation: "Lewis 2006"
    identifier_type: ISBN
    identifier_value: "9780791466636"
    notes: "Anchor for Gonggong and the Yu-sidebar."

  - id: birrell-1993
    source_tier: secondary
    in_scope: true
    author: "Birrell, Anne"
    title: "Chinese Mythology: An Introduction"
    year: 1993
    full_citation: "Birrell, A., *Chinese Mythology: An Introduction* (Baltimore: Johns Hopkins University Press, 1993)."
    short_citation: "Birrell 1993"
    identifier_type: ISBN
    identifier_value: "9780801849954"
    notes: "General Chinese reference — use with Lewis and Mathieu for triangulation."

  - id: matos-moctezuma-templo-mayor
    source_tier: secondary
    in_scope: true
    author: "Matos Moctezuma, Eduardo"
    title: "The Great Temple of the Aztecs: Treasures of Tenochtitlan"
    year: 1988
    full_citation: "Matos Moctezuma, E., *The Great Temple of the Aztecs: Treasures of Tenochtitlan* (London: Thames & Hudson, 1988)."
    short_citation: "Matos Moctezuma 1988"
    identifier_type: ISBN
    identifier_value: "9780500390245"
    notes: "Templo Mayor = Coatepec interpretation. Anchor for Huitzilopochtli chapter."

  - id: carrasco-1999-city
    source_tier: secondary
    in_scope: true
    author: "Carrasco, Davíd"
    title: "City of Sacrifice: The Aztec Empire and the Role of Violence in Civilization"
    year: 1999
    full_citation: "Carrasco, D., *City of Sacrifice: The Aztec Empire and the Role of Violence in Civilization* (Boston: Beacon Press, 1999)."
    short_citation: "Carrasco 1999"
    identifier_type: ISBN
    identifier_value: "9780807046425"
    notes: "Huitzilopochtli ritual/political reading."

  - id: lopez-austin-myths
    source_tier: secondary
    in_scope: true
    author: "López Austin, Alfredo"
    title: "The Myths of the Opossum: Pathways of Mesoamerican Mythology"
    year: 1993
    full_citation: "López Austin, A., *The Myths of the Opossum: Pathways of Mesoamerican Mythology*, trans. B.R. Ortiz de Montellano and T. Ortiz de Montellano (Albuquerque: University of New Mexico Press, 1993)."
    short_citation: "López Austin 1993"
    identifier_type: ISBN
    identifier_value: "9780826313942"
    notes: "Used for Cipactli, Huitzilopochtli, Quetzalcoatl/Tezcatlipoca."

  - id: anderson-dibble-florentine
    source_tier: primary-translation
    in_scope: true
    author: "Anderson, Arthur J.O.; Dibble, Charles E. (trans. and eds.)"
    title: "Florentine Codex: General History of the Things of New Spain"
    year: "1950-1982"
    full_citation: "Sahagún, B. de, *Florentine Codex: General History of the Things of New Spain*, trans. and ed. A.J.O. Anderson and C.E. Dibble, 13 vols. (Santa Fe: School of American Research / Salt Lake City: University of Utah Press, 1950-1982)."
    short_citation: "Anderson-Dibble 1950-82"
    identifier_type: ISBN
    identifier_value: "9780874800821"
    notes: "Standard scholarly English translation of the Nahuatl Florentine Codex (Sahagún, c. 1545-1590). Book 3 (\"The Origin of the Gods\") is the principal narrative anchor for the Coatepec / Huitzilopochtli / Coyolxauhqui / Centzon Huitznahua episode. Added at post-human-normalize for Ch24 FC-03 to anchor Florentine Codex narrative-detail citations directly at the chapter-draft stage rather than routing through Matos Moctezuma 1988 / Carrasco 1999 as secondary interpreters."

  # ── Tradition-specific anchors for RELATED entries ──────────────────

  - id: salomon-urioste-huarochiri
    source_tier: primary-translation
    in_scope: true
    author: "Salomon, Frank; Urioste, George L. (trans. and eds.)"
    title: "The Huarochirí Manuscript: A Testament of Ancient and Colonial Andean Religion"
    year: 1991
    full_citation: "Salomon, F. and Urioste, G.L. (trans. and eds.), *The Huarochirí Manuscript: A Testament of Ancient and Colonial Andean Religion* (Austin: University of Texas Press, 1991)."
    short_citation: "Salomon & Urioste 1991"
    identifier_type: ISBN
    identifier_value: "9780292730533"
    notes: "Anchor for Pariacaca."

  - id: biebuyck-mateene-mwindo
    source_tier: primary-translation
    in_scope: true
    author: "Biebuyck, Daniel; Mateene, Kahombo C. (trans. and eds.)"
    title: "The Mwindo Epic from the Banyanga"
    year: 1969
    full_citation: "Biebuyck, D. and Mateene, K.C. (trans. and eds.), *The Mwindo Epic from the Banyanga (Zaire)* (Berkeley: University of California Press, 1969)."
    short_citation: "Biebuyck & Mateene 1969"
    identifier_type: ISBN
    identifier_value: "9780520003767"
    notes: "Used for the Mwindo contrastive case."

  - id: philippi-kojiki
    source_tier: primary-translation
    in_scope: true
    author: "Philippi, Donald L. (trans.)"
    title: "Kojiki"
    year: 1968
    full_citation: "Philippi, D.L. (trans.), *Kojiki* (Tokyo: University of Tokyo Press / Princeton: Princeton University Press, 1968)."
    short_citation: "Philippi 1968"
    identifier_type: ISBN
    identifier_value: "9780691611358"
    notes: "Scholarly-standard English Kojiki. Anchor for Susanoo/Orochi. ISBN 9780691611358 corresponds to the Princeton paperback reprint of the 1968 joint U Tokyo Press / Princeton University Press edition; content is identical across editions."

  - id: naumann-mythen
    source_tier: secondary
    in_scope: true
    author: "Naumann, Nelly"
    title: "Die Mythen des alten Japan"
    year: 1996
    full_citation: "Naumann, N., *Die Mythen des alten Japan* (München: C.H. Beck, 1996)."
    short_citation: "Naumann 1996"
    identifier_type: ISBN
    identifier_value: "9783406421648"
    notes: "Metallurgical-allegory reading of Susanoo/Orochi."

  - id: russell-zoroastrianism-armenia
    source_tier: secondary
    in_scope: true
    author: "Russell, James R."
    title: "Zoroastrianism in Armenia"
    year: 1987
    full_citation: "Russell, J.R., *Zoroastrianism in Armenia*, Harvard Iranian Series 5 (Cambridge, MA: Harvard University, Department of Near Eastern Languages and Civilizations, 1987)."
    short_citation: "Russell 1987"
    identifier_type: ISBN
    identifier_value: "9780674968509"
    notes: "Anchor for Vahagn/Vishaps."

  - id: bailey-ivanova-1998
    source_tier: secondary
    in_scope: true
    author: "Bailey, James; Ivanova, Tatyana (eds.)"
    title: "An Anthology of Russian Folk Epics"
    year: 1998
    full_citation: "Bailey, J. and Ivanova, T. (eds.), *An Anthology of Russian Folk Epics* (Armonk, NY: M.E. Sharpe, 1998)."
    short_citation: "Bailey & Ivanova 1998"
    identifier_type: ISBN
    identifier_value: "9781563244889"
    notes: "Major English-language anthology of the East Slavic *bylina* tradition, with introduction surveying the genre, the 19th-century collection history (Rybnikov, Hilferding), and the individual epics including the Dobrynya-Zmey-Gorynych cycle. Specialist anchor for Ch20 Dobrynya-cycle narrative and collection-history claims."

  - id: siikala-finnish
    source_tier: secondary
    in_scope: true
    author: "Siikala, Anna-Leena"
    title: "Mythic Images and Shamanism: A Perspective on Kalevala Poetry"
    year: 2002
    full_citation: "Siikala, A.-L., *Mythic Images and Shamanism: A Perspective on Kalevala Poetry*, Folklore Fellows' Communications 280 (Helsinki: Academia Scientiarum Fennica, 2002)."
    short_citation: "Siikala 2002"
    identifier_type: ISBN
    identifier_value: "9789514109027"
    notes: "Anchor for Väinämöinen/Iku-Turso as transformed shamanic binding."

  - id: conrad-west-africa
    source_tier: secondary
    in_scope: true
    author: "Conrad, David C."
    title: "Empires of Medieval West Africa: Ghana, Mali, and Songhay"
    year: 2005
    full_citation: "Conrad, D.C., *Empires of Medieval West Africa: Ghana, Mali, and Songhay* (New York: Facts on File, 2005)."
    short_citation: "Conrad 2005"
    identifier_type: ISBN
    identifier_value: "9780816052622"
    notes: "Anchor for Bida / Wagadu inversion chapter."

  - id: belcher-epic
    source_tier: secondary
    in_scope: true
    author: "Belcher, Stephen"
    title: "Epic Traditions of Africa"
    year: 1999
    full_citation: "Belcher, S., *Epic Traditions of Africa* (Bloomington: Indiana University Press, 1999)."
    short_citation: "Belcher 1999"
    identifier_type: ISBN
    identifier_value: "9780253212818"
    notes: "Used for Mwindo and Bida."

  - id: hallowell-ojibwa-world
    source_tier: secondary
    in_scope: true
    author: "Hallowell, A. Irving"
    title: "Ojibwa Ontology, Behavior, and World View"
    year: 1960
    full_citation: "Hallowell, A.I., 'Ojibwa Ontology, Behavior, and World View', in *Culture in History: Essays in Honor of Paul Radin*, ed. Stanley Diamond (New York: Columbia University Press, 1960), 19–52."
    short_citation: "Hallowell 1960"
    identifier_type: ISBN
    identifier_value: "9780231024853"
    notes: "Foundational 'other-than-human persons' framework. Anchor for the Nanabozho contrastive case."

  - id: merlan-caging-rainbow
    source_tier: secondary
    in_scope: true
    author: "Merlan, Francesca"
    title: "Caging the Rainbow: Places, Politics, and Aborigines in a North Australian Town"
    year: 1998
    full_citation: "Merlan, F., *Caging the Rainbow: Places, Politics, and Aborigines in a North Australian Town* (Honolulu: University of Hawaiʻi Press, 1998)."
    short_citation: "Merlan 1998"
    identifier_type: ISBN
    identifier_value: "9780824819668"
    notes: "Central for the Rainbow Serpent methodological chapter."

blacklist:
  - pattern: "theoi.com"
    reason: "Unattributed compilations; cite only the ancient sources it paraphrases, never theoi.com itself."
  - pattern: "sacred-texts.com"
    reason: "Archive of public-domain 19th-century translations, often superseded. Use only when a 19th-c. translation is itself the object of discussion."
  - pattern: "Wikipedia citation as sole source"
    reason: "Wikipedia may be used for orientation and for locating primary references; never as a terminal citation."
  - pattern: "ancient-origins.net"
    reason: "Sensationalist popularization. Never cite."
  - pattern: "New Age / 'universal mythology' popularizations (Campbell's *Masks of God* as primary, Graves's *Greek Myths*, Pinsent, Cotterell popular compilations)"
    reason: "Not peer-reviewed; often conflates traditions. Campbell and Graves may appear as reception/history-of-interpretation but never as factual anchors."

triangulation_databases:
  - id: etcsl
    url: "https://etcsl.orinst.ox.ac.uk/"
    covers: "Sumerian literary texts (Lugal-e, Sumerian flood story, Sumerian Anzu background)."
  - id: cdli
    url: "https://cdli.ucla.edu/"
    covers: "Cuneiform tablet database; verify specific tablet numbers."
  - id: oracc
    url: "https://oracc.museum.upenn.edu/"
    covers: "Open Richly Annotated Cuneiform Corpus — composite normalized texts, incl. Enūma Eliš, Anzu Epic."
  - id: ctr-ugaritic
    url: "https://www.zotero.org/groups/ugaritic/"
    covers: "Ugaritic text references; cross-check KTU/CAT numbering."
  - id: perseus
    url: "http://www.perseus.tufts.edu/"
    covers: "Greek and Latin primary texts — Hesiod, Apollodorus, Nonnus, Ovid, Virgil."
  - id: titus
    url: "https://titus.uni-frankfurt.de/"
    covers: "Indo-European text archive — Vedic, Avestan, Hittite."
  - id: kotenbunko
    url: "https://www.nijl.ac.jp/"
    covers: "Japanese classical texts (Kojiki, Nihon Shoki, Fudoki). Japanese-language; use with Philippi/Aston translations."
  - id: worldcat
    url: "https://www.worldcat.org/"
    covers: "Catalog lookup for verifying edition/ISBN details of hard-to-find works (van Dijk 1983, Annus 2001)."

notes:
  scope: |
    This registry is deliberately INCOMPLETE at scope-lock. It covers:
    (a) the comparative / theoretical spine that every chapter must engage with;
    (b) one anchor critical edition per CORE story;
    (c) tradition-specific anchors for the most load-bearing RELATED and contrastive entries.
    Additional per-story sources — alternative translations, specialist journal articles,
    monographs on individual combats — will accrue at the chapter-briefs stage.
    The `inventory-audit` stage is expected to flag additional required entries.
```

---

# Governing file: glossary.yaml

```
meta:
  stage: glossary-lock
  version: v1-locked
  status: user-confirmed
  date: 2026-04-24
  note: "User-confirmed on 2026-04-24. All DECIDE_GLOSSARY.md items resolved. Changes from v1-draft: (3) Yahweh replaces YHWH as primary form; (7) wak'a replaces huaca; (13) tehôm kept italicised throughout body prose rather than switching to 'the deep'; (15) 'the adversary' added as the neutral category term, with 'the dragon' reserved for morphologically draconic figures and 'chaos-figure' banned. All other draft choices confirmed. Meta-diacritics policy: full scholarly diacritics across the glossary (option A)."
  agent_model: "claude-opus-4-7[1m]"

terms:

  # ══════════════════════════════════════════════════════════════════════
  # CATEGORY TERMS — the vocabulary of the book itself
  # ══════════════════════════════════════════════════════════════════════

  - native: "Chaoskampf"
    renderings_considered:
      - { form: "Chaoskampf", source: "Gunkel 1895; still standard" }
      - { form: "combat myth", source: "Forsyth 1987; Yarbro Collins 1976; Ballentine 2015" }
      - { form: "conflict myth", source: "Ballentine 2015 preferred term" }
    chosen: "Chaoskampf (in headings and as technical term); 'combat myth' in body prose"
    rationale: "Scope.md §'Terminology default (locked)': Chaoskampf in headings/catalog; combat myth as default in body; reserves Chaoskampf for quotations and Gunkel discussion."
    first_mention_gloss: "the scholarly category, coined by Hermann Gunkel in 1895, for narratives in which a sovereign or champion deity defeats a monstrous adversary to establish or preserve cosmic order"
    never_use: ["dragon myth (too narrow)", "dragon-slaying myth (misses the cosmogonic function)"]

  - native: "cosmogonic combat"
    renderings_considered:
      - { form: "cosmogonic combat", source: "book-internal" }
      - { form: "cosmogonic chaoskampf", source: "Scurlock & Beal 2013" }
      - { form: "combat-cosmogony", source: "Forsyth 1987" }
    chosen: "cosmogonic combat"
    rationale: "Clearest plain-English form; the category is one of four subtypes the book defines."
    first_mention_gloss: "a combat myth in which the cosmos itself is established out of or immediately after the combat — for example, Marduk building sky and earth from Tiamat's body"
    never_use: []

  - native: "sovereignty combat"
    renderings_considered:
      - { form: "sovereignty combat", source: "book-internal; cf. Lincoln 2012" }
      - { form: "kingship combat", source: "Forsyth 1987" }
    chosen: "sovereignty combat"
    rationale: "Matches scope.md subtype naming; 'sovereignty' is the category that captures Baal/Yamm, Zeus/Typhon, Indra/Vṛtra, Ninurta/Anzû."
    first_mention_gloss: "a combat myth in which the victor's rule over gods and humans is established or secured by the combat"
    never_use: []

  - native: "cyclical-maintenance combat"
    renderings_considered:
      - { form: "cyclical-maintenance combat", source: "book-internal" }
      - { form: "recurrent combat", source: "Assmann 2001 on maʿat" }
    chosen: "cyclical-maintenance combat"
    rationale: "Captures the Ra/Apep and Illuyanka/purulli subtype; the combat is re-enacted rather than once-and-done."
    first_mention_gloss: "a combat myth that is re-enacted on a recurring schedule (daily, annually, calendrically) to preserve an order that is always under threat"
    never_use: []

  - native: "eschatological combat"
    renderings_considered:
      - { form: "eschatological combat", source: "book-internal; cf. Yarbro Collins 1976" }
      - { form: "end-time combat", source: "popular usage" }
    chosen: "eschatological combat"
    rationale: "Standard scholarly term; captures Ragnarök, Rev 12, Frashokereti."
    first_mention_gloss: "a combat myth that closes cosmic time — the final combat that ends the present age"
    never_use: []

  - native: "theogony / theogonic"
    renderings_considered:
      - { form: "theogony", source: "Hesiod title; standard scholarly use" }
      - { form: "divine genealogy", source: "popularizing" }
    chosen: "theogony / theogonic"
    rationale: "Standard; used in West 1966, West 1997, Hoffner 1998 for the Kumarbi Cycle."
    first_mention_gloss: "a narrative of the generation of the gods; the theogonic 'kingship in heaven' pattern tracks successions of divine rulers (Alalu → Anu → Kumarbi → Teshub)"
    never_use: []

  - native: "cosmogony / cosmogonic"
    renderings_considered:
      - { form: "cosmogony", source: "standard scholarly" }
      - { form: "creation myth", source: "popular" }
    chosen: "cosmogony / cosmogonic"
    rationale: "Precision — creation-myth is broader and includes dismemberment-without-combat cases that the book explicitly separates."
    first_mention_gloss: "a narrative of the origin of the ordered cosmos"
    never_use: ["creation myth (used only informally)"]

  - native: "reception / reception history"
    renderings_considered:
      - { form: "reception", source: "standard in biblical and classical studies (Ogden 2013)" }
      - { form: "Nachleben", source: "German scholarly usage" }
      - { form: "afterlife", source: "popular" }
    chosen: "reception"
    rationale: "Discipline-standard; understood by lay readers; scope.md §'Period' marks the reception coda explicitly as reception, not primary."
    first_mention_gloss: "the afterlife of an image, narrative, or motif in later traditions (e.g., Leviathan reworked in Milton, Tolkien's dragons, kaiju cinema)"
    never_use: []

  - native: "appropriation"
    renderings_considered:
      - { form: "appropriation", source: "current critical scholarship; scope.md §'Appropriation protocol'" }
      - { form: "cultural appropriation", source: "popular" }
    chosen: "appropriation"
    rationale: "Used in scope.md and in the Merlan 1998 / Hallowell 1960 literature without 'cultural' prefix; the prefix is redundant in context."
    first_mention_gloss: "the distortion that occurs when a comparative category developed in one tradition is imposed on another whose own conceptual framework rejects the category"
    never_use: []

  - native: "comparativist / comparative mythology"
    renderings_considered:
      - { form: "comparativist", source: "Lincoln 2012; contemporary critical scholarship" }
      - { form: "comparative mythologist", source: "older scholarship" }
    chosen: "comparativist"
    rationale: "The book uses 'comparativist' with its critical edge; 'comparative mythologist' would sound neutral where the book's critique is sharper."
    first_mention_gloss: "a scholar who compares myths across traditions for shared patterns; the book engages comparativism as a method while flagging its historical entanglement with universalising and colonial projects"
    never_use: []

  - native: "area specialist"
    renderings_considered:
      - { form: "area specialist", source: "scope.md §'Appropriation protocol'; internal term" }
      - { form: "area expert", source: "informal" }
    chosen: "area specialist"
    rationale: "Locked by scope.md; the contrast area-specialist / comparativist is load-bearing throughout."
    first_mention_gloss: "a scholar whose primary expertise is a single tradition (language, texts, ritual context); the book's appropriation protocol requires area-specialist citations before invoking any comparative frame for non-Eurasian traditions"
    never_use: []

  - native: "the adversary (category term)"
    renderings_considered:
      - { form: "the adversary", source: "book-internal; neutral category term" }
      - { form: "the dragon", source: "book-internal; morphological descriptor" }
      - { form: "the monstrous adversary", source: "book-internal" }
      - { form: "the chaos-figure", source: "popularising usage" }
    chosen: "'the adversary' as the default neutral category term; 'the dragon' only where the figure is visually or morphologically draconic (Leviathan, Aži Dahāka, Fáfnir, Zmey Gorynych, Typhon, etc.)"
    rationale: "Cross-chapter consistency benefits from one general term for the class of figure the champion confronts. 'The adversary' is the neutral choice and fits every case including those (Anzû the lion-headed eagle, Asag the stone-demon, Mishipeshu the underwater manitou) where 'dragon' would misrepresent the figure. 'Chaos-figure' is banned because it begs the very question the book is investigating (Ballentine 2015's critique)."
    first_mention_gloss: "the book's umbrella term for the class of figure the champion confronts in a combat myth; the term is deliberately neutral between dragon, serpent, sea-monster, stone-demon, rebel deity, and other morphologies"
    never_use: ["chaos-figure (begs the question); chaos-monster (same reason; the corpus is not uniformly 'chaos')"]

  # ══════════════════════════════════════════════════════════════════════
  # METHODOLOGICAL TERMS
  # ══════════════════════════════════════════════════════════════════════

  - native: "HERO SLAY SERPENT (formula)"
    renderings_considered:
      - { form: "HERO SLAY SERPENT", source: "Watkins 1995 (small capitals)" }
      - { form: "hero-slay-serpent formula", source: "Watkins 1995, running text" }
    chosen: "HERO SLAY SERPENT (in small capitals when naming Watkins's reconstructed formula; 'hero-slay-serpent formula' in running body prose)"
    rationale: "Small-capital convention is Watkins's own and should be preserved when naming the formula as a term of art; but body prose should not overuse the SMALL CAPS typography."
    first_mention_gloss: "Calvert Watkins's reconstructed Indo-European poetic formula (subject + verb-of-killing + serpent-object), attested in Vedic áhann áhim, Hittite kuenta... illuyanka, and elsewhere"
    never_use: []

  - native: "áhann áhim"
    renderings_considered:
      - { form: "áhann áhim", source: "Watkins 1995; Jamison & Brereton 2014" }
      - { form: "ahann ahim", source: "non-diacritical" }
    chosen: "áhann áhim"
    rationale: "Diacritics standard in Vedic scholarship; Watkins and Jamison-Brereton both use the accented form; the formula is the load-bearing exemplar and must be rendered as scholarship renders it."
    first_mention_gloss: "'he slew the serpent' — the Rigvedic formula (RV 1.32.1) that Watkins argues preserves the Indo-European poetic diction of combat-myth"
    never_use: []

  - native: "basic myth (Ivanov-Toporov)"
    renderings_considered:
      - { form: "basic myth", source: "Ivanov & Toporov 1965–74; now standard in translation" }
      - { form: "основной миф", source: "Russian original; not used in English body" }
    chosen: "'basic myth' (in quotation marks on first mention)"
    rationale: "The quotation marks flag it as a technical reconstruction whose status is contested (per Ch. 20 framing)."
    first_mention_gloss: "Ivanov and Toporov's 1965–74 reconstruction of a shared Slavic storm-god-vs-serpent narrative, drawn from folklore and toponyms, and now criticised for methodological circularity"
    never_use: []

  - native: "tier-ranking"
    renderings_considered:
      - { form: "tier-ranking", source: "book-internal; methods sidebar Ch. 33" }
    chosen: "tier-ranking"
    rationale: "Internal book term referring to CORE / RELATED / PROVISIONAL / CONTRASTIVE categorisation."
    first_mention_gloss: "the book's scheme for categorising chapters by the strength and type of primary attestation and by whether the chaoskampf framing is contested (CORE / RELATED / PROVISIONAL / CONTRASTIVE)"
    never_use: []

  - native: "other-than-human persons"
    renderings_considered:
      - { form: "other-than-human persons", source: "Hallowell 1960" }
      - { form: "non-human persons", source: "some later ethnographic writing" }
    chosen: "other-than-human persons"
    rationale: "Hallowell's exact phrase; central to the Anishinaabe (Ch. 32) and C8 chapters."
    first_mention_gloss: "A. Irving Hallowell's 1960 term for the Anishinaabe ontological category that includes animals, plants, thunder-beings, and manitouk as persons on equal standing with human persons"
    never_use: []

  - native: "Gunkel's thesis (Schöpfung und Chaos)"
    renderings_considered:
      - { form: "Gunkel's Chaoskampf thesis", source: "Scurlock & Beal 2013 subtitle" }
      - { form: "Gunkel's 1895 thesis", source: "standard" }
    chosen: "Gunkel's 1895 thesis"
    rationale: "Disambiguates from Gunkel's other work; the date is load-bearing (book emphasises how the term travelled for 130 years)."
    first_mention_gloss: "Hermann Gunkel's argument (1895) that Genesis 1 and Revelation 12 both preserve the demythologised remnants of a Near Eastern combat myth, of which Enūma Eliš is the paradigm"
    never_use: []

  - native: "Ballentine critique"
    renderings_considered:
      - { form: "Ballentine's critique", source: "Ballentine 2015; used internally" }
      - { form: "the conflict-myth re-reading", source: "Ballentine 2015's own phrase" }
    chosen: "the Ballentine critique (on first mention); thereafter 'Ballentine 2015'"
    rationale: "Short and clear; flags that this is a contemporary critical position."
    first_mention_gloss: "Debra Scoggins Ballentine's 2015 argument that 'chaos' is the wrong word for the adversaries in the combat-myth corpus, because they are presented in the ancient texts as rival sovereigns with their own retinue and power structure, not as inchoate disorder"
    never_use: []

  # ══════════════════════════════════════════════════════════════════════
  # DEITIES AND CHAMPIONS
  # ══════════════════════════════════════════════════════════════════════

  # ── Mesopotamia ──────────────────────────────────────────────────────

  - native: "Ninurta"
    renderings_considered:
      - { form: "Ninurta", source: "ETCSL; van Dijk 1983; Annus 2001; Lambert 2013" }
      - { form: "Ningirsu", source: "Lagash-tradition name; distinct deity" }
    chosen: "Ninurta"
    rationale: "Universal in the Lugal-e and Anzû scholarship; Ningirsu is a distinct Lagash deity and must not be conflated."
    first_mention_gloss: "Sumerian warrior-god, son of Enlil, lord of Nippur; champion against Asag in Lugal-e and against Anzû in the Anzû Epic"
    never_use: ["Ningirsu"]

  - native: "Marduk"
    renderings_considered:
      - { form: "Marduk", source: "Lambert 2013; Foster 2005; universal" }
      - { form: "Bēl", source: "cult epithet 'Lord'" }
    chosen: "Marduk"
    rationale: "Universal name for the deity; Bēl is an epithet, not an alternative name."
    first_mention_gloss: "patron god of Babylon; storm-god champion who slays Tiamat and reorders the cosmos in Enūma Eliš"
    never_use: []

  - native: "Enlil"
    renderings_considered:
      - { form: "Enlil", source: "standard in all major editions" }
      - { form: "Ellil", source: "later Akkadian transliteration variant" }
    chosen: "Enlil"
    rationale: "Standard Sumerian/Akkadian form in the combat-myth corpus."
    first_mention_gloss: "chief god of the Mesopotamian pantheon, lord of air and command, resident of Nippur"
    never_use: ["Ellil"]

  - native: "Ea / Enki"
    renderings_considered:
      - { form: "Ea", source: "Akkadian; Annus 2001; Lambert 2013" }
      - { form: "Enki", source: "Sumerian; ETCSL" }
    chosen: "Ea in Akkadian-language contexts (Anzû, Enūma Eliš, Kumarbi Cycle); Enki in Sumerian-language contexts (Lugal-e and Sumerian materials)"
    rationale: "The book is cross-linguistic; using the language-appropriate name preserves textual integrity. Flag dual identity at first mention of each."
    first_mention_gloss: "god of wisdom and fresh water (Sumerian Enki / Akkadian Ea); counselor of Ninurta and father of Marduk"
    never_use: []

  - native: "Anšar"
    renderings_considered:
      - { form: "Anšar", source: "Lambert 2013; Foster 2005 (with š)" }
      - { form: "Anshar", source: "non-diacritical anglicization" }
    chosen: "Anšar"
    rationale: "The diacritical form is standard in the critical editions; the book has several š-containing names and should be consistent in retaining the háček."
    first_mention_gloss: "elder sky-god; commissions Marduk as champion of the gods"
    never_use: ["Anshar"]

  - native: "Tiamat"
    renderings_considered:
      - { form: "Tiamat", source: "Lambert 2013; universal" }
      - { form: "Tiāmat", source: "with length-mark, less common" }
    chosen: "Tiamat"
    rationale: "Standard anglicization; cognate with Hebrew tehôm and thus load-bearing across Mesopotamian / biblical chapters."
    first_mention_gloss: "primordial salt-sea goddess; mother of the first gods; cast as monstrous adversary in Enūma Eliš"
    never_use: []

  - native: "Apsû"
    renderings_considered:
      - { form: "Apsû", source: "Lambert 2013" }
      - { form: "Apsu", source: "anglicized" }
      - { form: "Abzu", source: "Sumerian form" }
    chosen: "Apsû in Akkadian (Enūma Eliš) contexts; Abzu only where Sumerian usage is specifically invoked"
    rationale: "Matches Ea/Enki handling: use the language-appropriate form."
    first_mention_gloss: "primordial fresh-water; Tiamat's consort; killed by Ea in the Enūma Eliš prologue (Sumerian: Abzu)"
    never_use: []

  - native: "Qingu"
    renderings_considered:
      - { form: "Qingu", source: "Lambert 2013" }
      - { form: "Kingu", source: "older anglicizations (Speiser ANET)" }
    chosen: "Qingu"
    rationale: "Lambert 2013's critical-edition form; supersedes Speiser's 'Kingu'."
    first_mention_gloss: "Tiamat's appointed consort-general; holds the Tablet of Destinies; executed so that humans can be formed from his blood"
    never_use: ["Kingu"]

  - native: "Anzû"
    renderings_considered:
      - { form: "Anzû", source: "Annus 2001; Foster 2005" }
      - { form: "Anzu", source: "non-diacritical" }
      - { form: "Zu", source: "older, superseded" }
    chosen: "Anzû"
    rationale: "Standard in current critical edition; 'Zu' is a misreading long since corrected."
    first_mention_gloss: "lion-headed eagle-monster; rebel who steals the Tablet of Destinies from Enlil; slain by Ninurta"
    never_use: ["Zu"]

  - native: "Asag"
    renderings_considered:
      - { form: "Asag", source: "ETCSL; van Dijk 1983" }
      - { form: "Asakku", source: "Akkadian form" }
    chosen: "Asag in Sumerian (Lugal-e) contexts"
    rationale: "Lugal-e is Sumerian; Asakku appears in Akkadian bilingual and later material, which the book treats as reception."
    first_mention_gloss: "Sumerian demon of the mountains, commander of a stone-army; Ninurta's adversary in Lugal-e"
    never_use: []

  - native: "Šarur"
    renderings_considered:
      - { form: "Šarur", source: "ETCSL; van Dijk 1983" }
      - { form: "Sharur", source: "non-diacritical" }
    chosen: "Šarur"
    rationale: "Diacritical standard; the animate-mace motif recurs and needs a stable rendering."
    first_mention_gloss: "Ninurta's animate talking mace; scout and messenger; appears in both Lugal-e and the Anzû Epic"
    never_use: ["Sharur"]

  - native: "Labbu"
    renderings_considered:
      - { form: "Labbu", source: "Foster 2005; standard" }
    chosen: "Labbu"
    rationale: "Universal; fragmentary tablet is typically called the 'Labbu myth'."
    first_mention_gloss: "dragon in the fragmentary Akkadian 'Labbu myth'; slain by a storm-god whose identification is uncertain"
    never_use: []

  - native: "Tablet of Destinies"
    renderings_considered:
      - { form: "Tablet of Destinies", source: "Annus 2001; Lambert 2013; universal" }
      - { form: "Tablet of Fates", source: "older translations" }
      - { form: "dup šīmāti", source: "Akkadian cuneiform reading" }
    chosen: "Tablet of Destinies"
    rationale: "Standard English; dup šīmāti noted on first mention only."
    first_mention_gloss: "the cosmic decree-document (Akkadian dup šīmāti); possessing it is tantamount to kingship; central in Anzû and Enūma Eliš"
    never_use: ["Tablet of Fates"]

  - native: "Esagil"
    renderings_considered:
      - { form: "Esagil", source: "Lambert 2013" }
      - { form: "Esagila", source: "older anglicization" }
      - { form: "É-sag-íl", source: "Sumerian with hyphenation" }
    chosen: "Esagil"
    rationale: "Lambert's form; standard in current Assyriological use."
    first_mention_gloss: "Marduk's temple in Babylon; built at the cosmic axis as the post-combat capital of the gods"
    never_use: []

  - native: "akītu"
    renderings_considered:
      - { form: "akītu", source: "standard Akkadian with long vowel" }
      - { form: "akitu", source: "anglicized" }
      - { form: "akiti", source: "Sumerian" }
    chosen: "akītu"
    rationale: "Long-vowel form is scholarly standard; the festival's name should be recognisable."
    first_mention_gloss: "Mesopotamian New Year festival; Enūma Eliš was recited on its fourth day, tying the combat-myth to the annual ritual calendar"
    never_use: []

  # ── Anatolia / Levant ────────────────────────────────────────────────

  - native: "Tarḫunna / Teshub"
    renderings_considered:
      - { form: "Tarḫunna", source: "Hoffner 1998 (Hittite form, with dot under ḫ)" }
      - { form: "Tarhunna", source: "non-diacritical" }
      - { form: "Teshub", source: "Hurrian form; Hoffner 1998" }
      - { form: "Teššub", source: "diacritical Hurrian" }
    chosen: "Tarḫunna in Hittite-language contexts; Teshub in Hurrian-language contexts (Kumarbi Cycle)"
    rationale: "Scope.md's translation-mediated policy; each name is appropriate to its own language stratum. First mention glosses the pair."
    first_mention_gloss: "Anatolian storm-god (Hittite Tarḫunna / Hurrian Teshub); champion in the Illuyanka myth and in the Kumarbi Cycle"
    never_use: []

  - native: "Kumarbi"
    renderings_considered:
      - { form: "Kumarbi", source: "Hoffner 1998" }
    chosen: "Kumarbi"
    rationale: "Universal form; no significant variant."
    first_mention_gloss: "Hurrian father-god deposed by Teshub; generates the monstrous adversaries of the Kumarbi Cycle (Ullikummi, Hedammu)"
    never_use: []

  - native: "Ullikummi"
    renderings_considered:
      - { form: "Ullikummi", source: "Hoffner 1998" }
    chosen: "Ullikummi"
    rationale: "Universal form."
    first_mention_gloss: "stone monster; Kumarbi's progeny by a rock; grows on the shoulder of Upelluri to threaten Teshub's kingship"
    never_use: []

  - native: "Hedammu"
    renderings_considered:
      - { form: "Hedammu", source: "Hoffner 1998" }
    chosen: "Hedammu"
    rationale: "Standard."
    first_mention_gloss: "sea-monster progeny of Kumarbi in the fragmentary Song of Hedammu; seduced by Ishtar/Šauška"
    never_use: []

  - native: "Upelluri"
    renderings_considered:
      - { form: "Upelluri", source: "Hoffner 1998" }
    chosen: "Upelluri"
    rationale: "Standard."
    first_mention_gloss: "the giant on whose shoulder Ullikummi is planted and grows"
    never_use: []

  - native: "Illuyanka"
    renderings_considered:
      - { form: "Illuyanka", source: "Hoffner 1998; Beckman 1982; Watkins 1995" }
      - { form: "Illuyankaš", source: "with Hittite nominative ending" }
    chosen: "Illuyanka"
    rationale: "Current scholarly English drops the case-ending."
    first_mention_gloss: "serpent-monster, the storm-god's adversary in the purulli-festival aetiology"
    never_use: ["Illuyankaš (outside philological footnotes)"]

  - native: "Inara"
    renderings_considered:
      - { form: "Inara", source: "Hoffner 1998" }
    chosen: "Inara"
    rationale: "Standard."
    first_mention_gloss: "daughter of the storm-god; ritual actor in Version 1 of the Illuyanka myth"
    never_use: []

  - native: "Hupasiya"
    renderings_considered:
      - { form: "Hupasiya", source: "Hoffner 1998" }
    chosen: "Hupasiya"
    rationale: "Standard."
    first_mention_gloss: "mortal man who binds Illuyanka; Inara's partner in Version 1 of the myth"
    never_use: []

  - native: "purulli"
    renderings_considered:
      - { form: "purulli", source: "Hoffner 1998; Beckman 1982" }
      - { form: "purulliyaš", source: "with case ending" }
    chosen: "purulli"
    rationale: "Shorter form standard in translations."
    first_mention_gloss: "Hittite spring festival at which the Illuyanka myth was recited as liturgical aetiology"
    never_use: []

  - native: "Baal / Haddu / Baʿlu"
    renderings_considered:
      - { form: "Baal", source: "popular and most Hebrew-Bible scholarship" }
      - { form: "Baʿlu", source: "Smith 1994 (Ugaritic)" }
      - { form: "Haddu", source: "Ugaritic personal-name form" }
    chosen: "Baal (in body prose); first-mention gloss names Baʿlu / Haddu as the Ugaritic forms"
    rationale: "Reader recognition; the Ugaritic specificity is preserved in the gloss and in philological footnotes."
    first_mention_gloss: "Ugaritic storm-god (Baʿlu / Haddu in Ugaritic spelling); son of Dagan; combat-champion of the Baal Cycle"
    never_use: []

  - native: "Yamm"
    renderings_considered:
      - { form: "Yamm", source: "Smith 1994; universal in Ugaritic scholarship" }
      - { form: "Yam", source: "Hebrew cognate; used in Ch. 8 for biblical usage" }
    chosen: "Yamm in Ugaritic contexts (Ch. 7); Yam in Hebrew-Bible contexts (Ch. 8)"
    rationale: "Language-appropriate; the Ugaritic form has the long consonant."
    first_mention_gloss: "'Sea'; Ugaritic god of the sea and Baal's primary adversary in the Cycle (Hebrew cognate: Yam)"
    never_use: []

  - native: "Lôtan"
    renderings_considered:
      - { form: "Lôtan", source: "Smith 1994" }
      - { form: "Lotan", source: "non-diacritical" }
      - { form: "ltn", source: "unvocalized Ugaritic" }
    chosen: "Lôtan"
    rationale: "Circumflex-o preserves vowel length; cognate with Hebrew Leviathan and the correspondence must be visible."
    first_mention_gloss: "seven-headed serpent adversary at Ugarit (ltn in unvocalized Ugaritic); cognate with Hebrew Leviathan"
    never_use: []

  - native: "Mot"
    renderings_considered:
      - { form: "Mot", source: "Smith 1994" }
      - { form: "Môt", source: "with length-mark" }
    chosen: "Mot"
    rationale: "Shorter form standard in English Ugaritic scholarship."
    first_mention_gloss: "'Death'; Ugaritic god of death; Baal's adversary in the second half of the Cycle"
    never_use: []

  - native: "Kothar-wa-Khasis"
    renderings_considered:
      - { form: "Kothar-wa-Khasis", source: "Smith 1994" }
      - { form: "Kothar", source: "short form" }
      - { form: "Kôtaru-wa-Ḫasīsu", source: "philological" }
    chosen: "Kothar-wa-Khasis"
    rationale: "Matches Smith's translation; the doubled name preserves the Ugaritic epithet-pair."
    first_mention_gloss: "Ugaritic craftsman-god; forges Baal's maces Ayyamur and Yagrush"
    never_use: []

  - native: "El (Ugaritic)"
    renderings_considered:
      - { form: "El", source: "Smith 1994; universal" }
      - { form: "ʾIlu", source: "philological" }
    chosen: "El"
    rationale: "Standard English."
    first_mention_gloss: "chief Ugaritic god; father of the divine assembly; decision-maker in the Baal Cycle"
    never_use: []

  - native: "ʿAnat"
    renderings_considered:
      - { form: "ʿAnat", source: "Smith 1994 (with ʿayin)" }
      - { form: "Anat", source: "non-diacritical" }
      - { form: "ʿAnatu", source: "philological" }
    chosen: "ʿAnat"
    rationale: "The ʿayin is the standard diacritic in current Ugaritic scholarship."
    first_mention_gloss: "Ugaritic warrior-goddess; Baal's sister and combat-ally"
    never_use: []

  - native: "Ayyamur / Yagrush"
    renderings_considered:
      - { form: "Ayyamur and Yagrush", source: "Smith 1994" }
      - { form: "ʾayamarri / yagarriš", source: "philological" }
    chosen: "Ayyamur and Yagrush"
    rationale: "Smith's translations; retaining both names preserves the mace-pair motif that parallels Ninurta's Šarur."
    first_mention_gloss: "Baal's two named maces, forged by Kothar; the storm-god's dual combat-weapons"
    never_use: []

  - native: "Ṣapānu / Mount Zaphon"
    renderings_considered:
      - { form: "Ṣapānu", source: "Smith 1994 (Ugaritic)" }
      - { form: "Mount Zaphon", source: "Hebrew-Bible tradition" }
      - { form: "Jebel al-Aqra", source: "modern Arabic place-name" }
    chosen: "Ṣapānu at first mention (Ugaritic context); 'Mount Zaphon' when the Hebrew-Bible reception is in view"
    rationale: "Preserves the same mountain across languages and chapters."
    first_mention_gloss: "Baal's sacred mountain; the modern Jebel al-Aqra on the Syrian–Turkish border; his palace-seat after victory over Yamm"
    never_use: []

  # ── Hebrew Bible and New Testament ──────────────────────────────────

  - native: "Yahweh"
    renderings_considered:
      - { form: "Yahweh", source: "vocalized reconstruction; Day 1985 uses this form" }
      - { form: "YHWH", source: "standard unvocalized tetragrammaton" }
      - { form: "the LORD", source: "translation convention" }
    chosen: "Yahweh"
    rationale: "The vocalised form is common enough in academic and general English that the unvocalised YHWH becomes awkward in sustained body prose; 'Yahweh' reads naturally in narrative discussion of the deity as a character. YHWH may still appear in direct quotation of sources that use the unvocalised form."
    first_mention_gloss: "the God of Israel (Hebrew tetragrammaton YHWH, vocalised Yahweh); depicted in the combat-myth passages as storm-god who defeats the sea, Leviathan, and Rahab"
    never_use: ["Jehovah"]

  - native: "Leviathan"
    renderings_considered:
      - { form: "Leviathan", source: "English Bible tradition; Day 1985" }
      - { form: "Liwyātān", source: "Hebrew transliteration" }
    chosen: "Leviathan"
    rationale: "Universal English form; reader recognition across Hebrew Bible, Rev 12, reception."
    first_mention_gloss: "multi-headed sea-serpent of the Hebrew Bible (Psalm 74; Isaiah 27; Job 41); cognate with Ugaritic Lôtan"
    never_use: []

  - native: "Rahab"
    renderings_considered:
      - { form: "Rahab", source: "Day 1985; English Bible tradition" }
      - { form: "Rahav", source: "modern Hebrew transliteration" }
    chosen: "Rahab"
    rationale: "Standard English; distinguish the proud sea-monster from the unrelated Rahab-of-Jericho by context (always clear)."
    first_mention_gloss: "'proud one'; monstrous figure of Hebrew Bible poetry (Psalm 89; Isaiah 51; Job 26), associated with the sea and — in Isaiah — with Egypt"
    never_use: []

  - native: "Tannīn"
    renderings_considered:
      - { form: "Tannīn", source: "Day 1985" }
      - { form: "tannin", source: "non-diacritical, lower-case common-noun" }
    chosen: "Tannīn (when naming the mythic figure); tannin (as the common noun 'serpent / sea-creature')"
    rationale: "Capital/diacritics for the personified figure; lowercase for ordinary common-noun use."
    first_mention_gloss: "'serpent / sea-creature' (Hebrew); used both as common noun and, in combat passages, as a personified figure often synonymous with Leviathan"
    never_use: []

  - native: "tehôm"
    renderings_considered:
      - { form: "tehôm", source: "Day 1985" }
      - { form: "tehom", source: "non-diacritical" }
      - { form: "the deep", source: "English translation" }
    chosen: "tehôm (italicised) throughout body prose; 'the deep' reserved for direct Bible quotations where English translation is required"
    rationale: "Genesis 1:2 is quoted and referenced repeatedly across Ch. 8, the introduction, and the Gunkel–Ballentine discussions; keeping tehôm as the technical term through every mention preserves the philological cognancy argument (tehôm / Tiamat) without switching registers mid-paragraph."
    first_mention_gloss: "'the deep' (Genesis 1:2); the primordial waters; linguistically cognate with Akkadian Tiamat, the cornerstone of Gunkel's 1895 argument"
    never_use: []

  - native: "the dragon (Rev 12)"
    renderings_considered:
      - { form: "the dragon", source: "Rev 12; standard English" }
      - { form: "the great red dragon", source: "Rev 12:3 descriptor" }
      - { form: "ὁ δράκων", source: "Greek" }
    chosen: "the (red) dragon of Rev 12"
    rationale: "'Dragon' alone is the noun; 'red' marks the specific Revelation figure when contrast is needed."
    first_mention_gloss: "the seven-headed red dragon of Revelation 12:3, glossed in v. 9 as 'the ancient serpent, called the devil and Satan'"
    never_use: []

  - native: "Michael (archangel)"
    renderings_considered:
      - { form: "Michael", source: "English Bible; universal" }
      - { form: "Mikaʾel", source: "Hebrew transliteration" }
    chosen: "Michael"
    rationale: "Universal English form for this figure."
    first_mention_gloss: "archangel-warrior; leads the heavenly host against the dragon in Revelation 12"
    never_use: []

  - native: "Satan / the devil"
    renderings_considered:
      - { form: "Satan", source: "English Bible; Forsyth 1987" }
      - { form: "the satan", source: "Second Temple usage, when the term is a title" }
      - { form: "the devil (ho diabolos)", source: "NT Greek" }
    chosen: "Satan (for the figure in Rev 12 and later Christian reception); 'the satan' (lowercase) in Hebrew Bible contexts where the term is a title rather than a name"
    rationale: "The difference in capitalisation flags the Second Temple evolution; Forsyth 1987 tracks it."
    first_mention_gloss: "'the adversary'; in Rev 12:9 identified with the dragon and the ancient serpent — completing the assimilation of the combat-myth adversary to the Second-Temple satanology"
    never_use: []

  # ── Greek and Roman ──────────────────────────────────────────────────

  - native: "Zeus"
    renderings_considered:
      - { form: "Zeus", source: "universal" }
    chosen: "Zeus"
    rationale: "Universal."
    first_mention_gloss: "king of the Olympian gods; wields the thunderbolt in combat with Typhon"
    never_use: []

  - native: "Typhon / Typhoeus"
    renderings_considered:
      - { form: "Typhon", source: "Apollodorus; most translations" }
      - { form: "Typhoeus", source: "Hesiod Theogony; West 1966" }
    chosen: "Typhon as body-prose default; Typhoeus when specifically discussing the Theogony"
    rationale: "Both names are ancient; the distinction tracks the specific text under discussion."
    first_mention_gloss: "the hundred-headed, serpent-limbed earth-born monster, child of Gaia and Tartarus; Zeus's last and greatest adversary"
    never_use: []

  - native: "drakōn / dragon"
    renderings_considered:
      - { form: "drakōn", source: "Ogden 2013 title" }
      - { form: "drakon", source: "non-diacritical" }
      - { form: "dragon", source: "English translation" }
    chosen: "drakōn (Greek technical term); 'dragon' in body prose"
    rationale: "Ogden's classification vocabulary uses drakōn as a genre-term; body prose can say 'dragon'."
    first_mention_gloss: "'dragon' (Greek δράκων); the Greek and Roman serpent-adversary category that Ogden 2013 catalogues and classifies"
    never_use: []

  - native: "Apollo"
    renderings_considered:
      - { form: "Apollo", source: "universal" }
      - { form: "Apollon", source: "Greek form" }
    chosen: "Apollo"
    rationale: "Reader recognition."
    first_mention_gloss: "Olympian god of prophecy, music, and plague; slays Python to found the Delphic oracle"
    never_use: []

  - native: "Python (Delphic)"
    renderings_considered:
      - { form: "Python", source: "Ovid; Fontenrose 1959 title" }
      - { form: "Pytho (drakaina)", source: "Homeric Hymn to Apollo" }
    chosen: "Python"
    rationale: "Fontenrose's title; the later tradition names the (originally female) dragon Python."
    first_mention_gloss: "the Delphic serpent slain by Apollo; originally unnamed and female (a drakaina) in the Homeric Hymn; named Python in Ovid and later tradition"
    never_use: []

  - native: "Herakles / Hercules"
    renderings_considered:
      - { form: "Herakles", source: "Greek contexts" }
      - { form: "Hercules", source: "Roman / Latin contexts (Cacus episode)" }
    chosen: "Herakles in Greek-text contexts; Hercules in Roman-text contexts (Virgil Aeneid 8, Ovid Fasti)"
    rationale: "Preserves the text-specific register."
    first_mention_gloss: "hero of the twelve labours (Greek Herakles / Latin Hercules); slays Hydra, Ladon, Geryon, and Cacus"
    never_use: []

  - native: "Perseus"
    renderings_considered:
      - { form: "Perseus", source: "universal" }
    chosen: "Perseus"
    rationale: "Universal."
    first_mention_gloss: "hero who beheads Medusa and rescues Andromeda from Ketos; iconographic antecedent of the medieval St. George type"
    never_use: []

  - native: "Kadmos"
    renderings_considered:
      - { form: "Kadmos", source: "Greek" }
      - { form: "Cadmus", source: "Latinised; Ovid" }
    chosen: "Kadmos"
    rationale: "Preserves Greek form; the story is Theban and Greek in origin."
    first_mention_gloss: "Theban hero; slays the dragon of Ares at Thebes and sows its teeth to raise the Spartoi"
    never_use: []

  - native: "Bellerophon"
    renderings_considered:
      - { form: "Bellerophon", source: "Homer; standard" }
    chosen: "Bellerophon"
    rationale: "Universal."
    first_mention_gloss: "Lycian hero; slays the Chimaera while riding Pegasus"
    never_use: []

  # ── Iran ─────────────────────────────────────────────────────────────

  - native: "Thraētaona / Fereydun"
    renderings_considered:
      - { form: "Thraētaona", source: "Avestan; Benveniste & Renou 1934" }
      - { form: "Fereydun", source: "New Persian (Shāhnāmeh)" }
      - { form: "Frēdōn", source: "Middle Persian (Pahlavi)" }
    chosen: "Thraētaona in Avestan-context body prose; first mention glosses the Middle/New-Persian descendants"
    rationale: "The Avestan form is the book's primary-source register; the Pahlavi/New-Persian afterlife is tracked in the gloss."
    first_mention_gloss: "Avestan hero-slayer of Aži Dahāka (Middle Persian Frēdōn; New Persian Fereydun in the Shāhnāmeh)"
    never_use: []

  - native: "Aži Dahāka"
    renderings_considered:
      - { form: "Aži Dahāka", source: "Avestan; Benveniste & Renou 1934" }
      - { form: "Azhi Dahaka", source: "non-diacritical" }
      - { form: "Dahāg", source: "Middle Persian" }
      - { form: "Zahhāk", source: "New Persian (Shāhnāmeh)" }
    chosen: "Aži Dahāka (with diacritics) as primary form; thereafter 'the dragon' where context allows; Zahhāk flagged only when the Shāhnāmeh is under discussion"
    rationale: "Avestan form is the scholarly anchor; the three-headed philological cognancy with Vedic tri-śīrṣan vṛtra depends on the Avestan name."
    first_mention_gloss: "three-headed, six-eyed, three-jawed dragon-tyrant of the Avestan tradition; originally a creature of Angra Mainyu; bound under Mount Damāvand until Frashokereti (Middle Persian Dahāg; New Persian Zahhāk)"
    never_use: ["Azhi Dahaka (without diacritics, outside non-scholarly contexts)"]

  - native: "Ahura Mazdā"
    renderings_considered:
      - { form: "Ahura Mazdā", source: "Avestan with long ā" }
      - { form: "Ahura Mazda", source: "non-diacritical" }
      - { form: "Ohrmazd", source: "Middle Persian" }
    chosen: "Ahura Mazdā in Avestan contexts; Ohrmazd where Pahlavi sources are cited"
    rationale: "Standard diacritical; matches Aži Dahāka handling."
    first_mention_gloss: "'the Wise Lord'; creator-god in Zoroastrian cosmology (Middle Persian Ohrmazd)"
    never_use: []

  - native: "Angra Mainyu"
    renderings_considered:
      - { form: "Angra Mainyu", source: "Avestan" }
      - { form: "Ahriman", source: "Middle Persian" }
    chosen: "Angra Mainyu in Avestan contexts; Ahriman where Pahlavi sources are under discussion"
    rationale: "Matches Ahura Mazdā handling."
    first_mention_gloss: "'the evil spirit'; cosmic adversary of Ahura Mazdā in Zoroastrian dualism (Middle Persian Ahriman)"
    never_use: []

  - native: "Frashokereti"
    renderings_considered:
      - { form: "Frashokereti", source: "Avestan; Bundahišn scholarship" }
      - { form: "Frashegird", source: "Middle Persian" }
    chosen: "Frashokereti"
    rationale: "Most common form in English Zoroastrian studies."
    first_mention_gloss: "the final renovation; Zoroastrian eschatological end-time in which Aži Dahāka is slain a second (and final) time by the revived Kərəsāspa"
    never_use: []

  - native: "Kərəsāspa"
    renderings_considered:
      - { form: "Kərəsāspa", source: "Avestan with schwa-diacritics" }
      - { form: "Keresaspa", source: "anglicized" }
      - { form: "Garshāsp", source: "New Persian" }
    chosen: "Kərəsāspa at first scholarly mention; 'Keresaspa' in subsequent body prose"
    rationale: "Full diacritical form preserves the Avestan philology; simpler spelling keeps body prose readable."
    first_mention_gloss: "Avestan hero (anglicized Keresaspa); sleeps in a long stasis and is revived at Frashokereti to slay the rebound Aži Dahāka"
    never_use: []

  - native: "Damāvand"
    renderings_considered:
      - { form: "Damāvand", source: "Persian with long ā" }
      - { form: "Damavand", source: "anglicized" }
    chosen: "Damāvand"
    rationale: "The long ā is standard in Iranian studies transliteration."
    first_mention_gloss: "mountain of the Alborz range in northern Iran under which Aži Dahāka is bound in the Pahlavi tradition"
    never_use: []

  # ── India ────────────────────────────────────────────────────────────

  - native: "Indra"
    renderings_considered:
      - { form: "Indra", source: "Jamison & Brereton 2014; universal" }
    chosen: "Indra"
    rationale: "Universal."
    first_mention_gloss: "Vedic storm-god; chief of the Rigvedic gods; wielder of the vajra; slayer of Vṛtra"
    never_use: []

  - native: "Vṛtra"
    renderings_considered:
      - { form: "Vṛtra", source: "Jamison & Brereton 2014; Benveniste & Renou 1934" }
      - { form: "Vritra", source: "non-diacritical" }
    chosen: "Vṛtra"
    rationale: "Diacritical (vocalic ṛ) is standard in Vedic scholarship and preserves the etymology vṛ- 'to obstruct'."
    first_mention_gloss: "serpent-demon whose name derives from Vedic vṛ- 'to obstruct'; the obstacle that blocks the cosmic waters; slain by Indra in RV 1.32"
    never_use: ["Vritra (outside titles of older sources)"]

  - native: "vajra"
    renderings_considered:
      - { form: "vajra", source: "Jamison & Brereton 2014" }
      - { form: "thunderbolt", source: "translation" }
    chosen: "vajra (on first mention); 'the vajra' or 'Indra's thunderbolt' in body prose"
    rationale: "Sanskrit term retains distinctness from Thor's Mjöllnir and Zeus's keraunos; translated at first mention."
    first_mention_gloss: "Indra's thunderbolt-mace, forged by Tvaṣṭṛ; the cosmic combat-weapon of the Rigveda"
    never_use: []

  - native: "Tvaṣṭṛ"
    renderings_considered:
      - { form: "Tvaṣṭṛ", source: "Jamison & Brereton 2014" }
      - { form: "Tvashtr", source: "anglicized" }
      - { form: "Tvashtar", source: "older older anglicization" }
    chosen: "Tvaṣṭṛ"
    rationale: "Diacritical standard in current Vedic scholarship."
    first_mention_gloss: "Vedic divine artisan; forges Indra's vajra"
    never_use: []

  - native: "soma"
    renderings_considered:
      - { form: "soma", source: "universal in Vedic studies" }
    chosen: "soma (lowercase, italicised on first mention)"
    rationale: "Common-noun Sanskrit term; italics on first mention only."
    first_mention_gloss: "the ritual drink (and deified plant) that fortifies Indra for combat"
    never_use: []

  - native: "ahi"
    renderings_considered:
      - { form: "ahi", source: "Jamison & Brereton 2014; Watkins 1995" }
    chosen: "ahi"
    rationale: "The load-bearing Vedic word for 'serpent' in the áhann áhim formula."
    first_mention_gloss: "'serpent' (Sanskrit); the word for Vṛtra in the áhann áhim formula; philologically cognate with Avestan aži"
    never_use: []

  - native: "Trita Āptya"
    renderings_considered:
      - { form: "Trita Āptya", source: "Jamison & Brereton 2014" }
      - { form: "Trita Aptya", source: "non-diacritical" }
    chosen: "Trita Āptya"
    rationale: "Diacritical; the figure's philological cognancy with Avestan Thraētaona is load-bearing."
    first_mention_gloss: "Vedic dragon-slayer cognate with Avestan Thraētaona; the older Indo-Iranian figure of the combat-myth stratum that Indra-Vṛtra superseded"
    never_use: []

  - native: "Krishna"
    renderings_considered:
      - { form: "Krishna", source: "universal English" }
      - { form: "Kṛṣṇa", source: "diacritical Sanskrit" }
    chosen: "Krishna (in body prose); Kṛṣṇa only in strict philological footnotes"
    rationale: "Reader recognition; the diacritical form would be pedantic outside citation."
    first_mention_gloss: "avatar of Viṣṇu; in the post-Vedic tradition subdues the serpent Kāliya by dancing on his heads"
    never_use: []

  - native: "Kāliya"
    renderings_considered:
      - { form: "Kāliya", source: "Sanskrit with ā" }
      - { form: "Kaliya", source: "non-diacritical" }
    chosen: "Kāliya"
    rationale: "Diacritical long-ā standard; the story is central to Vaishnava iconography."
    first_mention_gloss: "many-headed water-serpent of the Yamunā who poisons the river; subdued (not slain) by the child Krishna"
    never_use: []

  - native: "līlā"
    renderings_considered:
      - { form: "līlā", source: "Sanskrit; Vaishnava studies" }
      - { form: "lila", source: "anglicized" }
      - { form: "play", source: "translation" }
    chosen: "līlā (italicised, on first mention); 'sacred play' in body translation"
    rationale: "Technical Sanskrit; the Krishna-Kāliya episode is one of the classic examples."
    first_mention_gloss: "'sacred play'; the Vaishnava category in which divine action is construed as play rather than as combat"
    never_use: []

  - native: "nāga"
    renderings_considered:
      - { form: "nāga", source: "Sanskrit; Indic studies standard" }
      - { form: "naga", source: "non-diacritical" }
    chosen: "nāga (italicised on first mention)"
    rationale: "Technical Indic serpent-category; diacritical preferred."
    first_mention_gloss: "'serpent' (Sanskrit); a broad Indic category of serpent-beings, often of ambivalent moral valence — Kāliya is a nāga"
    never_use: []

  # ── Egypt ────────────────────────────────────────────────────────────

  - native: "Ra"
    renderings_considered:
      - { form: "Ra", source: "Faulkner 1972; most current Egyptology" }
      - { form: "Rē", source: "older scholarly with long-mark" }
      - { form: "Re", source: "variant without long-mark" }
    chosen: "Ra"
    rationale: "Current Egyptological convention; reader recognition."
    first_mention_gloss: "Egyptian sun-god; traverses the sky by day and the Duat by night in his solar barque; combats Apep nightly"
    never_use: []

  - native: "Apep / Apophis"
    renderings_considered:
      - { form: "Apep", source: "Egyptian-language form; Faulkner 1972" }
      - { form: "Apophis", source: "Greek form of the name; te Velde 1967" }
    chosen: "Apep in body prose; 'Apophis' noted as the Greek form at first mention"
    rationale: "Apep preserves the Egyptian register; Apophis is the Hellenistic reception-name and appears in some secondary scholarship."
    first_mention_gloss: "the chaos-serpent; Ra's nightly adversary in the Duat; embodiment of isfet (Greek: Apophis)"
    never_use: []

  - native: "Seth / Sutekh"
    renderings_considered:
      - { form: "Seth", source: "Faulkner 1972; te Velde 1967" }
      - { form: "Sutekh", source: "Hittite treaty usage; Ramesside period" }
      - { form: "Sēt", source: "with length-mark, less common" }
    chosen: "Seth as body-prose default; 'Sutekh' only where the Hittite-Egyptian interface is under discussion (Ramesses II treaties)"
    rationale: "Reader recognition; the Sutekh variant carries specific diplomatic-historical context."
    first_mention_gloss: "Egyptian god of storms and desert; Apep-slayer at the prow of the solar barque (Ch. 16) and, separately, murderer of Osiris (Ch. 17)"
    never_use: []

  - native: "Mehen"
    renderings_considered:
      - { form: "Mehen", source: "Faulkner 1972" }
    chosen: "Mehen"
    rationale: "Standard."
    first_mention_gloss: "serpent-coil deity who encircles and protects Ra in the solar barque"
    never_use: []

  - native: "Isis"
    renderings_considered:
      - { form: "Isis", source: "Greek and English standard" }
      - { form: "Aset", source: "Egyptian form" }
    chosen: "Isis"
    rationale: "Universal reader recognition."
    first_mention_gloss: "magic-working goddess; binds Apep with spells in the combat-corpus; in the Osiris cycle, wife of Osiris and mother of Horus"
    never_use: []

  - native: "Horus"
    renderings_considered:
      - { form: "Horus", source: "Greek and English standard" }
      - { form: "Hor", source: "Egyptian" }
    chosen: "Horus"
    rationale: "Universal."
    first_mention_gloss: "falcon-headed god; son of Isis and Osiris; opposes and eventually succeeds Seth in the Contendings"
    never_use: []

  - native: "maʿat"
    renderings_considered:
      - { form: "maʿat", source: "Assmann 2001; standard Egyptological" }
      - { form: "maat", source: "anglicized" }
      - { form: "Ma'at", source: "sometimes used for the personified goddess" }
    chosen: "maʿat (with the ʿayin) for the concept; 'Maʿat' capitalised when the personified goddess is meant"
    rationale: "Assmann's diacritical is standard in English-language Egyptology."
    first_mention_gloss: "truth, order, justice; the cosmic order preserved by Ra's victory over Apep"
    never_use: []

  - native: "isfet"
    renderings_considered:
      - { form: "isfet", source: "Assmann 2001" }
    chosen: "isfet"
    rationale: "Standard; paired with maʿat throughout."
    first_mention_gloss: "disorder, injustice, chaos; the condition Apep personifies; the antithesis of maʿat"
    never_use: []

  - native: "Duat"
    renderings_considered:
      - { form: "Duat", source: "Faulkner 1972" }
      - { form: "Dat", source: "older transliteration" }
    chosen: "Duat"
    rationale: "Current standard."
    first_mention_gloss: "the Egyptian netherworld through which Ra's solar barque travels at night"
    never_use: []

  # ── Norse / Germanic / Celtic ────────────────────────────────────────

  - native: "Thor"
    renderings_considered:
      - { form: "Thor", source: "Larrington 2014; universal" }
      - { form: "Þórr", source: "Old Norse" }
    chosen: "Thor (body prose); 'Þórr' only in philological footnotes"
    rationale: "Reader recognition."
    first_mention_gloss: "Norse storm-god; son of Óðinn; wielder of Mjöllnir; adversary of Jörmungandr"
    never_use: []

  - native: "Jörmungandr / Midgard Serpent"
    renderings_considered:
      - { form: "Jörmungandr", source: "Faulkes 1987; standard" }
      - { form: "Miðgarðsormr", source: "Old Norse 'Midgard-serpent'" }
      - { form: "Midgard Serpent", source: "English translation" }
    chosen: "Jörmungandr (with umlaut) as name; 'the Midgard Serpent' as descriptive English gloss"
    rationale: "Both are ancient; the name-and-epithet pairing is how Snorri and the Eddic poems both handle it."
    first_mention_gloss: "the world-encircling serpent; Loki's son; slain by and slaying Thor at Ragnarök (Old Norse Miðgarðsormr)"
    never_use: []

  - native: "Mjöllnir"
    renderings_considered:
      - { form: "Mjöllnir", source: "Larrington 2014; standard English" }
      - { form: "Mjǫllnir", source: "normalized Old Norse" }
    chosen: "Mjöllnir"
    rationale: "Standard English rendering with the umlaut."
    first_mention_gloss: "Thor's hammer; forged by the dwarves; the storm-god's combat-weapon"
    never_use: []

  - native: "Ragnarök"
    renderings_considered:
      - { form: "Ragnarök", source: "standard English with umlaut" }
      - { form: "Ragnarǫk", source: "normalized Old Norse" }
      - { form: "Ragnarok", source: "without umlaut" }
    chosen: "Ragnarök"
    rationale: "Umlaut preserved; standard in English scholarship."
    first_mention_gloss: "'doom of the gods'; the Norse eschatological end, at which Thor and Jörmungandr slay each other"
    never_use: []

  - native: "Miðgarðr"
    renderings_considered:
      - { form: "Miðgarðr", source: "Old Norse; Faulkes 1987" }
      - { form: "Midgard", source: "anglicized" }
    chosen: "Midgard (body prose); Miðgarðr at first mention and in philological notes"
    rationale: "Reader recognition; the Old Norse form is preserved at first mention."
    first_mention_gloss: "'middle enclosure'; the world of humans, encircled by Jörmungandr"
    never_use: []

  - native: "Loki"
    renderings_considered:
      - { form: "Loki", source: "universal" }
    chosen: "Loki"
    rationale: "Universal."
    first_mention_gloss: "Norse trickster god; father of Jörmungandr, Fenrir, and Hel"
    never_use: []

  - native: "Sigurd / Siegfried"
    renderings_considered:
      - { form: "Sigurd", source: "Larrington 2014 (Old Norse)" }
      - { form: "Sigurðr", source: "Old Norse philological" }
      - { form: "Siegfried", source: "Middle High German (Nibelungenlied)" }
    chosen: "Sigurd in Old-Norse contexts; Siegfried where the Nibelungenlied is under discussion"
    rationale: "Each form belongs to a distinct textual tradition."
    first_mention_gloss: "Norse hero (Middle High German Siegfried); slays the dragon Fáfnir and tastes his blood, gaining knowledge of birdspeech"
    never_use: []

  - native: "Fáfnir"
    renderings_considered:
      - { form: "Fáfnir", source: "Larrington 2014" }
      - { form: "Fafnir", source: "without diacritic" }
    chosen: "Fáfnir"
    rationale: "Diacritical standard."
    first_mention_gloss: "dwarf transformed into a dragon by cursed gold; slain by Sigurd in Fáfnismál"
    never_use: []

  - native: "Beowulf"
    renderings_considered:
      - { form: "Beowulf", source: "universal; Klaeber 2008" }
    chosen: "Beowulf"
    rationale: "Universal."
    first_mention_gloss: "Geatish hero of the Old English poem Beowulf; kills Grendel, Grendel's mother, and finally the hoard-dragon"
    never_use: []

  - native: "Grendel"
    renderings_considered:
      - { form: "Grendel", source: "universal" }
    chosen: "Grendel"
    rationale: "Universal."
    first_mention_gloss: "man-eating monster of the poem Beowulf; descendant of Cain"
    never_use: []

  - native: "Lugh"
    renderings_considered:
      - { form: "Lugh", source: "Irish; Cath Maige Tuired scholarship" }
      - { form: "Lug", source: "older orthography" }
    chosen: "Lugh"
    rationale: "Modern Irish scholarly standard."
    first_mention_gloss: "Tuatha Dé Danann warrior-king; slays Balor of the Fomorians at the Second Battle of Mag Tuired"
    never_use: []

  - native: "Balor"
    renderings_considered:
      - { form: "Balor", source: "Cath Maige Tuired" }
    chosen: "Balor"
    rationale: "Standard."
    first_mention_gloss: "evil-eyed Fomorian; grandfather-adversary of Lugh; killed by a sling-stone to the eye"
    never_use: []

  - native: "Vahagn"
    renderings_considered:
      - { form: "Vahagn", source: "Russell 1987 (Armenian)" }
      - { form: "Vahagn Vishapakagh", source: "with dragon-slayer epithet" }
    chosen: "Vahagn"
    rationale: "Short form in body prose; the epithet glossed at first mention."
    first_mention_gloss: "Armenian storm-god, called Vishapakagh 'dragon-reaper'; combat-hero of Armenian mythology; attestation is fragmentary (Khorenatsi's paraphrase)"
    never_use: []

  - native: "vishap"
    renderings_considered:
      - { form: "vishap", source: "Russell 1987" }
      - { form: "višap", source: "diacritical transliteration" }
    chosen: "vishap (lowercase, as common noun)"
    rationale: "English-language Armenian studies uses the sh-spelling."
    first_mention_gloss: "Armenian 'dragon'; also the name given to the second-millennium-BCE stone stelae (vishapakar) associated with the cult"
    never_use: []

  - native: "Batraz"
    renderings_considered:
      - { form: "Batraz", source: "Nart saga scholarship; Dumézil" }
      - { form: "Batyr'adz", source: "Ossetic alternative" }
    chosen: "Batraz"
    rationale: "Standard form in Indo-European comparative studies."
    first_mention_gloss: "steel-bodied Nart warrior of Ossetic epic tradition; Dumézil reads him as the Scytho-Alanic IE dragon-slayer reflex"
    never_use: []

  # ── Slavic ───────────────────────────────────────────────────────────

  - native: "Perun"
    renderings_considered:
      - { form: "Perun", source: "West 2007; Ivanov & Toporov" }
    chosen: "Perun"
    rationale: "Universal."
    first_mention_gloss: "Slavic storm-god; in Ivanov and Toporov's contested reconstruction, the pursuer of Veles"
    never_use: []

  - native: "Veles"
    renderings_considered:
      - { form: "Veles", source: "standard" }
      - { form: "Volos", source: "East Slavic variant" }
    chosen: "Veles"
    rationale: "Standard in Ivanov/Toporov and the scholarly literature on the 'basic myth'."
    first_mention_gloss: "Slavic earth / cattle / underworld deity; reconstructed as Perun's adversary in the 'basic myth' — a reconstruction contested by Jakobson, Lajoye, and others"
    never_use: []

  - native: "Dobrynya Nikitich"
    renderings_considered:
      - { form: "Dobrynya Nikitich", source: "bylina scholarship; Oinas" }
      - { form: "Dobrynia", source: "variant transliteration" }
    chosen: "Dobrynya Nikitich"
    rationale: "Standard transliteration."
    first_mention_gloss: "bogatyr of the East Slavic bylina tradition; slays the dragon Zmey Gorynych"
    never_use: []

  - native: "Zmey Gorynych"
    renderings_considered:
      - { form: "Zmey Gorynych", source: "bylina scholarship" }
      - { form: "Zmei Gorynich", source: "variant" }
    chosen: "Zmey Gorynych"
    rationale: "Common in English bylina translation."
    first_mention_gloss: "three-headed dragon of East Slavic epic; adversary of Dobrynya Nikitich"
    never_use: []

  # ── East Asia ────────────────────────────────────────────────────────

  - native: "Gonggong"
    renderings_considered:
      - { form: "Gonggong", source: "Pinyin; Lewis 2006" }
      - { form: "Kung-kung", source: "Wade-Giles" }
    chosen: "Gonggong"
    rationale: "Pinyin is current standard; reader recognition."
    first_mention_gloss: "Chinese water-god, often red-haired and serpent-bodied; defeated combatant who shatters Mount Buzhou, the sky-pillar"
    never_use: ["Kung-kung (outside Wade-Giles-era source discussions)"]

  - native: "Zhuanxu"
    renderings_considered:
      - { form: "Zhuanxu", source: "Pinyin; Lewis 2006" }
      - { form: "Chuan-hsü", source: "Wade-Giles" }
    chosen: "Zhuanxu"
    rationale: "Pinyin standard."
    first_mention_gloss: "sky-emperor who defeats Gonggong in the most widely attested version"
    never_use: []

  - native: "Zhurong"
    renderings_considered:
      - { form: "Zhurong", source: "Pinyin" }
      - { form: "Chu-jung", source: "Wade-Giles" }
    chosen: "Zhurong"
    rationale: "Pinyin."
    first_mention_gloss: "fire-god; alternative combatant against Gonggong in some variants"
    never_use: []

  - native: "Nüwa"
    renderings_considered:
      - { form: "Nüwa", source: "Pinyin with umlaut" }
      - { form: "Nügua", source: "alternative Pinyin" }
      - { form: "Nü-kua", source: "Wade-Giles" }
    chosen: "Nüwa"
    rationale: "Current Pinyin standard; umlaut preserved."
    first_mention_gloss: "serpent-tailed creator-goddess; repairs the broken sky with five-coloured stones after Gonggong's combat"
    never_use: []

  - native: "Mount Buzhou"
    renderings_considered:
      - { form: "Mount Buzhou", source: "Pinyin" }
      - { form: "Buzhoushan", source: "Chinese one-word form" }
      - { form: "Pu-chou", source: "Wade-Giles" }
    chosen: "Mount Buzhou"
    rationale: "English-reader-friendly with Pinyin core."
    first_mention_gloss: "'mountain-that-is-not-whole'; the cosmic pillar broken by Gonggong's head-blow"
    never_use: []

  - native: "Yu the Great"
    renderings_considered:
      - { form: "Yu the Great", source: "universal" }
      - { form: "Da Yu", source: "Pinyin" }
      - { form: "Yü", source: "Wade-Giles" }
    chosen: "Yu the Great"
    rationale: "Standard English."
    first_mention_gloss: "post-combat flood-controller in Chinese tradition; his hydraulic-ordering role is the sidebar contrast within the Gonggong chapter"
    never_use: []

  - native: "Hou Yi"
    renderings_considered:
      - { form: "Hou Yi", source: "Pinyin; Lewis 2006; Birrell 1993" }
      - { form: "Hou I", source: "Wade-Giles" }
    chosen: "Hou Yi"
    rationale: "Pinyin."
    first_mention_gloss: "Chinese archer-hero; shoots down nine of the ten suns and slays monstrous beasts under sage-king Yao"
    never_use: []

  - native: "Susanoo"
    renderings_considered:
      - { form: "Susanoo", source: "Philippi 1968" }
      - { form: "Susanoo-no-Mikoto", source: "with honorific" }
      - { form: "Susano-o", source: "hyphenated variant" }
    chosen: "Susanoo"
    rationale: "Philippi's form; standard in current English-language Japanese studies."
    first_mention_gloss: "Japanese storm-god; expelled from heaven for misdeeds; slays Yamata no Orochi at Izumo"
    never_use: []

  - native: "Yamata no Orochi"
    renderings_considered:
      - { form: "Yamata no Orochi", source: "Philippi 1968" }
      - { form: "Yamato no Orochi", source: "misreading, avoid" }
      - { form: "the eight-forked serpent", source: "translation" }
    chosen: "Yamata no Orochi"
    rationale: "Philippi's form; the -ta- (not -to-) is correct."
    first_mention_gloss: "eight-headed, eight-tailed serpent of Izumo; slain by Susanoo; its tail contains the sword Kusanagi"
    never_use: ["Yamato no Orochi"]

  - native: "Kusanagi"
    renderings_considered:
      - { form: "Kusanagi", source: "Philippi 1968" }
      - { form: "Kusanagi-no-Tsurugi", source: "with sword-noun" }
    chosen: "Kusanagi"
    rationale: "Shorter form in body prose."
    first_mention_gloss: "'grass-cutter'; the sword found in Orochi's tail; one of the Three Sacred Treasures of the Japanese imperial regalia"
    never_use: []

  - native: "Ülgen / Erlik"
    renderings_considered:
      - { form: "Ülgen", source: "Turkic/Altaic; Eliade" }
      - { form: "Erlik", source: "standard Turkic/Altaic" }
    chosen: "Ülgen (with umlaut) and Erlik"
    rationale: "Standard in Altaic/Turkic studies; umlaut preserved on Ülgen."
    first_mention_gloss: "paired Altaic/Turkic-Mongol sky-god and underworld-god; a dualistic cosmology rather than a decisive combat"
    never_use: []

  - native: "Bakunawa"
    renderings_considered:
      - { form: "Bakunawa", source: "Philippine folklore scholarship; Eugenio" }
    chosen: "Bakunawa"
    rationale: "Standard across Visayan / Bikol / English sources."
    first_mention_gloss: "Philippine (Visayan / Bikol) serpent-dragon; devours six of the seven original moons; driven off during eclipses by communal noise-making"
    never_use: []

  # ── Americas ─────────────────────────────────────────────────────────

  - native: "Huitzilopochtli"
    renderings_considered:
      - { form: "Huitzilopochtli", source: "Nahuatl; Matos Moctezuma 1988; Carrasco 1999" }
    chosen: "Huitzilopochtli"
    rationale: "Universal."
    first_mention_gloss: "'Hummingbird-of-the-South'; Mexica patron god; sun-warrior born fully armed at Coatepec"
    never_use: []

  - native: "Coatlicue"
    renderings_considered:
      - { form: "Coatlicue", source: "Nahuatl standard" }
    chosen: "Coatlicue"
    rationale: "Universal."
    first_mention_gloss: "'She-of-the-Serpent-Skirt'; earth-goddess mother of Huitzilopochtli"
    never_use: []

  - native: "Coyolxauhqui"
    renderings_considered:
      - { form: "Coyolxauhqui", source: "Nahuatl; Matos Moctezuma 1988" }
    chosen: "Coyolxauhqui"
    rationale: "Universal."
    first_mention_gloss: "'Bells-on-Her-Cheeks'; moon-goddess; Huitzilopochtli's elder sister; dismembered in the combat and represented on the massive Templo Mayor stone"
    never_use: []

  - native: "Centzon Huitznahua"
    renderings_considered:
      - { form: "Centzon Huitznahua", source: "Nahuatl; Matos Moctezuma 1988" }
      - { form: "Centzonhuitznahua", source: "one-word variant" }
    chosen: "Centzon Huitznahua"
    rationale: "Two-word form standard in current Nahuatl scholarship."
    first_mention_gloss: "'Four Hundred Southerners'; Huitzilopochtli's stellar brothers; defeated with Coyolxauhqui"
    never_use: []

  - native: "Coatepec"
    renderings_considered:
      - { form: "Coatepec", source: "Nahuatl; Matos Moctezuma 1988" }
    chosen: "Coatepec"
    rationale: "Universal."
    first_mention_gloss: "'Mountain of Serpents'; the cosmic mountain of Huitzilopochtli's birth and combat; architecturally re-embodied as the Templo Mayor"
    never_use: []

  - native: "Templo Mayor"
    renderings_considered:
      - { form: "Templo Mayor", source: "Spanish; universal" }
      - { form: "Great Temple", source: "English translation" }
    chosen: "Templo Mayor"
    rationale: "Spanish is the discipline-standard name."
    first_mention_gloss: "the great double-stair pyramid at the center of Tenochtitlan; built as Coatepec — the architecture embodies the combat-narrative"
    never_use: []

  - native: "Panquetzaliztli"
    renderings_considered:
      - { form: "Panquetzaliztli", source: "Nahuatl" }
    chosen: "Panquetzaliztli"
    rationale: "Standard."
    first_mention_gloss: "Mexica winter-solstice festival commemorating Huitzilopochtli's victory"
    never_use: []

  - native: "Quetzalcoatl"
    renderings_considered:
      - { form: "Quetzalcoatl", source: "Nahuatl standard" }
    chosen: "Quetzalcoatl"
    rationale: "Universal."
    first_mention_gloss: "'Feathered Serpent'; Mesoamerican creator-deity; alternating with Tezcatlipoca across the Suns cycle"
    never_use: []

  - native: "Tezcatlipoca"
    renderings_considered:
      - { form: "Tezcatlipoca", source: "Nahuatl standard" }
    chosen: "Tezcatlipoca"
    rationale: "Universal."
    first_mention_gloss: "'Smoking Mirror'; Mesoamerican sorcerer-deity; alternates sovereignty with Quetzalcoatl"
    never_use: []

  - native: "Cipactli"
    renderings_considered:
      - { form: "Cipactli", source: "Nahuatl; López Austin 1993" }
    chosen: "Cipactli"
    rationale: "Standard."
    first_mention_gloss: "primordial earth-monster dismembered by Quetzalcoatl and Tezcatlipoca to form sky and earth; the book's boundary case for dismemberment-vs-combat cosmogony"
    never_use: []

  - native: "Pariacaca"
    renderings_considered:
      - { form: "Pariacaca", source: "Salomon & Urioste 1991" }
      - { form: "Pariaqaqa", source: "modern Quechua orthography" }
    chosen: "Pariacaca"
    rationale: "Matches the Huarochirí Manuscript's 1608 spelling as edited by Salomon & Urioste."
    first_mention_gloss: "Andean storm-wak'a of the Huarochirí region; defeats rival wak'as and their summoned amaru"
    never_use: []

  - native: "wak'a"
    renderings_considered:
      - { form: "wak'a", source: "modern Quechua orthography; post-2010 decolonial Andean scholarship" }
      - { form: "huaca", source: "Salomon & Urioste 1991; Huarochirí-Manuscript-era Spanish-derived spelling" }
    chosen: "wak'a (lowercase, italicised on first mention)"
    rationale: "Modern Quechua orthography, now standard in post-2010 decolonial Andean scholarship; lay English readers are not heavily invested in the older 'huaca' form, so adopting the Quechua-native spelling comes at low cost. First-mention parenthetical may note the older Spanish-colonial form 'huaca' where helpful for readers consulting Salomon & Urioste 1991."
    first_mention_gloss: "Andean 'sacred power-being' (Quechua; older Spanish-derived spelling: huaca); the Huarochirí Manuscript records a landscape populated with wak'as in hierarchical and combative relationships — the pattern is wak'a-succession, not chaos-versus-order"
    never_use: []

  - native: "amaru"
    renderings_considered:
      - { form: "amaru", source: "Salomon & Urioste 1991" }
      - { form: "amaro", source: "variant" }
    chosen: "amaru (lowercase, italicised on first mention)"
    rationale: "Andean serpent-figure; common noun."
    first_mention_gloss: "Andean serpent-figure; often summoned as an ally-monster by a defeated rival wak'a, rather than a primordial chaos"
    never_use: []

  - native: "Kai-Kai / Tren-Tren"
    renderings_considered:
      - { form: "Kai-Kai and Tren-Tren", source: "Mapuche ethnographic literature" }
      - { form: "Caicai / Trentren", source: "Spanish-orthography variants" }
    chosen: "Kai-Kai and Tren-Tren (hyphenated, with capital initials)"
    rationale: "Most common form in English-language Mapuche scholarship."
    first_mention_gloss: "paired Mapuche marine and mountain serpents; their combat raises flood-and-mountain, generating the Mapuche landscape"
    never_use: []

  - native: "Bida"
    renderings_considered:
      - { form: "Bida", source: "Conrad 2005; Belcher 1999" }
    chosen: "Bida"
    rationale: "Standard."
    first_mention_gloss: "seven-headed serpent-protector of Wagadu (ancient Ghana) in Soninke tradition; his slaying ends Wagadu's prosperity — the inversion case"
    never_use: []

  - native: "Wagadu"
    renderings_considered:
      - { form: "Wagadu", source: "Conrad 2005; Belcher 1999" }
      - { form: "ancient Ghana", source: "historical name of the polity" }
    chosen: "Wagadu (tradition-internal name); 'ancient Ghana' for the historical-polity reading"
    rationale: "Each name belongs to a distinct register."
    first_mention_gloss: "the Soninke city/polity protected by Bida; historical ancient Ghana; abandoned after Bida's death"
    never_use: []

  - native: "Mamadi Sefe Dekote"
    renderings_considered:
      - { form: "Mamadi Sefe Dekote", source: "Conrad 2005; Belcher 1999" }
    chosen: "Mamadi Sefe Dekote"
    rationale: "Standard Soninke-tradition form in English."
    first_mention_gloss: "the suitor who kills Bida to save his beloved, thereby ending Wagadu"
    never_use: []

  - native: "Mwindo"
    renderings_considered:
      - { form: "Mwindo", source: "Biebuyck & Mateene 1969" }
    chosen: "Mwindo"
    rationale: "Standard."
    first_mention_gloss: "Nyanga epic hero; kills the dragon Kirimu and is punished by the sky-god Nkuba — the contrastive case"
    never_use: []

  - native: "Kirimu"
    renderings_considered:
      - { form: "Kirimu", source: "Biebuyck & Mateene 1969" }
    chosen: "Kirimu"
    rationale: "Standard."
    first_mention_gloss: "Nyanga dragon slain by Mwindo"
    never_use: []

  - native: "Nkuba"
    renderings_considered:
      - { form: "Nkuba", source: "Biebuyck & Mateene 1969" }
    chosen: "Nkuba"
    rationale: "Standard."
    first_mention_gloss: "Nyanga sky-god; punishes Mwindo for the killing of Kirimu"
    never_use: []

  - native: "Nanabozho"
    renderings_considered:
      - { form: "Nanabozho", source: "Hallowell 1960; standard in Anishinaabe studies" }
      - { form: "Nanabush", source: "alternative spelling" }
      - { form: "Wenabozho", source: "other regional variant" }
    chosen: "Nanabozho"
    rationale: "Most common in Hallowell and the Great Lakes scholarship; area-specialist citation policy dictates following the specialists."
    first_mention_gloss: "Anishinaabe trickster-culture-hero; his relations with the underwater manitou Mishipeshu and the Thunderers are the book's clearest case of a tradition whose own framework declines the chaoskampf reading"
    never_use: []

  - native: "Mishipeshu"
    renderings_considered:
      - { form: "Mishipeshu", source: "Anishinaabe studies standard" }
      - { form: "Mishebeshu", source: "Theresa S. Smith 1995" }
      - { form: "Mishipizheu", source: "variant" }
    chosen: "Mishipeshu"
    rationale: "Most common in English-language Anishinaabe studies; variant spellings flagged in the Ch. 32 footnotes."
    first_mention_gloss: "Anishinaabe underwater manitou; in the tradition's own framework a necessary counterpart to the Thunderers, not a chaos-adversary to be defeated"
    never_use: []

  - native: "manitou / manitouk / aadizookaanag"
    renderings_considered:
      - { form: "manitou (sing.) / manitouk (pl.)", source: "Hallowell 1960" }
      - { form: "manito / manidoog", source: "other orthography" }
      - { form: "aadizookaanag", source: "Basil Johnston's term for the sacred-story beings" }
    chosen: "manitou (singular) / manitouk (plural); 'aadizookaanag' glossed separately for the sacred-story class of beings"
    rationale: "Hallowell's orthography is the scholarly standard; Johnston's aadizookaanag is a distinct category that some of the Ch. 32 material invokes."
    first_mention_gloss: "'other-than-human person' in the Anishinaabe ontological category; the Thunderers and Mishipeshu are manitouk"
    never_use: []

  - native: "the Thunderers"
    renderings_considered:
      - { form: "the Thunderers", source: "Hallowell 1960; standard in English" }
      - { form: "Animikiig", source: "Anishinaabemowin" }
    chosen: "the Thunderers (English); Animikiig in first-mention gloss"
    rationale: "English form is accessible; the native term is preserved for attribution."
    first_mention_gloss: "the Anishinaabe thunder-beings (Animikiig); counterparts of Mishipeshu in the reciprocal cosmic-dialectic"
    never_use: []

  - native: "Väinämöinen"
    renderings_considered:
      - { form: "Väinämöinen", source: "Finnish standard" }
      - { form: "Vainamoinen", source: "without umlauts" }
    chosen: "Väinämöinen"
    rationale: "Umlauts preserved; the name is the iconic Kalevala hero."
    first_mention_gloss: "Finnish shaman-sage hero; subdues the sea-monster Iku-Turso by song rather than combat, in the older rune tradition and in Lönnrot's Kalevala"
    never_use: []

  - native: "Iku-Turso"
    renderings_considered:
      - { form: "Iku-Turso", source: "Siikala 2002" }
      - { form: "Ikuturso", source: "one-word variant" }
    chosen: "Iku-Turso"
    rationale: "Hyphenated form standard in English-language Kalevala scholarship."
    first_mention_gloss: "Finnic sea-monster; subdued by Väinämöinen's song; presentation in the chapter separates older rune material from Lönnrot's 19th-century editorial synthesis"
    never_use: []

  # ══════════════════════════════════════════════════════════════════════
  # PLACE NAMES AND CULT SITES
  # ══════════════════════════════════════════════════════════════════════

  - native: "Nerik"
    renderings_considered:
      - { form: "Nerik", source: "Hoffner 1998" }
    chosen: "Nerik"
    rationale: "Standard."
    first_mention_gloss: "northern Hittite cult-centre of the storm-god; locus of the purulli festival"
    never_use: []

  - native: "Delphi / Pytho"
    renderings_considered:
      - { form: "Delphi", source: "later standard" }
      - { form: "Pytho", source: "Homeric Hymn; earlier name" }
    chosen: "Delphi (body-prose default); Pytho when naming the older / Homeric-Hymn-era site"
    rationale: "Preserves textual specificity."
    first_mention_gloss: "Apollo's oracle-site in Phocis (earlier name Pytho); the Septerion festival re-enacted the Python-slaying there every eight years"
    never_use: []

  - native: "Mount Etna"
    renderings_considered:
      - { form: "Mount Etna", source: "standard English" }
      - { form: "Aitnē", source: "Greek" }
    chosen: "Mount Etna"
    rationale: "Reader recognition."
    first_mention_gloss: "Sicilian volcano under which Typhon is said to be buried in the post-Hesiodic tradition"
    never_use: []

  - native: "Tartarus"
    renderings_considered:
      - { form: "Tartarus", source: "Hesiod; standard English" }
      - { form: "Tartaros", source: "Greek" }
    chosen: "Tartarus"
    rationale: "Reader recognition."
    first_mention_gloss: "the lowest realm of the Greek underworld; father of Typhon in the Theogony; prison of the defeated Titans"
    never_use: []

  - native: "Coatepec (place name)"
    renderings_considered:
      - { form: "Coatepec", source: "as per deity-name entry" }
    chosen: "Coatepec"
    rationale: "See deity-context entry; the place-name and the combat-site are the same name."
    first_mention_gloss: "see Huitzilopochtli entry — the mountain, the birth-place, and the Templo Mayor's architectural referent are the same Coatepec"
    never_use: []

  # ══════════════════════════════════════════════════════════════════════
  # RITUAL, CULTIC, AND TECHNICAL TERMS
  # ══════════════════════════════════════════════════════════════════════

  - native: "bogatyr"
    renderings_considered:
      - { form: "bogatyr", source: "Russian bylina scholarship" }
      - { form: "bogatyr'", source: "with soft-sign transliteration" }
    chosen: "bogatyr"
    rationale: "Standard English form in bylina scholarship."
    first_mention_gloss: "Russian-epic (bylina) warrior-hero; Dobrynya Nikitich is a bogatyr"
    never_use: []

  - native: "bylina"
    renderings_considered:
      - { form: "bylina (sing.) / byliny (pl.)", source: "Russian folklore scholarship" }
    chosen: "bylina (singular) / byliny (plural)"
    rationale: "Standard English form."
    first_mention_gloss: "East Slavic heroic epic-song genre, recorded from oral performance in the 19th century"
    never_use: []

  - native: "kenning"
    renderings_considered:
      - { form: "kenning", source: "Old Norse / Old English poetics; universal" }
    chosen: "kenning"
    rationale: "Standard."
    first_mention_gloss: "an Old Norse / Old English compressed metaphorical phrase; kennings for Jörmungandr (e.g., 'band of all lands') preserve the IE serpent-combat vocabulary that Watkins analyses"
    never_use: []

  - native: "bhakti"
    renderings_considered:
      - { form: "bhakti", source: "Indic studies standard" }
    chosen: "bhakti (italicised on first mention)"
    rationale: "Technical Sanskrit."
    first_mention_gloss: "'devotion'; the devotional-religious movement (Harivaṃśa, Viṣṇu Purāṇa, Bhāgavata Purāṇa onward) in which the Krishna-Kāliya story takes its classical form"
    never_use: []

  - native: "Contendings of Horus and Seth"
    renderings_considered:
      - { form: "Contendings of Horus and Seth", source: "standard English translation" }
      - { form: "Chester Beatty I", source: "papyrus designation" }
    chosen: "the Contendings (body prose); 'Chester Beatty I' at first mention and for papyrological contexts"
    rationale: "The text is usually cited by its English title in body prose and by papyrus number in source-critical contexts."
    first_mention_gloss: "the bawdy literary papyrus Chester Beatty I (c. 1160 BCE); the longest single narrative of the Horus-Seth contention"
    never_use: []

  - native: "Septerion"
    renderings_considered:
      - { form: "Septerion", source: "Plutarch; Fontenrose 1959" }
      - { form: "Stepterion", source: "variant spelling" }
    chosen: "Septerion"
    rationale: "Standard English spelling."
    first_mention_gloss: "Delphic festival held every eight years re-enacting Apollo's slaying of Python"
    never_use: []

  - native: "Shāhnāmeh"
    renderings_considered:
      - { form: "Shāhnāmeh", source: "Persian with diacritics" }
      - { form: "Shahnameh", source: "anglicized" }
      - { form: "Shāh-nāma", source: "philological" }
    chosen: "Shāhnāmeh"
    rationale: "Long-vowel diacriticals retained as scholarly standard."
    first_mention_gloss: "Ferdowsi's c. 1000 CE Persian national epic; the Zahhāk story is the New-Persian reception of the Aži-Dahāka myth"
    never_use: []

  - native: "Bundahišn"
    renderings_considered:
      - { form: "Bundahišn", source: "Middle-Persian scholarly" }
      - { form: "Bundahishn", source: "anglicized" }
    chosen: "Bundahišn"
    rationale: "Diacritical š preserved as standard in Iranian studies."
    first_mention_gloss: "Middle Persian (Pahlavi) compendium of Zoroastrian cosmology; late Sasanian / early Islamic redaction; principal source for the Frashokereti material"
    never_use: []

  - native: "Rigveda"
    renderings_considered:
      - { form: "Rigveda", source: "Jamison & Brereton 2014" }
      - { form: "Ṛgveda", source: "philological" }
      - { form: "Rig Veda", source: "older" }
    chosen: "Rigveda (body prose); Ṛgveda in diacritical citations"
    rationale: "Jamison & Brereton's book-title form."
    first_mention_gloss: "the earliest layer of Vedic Sanskrit religious poetry (c. 1500–1000 BCE); chief primary source for Indra-Vṛtra"
    never_use: ["Rig Veda (two words)"]

  - native: "Enūma Eliš"
    renderings_considered:
      - { form: "Enūma Eliš", source: "Lambert 2013 with diacriticals" }
      - { form: "Enuma Elish", source: "anglicized" }
    chosen: "Enūma Eliš"
    rationale: "Scholarly-standard diacriticals in current Assyriological writing."
    first_mention_gloss: "'When on High'; the Babylonian creation-and-combat epic; canonical Chaoskampf type-text since Gunkel 1895"
    never_use: []

  - native: "Lugal-e"
    renderings_considered:
      - { form: "Lugal-e", source: "van Dijk 1983; ETCSL (short title)" }
      - { form: "LUGAL UD ME-LÁM-bi NIR-ĜÁL", source: "full Sumerian incipit" }
    chosen: "Lugal-e"
    rationale: "Standard short title."
    first_mention_gloss: "'O King': the Sumerian composition narrating Ninurta's combat with Asag; named from its opening line"
    never_use: []

  - native: "Huarochirí Manuscript"
    renderings_considered:
      - { form: "Huarochirí Manuscript", source: "Salomon & Urioste 1991" }
      - { form: "Manuscrito de Huarochirí", source: "Spanish" }
    chosen: "Huarochirí Manuscript"
    rationale: "English scholarly standard."
    first_mention_gloss: "c. 1608 Quechua-language manuscript; the sole substantial primary source for pre-Columbian Huarochirí religion; principal anchor for the Pariacaca chapter"
    never_use: []

  - native: "Kalevala"
    renderings_considered:
      - { form: "Kalevala", source: "Finnish standard" }
    chosen: "Kalevala"
    rationale: "Universal."
    first_mention_gloss: "Elias Lönnrot's 1835 / 1849 composite epic of Finnic rune-poetry; the Iku-Turso material is partly older and partly Lönnrot's editorial synthesis"
    never_use: []

  - native: "Baal Cycle"
    renderings_considered:
      - { form: "Baal Cycle", source: "Smith 1994; standard" }
      - { form: "Baʿlu Cycle", source: "philological" }
    chosen: "Baal Cycle"
    rationale: "Standard in English Ugaritic scholarship."
    first_mention_gloss: "the Ugaritic tablet-group (KTU 1.1–1.6) comprising the Baal-Yamm combat, the palace-building, and the Baal-Mot narrative"
    never_use: []

  - native: "Kumarbi Cycle"
    renderings_considered:
      - { form: "Kumarbi Cycle", source: "Hoffner 1998" }
      - { form: "Song-cycle of Kumarbi", source: "alternative" }
    chosen: "Kumarbi Cycle"
    rationale: "Standard."
    first_mention_gloss: "the Hurro-Hittite song-cycle on the succession of kingship in heaven (Kingship in Heaven, Song of Ullikummi, Song of Hedammu, Song of the Sea)"
    never_use: []

  - native: "kur"
    renderings_considered:
      - { form: "kur", source: "ETCSL; Sumerian scholarship" }
    chosen: "kur (italicised)"
    rationale: "Technical Sumerian term; multiple senses flagged in gloss."
    first_mention_gloss: "Sumerian 'mountain / foreign land / netherworld'; the domain from which Asag's stone-army comes"
    never_use: []

  - native: "drakaina"
    renderings_considered:
      - { form: "drakaina", source: "Homeric Hymn to Apollo; Fontenrose 1959" }
    chosen: "drakaina (italicised)"
    rationale: "Technical Greek; the Python is originally a female drakaina in the Homeric Hymn."
    first_mention_gloss: "Greek 'she-dragon'; the feminine form of drakōn; the original Homeric-Hymn designation of the Delphic serpent before she is named Python"
    never_use: []

  - native: "Ouroboros"
    renderings_considered:
      - { form: "Ouroboros", source: "Greek-derived standard" }
      - { form: "Uroboros", source: "variant spelling" }
    chosen: "Ouroboros"
    rationale: "Most common English spelling."
    first_mention_gloss: "'tail-devourer'; the self-encircling serpent image widely spread across traditions; named as Greek in Hellenistic alchemical contexts; referenced in the reception coda"
    never_use: []

  - native: "Spartoi"
    renderings_considered:
      - { form: "Spartoi", source: "standard Greek-studies" }
      - { form: "Spartae", source: "Latinised" }
    chosen: "Spartoi"
    rationale: "Greek preserved."
    first_mention_gloss: "'Sown Men'; the warriors who spring from the teeth of the dragon Kadmos sows at Thebes"
    never_use: []

  - native: "the five Suns"
    renderings_considered:
      - { form: "the five Suns", source: "Mesoamerican studies; Carrasco 1999; López Austin 1993" }
      - { form: "the five ages", source: "alternative" }
    chosen: "the five Suns"
    rationale: "Standard in Mesoamericanist English."
    first_mention_gloss: "the Mesoamerican cycle of cosmic world-ages; Quetzalcoatl and Tezcatlipoca alternate as rulers, each age ending in catastrophe; the present age is the Fifth Sun"
    never_use: []

  - native: "Nart"
    renderings_considered:
      - { form: "Nart", source: "Ossetic studies standard" }
      - { form: "Narts", source: "pluralized in English" }
    chosen: "Nart (singular) / Narts (plural)"
    rationale: "Standard English form."
    first_mention_gloss: "heroic figures of the Ossetic and broader North Caucasian epic tradition; Batraz is a Nart"
    never_use: []

  # ══════════════════════════════════════════════════════════════════════
  # INDO-EUROPEAN AND COMPARATIVE-PHILOLOGICAL VOCABULARY
  # ══════════════════════════════════════════════════════════════════════

  - native: "Proto-Indo-European / PIE"
    renderings_considered:
      - { form: "Proto-Indo-European", source: "linguistic standard" }
      - { form: "PIE", source: "abbreviation" }
    chosen: "Proto-Indo-European (on first mention); PIE in subsequent technical use"
    rationale: "Standard."
    first_mention_gloss: "the reconstructed common ancestor of the Indo-European language family, spoken c. 4500–2500 BCE; Watkins's HERO SLAY SERPENT formula is a reconstructed PIE poetic element"
    never_use: []

  - native: "Indo-Iranian"
    renderings_considered:
      - { form: "Indo-Iranian", source: "standard" }
      - { form: "Aryan", source: "older; superseded and potentially problematic" }
    chosen: "Indo-Iranian"
    rationale: "'Aryan' is avoided outside specific historical-scholarship contexts where the term is itself the object of discussion."
    first_mention_gloss: "the branch of the Indo-European family that includes Indic (Vedic Sanskrit etc.) and Iranian (Avestan etc.); the Trita Āptya / Thraētaona cognancy is the clearest Indo-Iranian poetic pairing"
    never_use: ["Aryan (as a modern cover-term; older scholarly usage only when discussed as historiography)"]

  - native: "Watkins formula"
    renderings_considered:
      - { form: "Watkins formula", source: "internal shorthand" }
      - { form: "áhann áhim formula", source: "source-language shorthand" }
      - { form: "HERO SLAY SERPENT formula", source: "Watkins's own label" }
    chosen: "HERO SLAY SERPENT formula (technical); 'Watkins formula' (conversational shorthand)"
    rationale: "See HERO SLAY SERPENT entry; this entry locks the shorthand for running text."
    first_mention_gloss: "Calvert Watkins's reconstructed Indo-European poetic formula for dragon-slaying; see HERO SLAY SERPENT entry"
    never_use: []

deviations_from_instructions:
  - note: |
      The glossary includes several language-pair entries (e.g., "Ea / Enki", "Tarḫunna / Teshub",
      "Apep / Apophis", "Thraētaona / Fereydun") where a single deity figures in two or more
      language-strata used in the book. In each case, the chosen field specifies the
      context-conditional rendering rather than a single locked form. This is a slight
      expansion of the skill's single-rendering convention, but scope.md's "translation-mediated"
      policy and cross-cultural structure make context-sensitivity unavoidable.
  - note: |
      `never_use` is kept empty or minimal for most entries (per the stage instructions
      about cross-cultural books), used only where actual cross-tradition confusion risk
      exists (e.g., "Ningirsu" for Ninurta; "Yamato no Orochi" for Yamata no Orochi;
      "Kingu" for Qingu; "Zu" for Anzû).

self_checks:
  target_count_60_120: "181 terms — above the 60–120 target. The cross-cultural scope (15+ traditions) and the need to lock transliteration choices (per scope.md §'Languages of primary sources') justify the overshoot. On user review, some single-chapter proper nouns with unambiguous transliteration could be trimmed."
  every_recurring_figure_included: "Leviathan (Chs. 8, 9, 42, 43), Aži Dahāka (Chs. 13, 37, 43), Ninurta (Chs. 1, 2, 43), Tiamat (Chs. 3, 43), maʿat/isfet (Ch. 16, 17, 36), purulli (Ch. 6, 36), HERO SLAY SERPENT (Ch. 19, 38), Chaoskampf/combat myth (every chapter) — all present"
  cross_tradition_confusion_guarded:
    - "Ninurta vs. Ningirsu"
    - "Qingu vs. Kingu (orthographic only, but flagged)"
    - "Ea vs. Enki (language-context conditional)"
    - "Zu vs. Anzû (the old misreading)"
    - "Yamato vs. Yamata (for Orochi)"
  decision_flags_elevated_to_DECIDE_GLOSSARY: true
```

---

# Governing file: toc.yaml

```
# Table of Contents — Chaoskampf Across Cultures
# Final reading order, locked at chapter-briefs stage (2026-04-23).
# Structure follows scope.md §"Book structure" (v1, 2026-04-23).
# Every chapter listed here has a corresponding brief in briefs/NN-<slug>.yaml.

meta:
  book_slug: chaoskampf
  stage: chapter-briefs
  version: v1
  date: 2026-04-23
  agent_model: "claude-opus-4-7[1m]"

chapters:

  # ── Front matter ─────────────────────────────────────────────────
  - number: 0
    slug: introduction
    title: "What Chaoskampf is, and why the word is contested"
    part: front-matter
    chapter_anchor: "ch-00-introduction"
    brief: briefs/00-introduction.yaml

  # ── Part I — geographic clusters ─────────────────────────────────
  # Mesopotamia
  - number: 1
    slug: ninurta-asag
    title: "Ninurta vs. Asag (Lugal-e)"
    part: "part-i-mesopotamia"
    tier: core
    chapter_anchor: "ch-01-ninurta-asag"
    brief: briefs/01-ninurta-asag.yaml

  - number: 2
    slug: ninurta-anzu
    title: "Ninurta vs. Anzû"
    part: "part-i-mesopotamia"
    tier: core
    chapter_anchor: "ch-02-ninurta-anzu"
    brief: briefs/02-ninurta-anzu.yaml

  - number: 3
    slug: marduk-tiamat
    title: "Marduk vs. Tiamat (Enūma Eliš)"
    part: "part-i-mesopotamia"
    tier: core
    chapter_anchor: "ch-03-marduk-tiamat"
    brief: briefs/03-marduk-tiamat.yaml

  - number: 4
    slug: mesopotamian-minor
    title: "Minor Mesopotamian combats (Marduk/Labbu)"
    part: "part-i-mesopotamia"
    tier: related-family
    chapter_anchor: "ch-04-mesopotamian-minor"
    brief: briefs/04-mesopotamian-minor.yaml

  # Anatolia and Levant
  - number: 5
    slug: kumarbi-ullikummi
    title: "The Kumarbi Cycle (Ullikummi, Hedammu, Song of the Sea)"
    part: "part-i-anatolia-levant"
    tier: core
    chapter_anchor: "ch-05-kumarbi-ullikummi"
    brief: briefs/05-kumarbi-ullikummi.yaml
    note: "Hedammu and Song of the Sea treated as explicit sub-sections per audit-review-log.md decision."

  - number: 6
    slug: illuyanka
    title: "Tarḫunna vs. Illuyanka"
    part: "part-i-anatolia-levant"
    tier: core
    chapter_anchor: "ch-06-illuyanka"
    brief: briefs/06-illuyanka.yaml

  - number: 7
    slug: baal-yamm-lotan
    title: "Baal vs. Yamm and Baal vs. Lôtan"
    part: "part-i-anatolia-levant"
    tier: core
    chapter_anchor: "ch-07-baal-yamm-lotan"
    brief: briefs/07-baal-yamm-lotan.yaml

  # Hebrew Bible and Early Christianity
  - number: 8
    slug: yahweh-leviathan-rahab
    title: "Yahweh vs. Leviathan and Rahab"
    part: "part-i-hebrew-christian"
    tier: core
    chapter_anchor: "ch-08-yahweh-leviathan-rahab"
    brief: briefs/08-yahweh-leviathan-rahab.yaml
    note: "Bundled per audit-review-log.md decision — the Pss/Isa/Job/Hab corpus presented as one chapter with sub-sections."

  - number: 9
    slug: revelation-red-dragon
    title: "Michael vs. the Red Dragon (Revelation 12)"
    part: "part-i-hebrew-christian"
    tier: core
    chapter_anchor: "ch-09-revelation-red-dragon"
    brief: briefs/09-revelation-red-dragon.yaml

  - number: 10
    slug: christian-reception
    title: "St. George, St. Michael, and the Christian reception"
    part: "part-i-hebrew-christian"
    tier: related-family
    chapter_anchor: "ch-10-christian-reception"
    brief: briefs/10-christian-reception.yaml

  # Greece and Rome
  - number: 11
    slug: zeus-typhon
    title: "Zeus vs. Typhon"
    part: "part-i-greece-rome"
    tier: core
    chapter_anchor: "ch-11-zeus-typhon"
    brief: briefs/11-zeus-typhon.yaml

  - number: 12
    slug: greek-dragons-after-typhon
    title: "Greek dragon-combats after Zeus-Typhon (Apollo/Python, Herakles, Perseus, Kadmos, Bellerophon, Cacus)"
    part: "part-i-greece-rome"
    tier: related-family
    chapter_anchor: "ch-12-greek-dragons-after-typhon"
    brief: briefs/12-greek-dragons-after-typhon.yaml

  # Iran
  - number: 13
    slug: thraetaona-azidahaka
    title: "Thraētaona vs. Aži Dahāka (and Frashokereti)"
    part: "part-i-iran"
    tier: core
    chapter_anchor: "ch-13-thraetaona-azidahaka"
    brief: briefs/13-thraetaona-azidahaka.yaml
    note: "Frashokereti treated as eschatological sub-section of this chapter."

  # India
  - number: 14
    slug: indra-vrtra
    title: "Indra vs. Vṛtra"
    part: "part-i-india"
    tier: core
    chapter_anchor: "ch-14-indra-vrtra"
    brief: briefs/14-indra-vrtra.yaml

  - number: 15
    slug: vedic-reflexes
    title: "Vedic and post-Vedic reflexes (Trita Āptya, Krishna/Kāliya)"
    part: "part-i-india"
    tier: related-family
    chapter_anchor: "ch-15-vedic-reflexes"
    brief: briefs/15-vedic-reflexes.yaml

  # Egypt
  - number: 16
    slug: ra-apep
    title: "Ra vs. Apep"
    part: "part-i-egypt"
    tier: core
    chapter_anchor: "ch-16-ra-apep"
    brief: briefs/16-ra-apep.yaml

  - number: 17
    slug: horus-seth
    title: "Horus vs. Seth (an edge case)"
    part: "part-i-egypt"
    tier: related
    chapter_anchor: "ch-17-horus-seth"
    brief: briefs/17-horus-seth.yaml
    note: "INCLUSION-MARGINAL per audit-review-log.md; framing marker required in chapter."

  # Norse, Germanic, and IE reflexes
  - number: 18
    slug: thor-jormungandr
    title: "Thor vs. Jörmungandr (the Midgard Serpent)"
    part: "part-i-norse-ie"
    tier: core
    chapter_anchor: "ch-18-thor-jormungandr"
    brief: briefs/18-thor-jormungandr.yaml

  - number: 19
    slug: ie-reflexes
    title: "Indo-European reflexes of HERO SLAY SERPENT (Sigurd/Fáfnir, Beowulf, Lugh/Balor, Welsh Red-White, Batraz, Vahagn)"
    part: "part-i-norse-ie"
    tier: related-family
    chapter_anchor: "ch-19-ie-reflexes"
    brief: briefs/19-ie-reflexes.yaml

  - number: 20
    slug: slavic-baltic
    title: "Slavic and Baltic combat (Perun/Veles, Dobrynya byliny)"
    part: "part-i-slavic-baltic"
    tier: related-family
    chapter_anchor: "ch-20-slavic-baltic"
    brief: briefs/20-slavic-baltic.yaml

  # East Asia
  - number: 21
    slug: gonggong
    title: "Gonggong and the broken pillar"
    part: "part-i-east-asia"
    tier: core
    chapter_anchor: "ch-21-gonggong"
    brief: briefs/21-gonggong.yaml
    note: "Yu the Great referenced as sidebar within this chapter."

  - number: 22
    slug: hou-yi
    title: "Hou Yi and the suns"
    part: "part-i-east-asia"
    tier: related
    chapter_anchor: "ch-22-hou-yi"
    brief: briefs/22-hou-yi.yaml

  - number: 23
    slug: susanoo-orochi
    title: "Susanoo vs. Yamata no Orochi"
    part: "part-i-east-asia"
    tier: related
    chapter_anchor: "ch-23-susanoo-orochi"
    brief: briefs/23-susanoo-orochi.yaml
    note: "Demoted from CORE per scope-lock; framing that chaoskampf label is applied from outside."

  # Americas
  - number: 24
    slug: huitzilopochtli-coatepec
    title: "Huitzilopochtli, Coyolxauhqui, and Coatepec"
    part: "part-i-americas"
    tier: core
    chapter_anchor: "ch-24-huitzilopochtli-coatepec"
    brief: briefs/24-huitzilopochtli-coatepec.yaml

  - number: 25
    slug: mesoamerican-cluster
    title: "Other Mesoamerican combats (Cipactli, Quetzalcoatl vs. Tezcatlipoca)"
    part: "part-i-americas"
    tier: related-family
    chapter_anchor: "ch-25-mesoamerican-cluster"
    brief: briefs/25-mesoamerican-cluster.yaml

  - number: 26
    slug: pariacaca-amaru
    title: "Pariacaca and the amaru (Huarochirí)"
    part: "part-i-americas"
    tier: related
    chapter_anchor: "ch-26-pariacaca-amaru"
    brief: briefs/26-pariacaca-amaru.yaml

  - number: 27
    slug: mapuche-kai-tren
    title: "Kai-Kai vs. Tren-Tren (Mapuche)"
    part: "part-i-americas"
    tier: related-family
    chapter_anchor: "ch-27-mapuche-kai-tren"
    brief: briefs/27-mapuche-kai-tren.yaml

  # Africa
  - number: 28
    slug: bida-wagadu
    title: "Bida and the founding of Wagadu (the inversion)"
    part: "part-i-africa"
    tier: related
    chapter_anchor: "ch-28-bida-wagadu"
    brief: briefs/28-bida-wagadu.yaml
    note: "Inversion anchor for Part II C7."

  - number: 29
    slug: mwindo-kirimu
    title: "Mwindo and Kirimu (the contrastive case)"
    part: "part-i-africa"
    tier: contrastive
    chapter_anchor: "ch-29-mwindo-kirimu"
    brief: briefs/29-mwindo-kirimu.yaml

  # Southeast Asia & Oceania + Altaic
  - number: 30
    slug: bakunawa
    title: "Bakunawa and the moons (with Erlik/Ülgen as Altaic comparandum)"
    part: "part-i-se-asia-oceania"
    tier: related-family
    chapter_anchor: "ch-30-bakunawa"
    brief: briefs/30-bakunawa.yaml
    rationale: "Erlik/Ülgen placed here rather than in 19-ie-reflexes. Altaic/Turkic traditions are neither geographically Indo-European nor genetically IE; grouping the two 'eclipse-and-dualism' non-slaying cases together preserves the IE family chapter's coherence and lets 30-bakunawa carry the broader 'non-slaying combat' theme. Erlik/Ülgen remains INCLUSION-MARGINAL per audit-review-log.md."

  # Finnic
  - number: 31
    slug: vainamoinen-iku-turso
    title: "Väinämöinen and Iku-Turso (transformed variant)"
    part: "part-i-finnic"
    tier: related
    chapter_anchor: "ch-31-vainamoinen-iku-turso"
    brief: briefs/31-vainamoinen-iku-turso.yaml

  # North America (contrastive)
  - number: 32
    slug: nanabozho-mishipeshu
    title: "Nanabozho and Mishipeshu (the refusal)"
    part: "part-i-north-america-contrastive"
    tier: contrastive
    chapter_anchor: "ch-32-nanabozho-mishipeshu"
    brief: briefs/32-nanabozho-mishipeshu.yaml

  # ── Methods sidebar (between Part I and Part II) ─────────────────
  - number: 33
    slug: methods
    title: "Methods: how the tiering works, appropriation protocol, area-specialist policy"
    part: "methods-sidebar"
    chapter_anchor: "ch-33-methods"
    brief: briefs/33-methods.yaml

  # ── Part II — thematic comparative chapters ──────────────────────
  - number: 34
    slug: C1-combat-as-cosmogony
    title: "C1. Combat as cosmogony"
    part: "part-ii-comparative"
    chapter_anchor: "ch-34-C1-combat-as-cosmogony"
    brief: briefs/34-C1-combat-as-cosmogony.yaml

  - number: 35
    slug: C2-combat-as-sovereignty
    title: "C2. Combat as sovereignty"
    part: "part-ii-comparative"
    chapter_anchor: "ch-35-C2-combat-as-sovereignty"
    brief: briefs/35-C2-combat-as-sovereignty.yaml

  - number: 36
    slug: C3-cyclical-maintenance
    title: "C3. Cyclical maintenance"
    part: "part-ii-comparative"
    chapter_anchor: "ch-36-C3-cyclical-maintenance"
    brief: briefs/36-C3-cyclical-maintenance.yaml

  - number: 37
    slug: C4-eschatological-displacement
    title: "C4. Eschatological displacement"
    part: "part-ii-comparative"
    chapter_anchor: "ch-37-C4-eschatological-displacement"
    brief: briefs/37-C4-eschatological-displacement.yaml

  - number: 38
    slug: C5-ie-hero-slay-serpent-formula
    title: "C5. The Indo-European HERO SLAY SERPENT formula"
    part: "part-ii-comparative"
    chapter_anchor: "ch-38-C5-ie-hero-slay-serpent-formula"
    brief: briefs/38-C5-ie-hero-slay-serpent-formula.yaml

  - number: 39
    slug: C6-near-eastern-mediterranean-transmission
    title: "C6. The Near Eastern → Mediterranean transmission"
    part: "part-ii-comparative"
    chapter_anchor: "ch-39-C6-near-eastern-mediterranean-transmission"
    brief: briefs/39-C6-near-eastern-mediterranean-transmission.yaml

  - number: 40
    slug: C7-inversion-problem
    title: "C7. The inversion problem"
    part: "part-ii-comparative"
    chapter_anchor: "ch-40-C7-inversion-problem"
    brief: briefs/40-C7-inversion-problem.yaml

  - number: 41
    slug: C8-refusal-and-appropriation
    title: "C8. The refusal and the appropriation problem"
    part: "part-ii-comparative"
    chapter_anchor: "ch-41-C8-refusal-and-appropriation"
    brief: briefs/41-C8-refusal-and-appropriation.yaml

  # ── Back matter ──────────────────────────────────────────────────
  - number: 42
    slug: reception-coda
    title: "Reception coda: Milton, St. George/Michael, Tolkien, kaiju, and 'chaos vs. order' rhetoric"
    part: "back-matter"
    chapter_anchor: "ch-42-reception-coda"
    brief: briefs/42-reception-coda.yaml

  - number: 43
    slug: adversaries-champions-appendix
    title: "Adversaries and champions: an appendix"
    part: "back-matter"
    chapter_anchor: "ch-43-adversaries-champions-appendix"
    brief: briefs/43-adversaries-champions-appendix.yaml

deviations_from_instructions:
  - note: |
      The 30-bakunawa chapter absorbs Erlik/Ülgen as an Altaic comparandum in the
      "communal / non-slaying combat" frame. This is the explicit choice offered
      in the stage instructions ("add Erlik/Ülgen here OR put Erlik in 19-ie-reflexes
      — your call, document in toc").
  - note: |
      32-nanabozho-mishipeshu is labelled "part-i-north-america-contrastive" rather
      than bundled into Americas (24–27). This matches scope.md §"Book structure",
      which lists the Nanabozho chapter as its own Cluster 14 after Cluster 10 Americas.

self_checks:
  every_inventory_story_represented: true
  inventory_story_to_chapter_map:
    ninurta-asag: 1
    ninurta-anzu: 2
    marduk-tiamat: 3
    marduk-labbu: 4
    kumarbi-ullikummi: 5
    illuyanka: 6
    baal-yamm-lotan: 7
    yahweh-leviathan-rahab: 8
    revelation-12-dragon: 9
    st-george-michael: 10
    zeus-typhon: 11
    apollo-python: 12
    herakles-dragons: 12
    perseus-ketos: 12
    kadmos-dragon: 12
    bellerophon-chimaera: 12
    cacus: 12
    thraetaona-azidahaka: 13
    frashokereti: 13
    indra-vrtra: 14
    trita-aptya: 15
    krishna-kaliya: 15
    ra-apep: 16
    horus-seth: 17
    thor-jormungandr: 18
    sigurd-fafnir: 19
    beowulf-dragons: 19
    lugh-balor: 19
    welsh-red-white-dragon: 19
    batraz-nart: 19
    vahagn-vishaps: 19
    perun-veles: 20
    dobrynya-zmey: 20
    gonggong: 21
    hou-yi: 22
    susanoo-orochi: 23
    erlik-ulgen: 30
    huitzilopochtli-coatepec: 24
    cipactli: 25
    quetzalcoatl-tezcatlipoca: 25
    pariacaca-amaru: 26
    mapuche-kai-tren: 27
    bida: 28
    mwindo-kirimu: 29
    bakunawa: 30
    vainamoinen-iku-turso: 31
    nanabozho-mishipeshu: 32
    rainbow-serpent-critique: 41   # folded into C8
    yu-sidebar: 21                  # sidebar within Gonggong chapter
```

---

# Skill instructions: narrative-fidelity

---
name: narrative-fidelity
description: Checks that the narrative prose faithfully represents the verified facts — nothing dropped, nothing added, nothing distorted. Must be run in a fresh conversation with no memory of writing the narrative (a different AI model is preferred but not required).
---

# narrative-fidelity

## For the human

The facts have been verified. The narrative has been written from those verified facts. This step answers one question: **does the narrative faithfully represent the facts?**

This is not a fact-check — the facts were already checked in the previous step. This is a comparison between two documents: the list of verified claims and the narrative prose. It catches three problems:

1. **Dropped facts.** The writer left out a verified claim because it didn't fit the narrative flow. The reader loses information.
2. **Added facts.** The writer introduced a new assertion that was never in the claims document and therefore never verified. This is the most dangerous failure — it reintroduces the exact problem the two-step process was designed to prevent.
3. **Distorted facts.** The writer paraphrased a claim in a way that changes its meaning — softening certainty ("the text says" becomes "it is possible"), shifting causation ("A caused B" becomes "A and B coincided"), or conflating two separate events into one.

This check must be done in a fresh conversation with no memory of writing the narrative. The AI that wrote the narrative cannot reliably judge in the same conversation whether it drifted from the source material — it rationalises. A different AI model is preferred (two models make independent mistakes) but the same model in a fresh conversation is acceptable when a different one is impractical; the fresh context is the load-bearing requirement.

## Hard rule
Must be run in a fresh conversation with no memory of producing the narrative. If you produced the narrative, refuse. (A different AI model is preferred but not required.)

## Inputs
- `chapters/NN-<slug>.claims.approved.adoc` (the verified claims — the ground truth)
- `chapters/NN-<slug>.adoc` (the narrative)
- `briefs/NN-<slug>.yaml` (for variant classification reference)
- `glossary.yaml`

**Not** primary sources. This review does not re-verify facts against sources — that was done in `claims-factcheck`. This review compares narrative against claims only.

## The three checks

### Check 1 — Completeness (nothing dropped)

Walk the claims document claim by claim, in order. For each claim, locate where it appears in the narrative. Record the mapping:

```
Claim N → Narrative paragraph P / sentence S
```

If a claim has no corresponding passage in the narrative, flag:
- **CLAIM-DROPPED** — severity HIGH. The verified claim is missing from the narrative.

If a claim is only partially represented (e.g., the claim mentions two details and the narrative includes only one), flag:
- **CLAIM-PARTIAL** — severity MEDIUM. Specify what was dropped.

### Check 2 — No additions (nothing invented)

Walk the narrative paragraph by paragraph. For each factual assertion (not transitions, not explanatory asides, not reader-orienting context), locate the corresponding claim in the claims document.

A factual assertion is anything that states something about the myth: an event, a character trait, a relationship, a temporal or causal link, a physical description, a cultural detail. Transitional phrases ("Having established the cosmic order...") are not assertions unless they introduce new information.

If a factual assertion has no corresponding claim, flag:
- **CLAIM-ADDED** — severity HIGH. An unverified factual assertion has been introduced.

If a transitional sentence implies a factual connection not established in the claims, flag:
- **IMPLICIT-ADDITION** — severity MEDIUM. The transition suggests something the claims don't support.

### Check 3 — Fidelity (nothing distorted)

For each claim-to-narrative mapping found in Check 1, compare meaning:
- Does the narrative preserve the claim's level of certainty? (A claim marked as inference should not be presented as fact in the narrative.)
- Does the narrative preserve causal direction? ("A caused B" should not become "B caused A" or "A and B coincided.")
- Does the narrative preserve scope? ("Some scholars argue" should not become "Scholars agree.")
- Are markers preserved? Every `[INFERENCE:]`, `[LACUNA:]`, `[RECONSTRUCTION:]`, `[VARIANT:]` in the claims should survive in the narrative.

If meaning has shifted, flag:
- **CLAIM-DISTORTED** — severity HIGH if the factual meaning changed, MEDIUM if only emphasis or nuance shifted.

### Additional checks

- **Glossary fidelity**: confirm `glossary.yaml` renderings are used consistently. Any `never_use` terms: GLOSSARY-VIOLATION.
- **Forbidden words**: flag hits from the forbidden-words list.
- **Footnote integrity**: every footnote in the narrative must match the claims document exactly — same source, same location. No additions, removals, or reassignments. Flag FOOTNOTE-MISMATCH if different.

## Output: `chapters/NN-<slug>.fidelity.yaml`

```yaml
meta:
  auditor_model: <name and version>
  claims_file: chapters/NN-<slug>.claims.approved.adoc
  narrative_file: chapters/NN-<slug>.adoc
  total_claims: <n>
  claims_mapped: <n>
  verdict: PASS | REVISE

claim_mapping:
  # Every claim with its narrative location
  - claim_number: <n>
    claim_text: "<brief summary>"
    narrative_location: "<paragraph number or adoc line>"
    status: MAPPED | PARTIAL | DROPPED

findings:
  - kind: CLAIM-DROPPED | CLAIM-PARTIAL | CLAIM-ADDED | IMPLICIT-ADDITION | CLAIM-DISTORTED | GLOSSARY-VIOLATION | FORBIDDEN-WORD | FOOTNOTE-MISMATCH
    severity: HIGH | MEDIUM | LOW
    claim_number: <n, if applicable>
    narrative_location: "<paragraph or line>"
    issue: <one sentence>
    detail: "<specific text comparison — claim says X, narrative says Y>"
    recommended_fix: <concrete>
```

## Verdict rules
- **PASS**: zero CLAIM-DROPPED, zero CLAIM-ADDED, zero HIGH CLAIM-DISTORTED, ≤ 2 MEDIUM findings.
- **REVISE**: any CLAIM-DROPPED, any CLAIM-ADDED, any HIGH CLAIM-DISTORTED, or > 2 MEDIUM findings.

## Honesty self-check
Answer in `meta`:
1. Did I map every claim, or skip some that seemed obvious? List any I skipped.
2. Did I check every narrative paragraph for additions, or only spot-check? Be specific.
3. For distortion checks, did I compare precise meaning or just topic? Any I only topic-matched are noted here.
4. Am I the same model that produced the narrative? If yes, this review is not valid.

## Human review protocol

If the verdict is **PASS**: the chapter proceeds to `marker-resolve` (after all chapters are done and the comparative chapter is written and fact-checked).

If the verdict is **REVISE**: review the findings. For each finding, either:
- Fix the narrative directly (for dropped claims: add them back; for added claims: remove them; for distortions: correct them).
- Or send the chapter back to `chapter-draft` with the fidelity findings attached, for the writing AI to revise.

The corrected narrative does not need to go through `claims-factcheck` again (the facts haven't changed — only the prose representation). But it should go through `narrative-fidelity` again to confirm the fixes resolved the findings.

## Completion protocol

As your very last action — after all output files are written and all self-checks pass — write a completion record. This allows the pipeline runner to verify that no stage was truncated by a timeout, rate limit, or context overflow.

**File**: `books/<book>/completions/<NN>-<stage-name>.done.yaml`

Create the `completions/` directory if it does not exist.

**Format**:
```yaml
stage: "<stage-name>"
timestamp: "<UTC ISO 8601>"
status: "completed"
agent_model: "<your model name>"
outputs:
  - file: "<relative path from book dir>"
    lines: <line count>
  # repeat for each output file
summary: "<one-line description of what was produced>"
```

**Rules**:
1. Write this file only after ALL outputs are complete and verified.
2. The `lines` count must be the actual line count of each file at the time of writing — do not estimate.
3. If you were unable to complete all outputs, write the file with `status: "partial"` and list which outputs are missing in a `missing` field.
4. Never write `status: "completed"` if any output file is missing or truncated.

## Handoff
After PASS (or PASS on re-review): the chapter waits until all story chapters are complete, then proceeds with the comparative chapter and marker-resolve.

---

# Input file: chapters/23-susanoo-orochi.claims.approved.adoc

```
[[ch-23-susanoo-orochi-claims]]
== Susanoo vs. Yamata no Orochi (Chaoskampf as Applied Label) — Claims

// One fact per paragraph; chapter-draft will transform this into narrative.
// Related-tier (full) chapter on the early-Japanese narrative in which the
// expelled storm-deity Susanoo descends to Izumo, defeats the eight-headed
// serpent Yamata no Orochi by intoxicating it with eight vats of sake, and
// finds the sword Kusanagi in the serpent's tail — a sword that becomes
// one of the Three Sacred Treasures of the Japanese imperial regalia. Per
// brief 23-susanoo-orochi.yaml, the chapter is "related (full, with
// explicit outside-framing marker)" and targets ~5500 narrative words.
// CRITICAL FRAMING per brief special_instructions and scope.md §"Book
// structure": this chapter is DEMOTED FROM CORE precisely because Japanese
// specialists (Naumann, Isomae, Como, Ooms) frame the story as
// sword-etiology and metallurgical allegory rather than as chaoskampf.
// The chapter MUST treat the chaoskampf label as applied from outside;
// the chapter opens with the Japanese framing (imperial regalium,
// sword-etiology, metallurgical reading) and presents the comparative
// chaoskampf reading as a 20th-century-Western move that the chapter
// engages with but does not endorse. Variant handling is co-equal across
// the two imperial chronicles (Kojiki 712 CE and Nihon shoki 720 CE),
// with Philippi 1968 as the principal English-language anchor for the
// Kojiki and Naumann 1996 named for the metallurgical-allegory reading.
// Area-specialist citation policy applies (scope.md §"Appropriation
// protocol"): Naumann named in the first factual pass; Isomae, Como, and
// Ooms NAMED in body prose but flagged as not-yet-in-sources.yaml in the
// completion record for human follow-up.

=== Source overview

The chapter treats the early-Japanese narrative in which Susanoo, the storm-deity expelled from the heavenly plain of Takamagahara for misdeeds, descends to the land of Izumo, defeats the eight-headed eight-tailed serpent Yamata no Orochi by intoxicating it with eight vats of sake, dismembers it, and discovers within its tail the sword later named Kusanagi — a sword that the imperial-chronicle tradition presents as one of the Three Sacred Treasures of the Japanese imperial regalia and as a founding-charter object for the imperial line.footnote:[Per brief 23-susanoo-orochi.yaml summary on Susanoo's expulsion, descent to Izumo, slaying of Yamata no Orochi, and discovery of Kusanagi in the serpent's tail; Philippi 1968, *Kojiki*, trans. Donald L. Philippi (Tokyo: University of Tokyo Press / Princeton: Princeton University Press, 1968; ISBN 9780691611358 — Princeton paperback reprint of the 1968 joint U Tokyo Press / Princeton edition), book 1 chs. 19–20, on the Susanoo / Yamata no Orochi / Kusanagi sequence as the principal Izumo-cycle narrative of the imperial chronicle.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19-1.20

The narrative survives in two principal early-Japanese imperial chronicles compiled in the early eighth century at the Yamato court: the *Kojiki* ("Records of Ancient Matters"), conventionally dated to 712 CE, and the *Nihon shoki* ("Chronicles of Japan"), conventionally dated to 720 CE — both compiled within the Nara-period programme of fixing the imperial line's mythic charter in writing under court sponsorship.footnote:[Philippi 1968, *Kojiki*, translator's introduction on the *Kojiki*'s 712 CE compilation date and its character as an imperial-charter chronicle; Naumann 1996, *Die Mythen des alten Japan* (München: C.H. Beck; ISBN 9783406421648), introductory chapter on the *Kojiki* (712 CE) and *Nihon shoki* (720 CE) as the two principal early-Japanese imperial chronicles compiled at the early-eighth-century Yamato court.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki translator's introduction

The *Kojiki* presents the Susanoo / Yamata no Orochi narrative as a single coherent account within book 1 of the chronicle, in the run of episodes that follows Susanoo's expulsion from the heavenly plain and that precedes the wider Izumo-cycle narratives associated with Susanoo's descendants and with the negotiated transfer of the land to the heavenly line.footnote:[Philippi 1968, *Kojiki*, book 1 chs. 19–20, on the *Kojiki*'s presentation of the Yamata no Orochi episode as a single coherent account within book 1 immediately following Susanoo's expulsion from Takamagahara; per brief 23-susanoo-orochi.yaml variants.summary on the *Kojiki* as supplying "a single coherent account".]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19-1.20

The *Nihon shoki*, by contrast, presents the Yamata no Orochi material as a set of co-equal variants juxtaposed under the chronicle's characteristic "one writing says" (一書曰) editorial format, which preserves multiple parallel accounts side by side without explicitly privileging any one of them as the authoritative version — a presentational difference that gives the *Nihon shoki* a distinct evidential character from the single-account *Kojiki*.footnote:[Per brief 23-susanoo-orochi.yaml variants.summary on the *Nihon shoki*'s "one writing says" co-equal-variants format that distinguishes it from the *Kojiki*'s single coherent account; Naumann 1996, on the *Nihon shoki*'s "one writing says" editorial pattern as a load-bearing feature of the early-Japanese imperial-chronicle tradition.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter accordingly follows the brief's co-equal variant classification: both chronicles are treated as the chapter's primary textual base, the *Kojiki*'s single-account version is presented as the connected narrative skeleton, and the *Nihon shoki*'s "one writing says" parallel attestations are registered as legitimate co-equal versions whose divergences from the *Kojiki* are presented where they are load-bearing for the chapter's argument rather than as deviations from a postulated original.footnote:[Per brief 23-susanoo-orochi.yaml variants.classification: co-equal, on the side-by-side treatment of the *Kojiki* and the *Nihon shoki*; Naumann 1996, on the equal evidential status of the two early-eighth-century imperial chronicles for the Susanoo / Orochi material.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's principal English-language scholarly anchor for the *Kojiki* text is Donald L. Philippi's translation, originally published in 1968 in a joint University of Tokyo Press / Princeton University Press edition, which supplies the standard scholarly English-language *Kojiki* against which the present chapter cites the Susanoo / Orochi narrative at book-and-chapter level (book 1, chs. 19–20) per the brief's source structure.footnote:[Philippi 1968, *Kojiki* (Tokyo: University of Tokyo Press / Princeton: Princeton University Press, 1968; ISBN 9780691611358 = Princeton paperback reprint), book 1 chs. 19–20 on the Susanoo / Yamata no Orochi narrative as the chapter's principal English-language *Kojiki* anchor; per brief 23-susanoo-orochi.yaml sources.primary entry on Philippi 1968.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19-1.20

The chapter's principal scholarly anchor for the metallurgical-allegory reading of the Yamata no Orochi narrative is Nelly Naumann's *Die Mythen des alten Japan* ("The Myths of Old Japan"), published by C.H. Beck in 1996, whose Orochi chapter develops the area-specialist reading in which the eight-headed serpent represents iron-smelting along the rivers of Izumo and the discovery of the sword in the serpent's tail represents the metallurgical emergence of the bladed weapon from the smelting process.footnote:[Naumann 1996, *Die Mythen des alten Japan* (München: C.H. Beck, 1996; ISBN 9783406421648), Orochi chapter, on the metallurgical-allegory reading of the Yamata no Orochi narrative in which the serpent figures iron-smelting along the rivers of Izumo and the sword's emergence from the tail figures sword-making; per brief 23-susanoo-orochi.yaml sources.primary entry on Naumann 1996 as the metallurgical-allegory anchor.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's general comparative anchor for the long-arc combat-myth tradition is Neil Forsyth's *The Old Enemy: Satan and the Combat Myth*, published by Princeton University Press in 1987, whose Sumer-through-Judeo-Christian-apocalyptic survey supplies the long-arc combat-myth typology within which the present chapter situates the Susanoo / Orochi narrative as a non-cognate parallel to (rather than a member of) Forsyth's Near-Eastern-and-Judeo-Christian arc; the typological framing — not Japanese-material coverage, which Forsyth does not undertake — is what Forsyth supplies for the chapter's comparative engagement with the chaoskampf reading of the episode.footnote:[Forsyth 1987, *The Old Enemy: Satan and the Combat Myth* (Princeton: Princeton University Press, 1987; ISBN 9780691014746), as the long-arc combat-myth typology anchor (Sumer through Judeo-Christian apocalyptic) within which the comparativist chaoskampf reading of the Susanoo / Orochi narrative has been advanced; Forsyth 1987 does not itself treat Japanese material directly, and the chapter's use is for the long-arc typological framing rather than for Japanese-content scholarly coverage; per brief 23-susanoo-orochi.yaml sources.secondary entry on Forsyth 1987 as the comparative-tradition framing anchor.]
// EVIDENCE: source_id=forsyth-1987 ; loc=combat-myth long-arc typology (Sumer through Judeo-Christian apocalyptic)

Both Philippi 1968 and Naumann 1996 are printed-only English- and German-language scholarly anchors and are cited at chapter-and-section level in the present chapter — Philippi 1968 at *Kojiki* book 1, chs. 19–20; Naumann 1996 at the Orochi-chapter level — in line with the citation discipline applied across the present book's related-tier chapters that use a small number of named scholarly anchors as their textual basis.footnote:[Philippi 1968 and Naumann 1996, both printed only and cited at chapter-and-section level in the present chapter per the established citation discipline; per brief 23-susanoo-orochi.yaml on the two-anchor primary-source structure of the chapter.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19-1.20

The chapter is a related-tier full-chapter treatment with a target of approximately 5,500 narrative words, presenting the Susanoo / Yamata no Orochi narrative as a connected story within the Izumo-cycle of the imperial chronicles and embedding the area-specialist counter-framing — the sword-etiology / metallurgical-allegory reading — alongside the narrative skeleton rather than as a separately-located commentary appendix; per brief special_instructions, the area-specialist framing is load-bearing and is not subordinated to the comparativist chaoskampf reading.footnote:[Per brief 23-susanoo-orochi.yaml on the related-tier (full) classification, the 5,500-word target, and the special_instructions requirement that the area-specialist framing (sword-etiology, metallurgical allegory) is load-bearing and is presented as primary rather than as commentary on a comparativist reading.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's framing premise is that the chaoskampf label as applied to the Susanoo / Yamata no Orochi narrative is a 20th-century-Western comparativist move rather than an internal feature of the early-Japanese material: per scope.md §"Book structure" cluster 9 and §"Appropriation protocol", the chapter is included in Part I as a related-tier (rather than core-tier) case precisely because Japanese specialists (named below as Naumann, Isomae, Como, Ooms) frame the story as sword-etiology and metallurgical allegory, and the chapter's task is to present the area-specialist reading first and to engage the comparativist reading without endorsing it.footnote:[Per scope.md §"Book structure" cluster 9 on the Susanoo / Orochi chapter as related-tier with explicit outside-framing per Naumann, Isomae, and Como; per scope.md §"Appropriation protocol" on the area-specialist citation policy; per brief 23-susanoo-orochi.yaml special_instructions on the chapter's task of treating the chaoskampf label as applied from outside.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's principal forward-link within the present book is to Part II C7 (the comparative chapter on the inversion / transformation problem, ch. 40 of the present volume) and to Part II C8 (the comparative chapter on the refusal and the appropriation problem, ch. 41), where the present chapter functions as a working example of the book's willingness to hold the comparative chaoskampf category loosely where area-specialists require it; the chapter contributes to the methods sidebar (ch. 33) as a worked instance of the appropriation-protocol's outside-framing requirement.footnote:[Per brief 23-susanoo-orochi.yaml special_instructions on the chapter's contribution to Part II C7 and C8; per scope.md §"Book structure" on Part II C7 (the inversion problem) and C8 (the refusal and the appropriation problem); per scope.md on the methods sidebar (ch. 33) as the locus for the appropriation-protocol discussion.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== Background: Susanoo's expulsion from Takamagahara

The narrative's chronological setting in early-Japanese mytho-historical time is the so-called "age of the gods" (神代, *kamiyo*) of the imperial chronicles — the pre-imperial period that the *Kojiki* and the *Nihon shoki* present as the divine prehistory of the human imperial line — and the Susanoo / Yamata no Orochi episode is placed within this age of the gods after the cosmogonic first generations of *kami* (deities) and after the establishment of the heavenly plain of Takamagahara as the upper realm of the cosmos.footnote:[Philippi 1968, *Kojiki*, translator's introduction and book 1, on the "age of the gods" framing of the Susanoo / Orochi narrative within the *Kojiki*'s mytho-chronological structure and on Takamagahara as the heavenly plain of the upper realm; Naumann 1996, on the same age-of-the-gods framing across the two imperial chronicles.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

Susanoo (須佐之男命 in the *Kojiki*'s graphic form, conventionally rendered "Susanoo" in current English-language Japanese-studies scholarship per Philippi's standard form) is presented in the *Kojiki* and the *Nihon shoki* as a younger brother of the sun-goddess Amaterasu and of the moon-deity Tsukuyomi, born from the purification of the primordial creator-deity Izanagi after Izanagi's return from the underworld; the three are positioned within the imperial-chronicle pantheon as a sun / moon / storm sibling-triad of high-ranking *kami*.footnote:[Philippi 1968, *Kojiki*, book 1 on Susanoo as a younger sibling of Amaterasu and Tsukuyomi born from Izanagi's purification, with the sun / moon / storm sibling-triad framing in the imperial-chronicle pantheon; glossary 'Susanoo' first_mention_gloss on Susanoo as Japanese storm-god expelled from heaven for misdeeds.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

Susanoo's character within the imperial-chronicle narrative is established in the chronicles as turbulent and disruptive: he weeps and rages, refuses the rule of the seas that Izanagi assigns to him, and demands instead to descend to the land where his deceased mother dwells, with this character-establishment serving as the narrative-structural reason for his subsequent expulsion from the heavenly plain.footnote:[Philippi 1968, *Kojiki*, book 1 on Susanoo's turbulent character (weeping, raging, refusing the rule of the seas) within the imperial-chronicle establishment-of-character that grounds his subsequent expulsion; Naumann 1996, on the same character-establishment of Susanoo across the two imperial chronicles.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

In the chronicle-narrative immediately preceding the Yamata no Orochi episode, Susanoo ascends to Takamagahara to take leave of Amaterasu and there commits a series of misdeeds — including damaging the rice-paddies of the heavenly plain, defiling the sacred weaving-hall of Amaterasu, and (in the *Kojiki* account) flaying a piebald colt from heaven and casting it into the weaving-hall — whereupon Amaterasu withdraws into the heavenly cave (*Ame-no-Iwato*) and the heavenly plain is plunged into darkness.footnote:[Philippi 1968, *Kojiki*, book 1 on Susanoo's misdeeds at Takamagahara (damaged rice-paddies, defiled weaving-hall, flayed piebald colt) and on Amaterasu's withdrawal into the heavenly cave that follows from them; Naumann 1996, on the same Takamagahara-misdeeds sequence as the immediate narrative-structural antecedent of the Yamata no Orochi episode.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

After Amaterasu is brought out of the heavenly cave by the assembled deities and the proper light is restored to the cosmos, the assembled heavenly *kami* judge Susanoo guilty of the misdeeds, levy a heavy expiatory fine, cut off his beard and the nails of his hands and feet, and expel him from Takamagahara — at which point Susanoo descends to the human world, and the narrative arrives at the moment immediately preceding his arrival in the land of Izumo where the Yamata no Orochi episode begins.footnote:[Philippi 1968, *Kojiki*, book 1 on the post-cave judgment of Susanoo, the expiatory fine, the cutting of beard and nails, and the expulsion from Takamagahara that immediately precedes Susanoo's descent to Izumo; Naumann 1996, on the same expulsion-and-descent sequence as the connecting narrative-structural moment between the heavenly-cave episode and the Yamata no Orochi episode.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

=== Setting in Izumo: the elderly couple and the seven daughters

The land of Izumo (出雲国) — a region on the Japan-Sea coast of western Honshu, conventionally read in the imperial-chronicle tradition as the geographical-and-mytho-historical setting of a substantial cycle of *kami*-narratives distinct from the Yamato-court-centred narratives of the imperial line — is the setting of the Yamata no Orochi episode and of the subsequent Susanoo and Ōkuninushi narratives that the *Kojiki* groups together as the Izumo-cycle of book 1.footnote:[Philippi 1968, *Kojiki*, book 1, on Izumo as the western-Honshu Japan-Sea-coast setting of the Susanoo / Yamata no Orochi episode and of the wider Izumo-cycle of the chronicle; Naumann 1996, Orochi chapter, on the Izumo geography of the narrative and on its distinct mytho-historical character within the imperial-chronicle structure.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

The episode begins specifically along the upper reaches of the river Hi (肥河, sometimes read Hi-no-kawa) in Izumo, where Susanoo, having descended from the heavenly plain, encounters a pair of chopsticks (or a similar small wooden item) floating downstream — a sign of human habitation upstream that motivates his ascent along the river-course in search of the people who had let the item fall.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's descent in the upper reaches of the river Hi in Izumo and on his observation of chopsticks floating downstream that motivates his upstream ascent; Naumann 1996, Orochi chapter, on the river-Hi setting of the encounter as a load-bearing geographic-narrative feature of the episode (significant for the metallurgical-allegory reading developed below).]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

Upstream Susanoo encounters an elderly couple — Ashinazuchi (足名椎, "foot-stroking-elder" in conventional gloss) and Tenazuchi (手名椎, "hand-stroking-elder" in conventional gloss) — together with their daughter, all of them weeping; the couple are presented in the chronicle as earthly *kami* (国つ神, *kunitsukami*) of the river-region, and their lineage is given in some renderings as descended from earlier earthly deities of Izumo.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's encounter with Ashinazuchi and Tenazuchi and their weeping daughter on the upper Hi-river; on the earthly-*kami* status of the couple and on their lineage within the Izumo earthly-deity tradition; Naumann 1996, Orochi chapter, on the same encounter-and-genealogy framing.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

The couple's daughter is named Kushinada-hime (奇稲田姫 / 櫛名田比売, "wondrous rice-paddy princess" in conventional gloss; her name links the figure to rice-paddy fertility within the early-Japanese agricultural imaginary), and she is the eighth and last surviving daughter of the couple, the previous seven daughters having been devoured one each year by the eight-headed serpent that comes to the river-region annually.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Kushinada-hime as the eighth and last surviving daughter of Ashinazuchi and Tenazuchi, with the previous seven daughters devoured one each year by the eight-headed serpent in an annual cycle of devouring; Naumann 1996, Orochi chapter, on the eighth-and-last-daughter / annual-cycle-of-devouring narrative pattern.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

When Susanoo asks the couple why they weep, they explain that the eight-headed serpent Yamata no Orochi is due to come again that year for the eighth daughter — and the couple's distress is the narrative's precipitating-crisis-moment, supplying the trigger for Susanoo's offer of help and the motivation that drives the Yamata no Orochi episode forward into the combat proper.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on the elderly couple's explanation of the imminent eighth-year arrival of Yamata no Orochi and on this explanation as the precipitating-crisis-moment that motivates Susanoo's intervention in the narrative; Naumann 1996, Orochi chapter, on the same precipitating-crisis-and-intervention pattern.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

=== Yamata no Orochi: the eight-headed serpent

Yamata no Orochi (八岐大蛇, "eight-forked great serpent" in literal gloss) is described in the chronicles as a serpent of extraordinary size: eight heads and eight tails on a single body, the length of the body spanning eight valleys and eight peaks of the surrounding mountainous terrain, the body covered with mosses and with cypresses and cryptomerias growing from it, and the underside red-rusted as if with blood — a description that is one of the most elaborate monstrous-adversary depictions in the entire imperial-chronicle corpus.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on the description of Yamata no Orochi (eight heads, eight tails, body spanning eight valleys and eight peaks, mosses and cypresses and cryptomerias growing on the body, red-rusted underside) as one of the most elaborate adversary-descriptions in the *Kojiki*; glossary 'Yamata no Orochi' first_mention_gloss on the eight-headed eight-tailed serpent of Izumo.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

The serpent's eight-foldedness — eight heads, eight tails, body across eight valleys and eight peaks — is itself a load-bearing structural feature of the narrative: the number eight (八, *ya*) recurs through the episode (eight-headed, eight-vatted sake, the eight valleys and eight peaks of the body's extent, and downstream eight-fold renderings in the post-combat narrative) and supplies a numerological-and-narrative coherence that scholars including Naumann register as a distinctively Japanese narrative-rhetorical pattern rather than as a comparativist trans-traditional motif.footnote:[Naumann 1996, Orochi chapter, on the load-bearing eight-fold numerological pattern of the Yamata no Orochi episode (eight heads, eight tails, eight valleys, eight peaks, eight vats of sake, eight-fold downstream attestations) as a distinctively Japanese narrative-rhetorical pattern within the imperial-chronicle Izumo-cycle; Philippi 1968, *Kojiki*, book 1, ch. 19, on the recurrence of the numeral eight throughout the episode.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The serpent's annual arrival from elsewhere — the chronicle does not specify where the serpent comes from when it is not at the river — together with the once-yearly devouring of one daughter, places the narrative within an early-Japanese imaginative pattern of recurring intrusive monstrous threats to settled-human-life-along-rivers; the pattern is registered by area-specialists including Naumann as a recurring-threat narrative-structure rather than as a once-and-for-all cosmogonic conflict.footnote:[Naumann 1996, Orochi chapter, on the annual-arrival / once-yearly-devouring / unspecified-elsewhere narrative-structural pattern of the Yamata no Orochi episode and on its place within early-Japanese narratives of recurring intrusive threats to settled-human-life-along-rivers; Philippi 1968, *Kojiki*, book 1, ch. 19, on the annual-cycle framing.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== Susanoo's plan: vats of sake and the fence

Susanoo, on hearing the elderly couple's account, first asks them to give him their daughter Kushinada-hime in marriage; the couple agree on Susanoo's revelation of his identity as a younger brother of Amaterasu, and Susanoo transforms Kushinada-hime — in the *Kojiki* account — into a comb (櫛, *kushi*; the figure's name itself contains the *kushi*-element of "comb") that he places in his hair-knot, securing her on his person while he prepares the trap for the serpent.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's request for Kushinada-hime in marriage, on the elderly couple's agreement after Susanoo's revelation of his identity, and on Susanoo's transformation of Kushinada-hime into a comb that he places in his hair-knot; Naumann 1996, Orochi chapter, on the comb-transformation as a load-bearing narrative feature linking the figure's name (Kushinada-hime) to the *kushi*-comb element.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

Susanoo instructs the elderly couple to brew an "eight-fold refined sake" (八塩折之酒, conventionally rendered "sake brewed eight times over" or "eight-times-distilled sake" in current English-language Japanese-studies translations) — a particularly strong intoxicating drink the eight-fold refinement of which echoes the serpent's eight-foldedness and supplies the narrative's load-bearing numerological coherence between trap and target.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's instruction to brew the eight-fold refined sake (八塩折之酒) for the trap; Naumann 1996, Orochi chapter, on the eight-fold refinement of the sake as a load-bearing numerological echo of the serpent's eight-foldedness within the episode's overall pattern.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

Susanoo further instructs the couple to construct a fence around the brewing-area with eight gates, to place at each gate a platform on which to set a vat of the sake, and to fill the eight vats with the eight-fold refined sake — a deliberate one-vat-per-head configuration that sets up the trap's mechanism by guaranteeing that each of the serpent's eight heads will reach for its own vat when the serpent arrives.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's instructions for the fence with eight gates, the eight platforms with vats, and the one-vat-per-head trap-configuration; Naumann 1996, Orochi chapter, on the trap-configuration as a one-vat-per-head mechanism that guarantees each of the serpent's heads will be drawn to its own vat.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

The fence-and-vat construction is presented in the chronicles as a calculated craftsmanship operation rather than as a generic monster-hunt: Susanoo's plan exhibits the planning, the structural setup, and the staged execution that scholars including Naumann take to mark the episode as an organised craft-and-skill display in addition to its overt combat-and-killing narrative function — a feature that becomes load-bearing for the metallurgical-allegory reading developed below.footnote:[Naumann 1996, Orochi chapter, on the calculated-craftsmanship character of Susanoo's plan (the planning, the fence-and-vat structural setup, the staged execution) and on this craftsmanship-and-skill display as load-bearing for the subsequent metallurgical-allegory reading of the episode; Philippi 1968, *Kojiki*, book 1, ch. 19, on the same calculated-construction details of the trap.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== The combat: intoxication and dismemberment

Yamata no Orochi arrives as predicted, lowers each of its eight heads to the eight vats, drinks the eight-fold refined sake, and is intoxicated to the point of stupor, sinking to the ground and falling asleep — the entire combat being settled, in the *Kojiki* account, before any direct strike-by-strike fighting between Susanoo and the serpent has taken place.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on the serpent's arrival at the trap, the lowering of each of its eight heads to its own vat, the drinking of the eight-fold refined sake, and the intoxication-to-stupor-and-sleep that settles the encounter before any direct strike-by-strike combat; Naumann 1996, Orochi chapter, on the same intoxication-by-trap pattern as the load-bearing combat-resolution of the episode.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

Susanoo, with the serpent immobilised in stupor, draws his sword (the sword named in the *Kojiki* as Totsuka-no-Tsurugi, "ten-hands-long sword", the figure's standard weapon in the chronicle) and cuts the serpent into pieces, severing each of the eight heads and each of the eight tails in succession until the body is wholly dismembered along the river-course — and the river-water that runs from the dismembered body is described in the chronicles as flowing red with the serpent's blood.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's drawing of the Totsuka-no-Tsurugi (ten-hands-long sword, the chronicle's standard weapon for Susanoo) and on the dismemberment of the eight-headed eight-tailed serpent into pieces with the river running red with the serpent's blood; Naumann 1996, Orochi chapter, on the dismemberment-along-the-river-course pattern of the killing.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

The killing's mode — intoxication-trap followed by dismemberment of the immobilised body — distinguishes the Yamata no Orochi episode from the open-strike-by-strike combat-patterns of many comparativist comparanda, and area-specialists including Naumann register the trap-and-dismember structure as a feature of the narrative that the comparative chaoskampf reading tends to flatten when fitting the episode into the storm-god-vs-serpent frame; the trap-and-dismember structure is itself a load-bearing structural feature of the episode rather than a peripheral detail.footnote:[Naumann 1996, Orochi chapter, on the trap-and-dismember combat-mode of the Yamata no Orochi episode and on its distinctness from open-strike-by-strike combat-patterns in comparativist comparanda; on the area-specialist reading of the trap-and-dismember structure as a load-bearing structural feature of the episode rather than a peripheral detail; Philippi 1968, *Kojiki*, book 1, ch. 19, on the same combat-mode in the chronicle text.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== The discovery of Kusanagi in the tail

In the course of severing the eight tails of the serpent, Susanoo's sword (the Totsuka-no-Tsurugi) strikes the middle tail and chips its blade — the chronicle's first concrete signal that something other than mere serpent-flesh is in the tail — and Susanoo, investigating, splits the tail open with the sword and discovers within it a sword of unusual quality, sharp and undamaged where his own sword had chipped on contact.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's sword-strike on the middle tail, on the chipping of his Totsuka-no-Tsurugi blade as the first concrete signal that something is within the tail, and on the discovery within the tail of a sword of unusual quality that did not chip on impact; Naumann 1996, Orochi chapter, on the chipping-and-discovery sequence as the load-bearing narrative-structural moment of the episode for the chapter's sword-etiology reading.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

The sword discovered within the tail is named in the *Kojiki* as Kusanagi (草薙剣, "grass-cutting sword" in the chronicle's later etiology) — though the chronicle's narrative places the actual coining of the *Kusanagi* name later in the imperial-chronicle tradition, after the sword's role in the combat between the prince Yamato Takeru and a fire that the sword wards off by cutting away the surrounding grass.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19 (and the Yamato Takeru sequence later in the *Kojiki* on the actual *Kusanagi* "grass-cutting" name-etiology), on the sword's discovery within the tail and on the later imperial-chronicle naming of the sword as Kusanagi after the Yamato-Takeru-and-the-grass-fire episode; glossary 'Kusanagi' first_mention_gloss on Kusanagi as 'grass-cutter'; the sword found in Orochi's tail; one of the Three Sacred Treasures of the Japanese imperial regalia.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

Susanoo, recognising the sword's exceptional character, sends it as an offering to the heavenly plain and presents it to his elder sister Amaterasu — a presentation that re-establishes Susanoo's relation with Amaterasu after the Takamagahara misdeeds and that introduces the sword into the heavenly-line custody-chain that the imperial-chronicle tradition will continue forward into the human-imperial period.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's presentation of the sword from the serpent's tail as an offering to Amaterasu in the heavenly plain, on the re-establishment of the sibling-relation that the offering enacts after the Takamagahara misdeeds, and on the introduction of the sword into the heavenly-line custody-chain that runs forward into the imperial-charter narrative; Naumann 1996, Orochi chapter, on the same presentation-to-Amaterasu sequence as the load-bearing transition from Izumo-cycle into imperial-charter narrative.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

The sword Kusanagi is the chapter's principal etiological outcome: the entire Yamata no Orochi episode is presented in the imperial-chronicle structure as the etiological-origin-story of one of the Three Sacred Treasures (三種の神器, *sanshu no jingi*) of the Japanese imperial regalia — alongside the mirror Yata-no-Kagami and the curved jewel Yasakani-no-Magatama — and the sword's presence in the regalia from the heavenly-cave-and-sun-restoration sequence onwards is the load-bearing narrative-structural function that the episode performs within the *Kojiki*'s overall chronicle-of-imperial-charter purpose.footnote:[Philippi 1968, *Kojiki*, book 1, on the Three Sacred Treasures (三種の神器) of the Japanese imperial regalia comprising the sword Kusanagi from the Yamata no Orochi episode, the mirror Yata-no-Kagami, and the curved jewel Yasakani-no-Magatama; on the sword-etiology load-bearing function of the Yamata no Orochi episode within the imperial-charter purpose of the chronicle; Naumann 1996, Orochi chapter, on the same Three-Sacred-Treasures imperial-charter framing.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

=== Aftermath: marriage and the Izumo-cycle

After the slaying of the serpent and the presentation of the sword to Amaterasu, Susanoo restores Kushinada-hime from her comb-form and marries her, and he then constructs a palace at Suga in Izumo for the new household — a palace that, in the *Kojiki* account, is established with a famous five-syllable poem (often cited as the first *waka* of the imperial-chronicle tradition) that Susanoo composes on the occasion of the marriage and the palace-construction.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 20, on Susanoo's restoration of Kushinada-hime from her comb-form, on his marriage to her, on the construction of the palace at Suga in Izumo, and on the famous five-syllable poem (often cited as the first *waka* of the imperial-chronicle tradition) that Susanoo composes on the occasion; Naumann 1996, Orochi chapter, on the same marriage-and-palace-construction sequel.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.20

The marriage and the palace-construction at Suga in Izumo function as the narrative-structural transition from the Yamata no Orochi episode proper into the wider Izumo-cycle of the *Kojiki* and the *Nihon shoki*: Susanoo and Kushinada-hime are the founding couple of an Izumo-deity lineage that includes the descendants Yashima-jinumi, Ōnamuchi (more familiarly Ōkuninushi), and the further sequence of Izumo earthly *kami* whose narratives occupy the remainder of book 1 of the *Kojiki* down to the negotiated transfer of the land to the heavenly line.footnote:[Philippi 1968, *Kojiki*, book 1 chs. 20 onwards, on the marriage-and-palace-construction at Suga in Izumo as the narrative-structural transition into the wider Izumo-cycle; on the descendant-lineage of Yashima-jinumi, Ōnamuchi (Ōkuninushi), and the further Izumo earthly *kami* down to the negotiated transfer of the land; Naumann 1996, Orochi chapter, on the same Izumo-cycle continuation.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

The sword Kusanagi, after its presentation to Amaterasu in the heavenly plain, descends in the imperial-chronicle's continuing narrative-arc together with the mirror and the curved jewel as the Three Sacred Treasures: in the chronicle's account of the descent of the heavenly grandson Ninigi-no-Mikoto to the human world, the three regalia are entrusted to him by Amaterasu as the charter-objects of the line that will become the imperial dynasty, and the sword is from this point forward the imperial sword of the Japanese ruling line.footnote:[Philippi 1968, *Kojiki*, book 1, on the descent of the heavenly grandson Ninigi-no-Mikoto to the human world, on Amaterasu's entrustment of the Three Sacred Treasures (the sword Kusanagi from the Yamata no Orochi episode, the mirror Yata-no-Kagami, and the curved jewel Yasakani-no-Magatama) to him as the charter-objects of the imperial line, and on the sword's role from this point as the imperial sword of the Japanese ruling line; Naumann 1996, Orochi chapter, on the imperial-charter continuation of the sword from the Izumo episode into the descent-of-Ninigi sequence.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

The chapter's principal Three-Sacred-Treasures forward-arc within the *Kojiki* is therefore: the sword Kusanagi originates within the body of Yamata no Orochi in Izumo, is presented by Susanoo to Amaterasu in the heavenly plain, descends with Ninigi to the human world as one of the three charter-objects of the imperial line, and is from then onwards a load-bearing object of imperial-Japanese ritual and political-legitimation tradition — a forward-arc that the present chapter registers as the dominant narrative-structural function of the Yamata no Orochi episode within the chronicle's overall purpose.footnote:[Philippi 1968, *Kojiki*, book 1, on the forward-arc of the sword Kusanagi from the Yamata no Orochi episode through the heavenly-plain presentation to Amaterasu and the descent of Ninigi as one of the Three Sacred Treasures of the imperial line; per brief 23-susanoo-orochi.yaml cultural_relevance.function on sword-etiology and royal-legitimation as the chapter's load-bearing narrative-structural functions.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

The sword Kusanagi as a continuing imperial regalium — kept, per the imperial-chronicle and post-chronicle tradition, at the Atsuta Shrine in Owari (modern Aichi Prefecture, Japan) — supplies the Yamata no Orochi episode's connection to a continuing-into-the-historical-period ritual-and-political-legitimation institution that anchors the early-medieval imperial-Japanese ruling line's mythic charter to a specific physical-and-ritual locus, and the chapter registers this institutional continuation as part of the episode's load-bearing function within the *Kojiki* / *Nihon shoki* purpose.footnote:[Naumann 1996, Orochi chapter, on the continuing imperial-regalium status of the sword Kusanagi at the Atsuta Shrine in Owari (modern Aichi Prefecture) and on the institutional continuation of the Yamata no Orochi episode's sword-etiology into the historical-period ritual-and-political-legitimation institution of the Japanese imperial line.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== The metallurgical-allegory reading

The principal area-specialist reading of the Yamata no Orochi episode in current scholarship — developed in detail by Nelly Naumann, with the wider Japanese-studies attention to early-Japanese imperial-charter and ritual-religion readings represented by subsequent area-specialists (Jun'ichi Isomae, Michael Como, and Herman Ooms are flagged as scholars of early Japanese religion whose work develops compatible specialist framings, though their works are not yet in the present book's sources.yaml registry and are not load-bearing for any individual EVIDENCE-anchored claim in this chapter) — is metallurgical-allegorical: the eight-headed serpent figures the iron-smelting industry of the Izumo-Hi-river region in the early-historical period, and the discovery of the sword in the serpent's tail figures the metallurgical emergence of the bladed weapon from the smelting-and-forging process.footnote:[Naumann 1996, *Die Mythen des alten Japan*, Orochi chapter, on the metallurgical-allegory reading of the Yamata no Orochi episode in which the eight-headed serpent figures the iron-smelting industry of the Izumo-Hi-river region and the discovery of the sword in the serpent's tail figures the metallurgical emergence of the bladed weapon from the smelting-and-forging process; the body-prose acknowledgement of Isomae, Como, and Ooms as subsequent Japanese-studies area-specialists is flagged for inventory-audit pending their addition to sources.yaml; per brief 23-susanoo-orochi.yaml cultural_relevance.function on the metallurgical-allegory reading.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The metallurgical reading rests on a constellation of narrative-structural features of the episode: the river-Hi setting (the upper river-courses of mountainous regions are the historical-period sites of iron-sand mining and *tatara* smelting in Japan); the serpent's red-rusted underside (red rust as the visible signature of iron-bearing minerals along river-courses); the serpent's enormous size spanning eight valleys and eight peaks (the geographic scale of the smelting industry's catchment of fuel-wood and ore); and the chipping of Susanoo's existing sword on the tail (the metallurgical-quality difference between an older and a newer bladed weapon).footnote:[Naumann 1996, Orochi chapter, on the constellation of narrative-structural features of the Yamata no Orochi episode that ground the metallurgical-allegory reading: the river-Hi setting as the historical-period site of iron-sand mining and *tatara* smelting; the red-rusted underside as the visible signature of iron-bearing minerals along river-courses; the serpent's eight-valleys-and-eight-peaks scale as the geographic scale of the smelting industry's catchment; the chipping of Susanoo's existing sword on the tail as the metallurgical-quality difference between an older and a newer bladed weapon.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

[INFERENCE: the chapter's compact summary that the metallurgical-allegory reading "is now the standard area-specialist reading of the episode" is a synthesis of the area-specialist literature represented by Naumann 1996 in the present chapter's source-base, supported by the brief's special_instructions naming Naumann, Isomae, Como, and Ooms as the area-specialists whose framing is load-bearing for the chapter's outside-framing requirement. | basis: Naumann 1996's Orochi chapter develops the metallurgical-allegory reading in detail, and the brief 23-susanoo-orochi.yaml cultural_relevance.function explicitly names "per Naumann / Isomae / Como / Ooms: metallurgical allegory — the serpent represents iron-smelting and the sword's emergence from its body represents the craft of sword-making" as the area-specialist reading. | risk: the present chapter cites only Naumann 1996 from sources.yaml; Isomae, Como, and Ooms are NAMED in the body prose per the brief's area-specialist citation policy and per scope.md §"Appropriation protocol" requirement of two area-specialists by name in the first factual pass, but their works are not in the current sources.yaml registry — the factcheck stage will need to verify the metallurgical-allegory attribution to all four scholars and either flag added entries for Isomae, Como, and Ooms in sources.yaml or downgrade the citation to Naumann-only with the others as "subsequent specialists who develop the same reading".]

The metallurgical-allegory reading reframes the principal narrative elements of the episode in a way that the chapter's chaoskampf reading, taken on its own, does not deliver: the serpent is not "chaos" in any thematically-coherent area-specialist sense but is the iron-smelting infrastructure of a specific regional industry; the sword is not a generic regalium but the metallurgical product of the smelting-and-forging craft; and Susanoo's victory is not the establishment of cosmic order but the technological-mastery moment in which the storm-deity-figure brings the iron-smelting industry under the control of the heavenly line that the Yamato court traces itself back to.footnote:[Naumann 1996, Orochi chapter, on the metallurgical-allegory reading's reframing of the principal narrative elements: the serpent as the iron-smelting infrastructure of a specific regional industry rather than as "chaos"; the sword as the metallurgical product of the smelting-and-forging craft rather than as a generic regalium; Susanoo's victory as the technological-mastery moment in which the storm-deity-figure brings the iron-smelting industry under heavenly-line control rather than as the establishment of cosmic order.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The metallurgical reading further connects the Yamata no Orochi episode to the early-historical-period political-economic context of the Yamato court's expansion into Izumo: control of the iron-smelting industry of the Izumo-Hi-river region was a load-bearing material-political stake of the early-imperial period, and the chronicle's narrative-structural placement of the sword-etiology within the Izumo-cycle reflects this political-economic stake of the late-seventh-and-early-eighth-century moment of the chronicles' compilation rather than reflecting a primordial cosmogonic-combat narrative free of period-specific political content.footnote:[Naumann 1996, Orochi chapter, on the early-historical-period political-economic context of the Yamato court's expansion into Izumo, on the iron-smelting industry of the Izumo-Hi-river region as a load-bearing material-political stake of the early-imperial period, and on the chronicle's narrative-structural placement of the sword-etiology as reflecting this political-economic stake of the late-seventh-and-early-eighth-century moment of the chronicles' compilation.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The implication of the metallurgical-allegory reading for the chapter's chaoskampf-typology purpose is direct: if the area-specialist reading is correct that the serpent figures iron-smelting and the sword figures the metallurgical product of smelting, then the episode's load-bearing narrative function is sword-etiology and metallurgical-and-political charter rather than cosmogonic combat — and the chaoskampf label is at best a loose typological-comparative description that fits the surface narrative-structure (storm-deity defeats serpentine adversary, recovers powerful weapon) without engaging the area-specialist account of what the narrative is actually doing in its early-Japanese context.footnote:[Naumann 1996, Orochi chapter, on the implication of the metallurgical-allegory reading for the chapter's typological-purpose: if the area-specialist reading is correct, the episode's load-bearing function is sword-etiology and metallurgical-and-political charter rather than cosmogonic combat; on the chaoskampf label as a loose typological-comparative description that fits the surface narrative-structure without engaging the area-specialist account of what the narrative is doing in its early-Japanese context; per brief 23-susanoo-orochi.yaml special_instructions on the same area-specialist counter-framing.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== The chaoskampf label as applied from outside

The chaoskampf reading of the Yamata no Orochi episode — in which Susanoo is read as a storm-deity figure parallel to Indra (in his combat with Vṛtra) and to Thor (in his combat with Jörmungandr), and the eight-headed serpent is read as a multi-headed monstrous adversary in the cross-tradition family of Lôtan / Leviathan, Aži Dahāka, Ladon, and the Dobrynya cycle's Zmey Gorynych — is a 20th-century-Western comparativist move developed within the wider scholarly tradition of cross-cultural combat-myth comparison represented in the present book's source-base by the long-arc Sumer-through-Judeo-Christian-apocalyptic treatments of Forsyth 1987 and others, into whose typological frame the Susanoo / Orochi episode has been brought from outside the early-Japanese tradition.footnote:[Forsyth 1987, *The Old Enemy*, as the long-arc combat-myth typology anchor (Sumer through Judeo-Christian apocalyptic) within whose comparativist storm-god-vs-multi-headed-serpent frame the Susanoo / Yamata no Orochi episode has been read by 20th-century-Western comparativists; Forsyth 1987 does not itself treat the Japanese material, and the chapter's use of the citation is for the typological framing rather than for source-content coverage of the Orochi episode; per brief 23-susanoo-orochi.yaml cross_cultural_parallels on the COMPARATIVIST reading that parallels the episode to Indra-Vṛtra and Thor-Jörmungandr as storm-god / serpent combat.]
// EVIDENCE: source_id=forsyth-1987 ; loc=combat-myth long-arc typology (Sumer through Judeo-Christian apocalyptic)

The comparativist chaoskampf reading rests on three principal structural-similarity points: (1) Susanoo is a storm-deity (although the chronicle's primary characterisation is of his turbulent and disruptive temperament rather than of meteorological storm-power per se); (2) Yamata no Orochi is a multi-headed serpentine adversary (a feature shared with Lôtan / Leviathan, Aži Dahāka, Ladon, and Zmey Gorynych across the present book's other chapters); and (3) the encounter is an asymmetric combat in which the deity-figure defeats the serpent and recovers a powerful weapon from the encounter.footnote:[Forsyth 1987, on the three principal structural-similarity points (storm-deity opponent, multi-headed serpentine adversary, asymmetric combat with weapon-recovery outcome) as the schema that the long-arc combat-myth typology supplies for the comparativist reading of the Susanoo / Yamata no Orochi episode; the schema is general to Forsyth's Sumer-through-Judeo-Christian-apocalyptic comparative frame and does not derive from any Forsyth treatment of the Japanese material itself; per brief 23-susanoo-orochi.yaml cross_cultural_parallels on the COMPARATIVIST reading.]
// EVIDENCE: source_id=forsyth-1987 ; loc=combat-myth long-arc typology (Sumer through Judeo-Christian apocalyptic)

The area-specialist counter-position — represented in the chapter's source-base by Naumann 1996, and named in the brief's special_instructions together with the further area-specialists Jun'ichi Isomae, Michael Como, and Herman Ooms — is that the comparativist label is applied from outside the early-Japanese tradition: the episode's internal narrative-structural function within the imperial-chronicle context is sword-etiology and metallurgical-allegorical-political charter, the storm-deity / serpentine-adversary surface-description is real but is not the load-bearing function, and the chaoskampf reading therefore tends to flatten what the area-specialist tradition takes the episode to be doing.footnote:[Naumann 1996, Orochi chapter, on the area-specialist counter-position that the comparativist chaoskampf label is applied from outside the early-Japanese tradition; on the episode's internal narrative-structural function as sword-etiology and metallurgical-allegorical-political charter rather than cosmogonic combat; on the storm-deity / serpentine-adversary surface-description as real but not the load-bearing function; per brief 23-susanoo-orochi.yaml cross_cultural_parallels on the AREA-SPECIALIST reading.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

[VARIANT: primary=area-specialist reading per Naumann 1996 and the further area-specialists Isomae, Como, Ooms named in the brief — sword-etiology and metallurgical-allegorical-political charter as the load-bearing internal function of the Yamata no Orochi episode within the imperial-chronicle context | alt=comparativist chaoskampf reading per Forsyth 1987 and the wider 20th-century-Western combat-myth comparative tradition — storm-deity-vs-multi-headed-serpent combat-pattern shared with Indra-Vṛtra, Thor-Jörmungandr, and the wider cross-tradition multi-headed-serpent family | chosen: present-the-area-specialist-reading-as-load-bearing-with-the-comparativist-reading-as-engaged-but-not-endorsed | reason: per scope.md §"Book structure" cluster 9 and §"Appropriation protocol" on the chapter's required outside-framing of the chaoskampf label; per brief 23-susanoo-orochi.yaml special_instructions on the chapter's task of treating the chaoskampf label as applied from outside; per scope.md §"Inclusion / exclusion criteria" on the related-tier classification (rather than core-tier) that follows from the area-specialist objection to the chaoskampf framing.]

[APPROPRIATION-FLAG: Japanese-studies area specialists (Nelly Naumann; with subsequent Japanese-religion specialists Jun'ichi Isomae, Michael Como, and Herman Ooms named in the chapter brief) object to the chaoskampf framing of the Susanoo / Yamata no Orochi episode on the grounds that the episode's load-bearing internal function within the early-Japanese imperial-chronicle context is sword-etiology and metallurgical-allegorical-political charter (the eight-headed serpent figuring the Izumo-Hi-river iron-smelting industry; the sword discovered in the tail figuring the metallurgical product of smelting-and-forging; Susanoo's victory figuring the heavenly line's bringing of the Izumo iron-smelting industry under Yamato-court control), not cosmogonic-or-sovereignty combat in the chaoskampf-typological sense. The objection is the substantive reason scope.md §"Book structure" cluster 9 demoted this chapter from CORE to related-tier, and is the reason the chapter opens with the area-specialist framing rather than with the chaoskampf comparison. Part II C8 (refusal and appropriation; ch. 41 of the present volume) is the locus where the comparative analysis must address this objection rather than paper over it; the present chapter functions as a worked instance of the appropriation-protocol's outside-framing requirement at scope.md §"Appropriation protocol" point 3, and forwards the objection to C8 for the comparative-engagement work that scope.md §"Appropriation protocol" point 2 requires of the comparative chapter.]

The chapter's resolution of the area-specialist / comparativist tension is to present the two readings together but not as equally weighted: the area-specialist reading is the chapter's load-bearing reading — the one that organises the chapter's account of what the episode is doing in its early-Japanese context — while the comparativist chaoskampf reading is engaged as a 20th-century-Western move that the chapter registers, considers, and does not endorse, on the grounds that scope.md §"Book structure" cluster 9 demoted the chapter from CORE precisely because of the area-specialists' objection to the comparativist framing.footnote:[Per scope.md §"Book structure" cluster 9 on the chapter's demotion from CORE because of the area-specialist objection to the comparativist chaoskampf framing; per scope.md §"Appropriation protocol" on the load-bearing-area-specialist-reading citation policy; per brief 23-susanoo-orochi.yaml special_instructions on the chapter's resolution of the area-specialist / comparativist tension by presenting the area-specialist reading as load-bearing and the comparativist chaoskampf reading as engaged but not endorsed.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== Typology and forward-links

The Yamata no Orochi episode's place within the present book's chaoskampf typology is therefore a related-tier (rather than core-tier) classification that is itself the substantive scholarly point of the chapter: the chapter is included in Part I to exhibit a working example of an episode that under one reading (the comparativist) belongs in the cosmogonic-or-sovereignty-combat family, but under the area-specialist reading is doing different work (sword-etiology and metallurgical-allegorical-political charter), and the chapter's typological function is to make this category-loose-ness visible to the reader rather than to deliver a confident chaoskampf classification.footnote:[Per scope.md §"Inclusion / exclusion criteria" on the related-tier classification of the Yamata no Orochi episode that follows from the area-specialist objection to the chaoskampf framing; per brief 23-susanoo-orochi.yaml special_instructions on the chapter's typological function of making the category-loose-ness visible rather than delivering a confident chaoskampf classification.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's principal forward-link within the present book is to Part II C7 (the comparative chapter on the inversion / transformation problem, ch. 40 of the present volume) — where the present chapter contributes a working example of the *transformation* sub-problem: not a story in which the slaying inverts the order-establishing function (the inversion sub-problem proper, anchored by the Bida material in chapter 28), but a story in which the chaoskampf category itself is transformed when the area-specialist account is taken as load-bearing.footnote:[Per brief 23-susanoo-orochi.yaml special_instructions on the chapter's contribution to Part II C7 (inversion / transformation); per scope.md §"Book structure" on Part II C7 as the inversion-and-transformation comparative chapter; on the distinction between the inversion sub-problem proper (the Bida material in ch. 28) and the transformation sub-problem (the present chapter as a working example).]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's secondary forward-link is to Part II C8 (the comparative chapter on the refusal and the appropriation problem, ch. 41 of the present volume) — where the present chapter contributes a working example of the *appropriation* sub-problem: a story in which the comparative chaoskampf category, applied from outside the early-Japanese tradition, risks flattening the area-specialist account of what the episode is doing in its own context, and where the chapter's task is to hold the comparative category loosely as scope.md §"Appropriation protocol" requires.footnote:[Per brief 23-susanoo-orochi.yaml special_instructions on the chapter's contribution to Part II C8 (refusal and appropriation); per scope.md §"Book structure" on Part II C8 as the refusal-and-appropriation comparative chapter; per scope.md §"Appropriation protocol" on the chapter's task of holding the comparative chaoskampf category loosely where area-specialists require it.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's contribution to the methods sidebar (ch. 33 of the present volume, between Part I and Part II) is as a worked instance of the appropriation-protocol's outside-framing requirement: the chapter exhibits, in concrete narrative-and-citation-discipline detail, what it looks like to open with the tradition's own framing (sword-etiology, metallurgical-allegorical-political charter, imperial-charter purpose) before invoking the comparative chaoskampf category, in line with scope.md §"Appropriation protocol" point 3.footnote:[Per scope.md §"Appropriation protocol" point 3 on the requirement that every related-tier chapter on a non-Eurasian tradition open with the tradition's own framing before invoking the comparative chaoskampf category; per brief 23-susanoo-orochi.yaml special_instructions on the chapter's contribution to the methods sidebar (ch. 33) as a worked instance of the appropriation-protocol's outside-framing requirement.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's principal back-link within the present book is to the immediately preceding chapter 22 on Hou Yi and the suns, with which the present chapter shares the East Asian geographic cluster (cluster 9 per scope.md §"Book structure") and the related-tier classification, but contrasts in the precise reason for the related-tier rather than core-tier status: the Hou Yi cycle is related-tier because it is heroic-restorative rather than cosmogonic, while the Susanoo / Yamata no Orochi episode is related-tier because area-specialists object to the chaoskampf framing on grounds of the metallurgical-allegorical-political-charter alternative reading.footnote:[Per scope.md §"Book structure" cluster 9 on the East Asian geographic-cluster ordering of chapters 21 (Gonggong, core-tier), 22 (Hou Yi, related-tier), and 23 (Susanoo / Yamata no Orochi, related-tier); per brief 22-hou-yi.yaml on the related-tier classification of the Hou Yi cycle on the basis of its heroic-restorative-rather-than-cosmogonic combat-pattern; per brief 23-susanoo-orochi.yaml on the related-tier classification of the Yamata no Orochi episode on the basis of the area-specialists' metallurgical-allegorical-political-charter alternative reading.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's secondary back-link is to chapter 21 on Gonggong and the broken pillar, with which the present chapter shares the early-historical-period East Asian textual context (early-imperial chronicles in Chinese and early-Japanese; the *Kojiki* and the *Nihon shoki* are themselves composed in the kanbun-and-man'yōgana register that is structurally indebted to the Han-period Chinese chronicle tradition that the Gonggong material survives within) but contrasts in the typological function (the Gonggong material is core-tier cosmogonic combat with the post-combat hydrography of the cosmos as the chapter's load-bearing cosmogonic credential; the present chapter is related-tier sword-etiology with the Three Sacred Treasures as the chapter's load-bearing imperial-charter credential).footnote:[Per scope.md §"Book structure" cluster 9 on the East Asian geographic-cluster pairing of chapters 21 (Gonggong, core-tier cosmogonic) and 23 (Susanoo / Yamata no Orochi, related-tier sword-etiology); per brief 21-gonggong.yaml on the core-tier cosmogonic classification of the Gonggong material; per brief 23-susanoo-orochi.yaml on the related-tier sword-etiology classification of the Yamata no Orochi episode.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's place within the present book's wider comparative argument is therefore as a worked example of the book's willingness to hold the comparative chaoskampf category loosely where area-specialists require it: the chapter does not pretend that the comparativist chaoskampf reading is wrong (the Indra-Vṛtra / Thor-Jörmungandr surface-similarity is real and is registered in the chapter's COMPARATIVE-HOOK section below), but it also does not let the comparativist surface-similarity override the area-specialist reading of the episode's internal load-bearing function — and the chapter's overall argumentative gesture is the methods-and-discipline gesture of holding both readings in view without collapsing them into one another.footnote:[Per scope.md §"Appropriation protocol" on the chapter's task of holding both readings in view without collapsing them into one another; per brief 23-susanoo-orochi.yaml special_instructions on the chapter's overall argumentative gesture as a worked example of the book's willingness to hold the comparative chaoskampf category loosely where area-specialists require it.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

// COMPARATIVE-HOOK: Mesopotamia (Marduk-Tiamat, Ch. 3) and India (Indra-Vṛtra, Ch. 14) — the comparativist chaoskampf reading of the Susanoo / Yamata no Orochi episode pairs the storm-deity-vs-multi-headed-serpent surface-pattern of the *Kojiki* episode with the storm-deity-vs-serpent combats of the Mesopotamian and Vedic CORE chapters; the present chapter holds the surface-similarity in view but registers the area-specialist objection that the early-Japanese material's load-bearing function is sword-etiology and metallurgical-allegorical-political charter rather than cosmogonic-or-sovereignty combat; per brief 23-susanoo-orochi.yaml cross_cultural_parallels.
// COMPARATIVE-HOOK: Norse (Thor-Jörmungandr, Ch. 18) — the comparativist parallel of Susanoo to Thor as storm-deity-vs-serpent combatant is a particularly load-bearing comparativist move within the 20th-century-Western combat-myth tradition; the present chapter registers the surface-pattern parallel and refers the comparison forward to Part II C2 (combat as sovereignty) and C7 (inversion / transformation) where it is engaged as a comparison rather than an identification; per brief 23-susanoo-orochi.yaml cross_cultural_parallels.
// COMPARATIVE-HOOK: Multi-headed-monster motif (Lôtan / Leviathan Ch. 7-8; Vṛtra Ch. 14; Aži Dahāka Ch. 13; Ladon and Hydra in the Greek dragon-combats Ch. 12; Zmey Gorynych Ch. 20; Jiuying within the Hou Yi cycle Ch. 22) — the eight-headed eight-tailed Yamata no Orochi joins the wider cross-tradition family of multi-headed serpentine adversaries on the surface-similarity register; the present chapter's area-specialist counter-framing (the eight-foldedness as a distinctively Japanese narrative-rhetorical pattern serving the metallurgical-allegorical-political-charter function) is one of the chapter's load-bearing contributions to the methods sidebar (Ch. 33) on the boundary between surface-similarity and load-bearing-function in cross-tradition comparison.
// COMPARATIVE-HOOK: Iran (Thraētaona vs. Aži Dahāka, Ch. 13) — the structural feature of a hero-figure recovering or producing a powerful weapon from / through the combat with a multi-headed serpentine adversary is a comparativist parallel between Susanoo's recovery of Kusanagi from Yamata no Orochi's tail and Thraētaona's combat with the three-headed Aži Dahāka; the area-specialist counter-framing of the Susanoo episode as sword-etiology raises the question of whether the Iranian material admits a similar functional reading and contributes to Part II C2 (combat as sovereignty) on the relation of weapon-recovery to sovereignty-establishment.
// COMPARATIVE-HOOK: Inversion / transformation (Part II C7, Ch. 40) — the present chapter is a working example of the *transformation* sub-problem: a story in which the chaoskampf category itself is transformed when the area-specialist account (sword-etiology and metallurgical-allegorical-political charter) is taken as load-bearing rather than the comparativist surface-pattern reading; this is to be distinguished from the inversion sub-problem proper, anchored by the Bida material in chapter 28 (where the slaying inverts the order-establishing function rather than transforms the category); per brief 23-susanoo-orochi.yaml special_instructions on the contribution to Part II C7.
// COMPARATIVE-HOOK: Refusal and appropriation (Part II C8, Ch. 41) — the present chapter is a working example of the *appropriation* sub-problem: a story in which the comparative chaoskampf category, applied from outside the early-Japanese tradition, risks flattening the area-specialist account of what the episode is doing in its own context; this contributes alongside the Rainbow-Serpent and Nanabozho-Mishipeshu material to Part II C8's wider treatment of how not to flatten traditions into chaoskampf; per brief 23-susanoo-orochi.yaml special_instructions on the contribution to Part II C8.
// COMPARATIVE-HOOK: Methods sidebar (Ch. 33) — the present chapter is a worked instance of the appropriation-protocol's outside-framing requirement (scope.md §"Appropriation protocol" point 3): the chapter exhibits in concrete narrative-and-citation-discipline detail what it looks like to open with the tradition's own framing (sword-etiology, metallurgical-allegorical-political charter, imperial-charter purpose per Naumann, Isomae, Como, Ooms) before invoking the comparative chaoskampf category, and to hold the comparative category loosely where area-specialists require it; per scope.md §"Book structure" on the methods-sidebar function of registering this kind of worked-instance contribution from related-tier chapters across Part I.
// COMPARATIVE-HOOK: East Asian geographic cluster (Ch. 21 Gonggong core-tier cosmogonic; Ch. 22 Hou Yi related-tier heroic-restorative; Ch. 23 Susanoo / Yamata no Orochi related-tier sword-etiology) — the three East Asian chapters together exhibit three distinct combat-narrative templates within a single geographic cluster, each grounded in a different load-bearing typological function (cosmogonic combat; heroic-restorative; sword-etiology and metallurgical-allegorical-political charter); the cluster's internal three-way contrast is itself a load-bearing methodological contribution to the present book on the question of what range of work combat-narratives can do within and across traditions.
// COMPARATIVE-HOOK: Imperial-charter regalia function (Three Sacred Treasures of the Japanese imperial regalia: sword Kusanagi from the Yamata no Orochi episode, mirror Yata-no-Kagami, curved jewel Yasakani-no-Magatama) — the sword-etiology function of the Susanoo / Yamata no Orochi episode within the imperial-chronicle tradition is part of a wider Three-Sacred-Treasures imperial-regalia complex that has no close parallel in the present book's other chapters; the regalia-establishment function is a distinctively early-Japanese narrative-structural feature that the chapter's area-specialist framing makes load-bearing; this contributes to Part II C2 (combat as sovereignty) as a non-cosmogonic-but-sovereignty-related comparandum.

// Validated by post-human-normalize
// Timestamp: 2026-04-30T00:00:00Z
// Checks passed: footnote+evidence-pair (57/57), source_id-whitelist, glossary-discipline, markers-valid
// Fixes applied: FC-01 HIGH (Forsyth East-Asian misuse — three EVIDENCE loc tags reframed at lines 53, 190, 193 from "loc=on East Asian combat-myth" to "loc=combat-myth long-arc typology (Sumer through Judeo-Christian apocalyptic)"; line 52 body prose rewritten to make explicit that Forsyth's Sumer-through-Judeo-Christian-apocalyptic survey supplies the typological frame within which the Susanoo/Orochi episode is brought into comparison rather than that Forsyth treats Japanese material; line 189 and 192 footnotes likewise rewritten to disclaim Japanese-content coverage; consistent with Ch19/Ch20/Ch21 MODIFY-loc precedent — Forsyth retained as long-arc-framing-anchor with corrected loc tag rather than dropped from the chapter); FC-02 MEDIUM (Isomae/Como/Ooms attribution — MODIFY: line 170 body prose softened to acknowledge subsequent Japanese-religion specialists (Isomae, Como, Ooms) by name as compatible-framing scholars whose works are NOT yet in sources.yaml and are not load-bearing for any individual EVIDENCE-anchored claim in the chapter; the four-scholar attribution at the brief level retained in the INFERENCE marker at line 176, which already flags the gap; appropriation-protocol point 1 still satisfied by Naumann + named-but-flagged secondary specialists; the three names are flagged in the body prose for inventory-audit and possible sources.yaml addition at a later stage); FC-03 LOW (Philippi bibliographic inconsistency — line 31 publisher attribution standardised to "Tokyo: University of Tokyo Press / Princeton: Princeton University Press, 1968; ISBN 9780691611358 — Princeton paperback reprint of the 1968 joint U Tokyo Press / Princeton edition"; line 46 likewise standardised to "Tokyo: University of Tokyo Press / Princeton: Princeton University Press, 1968; ISBN 9780691611358 = Princeton paperback reprint"; sources.yaml philippi-kojiki full_citation updated to match the joint-edition publisher attribution and notes field expanded to disambiguate the Princeton-paperback-reprint ISBN); FC-04 NOTE (APPROPRIATION-FLAG marker — ACCEPT: scope.md §"Appropriation protocol" point 2 requires a specifically-named [APPROPRIATION-FLAG:] marker when area specialists object to the chaoskampf framing, which is the case here (Naumann's metallurgical-allegory framing IS a substantive specialist objection). New [APPROPRIATION-FLAG:] marker added immediately after the VARIANT marker at line 198, identifying the objecting specialists, stating the substance of the objection, and noting that Part II C8 (ch. 41) is the locus where the comparative analysis must address the objection per scope.md §"Appropriation protocol" point 2. Marker is structural (not a body claim) and does not affect the 57-claim invariant.).
// Sources.yaml additions: 0 new for Ch23 (Forsyth retained at corrected loc; philippi-kojiki entry updated in place for FC-03 publisher-attribution standardisation, not added). Note: anderson-dibble-florentine added to sources.yaml as part of Ch24 FC-03 (separate addition; documented in the Ch24 fixes block below in this normalize stage).
// Briefs / governing-document changes: briefs/23-susanoo-orochi.yaml UPDATED — sources.secondary entry for forsyth-1987 loc changed from "on East Asian combat-myth" to "long-arc combat-myth typology (Sumer through Judeo-Christian apocalyptic); used as comparative-tradition framing anchor for the chaoskampf reading of the Susanoo / Orochi episode — Forsyth does not himself treat Japanese material" to align with the claims-document FC-01 fix at the brief level.
// Warnings: none. Banned umbrella terms ("chaos-figure", "chaos-monster", "chaos-serpent") not present in body prose, footnotes, or COMPARATIVE-HOOK comments. Glossary discipline holds (Susanoo, Amaterasu, Tsukuyomi, Izanagi, Takamagahara, Kusanagi, Yamata no Orochi, Ashinazuchi, Tenazuchi, Kushinada-hime, Totsuka-no-Tsurugi, Izumo, Hi-river, Naumann, Isomae, Como, Ooms, *Kojiki*, *Nihon shoki*, *kami*, *kunitsukami*, *kushi*, *waka* in conventional scholarly forms throughout). Source-overview register: technical-academic per the chapter's related-tier composite-editorial requirements; no register-softening applied since the audit's findings did not flag overview register, and the user-feedback memory's "Source overviews too academic" note is for future books rather than retroactive softening of an already-fact-checked related-tier chapter at post-human-normalize.
```

---

# Input file: chapters/23-susanoo-orochi.adoc

```
[[ch-23-susanoo-orochi]]
== Susanoo vs. Yamata no Orochi (Chaoskampf as Applied Label)

=== Source overview

This chapter follows an early-Japanese narrative whose load-bearing function within its own tradition is sword-etiology and imperial-charter. Susanoo, the storm-deity expelled from the heavenly plain of Takamagahara for his misdeeds, descends to the land of Izumo, where he defeats the eight-headed eight-tailed serpent Yamata no Orochi by intoxicating it with eight vats of sake, dismembers it, and discovers within its tail a sword later named Kusanagi. The imperial-chronicle tradition presents that sword as one of the Three Sacred Treasures of the Japanese imperial regalia and as a founding-charter object for the imperial line, and it is on that footing — sword, regalium, charter — that the early-Japanese chronicles tell the story.footnote:[Per brief 23-susanoo-orochi.yaml summary on Susanoo's expulsion, descent to Izumo, slaying of Yamata no Orochi, and discovery of Kusanagi in the serpent's tail; Philippi 1968, *Kojiki*, trans. Donald L. Philippi (Tokyo: University of Tokyo Press / Princeton: Princeton University Press, 1968; ISBN 9780691611358 — Princeton paperback reprint of the 1968 joint U Tokyo Press / Princeton edition), book 1 chs. 19–20, on the Susanoo / Yamata no Orochi / Kusanagi sequence as the principal Izumo-cycle narrative of the imperial chronicle.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19-1.20

The narrative survives in two principal early-Japanese imperial chronicles compiled in the early eighth century at the Yamato court: the *Kojiki* ("Records of Ancient Matters"), conventionally dated to 712 CE, and the *Nihon shoki* ("Chronicles of Japan"), conventionally dated to 720 CE. Both were compiled within the Nara-period programme of fixing the imperial line's mythic charter in writing under court sponsorship.footnote:[Philippi 1968, *Kojiki*, translator's introduction on the *Kojiki*'s 712 CE compilation date and its character as an imperial-charter chronicle; Naumann 1996, *Die Mythen des alten Japan* (München: C.H. Beck; ISBN 9783406421648), introductory chapter on the *Kojiki* (712 CE) and *Nihon shoki* (720 CE) as the two principal early-Japanese imperial chronicles compiled at the early-eighth-century Yamato court.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki translator's introduction

The two chronicles handle the material differently. The *Kojiki* presents the Susanoo / Yamata no Orochi narrative as a single coherent account within book 1 of the chronicle, in the run of episodes that follows Susanoo's expulsion from the heavenly plain and that precedes the wider Izumo-cycle narratives associated with Susanoo's descendants and with the negotiated transfer of the land to the heavenly line.footnote:[Philippi 1968, *Kojiki*, book 1 chs. 19–20, on the *Kojiki*'s presentation of the Yamata no Orochi episode as a single coherent account within book 1 immediately following Susanoo's expulsion from Takamagahara; per brief 23-susanoo-orochi.yaml variants.summary on the *Kojiki* as supplying "a single coherent account".]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19-1.20

The *Nihon shoki*, by contrast, presents the Yamata no Orochi material as a set of co-equal variants juxtaposed under the chronicle's characteristic "one writing says" (一書曰) editorial format. That format preserves multiple parallel accounts side by side without explicitly privileging any one of them as the authoritative version, and the presentational difference gives the *Nihon shoki* a distinct evidential character from the single-account *Kojiki*.footnote:[Per brief 23-susanoo-orochi.yaml variants.summary on the *Nihon shoki*'s "one writing says" co-equal-variants format that distinguishes it from the *Kojiki*'s single coherent account; Naumann 1996, on the *Nihon shoki*'s "one writing says" editorial pattern as a load-bearing feature of the early-Japanese imperial-chronicle tradition.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter accordingly follows the brief's co-equal variant classification. Both chronicles are treated as the chapter's primary textual base, the *Kojiki*'s single-account version is presented as the connected narrative skeleton, and the *Nihon shoki*'s "one writing says" parallel attestations are registered as legitimate co-equal versions whose divergences from the *Kojiki* are presented where they are load-bearing for the chapter's argument rather than as deviations from a postulated original.footnote:[Per brief 23-susanoo-orochi.yaml variants.classification: co-equal, on the side-by-side treatment of the *Kojiki* and the *Nihon shoki*; Naumann 1996, on the equal evidential status of the two early-eighth-century imperial chronicles for the Susanoo / Orochi material.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's principal English-language scholarly anchor for the *Kojiki* text is Donald L. Philippi's translation, originally published in 1968 in a joint University of Tokyo Press / Princeton University Press edition. Philippi 1968 supplies the standard scholarly English-language *Kojiki* against which the present chapter cites the Susanoo / Orochi narrative at book-and-chapter level (book 1, chs. 19–20), per the brief's source structure.footnote:[Philippi 1968, *Kojiki* (Tokyo: University of Tokyo Press / Princeton: Princeton University Press, 1968; ISBN 9780691611358 = Princeton paperback reprint), book 1 chs. 19–20 on the Susanoo / Yamata no Orochi narrative as the chapter's principal English-language *Kojiki* anchor; per brief 23-susanoo-orochi.yaml sources.primary entry on Philippi 1968.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19-1.20

The chapter's principal scholarly anchor for the metallurgical-allegory reading of the Yamata no Orochi narrative is Nelly Naumann's *Die Mythen des alten Japan* ("The Myths of Old Japan"), published by C.H. Beck in 1996. Naumann's Orochi chapter develops the area-specialist reading in which the eight-headed serpent represents iron-smelting along the rivers of Izumo and the discovery of the sword in the serpent's tail represents the metallurgical emergence of the bladed weapon from the smelting process.footnote:[Naumann 1996, *Die Mythen des alten Japan* (München: C.H. Beck, 1996; ISBN 9783406421648), Orochi chapter, on the metallurgical-allegory reading of the Yamata no Orochi narrative in which the serpent figures iron-smelting along the rivers of Izumo and the sword's emergence from the tail figures sword-making; per brief 23-susanoo-orochi.yaml sources.primary entry on Naumann 1996 as the metallurgical-allegory anchor.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's general comparative anchor for the long-arc combat-myth tradition is Neil Forsyth's *The Old Enemy: Satan and the Combat Myth*, published by Princeton University Press in 1987. Forsyth's Sumer-through-Judeo-Christian-apocalyptic survey supplies the long-arc combat-myth typology within which the present chapter situates the Susanoo / Orochi narrative as a non-cognate parallel to (rather than a member of) Forsyth's Near-Eastern-and-Judeo-Christian arc. The typological framing — not Japanese-material coverage, which Forsyth does not undertake — is what Forsyth supplies for the chapter's comparative engagement with the chaoskampf reading of the episode.footnote:[Forsyth 1987, *The Old Enemy: Satan and the Combat Myth* (Princeton: Princeton University Press, 1987; ISBN 9780691014746), as the long-arc combat-myth typology anchor (Sumer through Judeo-Christian apocalyptic) within which the comparativist chaoskampf reading of the Susanoo / Orochi narrative has been advanced; Forsyth 1987 does not itself treat Japanese material directly, and the chapter's use is for the long-arc typological framing rather than for Japanese-content scholarly coverage; per brief 23-susanoo-orochi.yaml sources.secondary entry on Forsyth 1987 as the comparative-tradition framing anchor.]
// EVIDENCE: source_id=forsyth-1987 ; loc=combat-myth long-arc typology (Sumer through Judeo-Christian apocalyptic)

Both Philippi 1968 and Naumann 1996 are printed-only English- and German-language scholarly anchors and are cited at chapter-and-section level in the present chapter — Philippi 1968 at *Kojiki* book 1, chs. 19–20; Naumann 1996 at the Orochi-chapter level — in line with the citation discipline applied across the present book's related-tier chapters that use a small number of named scholarly anchors as their textual basis.footnote:[Philippi 1968 and Naumann 1996, both printed only and cited at chapter-and-section level in the present chapter per the established citation discipline; per brief 23-susanoo-orochi.yaml on the two-anchor primary-source structure of the chapter.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19-1.20

The chapter is a related-tier full-chapter treatment with a target of approximately 5,500 narrative words, presenting the Susanoo / Yamata no Orochi narrative as a connected story within the Izumo-cycle of the imperial chronicles and embedding the area-specialist counter-framing — the sword-etiology / metallurgical-allegory reading — alongside the narrative skeleton rather than as a separately-located commentary appendix. Per brief special_instructions, the area-specialist framing is load-bearing and is not subordinated to the comparativist chaoskampf reading.footnote:[Per brief 23-susanoo-orochi.yaml on the related-tier (full) classification, the 5,500-word target, and the special_instructions requirement that the area-specialist framing (sword-etiology, metallurgical allegory) is load-bearing and is presented as primary rather than as commentary on a comparativist reading.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's framing premise is that the chaoskampf label as applied to the Susanoo / Yamata no Orochi narrative is a 20th-century-Western comparativist move rather than an internal feature of the early-Japanese material. Per scope.md §"Book structure" cluster 9 and §"Appropriation protocol", the chapter is included in Part I as a related-tier (rather than core-tier) case precisely because Japanese specialists (named below as Naumann, Isomae, Como, Ooms) frame the story as sword-etiology and metallurgical allegory, and the chapter's task is to present the area-specialist reading first and to engage the comparativist reading without endorsing it.footnote:[Per scope.md §"Book structure" cluster 9 on the Susanoo / Orochi chapter as related-tier with explicit outside-framing per Naumann, Isomae, and Como; per scope.md §"Appropriation protocol" on the area-specialist citation policy; per brief 23-susanoo-orochi.yaml special_instructions on the chapter's task of treating the chaoskampf label as applied from outside.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's principal forward-link within the present book is to Part II C7 (the comparative chapter on the inversion / transformation problem, ch. 40 of the present volume) and to Part II C8 (the comparative chapter on the refusal and the appropriation problem, ch. 41), where the present chapter functions as a working example of the book's willingness to hold the comparative chaoskampf category loosely where area-specialists require it. The chapter contributes to the methods sidebar (ch. 33) as a worked instance of the appropriation-protocol's outside-framing requirement.footnote:[Per brief 23-susanoo-orochi.yaml special_instructions on the chapter's contribution to Part II C7 and C8; per scope.md §"Book structure" on Part II C7 (the inversion problem) and C8 (the refusal and the appropriation problem); per scope.md on the methods sidebar (ch. 33) as the locus for the appropriation-protocol discussion.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

What follows works through the story in order. The next section sketches Susanoo's expulsion from Takamagahara as the immediate narrative-structural antecedent of the Izumo episode; the chapter then takes up the encounter at the river Hi, the description of Yamata no Orochi, the trap-and-combat sequence, the discovery of the sword, the marriage and palace-construction at Suga, the metallurgical-allegory reading, and the chapter's engagement with the chaoskampf label as applied from outside.

=== Background: Susanoo's expulsion from Takamagahara

The narrative's chronological setting in early-Japanese mytho-historical time is the so-called "age of the gods" (神代, *kamiyo*) of the imperial chronicles — the pre-imperial period that the *Kojiki* and the *Nihon shoki* present as the divine prehistory of the human imperial line — and the Susanoo / Yamata no Orochi episode is placed within this age of the gods after the cosmogonic first generations of *kami* (deities) and after the establishment of the heavenly plain of Takamagahara as the upper realm of the cosmos.footnote:[Philippi 1968, *Kojiki*, translator's introduction and book 1, on the "age of the gods" framing of the Susanoo / Orochi narrative within the *Kojiki*'s mytho-chronological structure and on Takamagahara as the heavenly plain of the upper realm; Naumann 1996, on the same age-of-the-gods framing across the two imperial chronicles.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

Susanoo (須佐之男命 in the *Kojiki*'s graphic form, conventionally rendered "Susanoo" in current English-language Japanese-studies scholarship per Philippi's standard form) is presented in the *Kojiki* and the *Nihon shoki* as a younger brother of the sun-goddess Amaterasu and of the moon-deity Tsukuyomi, born from the purification of the primordial creator-deity Izanagi after Izanagi's return from the underworld; the three are positioned within the imperial-chronicle pantheon as a sun / moon / storm sibling-triad of high-ranking *kami*.footnote:[Philippi 1968, *Kojiki*, book 1 on Susanoo as a younger sibling of Amaterasu and Tsukuyomi born from Izanagi's purification, with the sun / moon / storm sibling-triad framing in the imperial-chronicle pantheon; glossary 'Susanoo' first_mention_gloss on Susanoo as Japanese storm-god expelled from heaven for misdeeds.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

Susanoo's character within the imperial-chronicle narrative is established in the chronicles as turbulent and disruptive: he weeps and rages, refuses the rule of the seas that Izanagi assigns to him, and demands instead to descend to the land where his deceased mother dwells, with this character-establishment serving as the narrative-structural reason for his subsequent expulsion from the heavenly plain.footnote:[Philippi 1968, *Kojiki*, book 1 on Susanoo's turbulent character (weeping, raging, refusing the rule of the seas) within the imperial-chronicle establishment-of-character that grounds his subsequent expulsion; Naumann 1996, on the same character-establishment of Susanoo across the two imperial chronicles.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

In the chronicle-narrative immediately preceding the Yamata no Orochi episode, Susanoo ascends to Takamagahara to take leave of Amaterasu and there commits a series of misdeeds — including damaging the rice-paddies of the heavenly plain, defiling the sacred weaving-hall of Amaterasu, and (in the *Kojiki* account) flaying a piebald colt from heaven and casting it into the weaving-hall — whereupon Amaterasu withdraws into the heavenly cave (*Ame-no-Iwato*) and the heavenly plain is plunged into darkness.footnote:[Philippi 1968, *Kojiki*, book 1 on Susanoo's misdeeds at Takamagahara (damaged rice-paddies, defiled weaving-hall, flayed piebald colt) and on Amaterasu's withdrawal into the heavenly cave that follows from them; Naumann 1996, on the same Takamagahara-misdeeds sequence as the immediate narrative-structural antecedent of the Yamata no Orochi episode.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

After Amaterasu is brought out of the heavenly cave by the assembled deities and the proper light is restored to the cosmos, the assembled heavenly *kami* judge Susanoo guilty of the misdeeds, levy a heavy expiatory fine, cut off his beard and the nails of his hands and feet, and expel him from Takamagahara. At this point Susanoo descends to the human world, and the narrative arrives at the moment immediately preceding his arrival in the land of Izumo where the Yamata no Orochi episode begins.footnote:[Philippi 1968, *Kojiki*, book 1 on the post-cave judgment of Susanoo, the expiatory fine, the cutting of beard and nails, and the expulsion from Takamagahara that immediately precedes Susanoo's descent to Izumo; Naumann 1996, on the same expulsion-and-descent sequence as the connecting narrative-structural moment between the heavenly-cave episode and the Yamata no Orochi episode.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

=== Setting in Izumo: the elderly couple and the seven daughters

The land of Izumo (出雲国) — a region on the Japan-Sea coast of western Honshu, conventionally read in the imperial-chronicle tradition as the geographical-and-mytho-historical setting of a substantial cycle of *kami*-narratives distinct from the Yamato-court-centred narratives of the imperial line — is the setting of the Yamata no Orochi episode and of the subsequent Susanoo and Ōkuninushi narratives that the *Kojiki* groups together as the Izumo-cycle of book 1.footnote:[Philippi 1968, *Kojiki*, book 1, on Izumo as the western-Honshu Japan-Sea-coast setting of the Susanoo / Yamata no Orochi episode and of the wider Izumo-cycle of the chronicle; Naumann 1996, Orochi chapter, on the Izumo geography of the narrative and on its distinct mytho-historical character within the imperial-chronicle structure.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

The episode begins specifically along the upper reaches of the river Hi (肥河, sometimes read Hi-no-kawa) in Izumo, where Susanoo, having descended from the heavenly plain, encounters a pair of chopsticks (or a similar small wooden item) floating downstream — a sign of human habitation upstream that motivates his ascent along the river-course in search of the people who had let the item fall.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's descent in the upper reaches of the river Hi in Izumo and on his observation of chopsticks floating downstream that motivates his upstream ascent; Naumann 1996, Orochi chapter, on the river-Hi setting of the encounter as a load-bearing geographic-narrative feature of the episode (significant for the metallurgical-allegory reading developed below).]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

Upstream Susanoo encounters an elderly couple — Ashinazuchi (足名椎, "foot-stroking-elder" in conventional gloss) and Tenazuchi (手名椎, "hand-stroking-elder" in conventional gloss) — together with their daughter, all of them weeping. The couple are presented in the chronicle as earthly *kami* (国つ神, *kunitsukami*) of the river-region, and their lineage is given in some renderings as descended from earlier earthly deities of Izumo.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's encounter with Ashinazuchi and Tenazuchi and their weeping daughter on the upper Hi-river; on the earthly-*kami* status of the couple and on their lineage within the Izumo earthly-deity tradition; Naumann 1996, Orochi chapter, on the same encounter-and-genealogy framing.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

The couple's daughter is named Kushinada-hime (奇稲田姫 / 櫛名田比売, "wondrous rice-paddy princess" in conventional gloss; her name links the figure to rice-paddy fertility within the early-Japanese agricultural imaginary), and she is the eighth and last surviving daughter of the couple, the previous seven daughters having been devoured one each year by the eight-headed serpent that comes to the river-region annually.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Kushinada-hime as the eighth and last surviving daughter of Ashinazuchi and Tenazuchi, with the previous seven daughters devoured one each year by the eight-headed serpent in an annual cycle of devouring; Naumann 1996, Orochi chapter, on the eighth-and-last-daughter / annual-cycle-of-devouring narrative pattern.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

When Susanoo asks the couple why they weep, they explain that the eight-headed serpent Yamata no Orochi is due to come again that year for the eighth daughter — and the couple's distress is the narrative's precipitating-crisis-moment, supplying the trigger for Susanoo's offer of help and the motivation that drives the Yamata no Orochi episode forward into the combat proper.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on the elderly couple's explanation of the imminent eighth-year arrival of Yamata no Orochi and on this explanation as the precipitating-crisis-moment that motivates Susanoo's intervention in the narrative; Naumann 1996, Orochi chapter, on the same precipitating-crisis-and-intervention pattern.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

=== Yamata no Orochi: the eight-headed serpent

Yamata no Orochi (八岐大蛇, "eight-forked great serpent" in literal gloss) is described in the chronicles as a serpent of extraordinary size: eight heads and eight tails on a single body, the length of the body spanning eight valleys and eight peaks of the surrounding mountainous terrain, the body covered with mosses and with cypresses and cryptomerias growing from it, and the underside red-rusted as if with blood — a description that is one of the most elaborate monstrous-adversary depictions in the entire imperial-chronicle corpus.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on the description of Yamata no Orochi (eight heads, eight tails, body spanning eight valleys and eight peaks, mosses and cypresses and cryptomerias growing on the body, red-rusted underside) as one of the most elaborate adversary-descriptions in the *Kojiki*; glossary 'Yamata no Orochi' first_mention_gloss on the eight-headed eight-tailed serpent of Izumo.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

The serpent's eight-foldedness — eight heads, eight tails, body across eight valleys and eight peaks — is itself a load-bearing structural feature of the narrative. The number eight (八, *ya*) recurs through the episode (eight-headed, eight-vatted sake, the eight valleys and eight peaks of the body's extent, and downstream eight-fold renderings in the post-combat narrative) and supplies a numerological-and-narrative coherence that scholars including Naumann register as a distinctively Japanese narrative-rhetorical pattern rather than as a comparativist trans-traditional motif.footnote:[Naumann 1996, Orochi chapter, on the load-bearing eight-fold numerological pattern of the Yamata no Orochi episode (eight heads, eight tails, eight valleys, eight peaks, eight vats of sake, eight-fold downstream attestations) as a distinctively Japanese narrative-rhetorical pattern within the imperial-chronicle Izumo-cycle; Philippi 1968, *Kojiki*, book 1, ch. 19, on the recurrence of the numeral eight throughout the episode.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The serpent's annual arrival from elsewhere — the chronicle does not specify where the serpent comes from when it is not at the river — together with the once-yearly devouring of one daughter, places the narrative within an early-Japanese imaginative pattern of recurring intrusive monstrous threats to settled-human-life-along-rivers. The pattern is registered by area-specialists including Naumann as a recurring-threat narrative-structure rather than as a once-and-for-all cosmogonic conflict.footnote:[Naumann 1996, Orochi chapter, on the annual-arrival / once-yearly-devouring / unspecified-elsewhere narrative-structural pattern of the Yamata no Orochi episode and on its place within early-Japanese narratives of recurring intrusive threats to settled-human-life-along-rivers; Philippi 1968, *Kojiki*, book 1, ch. 19, on the annual-cycle framing.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== Susanoo's plan: vats of sake and the fence

Susanoo, on hearing the elderly couple's account, first asks them to give him their daughter Kushinada-hime in marriage. The couple agree on Susanoo's revelation of his identity as a younger brother of Amaterasu, and Susanoo transforms Kushinada-hime — in the *Kojiki* account — into a comb (櫛, *kushi*; the figure's name itself contains the *kushi*-element of "comb") that he places in his hair-knot, securing her on his person while he prepares the trap for the serpent.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's request for Kushinada-hime in marriage, on the elderly couple's agreement after Susanoo's revelation of his identity, and on Susanoo's transformation of Kushinada-hime into a comb that he places in his hair-knot; Naumann 1996, Orochi chapter, on the comb-transformation as a load-bearing narrative feature linking the figure's name (Kushinada-hime) to the *kushi*-comb element.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

Susanoo then instructs the elderly couple to brew an "eight-fold refined sake" (八塩折之酒, conventionally rendered "sake brewed eight times over" or "eight-times-distilled sake" in current English-language Japanese-studies translations) — a particularly strong intoxicating drink the eight-fold refinement of which echoes the serpent's eight-foldedness and supplies the narrative's load-bearing numerological coherence between trap and target.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's instruction to brew the eight-fold refined sake (八塩折之酒) for the trap; Naumann 1996, Orochi chapter, on the eight-fold refinement of the sake as a load-bearing numerological echo of the serpent's eight-foldedness within the episode's overall pattern.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

Susanoo further instructs the couple to construct a fence around the brewing-area with eight gates, to place at each gate a platform on which to set a vat of the sake, and to fill the eight vats with the eight-fold refined sake — a deliberate one-vat-per-head configuration that sets up the trap's mechanism by guaranteeing that each of the serpent's eight heads will reach for its own vat when the serpent arrives.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's instructions for the fence with eight gates, the eight platforms with vats, and the one-vat-per-head trap-configuration; Naumann 1996, Orochi chapter, on the trap-configuration as a one-vat-per-head mechanism that guarantees each of the serpent's heads will be drawn to its own vat.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

The fence-and-vat construction is presented in the chronicles as a calculated craftsmanship operation rather than as a generic monster-hunt. Susanoo's plan exhibits the planning, the structural setup, and the staged execution that scholars including Naumann take to mark the episode as an organised craft-and-skill display in addition to its overt combat-and-killing narrative function — a feature that becomes load-bearing for the metallurgical-allegory reading developed below.footnote:[Naumann 1996, Orochi chapter, on the calculated-craftsmanship character of Susanoo's plan (the planning, the fence-and-vat structural setup, the staged execution) and on this craftsmanship-and-skill display as load-bearing for the subsequent metallurgical-allegory reading of the episode; Philippi 1968, *Kojiki*, book 1, ch. 19, on the same calculated-construction details of the trap.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== The combat: intoxication and dismemberment

Yamata no Orochi arrives as predicted, lowers each of its eight heads to the eight vats, drinks the eight-fold refined sake, and is intoxicated to the point of stupor, sinking to the ground and falling asleep — the entire combat being settled, in the *Kojiki* account, before any direct strike-by-strike fighting between Susanoo and the serpent has taken place.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on the serpent's arrival at the trap, the lowering of each of its eight heads to its own vat, the drinking of the eight-fold refined sake, and the intoxication-to-stupor-and-sleep that settles the encounter before any direct strike-by-strike combat; Naumann 1996, Orochi chapter, on the same intoxication-by-trap pattern as the load-bearing combat-resolution of the episode.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

Susanoo, with the serpent immobilised in stupor, draws his sword (the sword named in the *Kojiki* as Totsuka-no-Tsurugi, "ten-hands-long sword", the figure's standard weapon in the chronicle) and cuts the serpent into pieces, severing each of the eight heads and each of the eight tails in succession until the body is wholly dismembered along the river-course — and the river-water that runs from the dismembered body is described in the chronicles as flowing red with the serpent's blood.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's drawing of the Totsuka-no-Tsurugi (ten-hands-long sword, the chronicle's standard weapon for Susanoo) and on the dismemberment of the eight-headed eight-tailed serpent into pieces with the river running red with the serpent's blood; Naumann 1996, Orochi chapter, on the dismemberment-along-the-river-course pattern of the killing.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

The killing's mode — intoxication-trap followed by dismemberment of the immobilised body — distinguishes the Yamata no Orochi episode from the open-strike-by-strike combat-patterns of many comparativist comparanda. Area-specialists including Naumann register the trap-and-dismember structure as a feature of the narrative that the comparative chaoskampf reading tends to flatten when fitting the episode into the storm-god-vs-serpent frame; the trap-and-dismember structure is itself a load-bearing structural feature of the episode rather than a peripheral detail.footnote:[Naumann 1996, Orochi chapter, on the trap-and-dismember combat-mode of the Yamata no Orochi episode and on its distinctness from open-strike-by-strike combat-patterns in comparativist comparanda; on the area-specialist reading of the trap-and-dismember structure as a load-bearing structural feature of the episode rather than a peripheral detail; Philippi 1968, *Kojiki*, book 1, ch. 19, on the same combat-mode in the chronicle text.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== The discovery of Kusanagi in the tail

In the course of severing the eight tails of the serpent, Susanoo's sword (the Totsuka-no-Tsurugi) strikes the middle tail and chips its blade — the chronicle's first concrete signal that something other than mere serpent-flesh is in the tail — and Susanoo, investigating, splits the tail open with the sword and discovers within it a sword of unusual quality, sharp and undamaged where his own sword had chipped on contact.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's sword-strike on the middle tail, on the chipping of his Totsuka-no-Tsurugi blade as the first concrete signal that something is within the tail, and on the discovery within the tail of a sword of unusual quality that did not chip on impact; Naumann 1996, Orochi chapter, on the chipping-and-discovery sequence as the load-bearing narrative-structural moment of the episode for the chapter's sword-etiology reading.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

The sword discovered within the tail is named in the *Kojiki* as Kusanagi (草薙剣, "grass-cutting sword" in the chronicle's later etiology) — though the chronicle's narrative places the actual coining of the *Kusanagi* name later in the imperial-chronicle tradition, after the sword's role in the combat between the prince Yamato Takeru and a fire that the sword wards off by cutting away the surrounding grass.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19 (and the Yamato Takeru sequence later in the *Kojiki* on the actual *Kusanagi* "grass-cutting" name-etiology), on the sword's discovery within the tail and on the later imperial-chronicle naming of the sword as Kusanagi after the Yamato-Takeru-and-the-grass-fire episode; glossary 'Kusanagi' first_mention_gloss on Kusanagi as 'grass-cutter'; the sword found in Orochi's tail; one of the Three Sacred Treasures of the Japanese imperial regalia.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

Susanoo, recognising the sword's exceptional character, sends it as an offering to the heavenly plain and presents it to his elder sister Amaterasu — a presentation that re-establishes Susanoo's relation with Amaterasu after the Takamagahara misdeeds and that introduces the sword into the heavenly-line custody-chain that the imperial-chronicle tradition will continue forward into the human-imperial period.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 19, on Susanoo's presentation of the sword from the serpent's tail as an offering to Amaterasu in the heavenly plain, on the re-establishment of the sibling-relation that the offering enacts after the Takamagahara misdeeds, and on the introduction of the sword into the heavenly-line custody-chain that runs forward into the imperial-charter narrative; Naumann 1996, Orochi chapter, on the same presentation-to-Amaterasu sequence as the load-bearing transition from Izumo-cycle into imperial-charter narrative.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.19

The sword Kusanagi is the chapter's principal etiological outcome. The entire Yamata no Orochi episode is presented in the imperial-chronicle structure as the etiological-origin-story of one of the Three Sacred Treasures (三種の神器, *sanshu no jingi*) of the Japanese imperial regalia — alongside the mirror Yata-no-Kagami and the curved jewel Yasakani-no-Magatama — and the sword's presence in the regalia from the heavenly-cave-and-sun-restoration sequence onwards is the load-bearing narrative-structural function that the episode performs within the *Kojiki*'s overall chronicle-of-imperial-charter purpose.footnote:[Philippi 1968, *Kojiki*, book 1, on the Three Sacred Treasures (三種の神器) of the Japanese imperial regalia comprising the sword Kusanagi from the Yamata no Orochi episode, the mirror Yata-no-Kagami, and the curved jewel Yasakani-no-Magatama; on the sword-etiology load-bearing function of the Yamata no Orochi episode within the imperial-charter purpose of the chronicle; Naumann 1996, Orochi chapter, on the same Three-Sacred-Treasures imperial-charter framing.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

=== Aftermath: marriage and the Izumo-cycle

After the slaying of the serpent and the presentation of the sword to Amaterasu, Susanoo restores Kushinada-hime from her comb-form and marries her, and he then constructs a palace at Suga in Izumo for the new household — a palace that, in the *Kojiki* account, is established with a famous five-syllable poem (often cited as the first *waka* of the imperial-chronicle tradition) that Susanoo composes on the occasion of the marriage and the palace-construction.footnote:[Philippi 1968, *Kojiki*, book 1, ch. 20, on Susanoo's restoration of Kushinada-hime from her comb-form, on his marriage to her, on the construction of the palace at Suga in Izumo, and on the famous five-syllable poem (often cited as the first *waka* of the imperial-chronicle tradition) that Susanoo composes on the occasion; Naumann 1996, Orochi chapter, on the same marriage-and-palace-construction sequel.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki 1.20

The marriage and the palace-construction at Suga in Izumo function as the narrative-structural transition from the Yamata no Orochi episode proper into the wider Izumo-cycle of the *Kojiki* and the *Nihon shoki*. Susanoo and Kushinada-hime are the founding couple of an Izumo-deity lineage that includes the descendants Yashima-jinumi, Ōnamuchi (more familiarly Ōkuninushi), and the further sequence of Izumo earthly *kami* whose narratives occupy the remainder of book 1 of the *Kojiki* down to the negotiated transfer of the land to the heavenly line.footnote:[Philippi 1968, *Kojiki*, book 1 chs. 20 onwards, on the marriage-and-palace-construction at Suga in Izumo as the narrative-structural transition into the wider Izumo-cycle; on the descendant-lineage of Yashima-jinumi, Ōnamuchi (Ōkuninushi), and the further Izumo earthly *kami* down to the negotiated transfer of the land; Naumann 1996, Orochi chapter, on the same Izumo-cycle continuation.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

The sword Kusanagi, after its presentation to Amaterasu in the heavenly plain, descends in the imperial-chronicle's continuing narrative-arc together with the mirror and the curved jewel as the Three Sacred Treasures: in the chronicle's account of the descent of the heavenly grandson Ninigi-no-Mikoto to the human world, the three regalia are entrusted to him by Amaterasu as the charter-objects of the line that will become the imperial dynasty, and the sword is from this point forward the imperial sword of the Japanese ruling line.footnote:[Philippi 1968, *Kojiki*, book 1, on the descent of the heavenly grandson Ninigi-no-Mikoto to the human world, on Amaterasu's entrustment of the Three Sacred Treasures (the sword Kusanagi from the Yamata no Orochi episode, the mirror Yata-no-Kagami, and the curved jewel Yasakani-no-Magatama) to him as the charter-objects of the imperial line, and on the sword's role from this point as the imperial sword of the Japanese ruling line; Naumann 1996, Orochi chapter, on the imperial-charter continuation of the sword from the Izumo episode into the descent-of-Ninigi sequence.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

The chapter's principal Three-Sacred-Treasures forward-arc within the *Kojiki* is therefore: the sword Kusanagi originates within the body of Yamata no Orochi in Izumo, is presented by Susanoo to Amaterasu in the heavenly plain, descends with Ninigi to the human world as one of the three charter-objects of the imperial line, and is from then onwards a load-bearing object of imperial-Japanese ritual and political-legitimation tradition — a forward-arc that the present chapter registers as the dominant narrative-structural function of the Yamata no Orochi episode within the chronicle's overall purpose.footnote:[Philippi 1968, *Kojiki*, book 1, on the forward-arc of the sword Kusanagi from the Yamata no Orochi episode through the heavenly-plain presentation to Amaterasu and the descent of Ninigi as one of the Three Sacred Treasures of the imperial line; per brief 23-susanoo-orochi.yaml cultural_relevance.function on sword-etiology and royal-legitimation as the chapter's load-bearing narrative-structural functions.]
// EVIDENCE: source_id=philippi-kojiki ; loc=Kojiki book 1

The sword Kusanagi as a continuing imperial regalium — kept, per the imperial-chronicle and post-chronicle tradition, at the Atsuta Shrine in Owari (modern Aichi Prefecture, Japan) — supplies the Yamata no Orochi episode's connection to a continuing-into-the-historical-period ritual-and-political-legitimation institution that anchors the early-medieval imperial-Japanese ruling line's mythic charter to a specific physical-and-ritual locus, and the chapter registers this institutional continuation as part of the episode's load-bearing function within the *Kojiki* / *Nihon shoki* purpose.footnote:[Naumann 1996, Orochi chapter, on the continuing imperial-regalium status of the sword Kusanagi at the Atsuta Shrine in Owari (modern Aichi Prefecture) and on the institutional continuation of the Yamata no Orochi episode's sword-etiology into the historical-period ritual-and-political-legitimation institution of the Japanese imperial line.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== The metallurgical-allegory reading

The principal area-specialist reading of the Yamata no Orochi episode in current scholarship — developed in detail by Nelly Naumann, with the wider Japanese-studies attention to early-Japanese imperial-charter and ritual-religion readings represented by subsequent area-specialists (Jun'ichi Isomae, Michael Como, and Herman Ooms are flagged as scholars of early Japanese religion whose work develops compatible specialist framings, though their works are not yet in the present book's sources.yaml registry and are not load-bearing for any individual EVIDENCE-anchored claim in this chapter) — is metallurgical-allegorical: the eight-headed serpent figures the iron-smelting industry of the Izumo-Hi-river region in the early-historical period, and the discovery of the sword in the serpent's tail figures the metallurgical emergence of the bladed weapon from the smelting-and-forging process.footnote:[Naumann 1996, *Die Mythen des alten Japan*, Orochi chapter, on the metallurgical-allegory reading of the Yamata no Orochi episode in which the eight-headed serpent figures the iron-smelting industry of the Izumo-Hi-river region and the discovery of the sword in the serpent's tail figures the metallurgical emergence of the bladed weapon from the smelting-and-forging process; the body-prose acknowledgement of Isomae, Como, and Ooms as subsequent Japanese-studies area-specialists is flagged for inventory-audit pending their addition to sources.yaml; per brief 23-susanoo-orochi.yaml cultural_relevance.function on the metallurgical-allegory reading.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The metallurgical reading rests on a constellation of narrative-structural features of the episode: the river-Hi setting (the upper river-courses of mountainous regions are the historical-period sites of iron-sand mining and *tatara* smelting in Japan); the serpent's red-rusted underside (red rust as the visible signature of iron-bearing minerals along river-courses); the serpent's enormous size spanning eight valleys and eight peaks (the geographic scale of the smelting industry's catchment of fuel-wood and ore); and the chipping of Susanoo's existing sword on the tail (the metallurgical-quality difference between an older and a newer bladed weapon).footnote:[Naumann 1996, Orochi chapter, on the constellation of narrative-structural features of the Yamata no Orochi episode that ground the metallurgical-allegory reading: the river-Hi setting as the historical-period site of iron-sand mining and *tatara* smelting; the red-rusted underside as the visible signature of iron-bearing minerals along river-courses; the serpent's eight-valleys-and-eight-peaks scale as the geographic scale of the smelting industry's catchment; the chipping of Susanoo's existing sword on the tail as the metallurgical-quality difference between an older and a newer bladed weapon.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

That the metallurgical reading is the standard area-specialist treatment is itself an editorial synthesis drawn from the brief's named scholars and from Naumann 1996's Orochi chapter, and the chapter flags the synthesis accordingly:

[INFERENCE: the chapter's compact summary that the metallurgical-allegory reading "is now the standard area-specialist reading of the episode" is a synthesis of the area-specialist literature represented by Naumann 1996 in the present chapter's source-base, supported by the brief's special_instructions naming Naumann, Isomae, Como, and Ooms as the area-specialists whose framing is load-bearing for the chapter's outside-framing requirement. | basis: Naumann 1996's Orochi chapter develops the metallurgical-allegory reading in detail, and the brief 23-susanoo-orochi.yaml cultural_relevance.function explicitly names "per Naumann / Isomae / Como / Ooms: metallurgical allegory — the serpent represents iron-smelting and the sword's emergence from its body represents the craft of sword-making" as the area-specialist reading. | risk: the present chapter cites only Naumann 1996 from sources.yaml; Isomae, Como, and Ooms are NAMED in the body prose per the brief's area-specialist citation policy and per scope.md §"Appropriation protocol" requirement of two area-specialists by name in the first factual pass, but their works are not in the current sources.yaml registry — the factcheck stage will need to verify the metallurgical-allegory attribution to all four scholars and either flag added entries for Isomae, Como, and Ooms in sources.yaml or downgrade the citation to Naumann-only with the others as "subsequent specialists who develop the same reading".]

The metallurgical-allegory reading reframes the principal narrative elements of the episode in a way that the chapter's chaoskampf reading, taken on its own, does not deliver: the serpent is not "chaos" in any thematically-coherent area-specialist sense but is the iron-smelting infrastructure of a specific regional industry; the sword is not a generic regalium but the metallurgical product of the smelting-and-forging craft; and Susanoo's victory is not the establishment of cosmic order but the technological-mastery moment in which the storm-deity-figure brings the iron-smelting industry under the control of the heavenly line that the Yamato court traces itself back to.footnote:[Naumann 1996, Orochi chapter, on the metallurgical-allegory reading's reframing of the principal narrative elements: the serpent as the iron-smelting infrastructure of a specific regional industry rather than as "chaos"; the sword as the metallurgical product of the smelting-and-forging craft rather than as a generic regalium; Susanoo's victory as the technological-mastery moment in which the storm-deity-figure brings the iron-smelting industry under heavenly-line control rather than as the establishment of cosmic order.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The metallurgical reading further connects the Yamata no Orochi episode to the early-historical-period political-economic context of the Yamato court's expansion into Izumo. Control of the iron-smelting industry of the Izumo-Hi-river region was a load-bearing material-political stake of the early-imperial period, and the chronicle's narrative-structural placement of the sword-etiology within the Izumo-cycle reflects this political-economic stake of the late-seventh-and-early-eighth-century moment of the chronicles' compilation rather than reflecting a primordial cosmogonic-combat narrative free of period-specific political content.footnote:[Naumann 1996, Orochi chapter, on the early-historical-period political-economic context of the Yamato court's expansion into Izumo, on the iron-smelting industry of the Izumo-Hi-river region as a load-bearing material-political stake of the early-imperial period, and on the chronicle's narrative-structural placement of the sword-etiology as reflecting this political-economic stake of the late-seventh-and-early-eighth-century moment of the chronicles' compilation.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The implication of the metallurgical-allegory reading for the chapter's chaoskampf-typology purpose is direct: if the area-specialist reading is correct that the serpent figures iron-smelting and the sword figures the metallurgical product of smelting, then the episode's load-bearing narrative function is sword-etiology and metallurgical-and-political charter rather than cosmogonic combat — and the chaoskampf label is at best a loose typological-comparative description that fits the surface narrative-structure (storm-deity defeats serpentine adversary, recovers powerful weapon) without engaging the area-specialist account of what the narrative is actually doing in its early-Japanese context.footnote:[Naumann 1996, Orochi chapter, on the implication of the metallurgical-allegory reading for the chapter's typological-purpose: if the area-specialist reading is correct, the episode's load-bearing function is sword-etiology and metallurgical-and-political charter rather than cosmogonic combat; on the chaoskampf label as a loose typological-comparative description that fits the surface narrative-structure without engaging the area-specialist account of what the narrative is doing in its early-Japanese context; per brief 23-susanoo-orochi.yaml special_instructions on the same area-specialist counter-framing.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== The chaoskampf label as applied from outside

The chaoskampf reading of the Yamata no Orochi episode — in which Susanoo is read as a storm-deity figure parallel to Indra (in his combat with Vṛtra) and to Thor (in his combat with Jörmungandr), and the eight-headed serpent is read as a multi-headed monstrous adversary in the cross-tradition family of Lôtan / Leviathan, Aži Dahāka, Ladon, and the Dobrynya cycle's Zmey Gorynych — is a 20th-century-Western comparativist move developed within the wider scholarly tradition of cross-cultural combat-myth comparison represented in the present book's source-base by the long-arc Sumer-through-Judeo-Christian-apocalyptic treatments of Forsyth 1987 and others, into whose typological frame the Susanoo / Orochi episode has been brought from outside the early-Japanese tradition.footnote:[Forsyth 1987, *The Old Enemy*, as the long-arc combat-myth typology anchor (Sumer through Judeo-Christian apocalyptic) within whose comparativist storm-god-vs-multi-headed-serpent frame the Susanoo / Yamata no Orochi episode has been read by 20th-century-Western comparativists; Forsyth 1987 does not itself treat the Japanese material, and the chapter's use of the citation is for the typological framing rather than for source-content coverage of the Orochi episode; per brief 23-susanoo-orochi.yaml cross_cultural_parallels on the COMPARATIVIST reading that parallels the episode to Indra-Vṛtra and Thor-Jörmungandr as storm-god / serpent combat.]
// EVIDENCE: source_id=forsyth-1987 ; loc=combat-myth long-arc typology (Sumer through Judeo-Christian apocalyptic)

The comparativist chaoskampf reading rests on three principal structural-similarity points: (1) Susanoo is a storm-deity (although the chronicle's primary characterisation is of his turbulent and disruptive temperament rather than of meteorological storm-power per se); (2) Yamata no Orochi is a multi-headed serpentine adversary (a feature shared with Lôtan / Leviathan, Aži Dahāka, Ladon, and Zmey Gorynych across the present book's other chapters); and (3) the encounter is an asymmetric combat in which the deity-figure defeats the serpent and recovers a powerful weapon from the encounter.footnote:[Forsyth 1987, on the three principal structural-similarity points (storm-deity opponent, multi-headed serpentine adversary, asymmetric combat with weapon-recovery outcome) as the schema that the long-arc combat-myth typology supplies for the comparativist reading of the Susanoo / Yamata no Orochi episode; the schema is general to Forsyth's Sumer-through-Judeo-Christian-apocalyptic comparative frame and does not derive from any Forsyth treatment of the Japanese material itself; per brief 23-susanoo-orochi.yaml cross_cultural_parallels on the COMPARATIVIST reading.]
// EVIDENCE: source_id=forsyth-1987 ; loc=combat-myth long-arc typology (Sumer through Judeo-Christian apocalyptic)

The area-specialist counter-position — represented in the chapter's source-base by Naumann 1996, and named in the brief's special_instructions together with the further area-specialists Jun'ichi Isomae, Michael Como, and Herman Ooms — is that the comparativist label is applied from outside the early-Japanese tradition: the episode's internal narrative-structural function within the imperial-chronicle context is sword-etiology and metallurgical-allegorical-political charter, the storm-deity / serpentine-adversary surface-description is real but is not the load-bearing function, and the chaoskampf reading therefore tends to flatten what the area-specialist tradition takes the episode to be doing.footnote:[Naumann 1996, Orochi chapter, on the area-specialist counter-position that the comparativist chaoskampf label is applied from outside the early-Japanese tradition; on the episode's internal narrative-structural function as sword-etiology and metallurgical-allegorical-political charter rather than cosmogonic combat; on the storm-deity / serpentine-adversary surface-description as real but not the load-bearing function; per brief 23-susanoo-orochi.yaml cross_cultural_parallels on the AREA-SPECIALIST reading.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The area-specialist and comparativist readings are presented side by side as a substantive variant choice that the chapter resolves in favour of the area-specialist reading:

[VARIANT: primary=area-specialist reading per Naumann 1996 and the further area-specialists Isomae, Como, Ooms named in the brief — sword-etiology and metallurgical-allegorical-political charter as the load-bearing internal function of the Yamata no Orochi episode within the imperial-chronicle context | alt=comparativist chaoskampf reading per Forsyth 1987 and the wider 20th-century-Western combat-myth comparative tradition — storm-deity-vs-multi-headed-serpent combat-pattern shared with Indra-Vṛtra, Thor-Jörmungandr, and the wider cross-tradition multi-headed-serpent family | chosen: present-the-area-specialist-reading-as-load-bearing-with-the-comparativist-reading-as-engaged-but-not-endorsed | reason: per scope.md §"Book structure" cluster 9 and §"Appropriation protocol" on the chapter's required outside-framing of the chaoskampf label; per brief 23-susanoo-orochi.yaml special_instructions on the chapter's task of treating the chaoskampf label as applied from outside; per scope.md §"Inclusion / exclusion criteria" on the related-tier classification (rather than core-tier) that follows from the area-specialist objection to the chaoskampf framing.]

That choice is the specific outcome of an area-specialist objection to the comparativist framing, and the chapter flags the objection explicitly under the appropriation-protocol marker the project reserves for cases of this kind:

[APPROPRIATION-FLAG: Japanese-studies area specialists (Nelly Naumann; with subsequent Japanese-religion specialists Jun'ichi Isomae, Michael Como, and Herman Ooms named in the chapter brief) object to the chaoskampf framing of the Susanoo / Yamata no Orochi episode on the grounds that the episode's load-bearing internal function within the early-Japanese imperial-chronicle context is sword-etiology and metallurgical-allegorical-political charter (the eight-headed serpent figuring the Izumo-Hi-river iron-smelting industry; the sword discovered in the tail figuring the metallurgical product of smelting-and-forging; Susanoo's victory figuring the heavenly line's bringing of the Izumo iron-smelting industry under Yamato-court control), not cosmogonic-or-sovereignty combat in the chaoskampf-typological sense. The objection is the substantive reason scope.md §"Book structure" cluster 9 demoted this chapter from CORE to related-tier, and is the reason the chapter opens with the area-specialist framing rather than with the chaoskampf comparison. Part II C8 (refusal and appropriation; ch. 41 of the present volume) is the locus where the comparative analysis must address this objection rather than paper over it; the present chapter functions as a worked instance of the appropriation-protocol's outside-framing requirement at scope.md §"Appropriation protocol" point 3, and forwards the objection to C8 for the comparative-engagement work that scope.md §"Appropriation protocol" point 2 requires of the comparative chapter.]

The chapter's resolution of the area-specialist / comparativist tension is to present the two readings together but not as equally weighted: the area-specialist reading is the chapter's load-bearing reading — the one that organises the chapter's account of what the episode is doing in its early-Japanese context — while the comparativist chaoskampf reading is engaged as a 20th-century-Western move that the chapter registers, considers, and does not endorse, on the grounds that scope.md §"Book structure" cluster 9 demoted the chapter from CORE precisely because of the area-specialists' objection to the comparativist framing.footnote:[Per scope.md §"Book structure" cluster 9 on the chapter's demotion from CORE because of the area-specialist objection to the comparativist chaoskampf framing; per scope.md §"Appropriation protocol" on the load-bearing-area-specialist-reading citation policy; per brief 23-susanoo-orochi.yaml special_instructions on the chapter's resolution of the area-specialist / comparativist tension by presenting the area-specialist reading as load-bearing and the comparativist chaoskampf reading as engaged but not endorsed.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

=== Typology and forward-links

The Yamata no Orochi episode's place within the present book's chaoskampf typology is therefore a related-tier (rather than core-tier) classification that is itself the substantive scholarly point of the chapter: the chapter is included in Part I to exhibit a working example of an episode that under one reading (the comparativist) belongs in the cosmogonic-or-sovereignty-combat family, but under the area-specialist reading is doing different work (sword-etiology and metallurgical-allegorical-political charter), and the chapter's typological function is to make this category-loose-ness visible to the reader rather than to deliver a confident chaoskampf classification.footnote:[Per scope.md §"Inclusion / exclusion criteria" on the related-tier classification of the Yamata no Orochi episode that follows from the area-specialist objection to the chaoskampf framing; per brief 23-susanoo-orochi.yaml special_instructions on the chapter's typological function of making the category-loose-ness visible rather than delivering a confident chaoskampf classification.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's principal forward-link within the present book is to Part II C7 (the comparative chapter on the inversion / transformation problem, ch. 40 of the present volume) — where the present chapter contributes a working example of the *transformation* sub-problem: not a story in which the slaying inverts the order-establishing function (the inversion sub-problem proper, anchored by the Bida material in chapter 28), but a story in which the chaoskampf category itself is transformed when the area-specialist account is taken as load-bearing.footnote:[Per brief 23-susanoo-orochi.yaml special_instructions on the chapter's contribution to Part II C7 (inversion / transformation); per scope.md §"Book structure" on Part II C7 as the inversion-and-transformation comparative chapter; on the distinction between the inversion sub-problem proper (the Bida material in ch. 28) and the transformation sub-problem (the present chapter as a working example).]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's secondary forward-link is to Part II C8 (the comparative chapter on the refusal and the appropriation problem, ch. 41 of the present volume) — where the present chapter contributes a working example of the *appropriation* sub-problem: a story in which the comparative chaoskampf category, applied from outside the early-Japanese tradition, risks flattening the area-specialist account of what the episode is doing in its own context, and where the chapter's task is to hold the comparative category loosely as scope.md §"Appropriation protocol" requires.footnote:[Per brief 23-susanoo-orochi.yaml special_instructions on the chapter's contribution to Part II C8 (refusal and appropriation); per scope.md §"Book structure" on Part II C8 as the refusal-and-appropriation comparative chapter; per scope.md §"Appropriation protocol" on the chapter's task of holding the comparative chaoskampf category loosely where area-specialists require it.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's contribution to the methods sidebar (ch. 33 of the present volume, between Part I and Part II) is as a worked instance of the appropriation-protocol's outside-framing requirement: the chapter exhibits, in concrete narrative-and-citation-discipline detail, what it looks like to open with the tradition's own framing (sword-etiology, metallurgical-allegorical-political charter, imperial-charter purpose) before invoking the comparative chaoskampf category, in line with scope.md §"Appropriation protocol" point 3.footnote:[Per scope.md §"Appropriation protocol" point 3 on the requirement that every related-tier chapter on a non-Eurasian tradition open with the tradition's own framing before invoking the comparative chaoskampf category; per brief 23-susanoo-orochi.yaml special_instructions on the chapter's contribution to the methods sidebar (ch. 33) as a worked instance of the appropriation-protocol's outside-framing requirement.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's principal back-link within the present book is to the immediately preceding chapter 22 on Hou Yi and the suns, with which the present chapter shares the East Asian geographic cluster (cluster 9 per scope.md §"Book structure") and the related-tier classification, but contrasts in the precise reason for the related-tier rather than core-tier status: the Hou Yi cycle is related-tier because it is heroic-restorative rather than cosmogonic, while the Susanoo / Yamata no Orochi episode is related-tier because area-specialists object to the chaoskampf framing on grounds of the metallurgical-allegorical-political-charter alternative reading.footnote:[Per scope.md §"Book structure" cluster 9 on the East Asian geographic-cluster ordering of chapters 21 (Gonggong, core-tier), 22 (Hou Yi, related-tier), and 23 (Susanoo / Yamata no Orochi, related-tier); per brief 22-hou-yi.yaml on the related-tier classification of the Hou Yi cycle on the basis of its heroic-restorative-rather-than-cosmogonic combat-pattern; per brief 23-susanoo-orochi.yaml on the related-tier classification of the Yamata no Orochi episode on the basis of the area-specialists' metallurgical-allegorical-political-charter alternative reading.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's secondary back-link is to chapter 21 on Gonggong and the broken pillar, with which the present chapter shares the early-historical-period East Asian textual context (early-imperial chronicles in Chinese and early-Japanese; the *Kojiki* and the *Nihon shoki* are themselves composed in the kanbun-and-man'yōgana register that is structurally indebted to the Han-period Chinese chronicle tradition that the Gonggong material survives within) but contrasts in the typological function (the Gonggong material is core-tier cosmogonic combat with the post-combat hydrography of the cosmos as the chapter's load-bearing cosmogonic credential; the present chapter is related-tier sword-etiology with the Three Sacred Treasures as the chapter's load-bearing imperial-charter credential).footnote:[Per scope.md §"Book structure" cluster 9 on the East Asian geographic-cluster pairing of chapters 21 (Gonggong, core-tier cosmogonic) and 23 (Susanoo / Yamata no Orochi, related-tier sword-etiology); per brief 21-gonggong.yaml on the core-tier cosmogonic classification of the Gonggong material; per brief 23-susanoo-orochi.yaml on the related-tier sword-etiology classification of the Yamata no Orochi episode.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

The chapter's place within the present book's wider comparative argument is therefore as a worked example of the book's willingness to hold the comparative chaoskampf category loosely where area-specialists require it: the chapter does not pretend that the comparativist chaoskampf reading is wrong (the Indra-Vṛtra / Thor-Jörmungandr surface-similarity is real and is registered in the chapter's COMPARATIVE-HOOK section below), but it also does not let the comparativist surface-similarity override the area-specialist reading of the episode's internal load-bearing function — and the chapter's overall argumentative gesture is the methods-and-discipline gesture of holding both readings in view without collapsing them into one another.footnote:[Per scope.md §"Appropriation protocol" on the chapter's task of holding both readings in view without collapsing them into one another; per brief 23-susanoo-orochi.yaml special_instructions on the chapter's overall argumentative gesture as a worked example of the book's willingness to hold the comparative chaoskampf category loosely where area-specialists require it.]
// EVIDENCE: source_id=naumann-mythen ; loc=Orochi chapter

// COMPARATIVE-HOOK: Mesopotamia (Marduk-Tiamat, Ch. 3) and India (Indra-Vṛtra, Ch. 14) — the comparativist chaoskampf reading of the Susanoo / Yamata no Orochi episode pairs the storm-deity-vs-multi-headed-serpent surface-pattern of the *Kojiki* episode with the storm-deity-vs-serpent combats of the Mesopotamian and Vedic CORE chapters; the present chapter holds the surface-similarity in view but registers the area-specialist objection that the early-Japanese material's load-bearing function is sword-etiology and metallurgical-allegorical-political charter rather than cosmogonic-or-sovereignty combat; per brief 23-susanoo-orochi.yaml cross_cultural_parallels.
// COMPARATIVE-HOOK: Norse (Thor-Jörmungandr, Ch. 18) — the comparativist parallel of Susanoo to Thor as storm-deity-vs-serpent combatant is a particularly load-bearing comparativist move within the 20th-century-Western combat-myth tradition; the present chapter registers the surface-pattern parallel and refers the comparison forward to Part II C2 (combat as sovereignty) and C7 (inversion / transformation) where it is engaged as a comparison rather than an identification; per brief 23-susanoo-orochi.yaml cross_cultural_parallels.
// COMPARATIVE-HOOK: Multi-headed-monster motif (Lôtan / Leviathan Ch. 7-8; Vṛtra Ch. 14; Aži Dahāka Ch. 13; Ladon and Hydra in the Greek dragon-combats Ch. 12; Zmey Gorynych Ch. 20; Jiuying within the Hou Yi cycle Ch. 22) — the eight-headed eight-tailed Yamata no Orochi joins the wider cross-tradition family of multi-headed serpentine adversaries on the surface-similarity register; the present chapter's area-specialist counter-framing (the eight-foldedness as a distinctively Japanese narrative-rhetorical pattern serving the metallurgical-allegorical-political-charter function) is one of the chapter's load-bearing contributions to the methods sidebar (Ch. 33) on the boundary between surface-similarity and load-bearing-function in cross-tradition comparison.
// COMPARATIVE-HOOK: Iran (Thraētaona vs. Aži Dahāka, Ch. 13) — the structural feature of a hero-figure recovering or producing a powerful weapon from / through the combat with a multi-headed serpentine adversary is a comparativist parallel between Susanoo's recovery of Kusanagi from Yamata no Orochi's tail and Thraētaona's combat with the three-headed Aži Dahāka; the area-specialist counter-framing of the Susanoo episode as sword-etiology raises the question of whether the Iranian material admits a similar functional reading and contributes to Part II C2 (combat as sovereignty) on the relation of weapon-recovery to sovereignty-establishment.
// COMPARATIVE-HOOK: Inversion / transformation (Part II C7, Ch. 40) — the present chapter is a working example of the *transformation* sub-problem: a story in which the chaoskampf category itself is transformed when the area-specialist account (sword-etiology and metallurgical-allegorical-political charter) is taken as load-bearing rather than the comparativist surface-pattern reading; this is to be distinguished from the inversion sub-problem proper, anchored by the Bida material in chapter 28 (where the slaying inverts the order-establishing function rather than transforms the category); per brief 23-susanoo-orochi.yaml special_instructions on the contribution to Part II C7.
// COMPARATIVE-HOOK: Refusal and appropriation (Part II C8, Ch. 41) — the present chapter is a working example of the *appropriation* sub-problem: a story in which the comparative chaoskampf category, applied from outside the early-Japanese tradition, risks flattening the area-specialist account of what the episode is doing in its own context; this contributes alongside the Rainbow-Serpent and Nanabozho-Mishipeshu material to Part II C8's wider treatment of how not to flatten traditions into chaoskampf; per brief 23-susanoo-orochi.yaml special_instructions on the contribution to Part II C8.
// COMPARATIVE-HOOK: Methods sidebar (Ch. 33) — the present chapter is a worked instance of the appropriation-protocol's outside-framing requirement (scope.md §"Appropriation protocol" point 3): the chapter exhibits in concrete narrative-and-citation-discipline detail what it looks like to open with the tradition's own framing (sword-etiology, metallurgical-allegorical-political charter, imperial-charter purpose per Naumann, Isomae, Como, Ooms) before invoking the comparative chaoskampf category, and to hold the comparative category loosely where area-specialists require it; per scope.md §"Book structure" on the methods-sidebar function of registering this kind of worked-instance contribution from related-tier chapters across Part I.
// COMPARATIVE-HOOK: East Asian geographic cluster (Ch. 21 Gonggong core-tier cosmogonic; Ch. 22 Hou Yi related-tier heroic-restorative; Ch. 23 Susanoo / Yamata no Orochi related-tier sword-etiology) — the three East Asian chapters together exhibit three distinct combat-narrative templates within a single geographic cluster, each grounded in a different load-bearing typological function (cosmogonic combat; heroic-restorative; sword-etiology and metallurgical-allegorical-political charter); the cluster's internal three-way contrast is itself a load-bearing methodological contribution to the present book on the question of what range of work combat-narratives can do within and across traditions.
// COMPARATIVE-HOOK: Imperial-charter regalia function (Three Sacred Treasures of the Japanese imperial regalia: sword Kusanagi from the Yamata no Orochi episode, mirror Yata-no-Kagami, curved jewel Yasakani-no-Magatama) — the sword-etiology function of the Susanoo / Yamata no Orochi episode within the imperial-chronicle tradition is part of a wider Three-Sacred-Treasures imperial-regalia complex that has no close parallel in the present book's other chapters; the regalia-establishment function is a distinctively early-Japanese narrative-structural feature that the chapter's area-specialist framing makes load-bearing; this contributes to Part II C2 (combat as sovereignty) as a non-cosmogonic-but-sovereignty-related comparandum.
```
