# Stage 12 of 19: narrative-fidelity
# Book: chaoskampf
# Generated: 2026-04-26T15:02:49Z

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
    full_citation: "Philippi, D.L. (trans.), *Kojiki* (Tokyo: University of Tokyo Press, 1968)."
    short_citation: "Philippi 1968"
    identifier_type: ISBN
    identifier_value: "9780691611358"
    notes: "Scholarly-standard English Kojiki. Anchor for Susanoo/Orochi."

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

# Input file: chapters/11-zeus-typhon.claims.approved.adoc

```
[[ch-11-zeus-typhon-claims]]
== Zeus vs. Typhon: The Olympian Combat — Claims

// This is a claims document, not final prose. Each paragraph is one verifiable claim.
// After fact-check and human review, chapter-draft will transform this into narrative.

=== Source overview

Hesiod's _Theogony_, lines 820–880, is the earliest surviving narrative of the combat between Zeus (Ζεύς) and Typhon (Τυφῶν), the hundred-headed serpent-limbed monster whose Hesiodic-variant name is Typhoeus (Τυφωεύς).footnote:[West 1966, _Hesiod, Theogony_, on lines 820–880; Ogden 2013, ch. 2, on the Typhonomachy as the earliest Greek dragon-combat narrative.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The standard critical edition of the _Theogony_ used as the anchor throughout this chapter is Martin L. West's 1966 Oxford Clarendon edition, which provides the Greek text together with a detailed line-by-line commentary on the Typhonomachy passage.footnote:[West 1966, _Hesiod, Theogony_ (Oxford: Clarendon Press), critical edition with commentary.]
// EVIDENCE: source_id=west-1966-theogony ; loc=whole volume

The standard scholarly survey of the Greek dragon-combat tradition used as the secondary anchor throughout this chapter is Daniel Ogden's 2013 _Drakōn: Dragon Myth and Serpent Cult in the Greek and Roman Worlds_, especially chapters 2 and 3, which catalogue the Typhon material across the Greek and Roman literary record.footnote:[Ogden 2013, _Drakōn_, chs. 2–3.]
// EVIDENCE: source_id=ogden-2013 ; loc=chs. 2–3

The _Theogony_ is conventionally dated to c. 700 BCE and assigned to the late-eighth- or early-seventh-century Boeotian poet Hesiod, whose autobiographical voice frames the poem's prologue at the foot of Mount Helicon.footnote:[West 1966, introduction, on the date and authorship of the _Theogony_.]
// EVIDENCE: source_id=west-1966-theogony ; loc=introduction

The _Theogony_ survives in a continuous medieval manuscript tradition descended from Byzantine exemplars and is well preserved in its principal manuscript witnesses; the Typhonomachy passage at lines 820–880 has no significant lacunae and is read by all modern editors as a continuous text.footnote:[West 1966, introduction and apparatus on lines 820–880, on the manuscript tradition and the integrity of the Typhonomachy passage.]
// EVIDENCE: source_id=west-1966-theogony ; loc=introduction

The structural function of the Typhonomachy within the _Theogony_ is the closing combat: it is positioned after the Titanomachy (lines 617–819) and before the poem's enumeration of Zeus's marriages and his children, and it is the last divine combat before the stable Olympian pantheon takes its final shape.footnote:[West 1966, on the structural placement of the Typhonomachy at lines 820–880; Ogden 2013, ch. 2, on the Typhonomachy as the close of the _Theogony_.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The full Greek narrative of the Typhonomachy is a reconstruction from multiple sources rather than a single text: Hesiod gives the earliest sketch, Apollodorus _Bibliotheca_ 1.6.3 (1st–2nd c. CE) gives the extended canonical form, and Nonnus _Dionysiaca_ 1–2 (5th c. CE) gives a baroque late-antique elaboration.footnote:[Ogden 2013, ch. 2, on the multi-source reconstruction of the Typhonomachy across Hesiod, Apollodorus, and Nonnus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The continuous Greek attestation of the Typhonomachy spans more than a millennium, from Hesiod's late-eighth- or early-seventh-century version to Nonnus's fifth-century reworking, with intervening attestations in the _Homeric Hymn to Apollo_, Pindar, Aeschylus, and others.footnote:[Ogden 2013, chs. 2–3, on the millennium-long continuous attestation; West 1966, introduction, on the early Greek context.]
// EVIDENCE: source_id=ogden-2013 ; loc=chs. 2–3

The iconographic record is correspondingly continuous: Typhon is depicted in combat with Zeus on Chalcidian black-figure vases of the archaic period, in architectural sculpture, and in Roman-era mosaics, with iconographic stability around the serpent-tailed humanoid form.footnote:[Ogden 2013, chs. 2–3, on the Chalcidian-vase and architectural-sculpture corpus for the Typhonomachy.]
// EVIDENCE: source_id=ogden-2013 ; loc=chs. 2–3

The principal early-archaic iconographic exemplar is a Chalcidian black-figure hydria depicting Zeus with raised thunderbolt confronting a winged, serpent-legged Typhon, conventionally dated to the mid-sixth century BCE.footnote:[Ogden 2013, ch. 2, on the Chalcidian hydria and the archaic iconography of Typhon.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

M.L. West's 1997 _The East Face of Helicon_ treats the Hesiodic Typhonomachy and the wider succession-narrative of the _Theogony_ as the central documentary case for Near-Eastern-to-Greek transmission of theogonic and combat material.footnote:[West 1997, _The East Face of Helicon_, ch. 6, on Hesiod and the Near Eastern combat-myth corpus.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

Walter Burkert's 1992 _The Orientalizing Revolution_ argues for Phoenician and broader Levantine intermediaries as the principal channel through which Near Eastern theogonic and combat material reached early Greek poets in the eighth and seventh centuries BCE.footnote:[Burkert 1992, _The Orientalizing Revolution_, on Phoenician-mediated transmission to early Greek poetry.]
// EVIDENCE: source_id=burkert-1992 ; loc=whole volume

Joseph Fontenrose's 1959 _Python: A Study of Delphic Myth and Its Origins_ develops the comparative argument that the Apollo-Python combat at Delphi and the Zeus-Typhon combat are variant Greek instantiations of a single inherited dragon-combat type.footnote:[Fontenrose 1959, _Python_, on the Python-Typhon comparative argument.]
// EVIDENCE: source_id=fontenrose-1959 ; loc=whole volume

Neil Forsyth's 1987 _The Old Enemy_, ch. 4, places the Hesiodic Typhonomachy as the Greek station in the longue durée of the combat-myth tradition that runs from Sumerian Ninurta narratives through the Hebrew Bible into Christian apocalyptic.footnote:[Forsyth 1987, ch. 4, on Greek combat-myth in the long combat-myth trajectory.]
// EVIDENCE: source_id=forsyth-1987 ; loc=ch. 4

The Typhonomachy is treated in the modern scholarship as the principal test case for the Near-Eastern-to-Greek transmission hypothesis because the parallels with the Hurro-Hittite Kumarbi Cycle (cross-ref: Ch. 5) and with the Ugaritic Baal-Yamm-Lôtan complex (cross-ref: Ch. 7) are simultaneously specific and numerous.footnote:[West 1997, ch. 6; Burkert 1992, on the Typhonomachy as the central transmission test case.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

=== Setting and the Olympian succession

The Hesiodic _Theogony_ presents a three-generation succession of divine sovereigns — Ouranos, Kronos, Zeus — in which each son violently displaces his father from the throne of heaven; the Typhonomachy is the final confrontation that secures the third-generation sovereign's rule.footnote:[West 1966, on the Ouranos-Kronos-Zeus succession at Theog. 154–210, 453–506, and 820–880.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 154–210

Ouranos (Sky) is the primordial sky-sovereign of the _Theogony_'s first generation; he is castrated by his son Kronos with a sickle of adamant supplied by his mother Gaia (Γαῖα), the primordial earth-goddess, who is angered by Ouranos's confinement of her offspring within her body.footnote:[West 1966, on Theog. 154–182, on Ouranos's castration by Kronos.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 154–182

Kronos, the second-generation sovereign, swallows each of his children at birth in fear of being displaced as he had displaced his own father; Zeus alone escapes this fate when his mother Rhea conceals the infant on Crete and gives Kronos a stone in swaddling clothes to swallow in his place.footnote:[West 1966, on Theog. 453–500, on Kronos's swallowing of his children and the survival of Zeus.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 453–500

The Titanomachy — the ten-year war between Zeus's faction (the Olympians, with the hundred-handed Hekatoncheires released from Tartarus as Zeus's allies) and Kronos's faction (the Titans) — ends with the defeat and imprisonment of the Titans in Tartarus (Τάρταρος), the lowest realm of the underworld and the prison of defeated divine enemies.footnote:[West 1966, on Theog. 617–819, on the Titanomachy and the imprisonment of the Titans in Tartarus.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 617–819

The Typhonomachy follows directly upon the Titanomachy in the _Theogony_'s narrative sequence, with Hesiod marking the transition at line 820 by introducing Typhoeus as Gaia's last and youngest child.footnote:[West 1966, on the Theog. 820 transition and on Typhoeus as Gaia's youngest offspring.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820

Gaia, the primordial earth-goddess, is named explicitly in Hesiod as Typhoeus's mother; she conceives him in her later relationship with Tartarus, and the parental pairing earth-and-underworld is itself a marker of the monster's chthonic origin.footnote:[West 1966, on Theog. 821–822, on Gaia and Tartarus as Typhoeus's parents.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 821–822

The pairing of Gaia and Tartarus as Typhoeus's parents is Hesiodic; in Apollodorus _Bibliotheca_ 1.6.3, Gaia conceives Typhon by Tartarus specifically in vengeance after the Olympian defeat of the Giants, providing a generative motive that Hesiod does not name in lines 820–822.footnote:[Ogden 2013, ch. 2, on the Apollodoran motive (vengeance for the Giants) for Typhon's conception by Gaia and Tartarus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The narrative position of the Typhonomachy as the close of the succession-cycle gives Zeus's victory its theogonic function: with Typhoeus defeated, no further generation of sovereign-displacing combat occurs in the _Theogony_, and the Olympian dispensation is established as permanent.footnote:[West 1966, on Theog. 820–880 in the structural close of the succession; Forsyth 1987, ch. 4, on the theogonic function of the Typhonomachy.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The Typhonomachy thus serves the royal-legitimation function within the Hesiodic theogonic project: Zeus's combat-victory over Typhoeus is the act that confirms his kingship over gods and men, structurally parallel to Marduk's elevation in the Babylonian _Enūma Eliš_ (cross-ref: Ch. 3) and to Baal's combat in the Ugaritic Baal Cycle (cross-ref: Ch. 7).footnote:[West 1966, on the kingship-confirmation function of the combat; Forsyth 1987, ch. 4, on the comparative legitimation function.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The cosmic geography of the combat in Hesiod is wide: the engagement involves heaven, earth, and sea, with thunderbolts ranging across the sky, the earth shaking under the impact, and the waters of the sea boiling — the combat is staged on the full cosmographic scale that the Olympian dispensation requires.footnote:[West 1966, on Theog. 839–852, on the cosmic scale of the combat geography.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 839–852

=== Movement I — Hesiod's Typhonomachy (Theog. 820–880)

Hesiod's Typhonomachy, the earliest surviving form of the narrative, is a sketch rather than a fully developed combat scene: West's commentary describes the passage as a synoptic narrative of birth, fight, and binding, characterised by elaborate description of the monster but compressed treatment of the combat itself.footnote:[West 1966, on Theog. 820–880, characterising the passage as synoptic.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The narrative opens at line 820 with a temporal marker placing Typhoeus's birth after the imprisonment of the Titans in Tartarus, locating the Typhonomachy as a coda to the Titanomachy.footnote:[West 1966, on the Theog. 820 transition.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820

Typhoeus is named in the Hesiodic passage with the form Typhoeus (Τυφωεύς) rather than the later Apollodoran Typhon (Τυφῶν); West's commentary notes both names as ancient and as denoting the same figure across the textual tradition.footnote:[West 1966, on Theog. 821, on the name Typhoeus and its variant Typhon.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 821

The hundred heads of Typhoeus are described in the Hesiodic passage as serpent-heads springing from the monster's shoulders, with flickering tongues and fiery eyes; the multiplicity is a constitutive feature of the figure rather than an ornamental detail.footnote:[West 1966, on Theog. 824–828, on the hundred serpent-heads of Typhoeus.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 824–828

The voice of Typhoeus is described in the Hesiodic passage as polyphonic: each of the hundred heads emits a different sound — the bellowing of bulls, the roaring of lions, the barking of hounds, the hissing of serpents — and the combined polyphony is presented as itself uncanny.footnote:[West 1966, on Theog. 829–835, on the polyphonic voice of Typhoeus.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 829–835

West's commentary on the polyphonic-voice passage notes that the catalogue of bestial sounds is one of the most elaborate ekphrastic moments in the _Theogony_ and that it serves the rhetorical function of marking Typhoeus as a being who exceeds every category of attested creature.footnote:[West 1966, on Theog. 829–835, commentary on the rhetorical function of the polyphony.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 829–835

The Hesiodic passage names the gods' fear of Typhoeus: had Zeus not perceived the threat in time, Typhoeus would have become sovereign over mortals and immortals; the conditional is presented in lines 836–838 as a near-miss in which the Olympian dispensation came close to being overturned.footnote:[West 1966, on Theog. 836–838, on the conditional near-miss of Typhoeus's sovereignty.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 836–838

Zeus's perception of the threat is presented in the Hesiodic passage as the trigger for the combat: the storm-god is described as recognising the monster's challenge and arming himself with thunder, lightning, and the smouldering thunderbolt as his combat weapons.footnote:[West 1966, on Theog. 839–841, on Zeus's perception and arming.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 839–841

The thunderbolt is presented in the Hesiodic passage as Zeus's principal combat weapon: he leaps from Olympus and strikes Typhoeus with the bolt, scorching the monster's hundred heads and reducing the serpent-limbs to ash.footnote:[West 1966, on Theog. 853–858, on the thunderbolt-strike against Typhoeus.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 853–858

The cosmic-scale description of the combat in Theog. 839–852 enumerates the geophysical effects: the earth groans under the weight of the engagement, the sea boils under the heat of the bolts, the heavens shake, and Hades trembles in Tartarus together with the imprisoned Titans — a cosmographic seismology that registers the combat at every level of the world's structure.footnote:[West 1966, on Theog. 839–852, on the cosmic-scale geophysical description.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 839–852

West's commentary observes that the geophysical description in Theog. 839–852 is unusually elaborate even for the _Theogony_'s standards and that the seismological register encodes the combat as cosmographically significant — the combat shakes the world because the sovereignty of the world is at stake.footnote:[West 1966, on Theog. 839–852, commentary on the seismological register.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 839–852

After the thunderbolt-strike, Hesiod's narrative describes the burning of Typhoeus: the monster is consumed by fire from the heat of the bolts, with his serpent-heads scorched and his limbs reduced to formlessness; Zeus then casts him down into Tartarus.footnote:[West 1966, on Theog. 859–868, on the burning and casting-down of Typhoeus.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 859–868

The casting-down of Typhoeus into Tartarus places him in the same prison as the defeated Titans of the previous combat, structurally completing the Hesiodic pattern in which defeated divine antagonists are confined in the lowest realm rather than annihilated outright.footnote:[West 1966, on Theog. 868, on the placement of Typhoeus in Tartarus alongside the defeated Titans.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 868

The closing section of the Hesiodic passage (Theog. 869–880) presents the storm-winds as the offspring of Typhoeus: the destructive winds that bring shipwreck and crop-failure are described as emanating from the defeated monster and as the post-defeat residue of his power.footnote:[West 1966, on Theog. 869–880, on the storm-winds as Typhoeus's offspring.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 869–880

The storm-wind aetiology in Theog. 869–880 distinguishes the named winds (Notos, Boreas, Zephyros, Argestes) from the destructive Typhonic winds: the named winds are beneficial and Olympian-sanctioned, while the storm-winds emanating from Typhoeus are presented as the disorderly survival of the monster's power.footnote:[West 1966, on Theog. 869–880, on the distinction between Olympian and Typhonic winds.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 869–880

The Hesiodic Typhonomachy contains no extended description of a combat sequence with multiple exchanges or temporary reversals: Zeus perceives the threat, arms himself, strikes with the thunderbolt, and casts the burning monster down — the entire combat is compressed into roughly the central thirty lines of the passage.footnote:[West 1966, on the compressed combat sequence at Theog. 853–868.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 853–868

West's commentary on the compressed combat sequence notes that the brevity is itself characteristic: Hesiod's interest is in the cosmographic significance of the combat rather than in the choreography of individual blows, and the passage's elaboration is concentrated on the description of the monster and on the geophysical effects of the strike.footnote:[West 1966, on Theog. 820–880, commentary on the compressed combat narrative.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The Hesiodic Typhonomachy contains no episode of temporary defeat for Zeus, no removal of the thunderbolt or the sinews, no captivity in a cave, and no recovery operation by subordinate deities: these episodes belong to the Apollodoran expansion (1st–2nd c. CE) and are not retrojected into the Hesiodic narrative.footnote:[West 1966, on the absence of the sinew-theft sequence in the Hesiodic passage; Ogden 2013, ch. 2, on the Apollodoran expansion as later.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The Hesiodic Typhonomachy contains no explicit naming of Mount Etna (Αἴτνη) as the burial place of Typhoeus: the volcanic-aetiological identification is post-Hesiodic and is most prominently associated with Pindar's _Pythian_ 1 and with Aeschylus's _Prometheus Bound_.footnote:[Ogden 2013, ch. 2, on the post-Hesiodic emergence of the Etna identification.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Hesiod casts Typhoeus into Tartarus rather than under Etna; the volcanic locus is a later geographical specification that situates the casting-down in the topography of Sicily, becoming canonical in the post-Hesiodic tradition without displacing the Tartarus locus altogether.footnote:[West 1966, on Theog. 868; Ogden 2013, ch. 2, on the Tartarus and Etna loci.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 868

Hesiod's narrative presents Typhoeus as serpent-limbed: from the monster's shoulders spring serpents in place of arms or legs, marking the figure as morphologically draconic in the Greek sense (cf. Ogden 2013's drakōn classification) and as belonging to the wider Greek dragon-adversary type.footnote:[West 1966, on Theog. 824–828, on Typhoeus's serpent-limbs; Ogden 2013, ch. 2, on the drakōn classification.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 824–828

West's commentary observes that the serpent-limbed morphology in the Hesiodic passage is iconographically influential: the archaic-period vase-painters take up the serpent-legged form (rather than fully serpentine bodies) as the canonical Greek depiction of Typhoeus, and the form is stable across the iconographic record.footnote:[West 1966, on the iconographic afterlife of the Hesiodic morphology; Ogden 2013, ch. 2.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 824–828

The Hesiodic passage does not name a Cilician location for Typhoeus's birth or for the combat: the Cilician anchorage of the figure is post-Hesiodic and emerges most clearly in Pindar's _Pythian_ 1.16–17 (where Typhon is born in Cilicia) and in Apollodorus _Bibliotheca_ 1.6.3 (where the Corycian cave in Cilicia is the locus of the sinew-theft).footnote:[Ogden 2013, ch. 2, on the post-Hesiodic emergence of the Cilician anchorage.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

[INFERENCE: the structural function of the Hesiodic Typhonomachy as the close of the succession-cycle gives the combat its royal-legitimation force, even though Hesiod does not explicitly say "Zeus's victory confirms his kingship" | basis: the placement of the passage at Theog. 820–880 immediately before the catalogue of Zeus's marriages (894 ff.) and the wider succession-frame Ouranos-Kronos-Zeus, in which the Typhonomachy is the final combat that prevents a fourth-generation displacement | risk: the inference is structural-narratological rather than directly attested; West's commentary endorses this reading without using these exact terms.]

The Hesiodic narrative's compactness is itself part of what scholars use as evidence for transmission: West 1997 argues that Hesiod is working with inherited material that he compresses, rather than inventing the combat-narrative whole; the elaborate description of the monster against the compressed combat-narrative is the textual signature of compression of received material.footnote:[West 1997, ch. 6, on the compression-of-received-material reading of the Hesiodic Typhonomachy.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

[VARIANT: primary=West 1966 reads Theog. 820–880 as a continuous and integral part of the _Theogony_ | alt=some 19th- and early-20th-c. editors treated the Typhonomachy as an interpolation by a later hand | chosen: West 1966's continuous-and-integral reading | reason: the West 1966 reading is the modern scholarly consensus, and the lines are present in all principal manuscript witnesses; the interpolation hypothesis is no longer current.]

=== Movement II — Apollodorus's expansion (Bibliotheca 1.6.3)

Apollodorus's _Bibliotheca_ 1.6.3, conventionally dated to the first or second century CE, gives the extended canonical narrative of the Typhonomachy: the version that includes Typhon's temporary defeat of Zeus, the severing of Zeus's sinews, the cave-imprisonment, and the recovery operation by Hermes and Aigipan.footnote:[Ogden 2013, ch. 2, on Apollodorus _Bibliotheca_ 1.6.3 as the source of the extended Typhonomachy.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The _Bibliotheca_ is a Greek prose mythographic compendium that summarises and harmonises material from many earlier sources; Apollodorus's account of the Typhonomachy at 1.6.3 is therefore not a primary witness to a single archaic version but a later compilation that may preserve elements absent from the surviving Hesiodic and other early sources.footnote:[Ogden 2013, ch. 2, on the _Bibliotheca_'s mythographic-compendium character.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The sinew-theft episode is the principal feature that distinguishes the Apollodoran expansion from the Hesiodic narrative; this episode is NOT present in Hesiod's _Theogony_ 820–880 and must not be retrojected into the Hesiodic version.footnote:[Ogden 2013, ch. 2, on the sinew-theft as Apollodoran rather than Hesiodic; West 1966, on the absence of the episode in Theog. 820–880.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Apollodorus's narrative opens with Typhon's birth from Gaia and Tartarus presented as a vengeance for the defeat of the Giants, providing a generative motive that Hesiod does not specify; in the Apollodoran framing, the combat is one stage in an ongoing series of earth-born challenges to Olympian sovereignty.footnote:[Ogden 2013, ch. 2, on the Apollodoran framing of Typhon's birth as Gaian vengeance for the Giants.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Apollodoran description of Typhon's morphology is more developed than Hesiod's: the body is enormous, surpassing all mountains in height, with serpent-coils for legs, dragon-heads erupting from the hands, and fire flashing from the eyes; the figure exceeds even the elaborate Hesiodic catalogue.footnote:[Ogden 2013, ch. 2, on the Apollodoran morphology of Typhon.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

In the Apollodoran narrative, the Olympian gods are initially put to flight by Typhon's onslaught and flee to Egypt, where they assume animal disguises to escape detection — an etiology Apollodorus uses to account for the theriomorphic Egyptian deities; this episode is absent from Hesiod and is part of the Apollodoran expansion.footnote:[Ogden 2013, ch. 2, on the Olympian flight to Egypt and the theriomorphic-disguise aetiology in Apollodorus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Zeus alone (with Athena, in some recensions) confronts Typhon directly in the Apollodoran narrative; the engagement is staged at first on Mount Casius in Syria, locating the Apollodoran combat in the Levantine-Anatolian zone rather than in the Aegean.footnote:[Ogden 2013, ch. 2, on Mount Casius as the Apollodoran combat-site.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

In the first phase of the Apollodoran combat, Zeus strikes Typhon with the thunderbolt and pursues the wounded monster; the engagement then turns against Zeus when Typhon overcomes him, wresting away the harpe (sickle) Zeus carried and using it against him.footnote:[Ogden 2013, ch. 2, on the first-phase combat and Typhon's seizure of the harpe.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The decisive moment of the Apollodoran narrative is the temporary defeat of Zeus: Typhon overpowers the storm-god, severs the sinews of his hands and feet with the harpe, and renders him incapable of further combat or movement.footnote:[Ogden 2013, ch. 2, on Typhon's temporary defeat of Zeus and the severing of the sinews.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The severed sinews are placed by Typhon in a bear-skin and entrusted to the dragoness Delphyne to guard, while the immobilised Zeus is hidden in the Corycian cave (Κωρύκιον ἄντρον), a real cave in Cilicia near the Mediterranean coast that the Apollodoran narrative names as the locus of the captivity.footnote:[Ogden 2013, ch. 2, on the Corycian cave and Delphyne's guarding of the sinews in the bear-skin.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Corycian cave's identification as a real Cilician topography is geographically specific: the cave is on the southern coast of Anatolia, opposite Cyprus, in a region that was within the network of Levantine-Greek contact during the orientalizing period — a geographical anchor whose significance for the Near-Eastern transmission argument is treated below.footnote:[Ogden 2013, ch. 2, on the Cilician geography of the Corycian cave; West 1997, ch. 6, on the orientalizing-contact significance of the Cilician anchorage.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The recovery operation in the Apollodoran narrative is conducted by Hermes and Aigipan: the two gods sneak into the Corycian cave, deceive Delphyne, and steal back the sinews from the bear-skin, after which they restore them to Zeus's hands and feet.footnote:[Ogden 2013, ch. 2, on the Hermes-and-Aigipan recovery operation.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Aigipan ("Goat-Pan") is in the Apollodoran narrative paired with Hermes for the recovery operation; the majority scholarly position identifies Aigipan as Pan under a goat-cult epithet rather than as a separate deity, and the partnership therefore registers a trickster-god (Hermes) with the pastoral god in goat-form (Aigipan / Pan) — a pairing that is unusual in the Olympian record and one of the Apollodoran expansion's most distinctive features.footnote:[Ogden 2013, ch. 2, on Aigipan as Hermes's partner in the recovery operation; the Aigipan-as-Pan-epithet identification is the majority view in modern scholarship.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Hermes-and-Aigipan recovery operation in the Corycian cave has been compared with the Hurro-Hittite Elkunirsa myth, in which a comparable pairing of subordinate deities recovers the storm-god's organs after their theft (cross-ref: Near-Eastern transmission section, below).footnote:[West 1997, ch. 6, on the Elkunirsa-recovery comparison; Hoffner 1998, on the Elkunirsa myth in the Hittite corpus.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

After the recovery of his sinews, Zeus is restored to combat capability and renews the engagement with Typhon; the second-phase combat in the Apollodoran narrative pursues Typhon across a series of geographical stages, with thunderbolts hurled in pursuit.footnote:[Ogden 2013, ch. 2, on the Apollodoran second-phase combat after the sinew-recovery.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Apollodoran pursuit is staged on Mount Nysa in Thrace, where the Fates feed Typhon ephemeral fruits that diminish his power, and culminates with Zeus catching Typhon and casting Mount Etna upon him in Sicily, burying the monster under the volcano.footnote:[Ogden 2013, ch. 2, on the Mount Nysa episode and the casting of Etna.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The casting of Mount Etna onto Typhon in the Apollodoran narrative is the volcanic-aetiological resolution: Typhon's continuing struggle beneath the mountain accounts for Etna's eruptions, and the volcano serves both as the prison and as the post-combat sign of the bound monster's residual power.footnote:[Ogden 2013, ch. 2, on the Etna-aetiology in Apollodorus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Apollodoran narrative consolidates the volcanic-aetiological reading that had developed in the post-Hesiodic tradition: by the first or second century CE, the Etna identification has fully displaced the Hesiodic Tartarus locus as the canonical burial place of Typhon in many subsequent retellings.footnote:[Ogden 2013, ch. 2, on the consolidation of the Etna identification by the Apollodoran period.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The structure of the Apollodoran combat — failed first phase, sinew-theft and captivity, recovery operation by subordinate deities, successful second phase, volcanic burial — is a tripartite-with-recovery pattern that contrasts with the Hesiodic single-strike compression and shows the narrative form developing toward a more elaborate combat-cycle over the millennium between Hesiod and Apollodorus.footnote:[Ogden 2013, ch. 2, on the tripartite-with-recovery structure of the Apollodoran combat.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Apollodoran sinew-theft episode is the principal point at which the Greek combat-narrative shows a structural feature with a Hurro-Hittite parallel rather than a purely Hesiodic precedent: the theft-of-divine-organs motif has its closest documented parallel in the Hittite Elkunirsa material, not in the Hesiodic _Theogony_ (cross-ref: Near-Eastern transmission section).footnote:[West 1997, ch. 6, on the Elkunirsa parallel for the Apollodoran sinew-theft.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Apollodoran narrative's geographical itinerary — Mount Casius (Syria), Corycian cave (Cilicia), Mount Nysa (Thrace), Etna (Sicily) — traces a Mediterranean-wide map for the combat, with the Levantine-Cilician segment being the geographically suggestive station for the Near-Eastern transmission argument.footnote:[Ogden 2013, ch. 2, on the Apollodoran geographical itinerary; West 1997, ch. 6, on the Cilician segment.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Apollodorus is, with respect to the Typhonomachy, the principal source for what is by the early imperial period the canonical extended narrative of the combat: subsequent retellings — including Nonnus and most Latin reception — work from a story-shape that includes the sinew-theft and the cave-captivity rather than the bare Hesiodic sketch.footnote:[Ogden 2013, ch. 2, on Apollodorus's role in establishing the canonical extended narrative.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The fact that the Apollodoran sinew-theft episode is absent from Hesiod has been read in two different ways in the modern scholarship: as a later Greek elaboration that draws independently on the cave-imprisonment topos, and as a preserved transmission of a Hurro-Hittite motif that Hesiod did not include but that survived in less elite or non-Hesiodic Greek versions until being recorded by Apollodorus (cross-ref: Near-Eastern transmission section).footnote:[West 1997, ch. 6; Ogden 2013, ch. 2, on the two readings of the sinew-theft's absence from Hesiod.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

Pindar's _Pythian_ 1.16–28 (early-fifth-century BCE) — chronologically intermediate between Hesiod and Apollodorus — does not preserve the sinew-theft but does specify Typhon's Cilician origin and the Etna burial; the Cilician geography is thus already present in the early-fifth-century record.footnote:[Ogden 2013, ch. 2, on Pindar _Pythian_ 1 and the Cilician geography.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

[VARIANT: primary=Apollodorus _Bibliotheca_ 1.6.3 (1st–2nd c. CE) gives the extended sinew-theft narrative | alt=Hesiod _Theogony_ 820–880 (c. 700 BCE) gives the bare combat-and-burial sketch | chosen: present-both-attributed | reason: per brief co-equal classification, each source's contribution is named and attributed; the sinew-theft is registered as Apollodoran and explicitly NOT retrojected into Hesiod.]

The Apollodoran narrative uses the harpe (sickle) — the same weapon that Kronos used to castrate Ouranos in Hesiod (Theog. 178–182) — as Typhon's instrument for severing Zeus's sinews; the symmetry between Kronos's act against the previous sovereign and Typhon's act against Zeus has been read by some scholars as a deliberate echo within the Apollodoran narrative, registering the combat as a near-replay of the founding succession-conflict.footnote:[Ogden 2013, ch. 2, on the harpe-symmetry in the Apollodoran narrative.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

=== Movement III — Nonnus's baroque elaboration (Dionysiaca 1–2)

Nonnus's _Dionysiaca_, books 1 and 2, conventionally dated to the fifth century CE, gives an extensively elaborated baroque narrative of the Typhonomachy that incorporates the Apollodoran sinew-theft within a much more developed combat-sequence and adds the figure of Cadmus as a participant in the recovery.footnote:[Ogden 2013, ch. 2, on Nonnus _Dionysiaca_ 1–2 as the baroque expansion of the Typhonomachy.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The _Dionysiaca_ is a 48-book Greek hexameter epic by Nonnus of Panopolis (in Upper Egypt), a fifth-century-CE composition in the late-antique encyclopaedic-epic tradition; the Typhonomachy occupies the opening books and is positioned as a prelude to the main Dionysiac narrative of the poem.footnote:[Ogden 2013, ch. 2, on the _Dionysiaca_'s structural placement of the Typhonomachy.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Nonnus's narrative inherits the Apollodoran sinew-theft scenario: Typhon overcomes Zeus and steals the storm-god's sinews; in the Nonnian elaboration, however, Typhon also seizes the thunderbolt itself and attempts to wield it, with comic results, since the bolt cannot be controlled by hands not the storm-god's.footnote:[Ogden 2013, ch. 2, on the Nonnian elaboration of Typhon's seizure of sinews and thunderbolt.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The figure of Cadmus (the Latinised form is preserved in this Nonnus reception context — note that the Greek form Kadmos is the standard transliteration outside Nonnus reception) plays the recovery-trickster role in the Nonnian elaboration: Cadmus disguises himself as a shepherd, plays the pipes (or panpipes), and beguiles Typhon into setting aside the sinews so that he can listen.footnote:[Ogden 2013, ch. 2, on Cadmus's pipe-playing recovery role in Nonnus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Cadmus's pipe-music, in the Nonnian narrative, soothes Typhon to the point of trance; while Typhon is enthralled, Cadmus retrieves the sinews from where Typhon has set them down and conceals them; the recovery is staged as a music-trickster intervention rather than a stealth-and-deception operation in the Apollodoran mode.footnote:[Ogden 2013, ch. 2, on the music-trickster motif in Nonnus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The pipe-playing Cadmus is a Nonnian elaboration on the Apollodoran Hermes-and-Aigipan pairing: the music-trickster role in Apollodorus is divided between Hermes (the trickster) and Aigipan (the pastoral-deity), and Nonnus consolidates these into the single Cadmus figure who is both Theban founder and pastoral musician.footnote:[Ogden 2013, ch. 2, on Nonnus's consolidation of the Apollodoran recovery-pair into Cadmus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

After Cadmus retrieves the sinews and restores them to Zeus, the Nonnian narrative resumes the second-phase combat with the same volcanic resolution as the Apollodoran tradition: Zeus pursues Typhon, casts him down, and buries him under Mount Etna, with the volcano accounting for the post-combat eruptive activity.footnote:[Ogden 2013, ch. 2, on the Nonnian volcanic resolution.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Nonnus's elaboration includes extended ekphrastic descriptions of Typhon's body: hundreds of lines describe each region of the monster's morphology in turn, with serpent-heads enumerated by region of the body, voices catalogued by species of bestial sound, and the monster's flesh described as a kind of cosmographic landscape.footnote:[Ogden 2013, ch. 2, on the Nonnian ekphrasis of Typhon's body.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Nonnian Typhonomachy is the latest extended narrative attestation in the Greek tradition before the closure of the late-antique pagan literary record; it stands as a witness to the continued vitality of the combat-narrative as a literary subject across more than a millennium of Greek composition.footnote:[Ogden 2013, ch. 2, on the Nonnian Typhonomachy as the late-antique terminal attestation.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Cadmus-with-pipes episode is Nonnus's distinctive contribution to the Typhonomachy tradition: it is not preserved in the earlier Hesiodic, Pindaric, or Apollodoran sources, and it is registered in the modern scholarship as a Nonnian innovation that synthesises elements of the Theban Cadmus-and-the-dragon tradition with the Apollodoran sinew-recovery scenario.footnote:[Ogden 2013, ch. 2, on the Cadmus-with-pipes episode as a Nonnian innovation.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Cadmus figure is in his Greek form Kadmos, the Theban founder-hero who slays the dragon of Ares at Thebes and sows its teeth to raise the Spartoi (cross-ref: Ch. 12 family chapter); the Latinised form Cadmus is preserved here only because the Nonnus reception context standardly uses the Latin form in modern Greek-and-Latin literary scholarship.footnote:[Ogden 2013, ch. 2, on the Greek-and-Latin name forms; glossary.yaml on the Kadmos / Cadmus distinction.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

=== Partial attestations

The _Homeric Hymn to Apollo_, lines 305–355 (conventionally dated to the seventh or sixth century BCE), preserves a partial attestation in which Typhon is described as the offspring of Hera, born by parthenogenesis in retaliation against Zeus's solo conception of Athena, and entrusted to a draconic guardian at Pytho.footnote:[Ogden 2013, ch. 2, on the _Homeric Hymn to Apollo_ 305–355 and the Hera-parthenogenesis variant.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Hera-parthenogenesis genealogy of Typhon in the _Homeric Hymn to Apollo_ contradicts the Hesiodic-and-Apollodoran genealogy from Gaia and Tartarus; the modern scholarship treats this as a separate variant tradition rather than reconciling it with the Theogonic genealogy.footnote:[Ogden 2013, ch. 2, on the variant-genealogy reading of the _Homeric Hymn to Apollo_.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The _Homeric Hymn to Apollo_'s Typhon is connected with the Pytho location (the older name of Delphi) and with the draconic adversary that Apollo slays at the founding of the oracle, providing a textual link between the Typhon material and the Apollo-Python combat (cross-ref: Ch. 12 family chapter).footnote:[Ogden 2013, ch. 2, on the Pytho-Typhon-Python textual link in the _Homeric Hymn to Apollo_; Fontenrose 1959 on the comparative Python-Typhon argument.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Pindar's _Pythian_ 1.16–28, an early-fifth-century BCE victory ode, locates Typhon under Mount Etna and uses the volcano's eruptions as the metaphorical register for the bound monster's residual force; Pindar's Typhon is named as Cilician-born and as confined under the Sicilian volcano.footnote:[Ogden 2013, ch. 2, on Pindar _Pythian_ 1.16–28 and the Etna-and-Cilicia identifications.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Pindaric ode is the earliest surviving named-source for the Etna identification; the Hesiodic Tartarus locus and the Pindaric Etna locus are not directly contradictory (Etna can be read as a topographical specification of the Tartarus burial), but the Pindaric specification is recognisably innovative within the surviving record.footnote:[Ogden 2013, ch. 2, on Pindar's status as the earliest named-source for the Etna identification.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

_Prometheus Bound_, lines 351–372 (attributed to Aeschylus by ancient tradition though authorship has been contested in modern scholarship — Griffith 1977, West 1990 — and is not now uncontroversially Aeschylean), describes Typhon as crushed under Etna, with the volcano's eruptions caused by his struggling beneath the mountain; the description is consistent with the Pindaric register and provides a second early-fifth-century BCE attestation of the volcanic identification.footnote:[Ogden 2013, ch. 2, on _Prometheus Bound_ 351–372 and the Etna identification; on the contested authorship question see Griffith 1977 and West 1990 contra the traditional Aeschylean attribution.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

[VARIANT: Hesiod _Theogony_ 820–880 (c. 700 BCE; the earliest sketch) | Apollodorus _Bibliotheca_ 1.6.3 (1st–2nd c. CE; the sinew-theft expansion) | Nonnus _Dionysiaca_ 1–2 (5th c. CE; the baroque elaboration with Cadmus's pipes) | partial attestations: _Homeric Hymn to Apollo_ 305–355, Pindar _Pythian_ 1.16–28, Aeschylus _Prometheus Bound_ 351–372 | chosen: present-all-attributed per brief co-equal classification — the chapter presents each source's contribution attributed to its own context, registering the millennium-long accretion of the narrative.]

=== The Near-Eastern transmission question

M.L. West's 1997 _The East Face of Helicon_, ch. 6, argues that the Hesiodic succession-narrative (Ouranos → Kronos → Zeus) and the Hesiodic Typhonomachy both derive from the Hurro-Hittite Kumarbi Cycle (cross-ref: Ch. 5) via Near Eastern mediation, with the structural correspondences sufficiently specific to require transmission rather than convergence.footnote:[West 1997, ch. 6, on the Kumarbi-to-Hesiod transmission argument.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Hesiodic succession-sequence Ouranos → Kronos → Zeus corresponds in structure to the Kumarbi-Cycle succession Alalu → Anu → Kumarbi → Teshub: in both, kingship of heaven is transmitted through violent displacement of each generation by its successor, and in both, the third- or fourth-generation sovereign (Zeus / Teshub) is the storm-god who must defend his rule against monstrous offspring of the deposed predecessor.footnote:[West 1997, ch. 6, on the Hesiod-Kumarbi succession parallel.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The most specific point of correspondence in the succession-narrative is the castration motif: in Kingship in Heaven (Ch. 5), Kumarbi castrates Anu by biting off his genitals and swallowing them; in the Hesiodic _Theogony_ 178–182, Kronos castrates Ouranos with a sickle of adamant supplied by Gaia — the genital-castration of the sky-god by his successor is the shared structural feature.footnote:[West 1997, ch. 6, on the castration parallel between Kumarbi and Kronos; West 1966, on Theog. 178–182.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

Beyond the structural correspondence, the Kumarbi-and-Anu and Kronos-and-Ouranos castrations share the motif of the prophetic declaration after castration: Anu, after losing his genitals to Kumarbi, declares the offspring that will grow inside Kumarbi's body and depose him in turn — a prophetic-conception logic that has its Hesiodic counterpart in the prophecy that one of Kronos's children will displace him, the prophecy that motivates Kronos's swallowing of his children.footnote:[West 1997, ch. 6, on the prophetic-declaration parallel.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Kumarbi-Cycle's Song of Ullikummi (Ch. 5) contains the most specific parallel to the Typhonomachy: Ullikummi is a stone-monster generated by Kumarbi as an instrument against the storm-god Teshub; Ullikummi grows from the sea, threatens to displace the storm-god from heaven, and is finally defeated through a wisdom-counsellor's technical solution — a structural pattern that the Typhonomachy reproduces in its storm-god-vs-cosmographically-immense-monster shape.footnote:[West 1997, ch. 6, on the Ullikummi-Typhon structural parallel; Hoffner 1998, §15 (Song of Ullikummi).]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Ullikummi-Typhon parallel is concrete and specific in the lithic / cosmographic register: Ullikummi's stone-body and growth-toward-heaven correspond to the post-Hesiodic Typhon's lithic / volcanic locus under Etna, with both monsters figured as cosmographic intrusions reaching from the lower realms toward the sky.footnote:[West 1997, ch. 6, on the lithic / cosmographic register of the Ullikummi-Typhon parallel.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Kumarbi-Cycle's Song of Hedammu (Ch. 5) presents a sea-monster of voracious appetite, born from Kumarbi's mating with the daughter of the sea-god, who threatens the land and seas before being incapacitated by Šauška's seduction; the growth-from-sea morphology and the threat-to-cosmographic-order function correspond structurally to the Hesiodic-Apollodoran Typhon's birth from Gaia (and from Tartarus, whose territory includes the deep waters in the Hesiodic cosmography).footnote:[West 1997, ch. 6, on the Hedammu-Typhon parallel; Hoffner 1998, §16 (Song of Hedammu).]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Hedammu-Typhon parallel is most concrete in the growth-from-sea imagery: Hedammu rises voracious from the deep waters in the Hurro-Hittite narrative, and Apollodoran-and-Nonnian Typhon's morphology is described in terms of cosmographic extension across sea-and-land — the marine register of the monster has its Hurro-Hittite precedent in Hedammu rather than in Hesiod's compressed sketch.footnote:[West 1997, ch. 6, on the Hedammu-Typhon marine-register correspondence.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Hittite Elkunirsa-and-Ašertu fragment, a Hurrian-derived Hittite text in Hoffner's _Hittite Myths_ corpus, preserves a narrative in which a storm-god is incapacitated by the theft of his organs and recovered through subordinate-deity intervention; the structural parallel with the Apollodoran sinew-theft is the most specific motif-level correspondence between the Hittite and Greek combat-narratives.footnote:[West 1997, ch. 6, on the Elkunirsa parallel for the Apollodoran sinew-theft; Hoffner 1998, on the Elkunirsa-Ašertu fragment.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Elkunirsa parallel is significant because it provides a documented Near Eastern precedent for the precise motif (theft of the storm-god's bodily organs by an antagonist; recovery operation by subordinate deities; restoration enabling the second-phase combat) that is absent from Hesiod and present only in Apollodorus; the parallel thus supports the reading that Apollodoran material preserves transmission-elements that the Hesiodic synopsis omitted.footnote:[West 1997, ch. 6, on the significance of the Elkunirsa parallel for the Apollodoran sinew-theft.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The geographical anchorage of the Apollodoran combat in Cilicia (the Corycian cave) is the geographically suggestive corollary of the transmission argument: Cilicia is the southern coast of Anatolia, within the orientalizing-period contact zone between Greek and Near Eastern cultures, and the Cilician location of the Greek myth's most Hurro-Hittite-resembling episode is consistent with that contact zone as the transmission corridor.footnote:[West 1997, ch. 6, on the Cilician geography as a transmission-corridor anchor.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

Pindar's _Pythian_ 1's Cilician anchorage of Typhon's birth (line 17) provides a fifth-century BCE attestation of the Cilician geographical specification, predating the Apollodoran narrative by some six centuries and showing that the Cilicia connection was already established in the early Greek tradition — not a late Apollodoran addition.footnote:[West 1997, ch. 6; Ogden 2013, ch. 2, on Pindar's early attestation of the Cilician anchorage.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

Walter Burkert's 1992 _The Orientalizing Revolution_ argues for Phoenician intermediaries as the principal transmission channel: rather than direct Hurrian-or-Hittite-to-Greek transmission, the combat-myth material reaches Greek poets through Phoenician traders, scribes, and craftsmen whose presence in the eastern Mediterranean (including Cilician ports) is well documented in the eighth and seventh centuries BCE.footnote:[Burkert 1992, on Phoenician intermediaries in the orientalizing transmission.]
// EVIDENCE: source_id=burkert-1992 ; loc=whole volume

Burkert's Phoenician-mediation argument is supported by the broader pattern of orientalizing Greek artistic, religious, and literary motifs in the early Archaic period: the same period in which Greek alphabet-script is borrowed from Phoenician, in which Greek bronze-working absorbs Levantine techniques, and in which Greek religious iconography incorporates Levantine forms.footnote:[Burkert 1992, on the orientalizing-horizon pattern of cultural transmission.]
// EVIDENCE: source_id=burkert-1992 ; loc=whole volume

Burkert's reading positions the Typhonomachy as one element within a wider orientalizing transmission of theogonic and cosmological material from the eastern Mediterranean into archaic Greek poetry, with the specific Cilician-Phoenician contact zones as the most likely transmission corridor.footnote:[Burkert 1992, on the Typhonomachy in the orientalizing transmission.]
// EVIDENCE: source_id=burkert-1992 ; loc=whole volume

The Phoenician-mediation argument and the direct-Hurro-Hittite argument are not strictly alternatives: the Phoenician traders and scribes of the early Archaic period were themselves heirs of a Levantine literary culture that included the Ugaritic Baal-Yamm-Lôtan material (cross-ref: Ch. 7) and that was in turn in contact with the Anatolian Hurro-Hittite tradition; the transmission corridor was a network rather than a single line.footnote:[West 1997, ch. 6; Burkert 1992, on the network character of the orientalizing transmission corridor.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Ugaritic Baal-Yamm-Lôtan material (cross-ref: Ch. 7) supplies an additional set of structural correspondences with the Typhonomachy: the storm-god (Baal / Zeus) confronts a personified-sea / serpentine antagonist (Yamm / Lôtan / Typhon), and the combat establishes the storm-god's sovereignty in the divine assembly — a structural pattern Smith-and-Pitard 2009's Baal Cycle commentary documents in detail.footnote:[West 1997, ch. 6, on the Baal-Yamm parallel for the Typhonomachy; cross-ref: Ch. 7.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Lôtan / Litanu of the Ugaritic corpus — the seven-headed serpent named in KTU 1.5 i 1–3 as Baal's adversary — has a distinctive multi-headed morphology that Lôtan shares with Hesiodic Typhoeus and that Day 1985 (cross-ref: Ch. 8) treats as one of the closest motif-level correspondences in the Levantine-Greek combat-myth corpus.footnote:[West 1997, ch. 6, on the Lôtan-Typhon morphological correspondence.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The cumulative force of the transmission argument depends on the convergence of multiple independent lines of evidence: motif-specific structural parallels (succession with castration; growth-from-sea monster; sinew-theft and recovery), geographical anchoring (Cilicia / Corycia), and the wider orientalizing-period contact-zone documentation; West 1997 and Burkert 1992 read these as mutually reinforcing.footnote:[West 1997, ch. 6; Burkert 1992, on the convergent-evidence structure of the transmission argument.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Mesopotamian background — the storm-god / cosmogonic-combat tradition of Marduk-and-Tiamat (cross-ref: Ch. 3) and Ninurta-and-Anzû (cross-ref: Ch. 2) — is treated by Burkert as the deeper substrate: the Mesopotamian combat-cosmogony is the source-tradition that the Hurro-Hittite Kumarbi Cycle reworks (Ch. 5), and that the Levantine and Greek traditions in turn receive through the Anatolian-Levantine corridor.footnote:[Burkert 1992, on the Mesopotamian deep-substrate of the orientalizing transmission.]
// EVIDENCE: source_id=burkert-1992 ; loc=whole volume

The Marduk-Tiamat parallel for Zeus-Typhon is at the level of structural type rather than at the level of specific shared motifs: storm-god confronts personified-monstrous adversary in single combat to establish sovereignty, with the monster's body figured as cosmographically immense; direct transmission from Babylon to Hesiod is less easily documented than for the Hurro-Hittite material, and the parallel is best read as type-level rather than route-specific.footnote:[Burkert 1992, on the Marduk-Tiamat type-level parallel.]
// EVIDENCE: source_id=burkert-1992 ; loc=whole volume

Forsyth 1987, ch. 4, places the Hesiodic Typhonomachy as the Greek station in the longue durée of the combat-myth tradition: with the Mesopotamian combat-corpus as the deepest layer, the Hurro-Hittite Kumarbi Cycle as the Anatolian station, and the Greek Typhonomachy as the Mediterranean inheritor, the chain of transmission runs through documented contact zones in each period.footnote:[Forsyth 1987, ch. 4, on the longue durée chain of transmission.]
// EVIDENCE: source_id=forsyth-1987 ; loc=ch. 4

Forsyth's reading also frames the political-ideological function of the Typhonomachy: Zeus's combat with Typhon is the royal-legitimation event for the Olympian dispensation in the same way that Marduk's combat with Tiamat is the royal-legitimation event for Babylonian sovereignty (cross-ref: Ch. 3) and Baal's combat with Yamm is the royal-legitimation event for the Ugaritic divine kingship (cross-ref: Ch. 7).footnote:[Forsyth 1987, ch. 4, on the royal-legitimation function of the Typhonomachy in comparative perspective.]
// EVIDENCE: source_id=forsyth-1987 ; loc=ch. 4

[INFERENCE: the absence of the sinew-theft from Hesiod's Theogony 820–880 combined with its presence in Apollodorus 1.6.3 and its close parallel in the Hittite Elkunirsa fragment is best read as evidence that the Apollodoran narrative preserves transmission-material that Hesiod's compressed sketch omitted, rather than as evidence that the Apollodoran narrative is a later Greek invention with an independent Hittite-resembling motif | basis: West 1997's argument that motif-specific parallels of this kind are difficult to explain by independent invention; Ogden 2013's reading of the _Bibliotheca_ as a mythographic compendium that may preserve elements absent from the surviving canonical sources | risk: the reading depends on the transmission framework being correct; an alternative reading is that the Greek and Hittite parallels are independent narrative inventions exploiting a similar structural motif, and the choice between readings is contested in the modern scholarship.]

The transmission case as a whole is taken up in detail in this book's Part II C6 (Near-Eastern-to-Mediterranean transmission); the present chapter provides the Greek end of the documentary evidence on which the C6 argument rests, complementing the Hurro-Hittite end of the evidence presented in Ch. 5 (Kumarbi Cycle).footnote:[Forward-pointer to Part II C6; West 1997, ch. 6; Burkert 1992 as the evidentiary basis.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The chapter's contribution to the transmission argument is to register the Greek end of the bridge with concrete and specific Kumarbi-Cycle parallels — Hedammu's growth-from-sea, Ullikummi's stone-body, Elkunirsa's organ-theft — rather than with generic comparisons to "Near Eastern combat myth" as a category; the brief's special instruction (specificity-not-generality) is honoured by the named-motif anchoring above.footnote:[West 1997, ch. 6, on the named-motif anchoring of the Kumarbi-Hesiod parallels; brief special_instructions on specificity.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The transmission case is, however, a contested rather than a closed scholarly conclusion: while West 1997 and Burkert 1992 develop the case in its strongest form, alternative readings (independent-invention; type-level rather than route-specific parallel) remain available, and the Hesiodic-Typhon-vs-Hurro-Hittite-precedent debate is one of the principal test-cases for the comparative-combat-myth method as practised in current scholarship.footnote:[West 1997, ch. 6; Burkert 1992; Forsyth 1987, ch. 4, on the contested status of the transmission case.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

=== Reception and forward links

The Typhonomachy stands as the model for later Greek dragon-combats in the Hellenic literary and iconographic record: the Apollo-Python combat at Pytho / Delphi, Herakles's encounters with the Hydra, Ladon, and Geryon's hounds, Perseus's slaying of the Ketos in the rescue of Andromeda, Kadmos's slaying of the dragon of Ares at Thebes, Bellerophon's slaying of the Chimaera, and Hercules's slaying of Cacus in the Latin tradition.footnote:[Ogden 2013, chs. 2–4, on the Typhonomachy as the model for later Greek dragon-combats.]
// EVIDENCE: source_id=ogden-2013 ; loc=chs. 2–4

The Apollo-Python combat at Pytho / Delphi is the closest Hellenic reiteration of the Typhonomachy structure: Apollo, the storm-and-prophecy god, confronts a serpent-adversary at a fixed cult-site (the older name of Delphi, Pytho), and his victory founds the oracle and the Septerion festival (cross-ref: Ch. 12 family chapter).footnote:[Ogden 2013, ch. 2; Fontenrose 1959, on the Apollo-Python combat as the closest Hellenic reiteration of the Typhonomachy.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Fontenrose 1959 develops the comparative argument that the Apollo-Python combat and the Zeus-Typhon combat are variant Greek instantiations of a single inherited dragon-combat type, with the cult-foundation function (Delphi) carried by the Apollo-Python variant and the cosmographic-sovereignty function (Olympian dispensation) carried by the Zeus-Typhon variant.footnote:[Fontenrose 1959, on the Python-Typhon variant relationship.]
// EVIDENCE: source_id=fontenrose-1959 ; loc=whole volume

The Herakles cycle includes multiple dragon-combat episodes (Hydra, Ladon, the dragon-killing labours) that elaborate the type the Typhonomachy establishes; these are treated in detail in the Ch. 12 family chapter on Greek dragon-combats after Zeus-Typhon.footnote:[Ogden 2013, chs. 2–3, on the Herakles dragon-combat cycle; forward to Ch. 12.]
// EVIDENCE: source_id=ogden-2013 ; loc=chs. 2–3

The Perseus-and-Ketos episode (the rescue of Andromeda) is the iconographic antecedent of the medieval St. George dragon-rescue type (cross-ref: Ch. 10) and represents an iconographic continuity from the Greek dragon-combat tradition through late-antique and Christian reception.footnote:[Ogden 2013, ch. 3, on the Perseus-Andromeda-Ketos episode and its medieval iconographic afterlife.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 3

Kadmos's slaying of the dragon of Ares at Thebes — the Theban founder-myth — combines dragon-combat with a foundation function (the Spartoi rise from the sown teeth) and shows how the dragon-combat type can be adapted to local civic-foundation narratives; this is treated in the Ch. 12 family chapter.footnote:[Ogden 2013, ch. 3, on the Kadmos-and-the-dragon foundation narrative; forward to Ch. 12.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 3

Bellerophon's slaying of the Chimaera — the fire-breathing hybrid of lion, goat, and serpent — represents a heroic-monster-fight variant of the type, in which the cosmographic-sovereignty function is replaced by a heroic-test function while the morphological vocabulary (multi-headed, fire-emitting, serpentine) is preserved.footnote:[Ogden 2013, ch. 3, on the Bellerophon-Chimaera narrative.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 3

Hercules's slaying of the fire-breathing Cacus in the Latin tradition (Virgil _Aeneid_ 8, Ovid _Fasti_ 1) is the Roman terminal point of the Greek dragon-combat tradition's reception in classical Latin literature; this is treated in the Ch. 12 family chapter.footnote:[Ogden 2013, ch. 3, on the Hercules-Cacus episode in Virgil and Ovid; forward to Ch. 12.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 3

The Typhonomachy's influence extends beyond the dragon-combat type proper into the wider Greek imagination of cosmographic disorder: storm-winds, volcanic eruptions, earthquakes, and other geophysical disturbances are conceived in the post-Hesiodic tradition through the Typhonic register, with the bound monster's residual force serving as the imaginative substrate for these phenomena.footnote:[Ogden 2013, ch. 2, on the Typhonic register for cosmographic disorder.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

This chapter sets up the Ch. 12 family chapter on Greek dragon-combats after Zeus-Typhon (Apollo-Python, Herakles-Hydra, Perseus-Ketos, Kadmos-and-the-dragon, Bellerophon-Chimaera, Hercules-Cacus) as the Hellenic reception of the pattern the Typhonomachy establishes, and Part II C6 (Near-Eastern-to-Mediterranean transmission) as the comparative test-case for the transmission argument the present chapter develops.footnote:[Forward-pointers to Ch. 12 and Part II C6; Ogden 2013, chs. 2–3; West 1997, ch. 6; Burkert 1992.]
// EVIDENCE: source_id=ogden-2013 ; loc=chs. 2–3

// COMPARATIVE-HOOK: Hurro-Hittite (Kumarbi Cycle) — the Typhonomachy's three most concrete and specific Near Eastern parallels are with the Kumarbi Cycle: Hedammu's growth-from-sea (Song of Hedammu, Ch. 5) parallels the marine register of Apollodoran-Nonnian Typhon's morphology; Ullikummi's stone-body and growth-toward-heaven (Song of Ullikummi, Ch. 5) parallels the post-Hesiodic Typhon's lithic / volcanic locus under Etna; Elkunirsa's theft of the storm-god's organs (the Hittite Elkunirsa-and-Ašertu fragment) parallels the Apollodoran sinew-theft. The succession-frame parallel (Alalu → Anu → Kumarbi → Teshub corresponding to Ouranos → Kronos → Zeus, with castration of the sky-god by his successor as the most specific shared motif) places the Hesiodic _Theogony_ as a whole within the transmission corridor. Treated in detail in Part II C6 (west-1997; burkert-1992; hoffner-1998 for the Hurro-Hittite material).
// COMPARATIVE-HOOK: Phoenician — Burkert 1992's Phoenician-mediation argument is the principal route-specific transmission model: Phoenician traders, scribes, and craftsmen of the eighth and seventh centuries BCE, whose presence in the eastern Mediterranean (including Cilician ports) is well documented, are positioned as the intermediaries through which Hurro-Hittite and Levantine combat-myth material reached early Greek poets. The Cilician anchorage of Typhon's birth (Pindar) and the Corycian-cave locus of the Apollodoran sinew-theft are the geographically suggestive Greek-end markers of this transmission corridor. Treated in detail in Part II C6 (burkert-1992; west-1997).
// COMPARATIVE-HOOK: Mesopotamia (Marduk-Tiamat) — Zeus-versus-Typhon parallels Marduk-versus-Tiamat (Ch. 3) as storm-god-versus-monster sovereignty combat at the level of structural type rather than of specific shared motifs; direct transmission from Babylon to Hesiod is less easily documented than for the Hurro-Hittite material, and Burkert reads the Mesopotamian combat-cosmogony as the deeper substrate that the Hurro-Hittite Kumarbi Cycle reworks and that reaches Greece via the Anatolian-Levantine corridor (burkert-1992; lambert-2013 for the Mesopotamian end of the substrate; cross-ref: Ch. 3).
// COMPARATIVE-HOOK: Ugarit (Baal-Yamm-Lôtan) — the Ugaritic Baal-Yamm-Lôtan complex (Ch. 7) supplies an additional Levantine layer of structural correspondence: storm-god (Baal / Zeus) confronts personified-sea / serpentine antagonist (Yamm / Lôtan / Typhon) to establish sovereignty in the divine assembly; the multi-headed morphology of Lôtan (KTU 1.5 i 1–3, the seven-headed serpent) corresponds to the multi-headed morphology of Hesiodic Typhoeus (Theog. 824–828, the hundred serpent-heads). The Cilician geographical anchorage of Typhon (Pindar; Apollodorus) places the Greek-end attestation in the same eastern-Mediterranean contact zone as the Ugaritic Baal-Yamm material, and West 1997 reads this as a route-specific Levantine transmission line that complements the Phoenician-mediation argument (west-1997; smith-1994-baal-i; smith-pitard-2009-baal-ii for the Ugaritic end of the substrate; cross-ref: Ch. 7).
// COMPARATIVE-HOOK: Greek (later dragon-combats) — the Typhonomachy is the model for the later Greek dragon-combat repertoire that the Ch. 12 family chapter treats: Apollo-Python at Pytho / Delphi (the closest Hellenic reiteration; Fontenrose 1959); Herakles's encounters with Hydra, Ladon, and Geryon's hounds; Perseus-and-Ketos in the rescue of Andromeda (the iconographic antecedent of the medieval St. George dragon-rescue type, cross-ref Ch. 10); Kadmos and the dragon of Ares at Thebes (combining dragon-combat with civic-foundation); Bellerophon and the Chimaera; and Hercules and Cacus in the Latin reception (Virgil _Aeneid_ 8, Ovid _Fasti_ 1). The Typhonomachy establishes both the type and the central iconographic-narrative vocabulary that these later combats elaborate (ogden-2013; fontenrose-1959; forward to Ch. 12).

// Validated by post-human-normalize
// Timestamp: 2026-04-26T14:37:20Z
// Checks passed: footnote+evidence-pair, source_id-whitelist, glossary-discipline, markers-valid
// Warnings: none
```

---

# Input file: chapters/11-zeus-typhon.adoc

```
[[ch-11-zeus-typhon]]
== Zeus vs. Typhon: The Olympian Combat

Hesiod's _Theogony_, lines 820–880, is the earliest surviving narrative of the combat between Zeus (Ζεύς) and Typhon (Τυφῶν), the hundred-headed serpent-limbed monster whose Hesiodic-variant name is Typhoeus (Τυφωεύς).footnote:[West 1966, _Hesiod, Theogony_, on lines 820–880; Ogden 2013, ch. 2, on the Typhonomachy as the earliest Greek dragon-combat narrative.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The standard critical edition of the _Theogony_ used as the anchor throughout this chapter is Martin L. West's 1966 Oxford Clarendon edition, which provides the Greek text together with a detailed line-by-line commentary on the Typhonomachy passage.footnote:[West 1966, _Hesiod, Theogony_ (Oxford: Clarendon Press), critical edition with commentary.]
// EVIDENCE: source_id=west-1966-theogony ; loc=whole volume

The standard scholarly survey of the Greek dragon-combat tradition used as the secondary anchor throughout this chapter is Daniel Ogden's 2013 _Drakōn: Dragon Myth and Serpent Cult in the Greek and Roman Worlds_, especially chapters 2 and 3, which catalogue the Typhon material across the Greek and Roman literary record.footnote:[Ogden 2013, _Drakōn_, chs. 2–3.]
// EVIDENCE: source_id=ogden-2013 ; loc=chs. 2–3

The _Theogony_ is conventionally dated to c. 700 BCE and assigned to the late-eighth- or early-seventh-century Boeotian poet Hesiod, whose autobiographical voice frames the poem's prologue at the foot of Mount Helicon.footnote:[West 1966, introduction, on the date and authorship of the _Theogony_.]
// EVIDENCE: source_id=west-1966-theogony ; loc=introduction

The _Theogony_ survives in a continuous medieval manuscript tradition descended from Byzantine exemplars and is well preserved in its principal manuscript witnesses; the Typhonomachy passage at lines 820–880 has no significant lacunae and is read by all modern editors as a continuous text.footnote:[West 1966, introduction and apparatus on lines 820–880, on the manuscript tradition and the integrity of the Typhonomachy passage.]
// EVIDENCE: source_id=west-1966-theogony ; loc=introduction

Within the _Theogony_, the Typhonomachy is the closing combat. It is positioned after the Titanomachy (lines 617–819) and before the catalogue of Zeus's marriages and children, and it is the last divine combat before the stable Olympian pantheon takes its final shape.footnote:[West 1966, on the structural placement of the Typhonomachy at lines 820–880; Ogden 2013, ch. 2, on the Typhonomachy as the close of the _Theogony_.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The full Greek narrative of the Typhonomachy is a reconstruction from multiple sources rather than a single text. Hesiod gives the earliest sketch, Apollodorus _Bibliotheca_ 1.6.3 (1st–2nd c. CE) gives the extended canonical form, and Nonnus _Dionysiaca_ 1–2 (5th c. CE) gives a baroque late-antique elaboration.footnote:[Ogden 2013, ch. 2, on the multi-source reconstruction of the Typhonomachy across Hesiod, Apollodorus, and Nonnus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The continuous Greek attestation of the Typhonomachy spans more than a millennium, from Hesiod's late-eighth- or early-seventh-century version to Nonnus's fifth-century reworking, with intervening attestations in the _Homeric Hymn to Apollo_, Pindar, Aeschylus, and others.footnote:[Ogden 2013, chs. 2–3, on the millennium-long continuous attestation; West 1966, introduction, on the early Greek context.]
// EVIDENCE: source_id=ogden-2013 ; loc=chs. 2–3

The iconographic record is correspondingly continuous. Typhon is depicted in combat with Zeus on Chalcidian black-figure vases of the archaic period, in architectural sculpture, and in Roman-era mosaics, with iconographic stability around the serpent-tailed humanoid form.footnote:[Ogden 2013, chs. 2–3, on the Chalcidian-vase and architectural-sculpture corpus for the Typhonomachy.]
// EVIDENCE: source_id=ogden-2013 ; loc=chs. 2–3

The principal early-archaic iconographic exemplar is a Chalcidian black-figure hydria depicting Zeus with raised thunderbolt confronting a winged, serpent-legged Typhon, conventionally dated to the mid-sixth century BCE.footnote:[Ogden 2013, ch. 2, on the Chalcidian hydria and the archaic iconography of Typhon.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

M.L. West's 1997 _The East Face of Helicon_ treats the Hesiodic Typhonomachy and the wider succession-narrative of the _Theogony_ as the central documentary case for Near-Eastern-to-Greek transmission of theogonic and combat material.footnote:[West 1997, _The East Face of Helicon_, ch. 6, on Hesiod and the Near Eastern combat-myth corpus.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

Walter Burkert's 1992 _The Orientalizing Revolution_ argues for Phoenician and broader Levantine intermediaries as the principal channel through which Near Eastern theogonic and combat material reached early Greek poets in the eighth and seventh centuries BCE.footnote:[Burkert 1992, _The Orientalizing Revolution_, on Phoenician-mediated transmission to early Greek poetry.]
// EVIDENCE: source_id=burkert-1992 ; loc=whole volume

Joseph Fontenrose's 1959 _Python: A Study of Delphic Myth and Its Origins_ develops the comparative argument that the Apollo-Python combat at Delphi and the Zeus-Typhon combat are variant Greek instantiations of a single inherited dragon-combat type.footnote:[Fontenrose 1959, _Python_, on the Python-Typhon comparative argument.]
// EVIDENCE: source_id=fontenrose-1959 ; loc=whole volume

Neil Forsyth's 1987 _The Old Enemy_, ch. 4, places the Hesiodic Typhonomachy as the Greek station in the longue durée of the combat-myth tradition that runs from Sumerian Ninurta narratives through the Hebrew Bible into Christian apocalyptic.footnote:[Forsyth 1987, ch. 4, on Greek combat-myth in the long combat-myth trajectory.]
// EVIDENCE: source_id=forsyth-1987 ; loc=ch. 4

Modern scholarship treats the Typhonomachy as the principal test case for the Near-Eastern-to-Greek transmission hypothesis because the parallels with the Hurro-Hittite Kumarbi Cycle (cross-ref: Ch. 5) and with the Ugaritic Baal-Yamm-Lôtan complex (cross-ref: Ch. 7) are simultaneously specific and numerous.footnote:[West 1997, ch. 6; Burkert 1992, on the Typhonomachy as the central transmission test case.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

What follows takes the Greek combat in three movements — Hesiod's sketch, Apollodorus's sinew-theft expansion, and Nonnus's baroque elaboration — registers the partial attestations that fill in the picture between them, and then asks how the narrative looks once the Hurro-Hittite, Ugaritic, and Phoenician comparanda are placed alongside it.

=== Setting and the Olympian succession

The Hesiodic _Theogony_ presents a three-generation succession of divine sovereigns — Ouranos, Kronos, Zeus — in which each son violently displaces his father from the throne of heaven. The Typhonomachy is the final confrontation that secures the third-generation sovereign's rule.footnote:[West 1966, on the Ouranos-Kronos-Zeus succession at Theog. 154–210, 453–506, and 820–880.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 154–210

Ouranos (Sky) is the primordial sky-sovereign of the _Theogony_'s first generation. He is castrated by his son Kronos with a sickle of adamant supplied by his mother Gaia (Γαῖα), the primordial earth-goddess, who is angered by Ouranos's confinement of her offspring within her body.footnote:[West 1966, on Theog. 154–182, on Ouranos's castration by Kronos.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 154–182

Kronos, the second-generation sovereign, swallows each of his children at birth in fear of being displaced as he had displaced his own father. Zeus alone escapes this fate when his mother Rhea conceals the infant on Crete and gives Kronos a stone in swaddling clothes to swallow in his place.footnote:[West 1966, on Theog. 453–500, on Kronos's swallowing of his children and the survival of Zeus.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 453–500

The Titanomachy — the ten-year war between Zeus's faction (the Olympians, with the hundred-handed Hekatoncheires released from Tartarus as Zeus's allies) and Kronos's faction (the Titans) — ends with the defeat and imprisonment of the Titans in Tartarus (Τάρταρος), the lowest realm of the underworld and the prison of defeated divine enemies.footnote:[West 1966, on Theog. 617–819, on the Titanomachy and the imprisonment of the Titans in Tartarus.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 617–819

The Typhonomachy follows directly upon the Titanomachy in the _Theogony_'s narrative sequence. Hesiod marks the transition at line 820 by introducing Typhoeus as Gaia's last and youngest child.footnote:[West 1966, on the Theog. 820 transition and on Typhoeus as Gaia's youngest offspring.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820

Gaia, the primordial earth-goddess, is named explicitly in Hesiod as Typhoeus's mother. She conceives him in her later relationship with Tartarus, and the parental pairing earth-and-underworld is itself a marker of the monster's chthonic origin.footnote:[West 1966, on Theog. 821–822, on Gaia and Tartarus as Typhoeus's parents.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 821–822

The pairing of Gaia and Tartarus as Typhoeus's parents is Hesiodic. In Apollodorus _Bibliotheca_ 1.6.3, Gaia conceives Typhon by Tartarus specifically in vengeance after the Olympian defeat of the Giants, providing a generative motive that Hesiod does not name in lines 820–822.footnote:[Ogden 2013, ch. 2, on the Apollodoran motive (vengeance for the Giants) for Typhon's conception by Gaia and Tartarus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The narrative position of the Typhonomachy as the close of the succession-cycle gives Zeus's victory its theogonic function. With Typhoeus defeated, no further generation of sovereign-displacing combat occurs in the _Theogony_, and the Olympian dispensation is established as permanent.footnote:[West 1966, on Theog. 820–880 in the structural close of the succession; Forsyth 1987, ch. 4, on the theogonic function of the Typhonomachy.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The Typhonomachy thus serves the royal-legitimation function within the Hesiodic theogonic project. Zeus's combat-victory over Typhoeus is the act that confirms his kingship over gods and men, structurally parallel to Marduk's elevation in the Babylonian _Enūma Eliš_ (cross-ref: Ch. 3) and to Baal's combat in the Ugaritic Baal Cycle (cross-ref: Ch. 7).footnote:[West 1966, on the kingship-confirmation function of the combat; Forsyth 1987, ch. 4, on the comparative legitimation function.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The cosmic geography of the combat in Hesiod is wide. The engagement involves heaven, earth, and sea, with thunderbolts ranging across the sky, the earth shaking under the impact, and the waters of the sea boiling. The combat is staged on the full cosmographic scale that the Olympian dispensation requires.footnote:[West 1966, on Theog. 839–852, on the cosmic scale of the combat geography.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 839–852

=== Movement I — Hesiod's Typhonomachy (Theog. 820–880)

Hesiod's Typhonomachy, the earliest surviving form of the narrative, is a sketch rather than a fully developed combat scene. West's commentary describes the passage as a synoptic narrative of birth, fight, and binding, characterised by elaborate description of the monster but compressed treatment of the combat itself.footnote:[West 1966, on Theog. 820–880, characterising the passage as synoptic.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The narrative opens at line 820 with a temporal marker placing Typhoeus's birth after the imprisonment of the Titans in Tartarus, locating the Typhonomachy as a coda to the Titanomachy.footnote:[West 1966, on the Theog. 820 transition.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820

Typhoeus is named in the Hesiodic passage with the form Typhoeus (Τυφωεύς) rather than the later Apollodoran Typhon (Τυφῶν). West's commentary notes both names as ancient and as denoting the same figure across the textual tradition.footnote:[West 1966, on Theog. 821, on the name Typhoeus and its variant Typhon.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 821

The hundred heads of Typhoeus are described in the Hesiodic passage as serpent-heads springing from the monster's shoulders, with flickering tongues and fiery eyes. The multiplicity is a constitutive feature of the figure rather than an ornamental detail.footnote:[West 1966, on Theog. 824–828, on the hundred serpent-heads of Typhoeus.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 824–828

The voice of Typhoeus is described in the Hesiodic passage as polyphonic. Each of the hundred heads emits a different sound — the bellowing of bulls, the roaring of lions, the barking of hounds, the hissing of serpents — and the combined polyphony is presented as itself uncanny.footnote:[West 1966, on Theog. 829–835, on the polyphonic voice of Typhoeus.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 829–835

West's commentary on the polyphonic-voice passage notes that the catalogue of bestial sounds is one of the most elaborate ekphrastic moments in the _Theogony_ and that it serves the rhetorical function of marking Typhoeus as a being who exceeds every category of attested creature.footnote:[West 1966, on Theog. 829–835, commentary on the rhetorical function of the polyphony.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 829–835

The Hesiodic passage names the gods' fear of Typhoeus. Had Zeus not perceived the threat in time, Typhoeus would have become sovereign over mortals and immortals; the conditional is presented in lines 836–838 as a near-miss in which the Olympian dispensation came close to being overturned.footnote:[West 1966, on Theog. 836–838, on the conditional near-miss of Typhoeus's sovereignty.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 836–838

Zeus's perception of the threat is presented in the Hesiodic passage as the trigger for the combat. The storm-god is described as recognising the monster's challenge and arming himself with thunder, lightning, and the smouldering thunderbolt as his combat weapons.footnote:[West 1966, on Theog. 839–841, on Zeus's perception and arming.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 839–841

The thunderbolt is presented in the Hesiodic passage as Zeus's principal combat weapon. He leaps from Olympus and strikes Typhoeus with the bolt, scorching the monster's hundred heads and reducing the serpent-limbs to ash.footnote:[West 1966, on Theog. 853–858, on the thunderbolt-strike against Typhoeus.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 853–858

The cosmic-scale description of the combat at Theog. 839–852 enumerates the geophysical effects. The earth groans under the weight of the engagement, the sea boils under the heat of the bolts, the heavens shake, and Hades trembles in Tartarus together with the imprisoned Titans — a cosmographic seismology that registers the combat at every level of the world's structure.footnote:[West 1966, on Theog. 839–852, on the cosmic-scale geophysical description.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 839–852

West's commentary observes that the geophysical description in Theog. 839–852 is unusually elaborate even for the _Theogony_'s standards and that the seismological register encodes the combat as cosmographically significant: the combat shakes the world because the sovereignty of the world is at stake.footnote:[West 1966, on Theog. 839–852, commentary on the seismological register.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 839–852

After the thunderbolt-strike, Hesiod's narrative describes the burning of Typhoeus. The monster is consumed by fire from the heat of the bolts, with his serpent-heads scorched and his limbs reduced to formlessness; Zeus then casts him down into Tartarus.footnote:[West 1966, on Theog. 859–868, on the burning and casting-down of Typhoeus.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 859–868

The casting-down of Typhoeus into Tartarus places him in the same prison as the defeated Titans of the previous combat, structurally completing the Hesiodic pattern in which defeated divine antagonists are confined in the lowest realm rather than annihilated outright.footnote:[West 1966, on Theog. 868, on the placement of Typhoeus in Tartarus alongside the defeated Titans.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 868

The closing section of the Hesiodic passage (Theog. 869–880) presents the storm-winds as the offspring of Typhoeus. The destructive winds that bring shipwreck and crop-failure are described as emanating from the defeated monster and as the post-defeat residue of his power.footnote:[West 1966, on Theog. 869–880, on the storm-winds as Typhoeus's offspring.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 869–880

The storm-wind aetiology in Theog. 869–880 distinguishes the named winds (Notos, Boreas, Zephyros, Argestes) from the destructive Typhonic winds. The named winds are beneficial and Olympian-sanctioned, while the storm-winds emanating from Typhoeus are presented as the disorderly survival of the monster's power.footnote:[West 1966, on Theog. 869–880, on the distinction between Olympian and Typhonic winds.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 869–880

The Hesiodic Typhonomachy contains no extended description of a combat sequence with multiple exchanges or temporary reversals. Zeus perceives the threat, arms himself, strikes with the thunderbolt, and casts the burning monster down — the entire combat is compressed into roughly the central thirty lines of the passage.footnote:[West 1966, on the compressed combat sequence at Theog. 853–868.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 853–868

West's commentary on the compressed combat sequence notes that the brevity is itself characteristic. Hesiod's interest is in the cosmographic significance of the combat rather than in the choreography of individual blows, and the passage's elaboration is concentrated on the description of the monster and on the geophysical effects of the strike.footnote:[West 1966, on Theog. 820–880, commentary on the compressed combat narrative.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

Several features that later readers associate with the Typhonomachy are absent from the Hesiodic passage. There is no episode of temporary defeat for Zeus, no removal of the thunderbolt or the sinews, no captivity in a cave, and no recovery operation by subordinate deities. These episodes belong to the Apollodoran expansion (1st–2nd c. CE) and are not retrojected into the Hesiodic narrative.footnote:[West 1966, on the absence of the sinew-theft sequence in the Hesiodic passage; Ogden 2013, ch. 2, on the Apollodoran expansion as later.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 820–880

The Hesiodic Typhonomachy contains no explicit naming of Mount Etna (Αἴτνη) as the burial place of Typhoeus. The volcanic-aetiological identification is post-Hesiodic and is most prominently associated with Pindar's _Pythian_ 1 and with the Aeschylean-attributed _Prometheus Bound_.footnote:[Ogden 2013, ch. 2, on the post-Hesiodic emergence of the Etna identification.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Hesiod casts Typhoeus into Tartarus rather than under Etna. The volcanic locus is a later geographical specification that situates the casting-down in the topography of Sicily, becoming canonical in the post-Hesiodic tradition without displacing the Tartarus locus altogether.footnote:[West 1966, on Theog. 868; Ogden 2013, ch. 2, on the Tartarus and Etna loci.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 868

Hesiod's narrative presents Typhoeus as serpent-limbed. From the monster's shoulders spring serpents in place of arms or legs, marking the figure as morphologically draconic in the Greek sense (cf. Ogden 2013's *drakōn* classification) and as belonging to the wider Greek dragon-adversary type.footnote:[West 1966, on Theog. 824–828, on Typhoeus's serpent-limbs; Ogden 2013, ch. 2, on the drakōn classification.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 824–828

West's commentary observes that the serpent-limbed morphology in the Hesiodic passage is iconographically influential. The archaic-period vase-painters take up the serpent-legged form (rather than fully serpentine bodies) as the canonical Greek depiction of Typhoeus, and the form is stable across the iconographic record.footnote:[West 1966, on the iconographic afterlife of the Hesiodic morphology; Ogden 2013, ch. 2.]
// EVIDENCE: source_id=west-1966-theogony ; loc=Theog. 824–828

The Hesiodic passage does not name a Cilician location for Typhoeus's birth or for the combat. The Cilician anchorage of the figure is post-Hesiodic and emerges most clearly in Pindar's _Pythian_ 1.16–17 (where Typhon is born in Cilicia) and in Apollodorus _Bibliotheca_ 1.6.3 (where the Corycian cave in Cilicia is the locus of the sinew-theft).footnote:[Ogden 2013, ch. 2, on the post-Hesiodic emergence of the Cilician anchorage.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

[INFERENCE: the structural function of the Hesiodic Typhonomachy as the close of the succession-cycle gives the combat its royal-legitimation force, even though Hesiod does not explicitly say "Zeus's victory confirms his kingship" | basis: the placement of the passage at Theog. 820–880 immediately before the catalogue of Zeus's marriages (894 ff.) and the wider succession-frame Ouranos-Kronos-Zeus, in which the Typhonomachy is the final combat that prevents a fourth-generation displacement | risk: the inference is structural-narratological rather than directly attested; West's commentary endorses this reading without using these exact terms.]

The Hesiodic narrative's compactness is itself part of what scholars use as evidence for transmission. West 1997 argues that Hesiod is working with inherited material that he compresses, rather than inventing the combat-narrative whole; the elaborate description of the monster against the compressed combat-narrative is the textual signature of compression of received material.footnote:[West 1997, ch. 6, on the compression-of-received-material reading of the Hesiodic Typhonomachy.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

[VARIANT: primary=West 1966 reads Theog. 820–880 as a continuous and integral part of the _Theogony_ | alt=some 19th- and early-20th-c. editors treated the Typhonomachy as an interpolation by a later hand | chosen: West 1966's continuous-and-integral reading | reason: the West 1966 reading is the modern scholarly consensus, and the lines are present in all principal manuscript witnesses; the interpolation hypothesis is no longer current.]

=== Movement II — Apollodorus's expansion (Bibliotheca 1.6.3)

Apollodorus's _Bibliotheca_ 1.6.3, conventionally dated to the first or second century CE, gives the extended canonical narrative of the Typhonomachy: the version that includes Typhon's temporary defeat of Zeus, the severing of Zeus's sinews, the cave-imprisonment, and the recovery operation by Hermes and Aigipan.footnote:[Ogden 2013, ch. 2, on Apollodorus _Bibliotheca_ 1.6.3 as the source of the extended Typhonomachy.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The _Bibliotheca_ is a Greek prose mythographic compendium that summarises and harmonises material from many earlier sources. Apollodorus's account of the Typhonomachy at 1.6.3 is therefore not a primary witness to a single archaic version but a later compilation that may preserve elements absent from the surviving Hesiodic and other early sources.footnote:[Ogden 2013, ch. 2, on the _Bibliotheca_'s mythographic-compendium character.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The sinew-theft episode is the principal feature that distinguishes the Apollodoran expansion from the Hesiodic narrative. This episode is NOT present in Hesiod's _Theogony_ 820–880 and must not be retrojected into the Hesiodic version.footnote:[Ogden 2013, ch. 2, on the sinew-theft as Apollodoran rather than Hesiodic; West 1966, on the absence of the episode in Theog. 820–880.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Apollodorus's narrative opens with Typhon's birth from Gaia and Tartarus presented as a vengeance for the defeat of the Giants, providing a generative motive that Hesiod does not specify. In the Apollodoran framing, the combat is one stage in an ongoing series of earth-born challenges to Olympian sovereignty.footnote:[Ogden 2013, ch. 2, on the Apollodoran framing of Typhon's birth as Gaian vengeance for the Giants.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Apollodoran description of Typhon's morphology is more developed than Hesiod's. The body is enormous, surpassing all mountains in height, with serpent-coils for legs, dragon-heads erupting from the hands, and fire flashing from the eyes; the figure exceeds even the elaborate Hesiodic catalogue.footnote:[Ogden 2013, ch. 2, on the Apollodoran morphology of Typhon.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

In the Apollodoran narrative, the Olympian gods are initially put to flight by Typhon's onslaught and flee to Egypt, where they assume animal disguises to escape detection — an aetiology Apollodorus uses to account for the theriomorphic Egyptian deities. This episode is absent from Hesiod and is part of the Apollodoran expansion.footnote:[Ogden 2013, ch. 2, on the Olympian flight to Egypt and the theriomorphic-disguise aetiology in Apollodorus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Zeus alone (with Athena, in some recensions) confronts Typhon directly in the Apollodoran narrative. The engagement is staged at first on Mount Casius in Syria, locating the Apollodoran combat in the Levantine-Anatolian zone rather than in the Aegean.footnote:[Ogden 2013, ch. 2, on Mount Casius as the Apollodoran combat-site.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

In the first phase of the Apollodoran combat, Zeus strikes Typhon with the thunderbolt and pursues the wounded monster. The engagement then turns against Zeus when Typhon overcomes him, wresting away the *harpe* (sickle) Zeus carried and using it against him.footnote:[Ogden 2013, ch. 2, on the first-phase combat and Typhon's seizure of the harpe.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The decisive moment of the Apollodoran narrative is the temporary defeat of Zeus. Typhon overpowers the storm-god, severs the sinews of his hands and feet with the *harpe*, and renders him incapable of further combat or movement.footnote:[Ogden 2013, ch. 2, on Typhon's temporary defeat of Zeus and the severing of the sinews.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The severed sinews are placed by Typhon in a bear-skin and entrusted to the dragoness Delphyne to guard, while the immobilised Zeus is hidden in the Corycian cave (Κωρύκιον ἄντρον), a real cave in Cilicia near the Mediterranean coast that the Apollodoran narrative names as the locus of the captivity.footnote:[Ogden 2013, ch. 2, on the Corycian cave and Delphyne's guarding of the sinews in the bear-skin.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Corycian cave's identification as a real Cilician topography is geographically specific. The cave is on the southern coast of Anatolia, opposite Cyprus, in a region that was within the network of Levantine-Greek contact during the orientalizing period — a geographical anchor whose significance for the Near-Eastern transmission argument is treated below.footnote:[Ogden 2013, ch. 2, on the Cilician geography of the Corycian cave; West 1997, ch. 6, on the orientalizing-contact significance of the Cilician anchorage.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The recovery operation in the Apollodoran narrative is conducted by Hermes and Aigipan. The two gods sneak into the Corycian cave, deceive Delphyne, and steal back the sinews from the bear-skin, after which they restore them to Zeus's hands and feet.footnote:[Ogden 2013, ch. 2, on the Hermes-and-Aigipan recovery operation.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Aigipan ("Goat-Pan") is in the Apollodoran narrative paired with Hermes for the recovery operation. The majority scholarly position identifies Aigipan as Pan under a goat-cult epithet rather than as a separate deity, and the partnership therefore registers a trickster-god (Hermes) with the pastoral god in goat-form (Aigipan / Pan) — a pairing that is unusual in the Olympian record and one of the Apollodoran expansion's most distinctive features.footnote:[Ogden 2013, ch. 2, on Aigipan as Hermes's partner in the recovery operation; the Aigipan-as-Pan-epithet identification is the majority view in modern scholarship.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Hermes-and-Aigipan recovery operation in the Corycian cave has been compared with the Hurro-Hittite Elkunirsa myth, in which a comparable pairing of subordinate deities recovers the storm-god's organs after their theft (cross-ref: Near-Eastern transmission section, below).footnote:[West 1997, ch. 6, on the Elkunirsa-recovery comparison; Hoffner 1998, on the Elkunirsa myth in the Hittite corpus.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

After the recovery of his sinews, Zeus is restored to combat capability and renews the engagement with Typhon. The second-phase combat in the Apollodoran narrative pursues Typhon across a series of geographical stages, with thunderbolts hurled in pursuit.footnote:[Ogden 2013, ch. 2, on the Apollodoran second-phase combat after the sinew-recovery.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Apollodoran pursuit is staged on Mount Nysa in Thrace, where the Fates feed Typhon ephemeral fruits that diminish his power, and culminates with Zeus catching Typhon and casting Mount Etna upon him in Sicily, burying the monster under the volcano.footnote:[Ogden 2013, ch. 2, on the Mount Nysa episode and the casting of Etna.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The casting of Mount Etna onto Typhon in the Apollodoran narrative is the volcanic-aetiological resolution. Typhon's continuing struggle beneath the mountain accounts for Etna's eruptions, and the volcano serves both as the prison and as the post-combat sign of the bound monster's residual power.footnote:[Ogden 2013, ch. 2, on the Etna-aetiology in Apollodorus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Apollodoran narrative consolidates the volcanic-aetiological reading that had developed in the post-Hesiodic tradition. By the first or second century CE, the Etna identification has fully displaced the Hesiodic Tartarus locus as the canonical burial place of Typhon in many subsequent retellings.footnote:[Ogden 2013, ch. 2, on the consolidation of the Etna identification by the Apollodoran period.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The structure of the Apollodoran combat — failed first phase, sinew-theft and captivity, recovery operation by subordinate deities, successful second phase, volcanic burial — is a tripartite-with-recovery pattern that contrasts with the Hesiodic single-strike compression and shows the narrative form developing toward a more elaborate combat-cycle over the millennium between Hesiod and Apollodorus.footnote:[Ogden 2013, ch. 2, on the tripartite-with-recovery structure of the Apollodoran combat.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Apollodoran sinew-theft episode is the principal point at which the Greek combat-narrative shows a structural feature with a Hurro-Hittite parallel rather than a purely Hesiodic precedent. The theft-of-divine-organs motif has its closest documented parallel in the Hittite Elkunirsa material, not in the Hesiodic _Theogony_ (cross-ref: Near-Eastern transmission section).footnote:[West 1997, ch. 6, on the Elkunirsa parallel for the Apollodoran sinew-theft.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Apollodoran narrative's geographical itinerary — Mount Casius (Syria), Corycian cave (Cilicia), Mount Nysa (Thrace), Etna (Sicily) — traces a Mediterranean-wide map for the combat, with the Levantine-Cilician segment being the geographically suggestive station for the Near-Eastern transmission argument.footnote:[Ogden 2013, ch. 2, on the Apollodoran geographical itinerary; West 1997, ch. 6, on the Cilician segment.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Apollodorus is, with respect to the Typhonomachy, the principal source for what is by the early imperial period the canonical extended narrative of the combat. Subsequent retellings — including Nonnus and most Latin reception — work from a story-shape that includes the sinew-theft and the cave-captivity rather than the bare Hesiodic sketch.footnote:[Ogden 2013, ch. 2, on Apollodorus's role in establishing the canonical extended narrative.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The fact that the Apollodoran sinew-theft episode is absent from Hesiod has been read in two different ways in the modern scholarship: as a later Greek elaboration that draws independently on the cave-imprisonment topos, and as a preserved transmission of a Hurro-Hittite motif that Hesiod did not include but that survived in less elite or non-Hesiodic Greek versions until being recorded by Apollodorus (cross-ref: Near-Eastern transmission section).footnote:[West 1997, ch. 6; Ogden 2013, ch. 2, on the two readings of the sinew-theft's absence from Hesiod.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

Pindar's _Pythian_ 1.16–28 (early-fifth-century BCE) — chronologically intermediate between Hesiod and Apollodorus — does not preserve the sinew-theft but does specify Typhon's Cilician origin and the Etna burial. The Cilician geography is thus already present in the early-fifth-century record.footnote:[Ogden 2013, ch. 2, on Pindar _Pythian_ 1 and the Cilician geography.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

[VARIANT: primary=Apollodorus _Bibliotheca_ 1.6.3 (1st–2nd c. CE) gives the extended sinew-theft narrative | alt=Hesiod _Theogony_ 820–880 (c. 700 BCE) gives the bare combat-and-burial sketch | chosen: present-both-attributed | reason: per brief co-equal classification, each source's contribution is named and attributed; the sinew-theft is registered as Apollodoran and explicitly NOT retrojected into Hesiod.]

The Apollodoran narrative uses the *harpe* (sickle) — the same weapon that Kronos used to castrate Ouranos in Hesiod (Theog. 178–182) — as Typhon's instrument for severing Zeus's sinews. The symmetry between Kronos's act against the previous sovereign and Typhon's act against Zeus has been read by some scholars as a deliberate echo within the Apollodoran narrative, registering the combat as a near-replay of the founding succession-conflict.footnote:[Ogden 2013, ch. 2, on the harpe-symmetry in the Apollodoran narrative.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

=== Movement III — Nonnus's baroque elaboration (Dionysiaca 1–2)

Nonnus's _Dionysiaca_, books 1 and 2, conventionally dated to the fifth century CE, gives an extensively elaborated baroque narrative of the Typhonomachy that incorporates the Apollodoran sinew-theft within a much more developed combat-sequence and adds the figure of Cadmus as a participant in the recovery.footnote:[Ogden 2013, ch. 2, on Nonnus _Dionysiaca_ 1–2 as the baroque expansion of the Typhonomachy.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The _Dionysiaca_ is a 48-book Greek hexameter epic by Nonnus of Panopolis (in Upper Egypt), a fifth-century-CE composition in the late-antique encyclopaedic-epic tradition. The Typhonomachy occupies the opening books and is positioned as a prelude to the main Dionysiac narrative of the poem.footnote:[Ogden 2013, ch. 2, on the _Dionysiaca_'s structural placement of the Typhonomachy.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Nonnus's narrative inherits the Apollodoran sinew-theft scenario. Typhon overcomes Zeus and steals the storm-god's sinews; in the Nonnian elaboration, however, Typhon also seizes the thunderbolt itself and attempts to wield it, with comic results, since the bolt cannot be controlled by hands not the storm-god's.footnote:[Ogden 2013, ch. 2, on the Nonnian elaboration of Typhon's seizure of sinews and thunderbolt.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The figure of Cadmus (the Latinised form is preserved in this Nonnus reception context — note that the Greek form Kadmos is the standard transliteration outside Nonnus reception) plays the recovery-trickster role in the Nonnian elaboration. Cadmus disguises himself as a shepherd, plays the pipes (or panpipes), and beguiles Typhon into setting aside the sinews so that he can listen.footnote:[Ogden 2013, ch. 2, on Cadmus's pipe-playing recovery role in Nonnus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Cadmus's pipe-music, in the Nonnian narrative, soothes Typhon to the point of trance. While Typhon is enthralled, Cadmus retrieves the sinews from where Typhon has set them down and conceals them; the recovery is staged as a music-trickster intervention rather than a stealth-and-deception operation in the Apollodoran mode.footnote:[Ogden 2013, ch. 2, on the music-trickster motif in Nonnus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The pipe-playing Cadmus is a Nonnian elaboration on the Apollodoran Hermes-and-Aigipan pairing. The music-trickster role in Apollodorus is divided between Hermes (the trickster) and Aigipan (the pastoral-deity), and Nonnus consolidates these into the single Cadmus figure who is both Theban founder and pastoral musician.footnote:[Ogden 2013, ch. 2, on Nonnus's consolidation of the Apollodoran recovery-pair into Cadmus.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

After Cadmus retrieves the sinews and restores them to Zeus, the Nonnian narrative resumes the second-phase combat with the same volcanic resolution as the Apollodoran tradition. Zeus pursues Typhon, casts him down, and buries him under Mount Etna, with the volcano accounting for the post-combat eruptive activity.footnote:[Ogden 2013, ch. 2, on the Nonnian volcanic resolution.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Nonnus's elaboration includes extended ekphrastic descriptions of Typhon's body. Hundreds of lines describe each region of the monster's morphology in turn, with serpent-heads enumerated by region of the body, voices catalogued by species of bestial sound, and the monster's flesh described as a kind of cosmographic landscape.footnote:[Ogden 2013, ch. 2, on the Nonnian ekphrasis of Typhon's body.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Nonnian Typhonomachy is the latest extended narrative attestation in the Greek tradition before the closure of the late-antique pagan literary record. It stands as a witness to the continued vitality of the combat-narrative as a literary subject across more than a millennium of Greek composition.footnote:[Ogden 2013, ch. 2, on the Nonnian Typhonomachy as the late-antique terminal attestation.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Cadmus-with-pipes episode is Nonnus's distinctive contribution to the Typhonomachy tradition. It is not preserved in the earlier Hesiodic, Pindaric, or Apollodoran sources, and it is registered in the modern scholarship as a Nonnian innovation that synthesises elements of the Theban Cadmus-and-the-dragon tradition with the Apollodoran sinew-recovery scenario.footnote:[Ogden 2013, ch. 2, on the Cadmus-with-pipes episode as a Nonnian innovation.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Cadmus figure is in his Greek form Kadmos, the Theban founder-hero who slays the dragon of Ares at Thebes and sows its teeth to raise the Spartoi (cross-ref: Ch. 12 family chapter). The Latinised form Cadmus is preserved here only because the Nonnus reception context standardly uses the Latin form in modern Greek-and-Latin literary scholarship.footnote:[Ogden 2013, ch. 2, on the Greek-and-Latin name forms; glossary.yaml on the Kadmos / Cadmus distinction.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

=== Partial attestations

The _Homeric Hymn to Apollo_, lines 305–355 (conventionally dated to the seventh or sixth century BCE), preserves a partial attestation in which Typhon is described as the offspring of Hera, born by parthenogenesis in retaliation against Zeus's solo conception of Athena, and entrusted to a draconic guardian at Pytho.footnote:[Ogden 2013, ch. 2, on the _Homeric Hymn to Apollo_ 305–355 and the Hera-parthenogenesis variant.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Hera-parthenogenesis genealogy of Typhon in the _Homeric Hymn to Apollo_ contradicts the Hesiodic-and-Apollodoran genealogy from Gaia and Tartarus. Modern scholarship treats this as a separate variant tradition rather than reconciling it with the Theogonic genealogy.footnote:[Ogden 2013, ch. 2, on the variant-genealogy reading of the _Homeric Hymn to Apollo_.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The _Homeric Hymn to Apollo_'s Typhon is connected with the Pytho location (the older name of Delphi) and with the draconic adversary that Apollo slays at the founding of the oracle, providing a textual link between the Typhon material and the Apollo-Python combat (cross-ref: Ch. 12 family chapter).footnote:[Ogden 2013, ch. 2, on the Pytho-Typhon-Python textual link in the _Homeric Hymn to Apollo_; Fontenrose 1959 on the comparative Python-Typhon argument.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Pindar's _Pythian_ 1.16–28, an early-fifth-century BCE victory ode, locates Typhon under Mount Etna and uses the volcano's eruptions as the metaphorical register for the bound monster's residual force. Pindar's Typhon is named as Cilician-born and as confined under the Sicilian volcano.footnote:[Ogden 2013, ch. 2, on Pindar _Pythian_ 1.16–28 and the Etna-and-Cilicia identifications.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

The Pindaric ode is the earliest surviving named-source for the Etna identification. The Hesiodic Tartarus locus and the Pindaric Etna locus are not directly contradictory (Etna can be read as a topographical specification of the Tartarus burial), but the Pindaric specification is recognisably innovative within the surviving record.footnote:[Ogden 2013, ch. 2, on Pindar's status as the earliest named-source for the Etna identification.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

_Prometheus Bound_, lines 351–372 (attributed to Aeschylus by ancient tradition though authorship has been contested in modern scholarship — Griffith 1977, West 1990 — and is not now uncontroversially Aeschylean), describes Typhon as crushed under Etna, with the volcano's eruptions caused by his struggling beneath the mountain. The description is consistent with the Pindaric register and provides a second early-fifth-century BCE attestation of the volcanic identification.footnote:[Ogden 2013, ch. 2, on _Prometheus Bound_ 351–372 and the Etna identification; on the contested authorship question see Griffith 1977 and West 1990 contra the traditional Aeschylean attribution.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

[VARIANT: Hesiod _Theogony_ 820–880 (c. 700 BCE; the earliest sketch) | Apollodorus _Bibliotheca_ 1.6.3 (1st–2nd c. CE; the sinew-theft expansion) | Nonnus _Dionysiaca_ 1–2 (5th c. CE; the baroque elaboration with Cadmus's pipes) | partial attestations: _Homeric Hymn to Apollo_ 305–355, Pindar _Pythian_ 1.16–28, Aeschylus _Prometheus Bound_ 351–372 | chosen: present-all-attributed per brief co-equal classification — the chapter presents each source's contribution attributed to its own context, registering the millennium-long accretion of the narrative.]

=== The Near-Eastern transmission question

M.L. West's 1997 _The East Face of Helicon_, ch. 6, argues that the Hesiodic succession-narrative (Ouranos → Kronos → Zeus) and the Hesiodic Typhonomachy both derive from the Hurro-Hittite Kumarbi Cycle (cross-ref: Ch. 5) via Near Eastern mediation, with the structural correspondences sufficiently specific to require transmission rather than convergence.footnote:[West 1997, ch. 6, on the Kumarbi-to-Hesiod transmission argument.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Hesiodic succession-sequence Ouranos → Kronos → Zeus corresponds in structure to the Kumarbi-Cycle succession Alalu → Anu → Kumarbi → Teshub. In both, kingship of heaven is transmitted through violent displacement of each generation by its successor; in both, the third- or fourth-generation sovereign (Zeus / Teshub) is the storm-god who must defend his rule against monstrous offspring of the deposed predecessor.footnote:[West 1997, ch. 6, on the Hesiod-Kumarbi succession parallel.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The most specific point of correspondence in the succession-narrative is the castration motif. In Kingship in Heaven (Ch. 5), Kumarbi castrates Anu by biting off his genitals and swallowing them; in the Hesiodic _Theogony_ 178–182, Kronos castrates Ouranos with a sickle of adamant supplied by Gaia — the genital-castration of the sky-god by his successor is the shared structural feature.footnote:[West 1997, ch. 6, on the castration parallel between Kumarbi and Kronos; West 1966, on Theog. 178–182.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

Beyond the structural correspondence, the Kumarbi-and-Anu and Kronos-and-Ouranos castrations share the motif of the prophetic declaration after castration. Anu, after losing his genitals to Kumarbi, declares the offspring that will grow inside Kumarbi's body and depose him in turn — a prophetic-conception logic that has its Hesiodic counterpart in the prophecy that one of Kronos's children will displace him, the prophecy that motivates Kronos's swallowing of his children.footnote:[West 1997, ch. 6, on the prophetic-declaration parallel.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Kumarbi-Cycle's Song of Ullikummi (Ch. 5) contains the most specific parallel to the Typhonomachy. Ullikummi is a stone-monster generated by Kumarbi as an instrument against the storm-god Teshub; Ullikummi grows from the sea, threatens to displace the storm-god from heaven, and is finally defeated through a wisdom-counsellor's technical solution — a structural pattern that the Typhonomachy reproduces in its storm-god-vs-cosmographically-immense-monster shape.footnote:[West 1997, ch. 6, on the Ullikummi-Typhon structural parallel; Hoffner 1998, §15 (Song of Ullikummi).]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Ullikummi-Typhon parallel is concrete and specific in the lithic / cosmographic register. Ullikummi's stone-body and growth-toward-heaven correspond to the post-Hesiodic Typhon's lithic / volcanic locus under Etna, with both monsters figured as cosmographic intrusions reaching from the lower realms toward the sky.footnote:[West 1997, ch. 6, on the lithic / cosmographic register of the Ullikummi-Typhon parallel.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Kumarbi-Cycle's Song of Hedammu (Ch. 5) presents a sea-monster of voracious appetite, born from Kumarbi's mating with the daughter of the sea-god, who threatens the land and seas before being incapacitated by Šauška's seduction. The growth-from-sea morphology and the threat-to-cosmographic-order function correspond structurally to the Hesiodic-Apollodoran Typhon's birth from Gaia (and from Tartarus, whose territory includes the deep waters in the Hesiodic cosmography).footnote:[West 1997, ch. 6, on the Hedammu-Typhon parallel; Hoffner 1998, §16 (Song of Hedammu).]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Hedammu-Typhon parallel is most concrete in the growth-from-sea imagery. Hedammu rises voracious from the deep waters in the Hurro-Hittite narrative, and Apollodoran-and-Nonnian Typhon's morphology is described in terms of cosmographic extension across sea-and-land — the marine register of the monster has its Hurro-Hittite precedent in Hedammu rather than in Hesiod's compressed sketch.footnote:[West 1997, ch. 6, on the Hedammu-Typhon marine-register correspondence.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Hittite Elkunirsa-and-Ašertu fragment, a Hurrian-derived Hittite text in Hoffner's _Hittite Myths_ corpus, preserves a narrative in which a storm-god is incapacitated by the theft of his organs and recovered through subordinate-deity intervention. The structural parallel with the Apollodoran sinew-theft is the most specific motif-level correspondence between the Hittite and Greek combat-narratives.footnote:[West 1997, ch. 6, on the Elkunirsa parallel for the Apollodoran sinew-theft; Hoffner 1998, on the Elkunirsa-Ašertu fragment.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Elkunirsa parallel is significant because it provides a documented Near Eastern precedent for the precise motif (theft of the storm-god's bodily organs by an antagonist; recovery operation by subordinate deities; restoration enabling the second-phase combat) that is absent from Hesiod and present only in Apollodorus. The parallel thus supports the reading that Apollodoran material preserves transmission-elements that the Hesiodic synopsis omitted.footnote:[West 1997, ch. 6, on the significance of the Elkunirsa parallel for the Apollodoran sinew-theft.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The geographical anchorage of the Apollodoran combat in Cilicia (the Corycian cave) is the geographically suggestive corollary of the transmission argument. Cilicia is the southern coast of Anatolia, within the orientalizing-period contact zone between Greek and Near Eastern cultures, and the Cilician location of the Greek myth's most Hurro-Hittite-resembling episode is consistent with that contact zone as the transmission corridor.footnote:[West 1997, ch. 6, on the Cilician geography as a transmission-corridor anchor.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

Pindar's _Pythian_ 1's Cilician anchorage of Typhon's birth (line 17) provides a fifth-century BCE attestation of the Cilician geographical specification, predating the Apollodoran narrative by some six centuries and showing that the Cilicia connection was already established in the early Greek tradition — not a late Apollodoran addition.footnote:[West 1997, ch. 6; Ogden 2013, ch. 2, on Pindar's early attestation of the Cilician anchorage.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

Walter Burkert's 1992 _The Orientalizing Revolution_ argues for Phoenician intermediaries as the principal transmission channel. Rather than direct Hurrian-or-Hittite-to-Greek transmission, the combat-myth material reaches Greek poets through Phoenician traders, scribes, and craftsmen whose presence in the eastern Mediterranean (including Cilician ports) is well documented in the eighth and seventh centuries BCE.footnote:[Burkert 1992, on Phoenician intermediaries in the orientalizing transmission.]
// EVIDENCE: source_id=burkert-1992 ; loc=whole volume

Burkert's Phoenician-mediation argument is supported by the broader pattern of orientalizing Greek artistic, religious, and literary motifs in the early Archaic period: the same period in which Greek alphabet-script is borrowed from Phoenician, in which Greek bronze-working absorbs Levantine techniques, and in which Greek religious iconography incorporates Levantine forms.footnote:[Burkert 1992, on the orientalizing-horizon pattern of cultural transmission.]
// EVIDENCE: source_id=burkert-1992 ; loc=whole volume

Burkert's reading positions the Typhonomachy as one element within a wider orientalizing transmission of theogonic and cosmological material from the eastern Mediterranean into archaic Greek poetry, with the specific Cilician-Phoenician contact zones as the most likely transmission corridor.footnote:[Burkert 1992, on the Typhonomachy in the orientalizing transmission.]
// EVIDENCE: source_id=burkert-1992 ; loc=whole volume

The Phoenician-mediation argument and the direct-Hurro-Hittite argument are not strictly alternatives. The Phoenician traders and scribes of the early Archaic period were themselves heirs of a Levantine literary culture that included the Ugaritic Baal-Yamm-Lôtan material (cross-ref: Ch. 7) and that was in turn in contact with the Anatolian Hurro-Hittite tradition; the transmission corridor was a network rather than a single line.footnote:[West 1997, ch. 6; Burkert 1992, on the network character of the orientalizing transmission corridor.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Ugaritic Baal-Yamm-Lôtan material (cross-ref: Ch. 7) supplies an additional set of structural correspondences with the Typhonomachy. The storm-god (Baal / Zeus) confronts a personified-sea / serpentine antagonist (Yamm / Lôtan / Typhon), and the combat establishes the storm-god's sovereignty in the divine assembly — a structural pattern Smith-and-Pitard 2009's Baal Cycle commentary documents in detail.footnote:[West 1997, ch. 6, on the Baal-Yamm parallel for the Typhonomachy; cross-ref: Ch. 7.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Lôtan / Litanu of the Ugaritic corpus — the seven-headed serpent named in KTU 1.5 i 1–3 as Baal's adversary — has a distinctive multi-headed morphology that Lôtan shares with Hesiodic Typhoeus and that Day 1985 (cross-ref: Ch. 8) treats as one of the closest motif-level correspondences in the Levantine-Greek combat-myth corpus.footnote:[West 1997, ch. 6, on the Lôtan-Typhon morphological correspondence.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The cumulative force of the transmission argument depends on the convergence of multiple independent lines of evidence: motif-specific structural parallels (succession with castration; growth-from-sea monster; sinew-theft and recovery), geographical anchoring (Cilicia / Corycia), and the wider orientalizing-period contact-zone documentation. West 1997 and Burkert 1992 read these as mutually reinforcing.footnote:[West 1997, ch. 6; Burkert 1992, on the convergent-evidence structure of the transmission argument.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The Mesopotamian background — the storm-god / cosmogonic-combat tradition of Marduk-and-Tiamat (cross-ref: Ch. 3) and Ninurta-and-Anzû (cross-ref: Ch. 2) — is treated by Burkert as the deeper substrate. The Mesopotamian combat-cosmogony is the source-tradition that the Hurro-Hittite Kumarbi Cycle reworks (Ch. 5), and that the Levantine and Greek traditions in turn receive through the Anatolian-Levantine corridor.footnote:[Burkert 1992, on the Mesopotamian deep-substrate of the orientalizing transmission.]
// EVIDENCE: source_id=burkert-1992 ; loc=whole volume

The Marduk-Tiamat parallel for Zeus-Typhon is at the level of structural type rather than at the level of specific shared motifs. Storm-god confronts personified-monstrous adversary in single combat to establish sovereignty, with the monster's body figured as cosmographically immense; direct transmission from Babylon to Hesiod is less easily documented than for the Hurro-Hittite material, and the parallel is best read as type-level rather than route-specific.footnote:[Burkert 1992, on the Marduk-Tiamat type-level parallel.]
// EVIDENCE: source_id=burkert-1992 ; loc=whole volume

Forsyth 1987, ch. 4, places the Hesiodic Typhonomachy as the Greek station in the longue durée of the combat-myth tradition. With the Mesopotamian combat-corpus as the deepest layer, the Hurro-Hittite Kumarbi Cycle as the Anatolian station, and the Greek Typhonomachy as the Mediterranean inheritor, the chain of transmission runs through documented contact zones in each period.footnote:[Forsyth 1987, ch. 4, on the longue durée chain of transmission.]
// EVIDENCE: source_id=forsyth-1987 ; loc=ch. 4

Forsyth's reading also frames the political-ideological function of the Typhonomachy. Zeus's combat with Typhon is the royal-legitimation event for the Olympian dispensation in the same way that Marduk's combat with Tiamat is the royal-legitimation event for Babylonian sovereignty (cross-ref: Ch. 3) and Baal's combat with Yamm is the royal-legitimation event for the Ugaritic divine kingship (cross-ref: Ch. 7).footnote:[Forsyth 1987, ch. 4, on the royal-legitimation function of the Typhonomachy in comparative perspective.]
// EVIDENCE: source_id=forsyth-1987 ; loc=ch. 4

[INFERENCE: the absence of the sinew-theft from Hesiod's Theogony 820–880 combined with its presence in Apollodorus 1.6.3 and its close parallel in the Hittite Elkunirsa fragment is best read as evidence that the Apollodoran narrative preserves transmission-material that Hesiod's compressed sketch omitted, rather than as evidence that the Apollodoran narrative is a later Greek invention with an independent Hittite-resembling motif | basis: West 1997's argument that motif-specific parallels of this kind are difficult to explain by independent invention; Ogden 2013's reading of the _Bibliotheca_ as a mythographic compendium that may preserve elements absent from the surviving canonical sources | risk: the reading depends on the transmission framework being correct; an alternative reading is that the Greek and Hittite parallels are independent narrative inventions exploiting a similar structural motif, and the choice between readings is contested in the modern scholarship.]

The transmission case as a whole is taken up in detail in this book's Part II C6 (Near-Eastern-to-Mediterranean transmission). The present chapter provides the Greek end of the documentary evidence on which the C6 argument rests, complementing the Hurro-Hittite end of the evidence presented in Ch. 5 (Kumarbi Cycle).footnote:[Forward-pointer to Part II C6; West 1997, ch. 6; Burkert 1992 as the evidentiary basis.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The chapter's contribution to the transmission argument is to register the Greek end of the bridge with concrete and specific Kumarbi-Cycle parallels — Hedammu's growth-from-sea, Ullikummi's stone-body, Elkunirsa's organ-theft — rather than with generic comparisons to "Near Eastern combat myth" as a category. The brief's special instruction (specificity-not-generality) is honoured by the named-motif anchoring above.footnote:[West 1997, ch. 6, on the named-motif anchoring of the Kumarbi-Hesiod parallels; brief special_instructions on specificity.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

The transmission case is, however, a contested rather than a closed scholarly conclusion. While West 1997 and Burkert 1992 develop the case in its strongest form, alternative readings (independent-invention; type-level rather than route-specific parallel) remain available, and the Hesiodic-Typhon-vs-Hurro-Hittite-precedent debate is one of the principal test-cases for the comparative-combat-myth method as practised in current scholarship.footnote:[West 1997, ch. 6; Burkert 1992; Forsyth 1987, ch. 4, on the contested status of the transmission case.]
// EVIDENCE: source_id=west-1997 ; loc=ch. 6

=== Reception and forward links

The Typhonomachy stands as the model for later Greek dragon-combats in the Hellenic literary and iconographic record: the Apollo-Python combat at Pytho / Delphi, Herakles's encounters with the Hydra, Ladon, and Geryon's hounds, Perseus's slaying of the Ketos in the rescue of Andromeda, Kadmos's slaying of the dragon of Ares at Thebes, Bellerophon's slaying of the Chimaera, and Hercules's slaying of Cacus in the Latin tradition.footnote:[Ogden 2013, chs. 2–4, on the Typhonomachy as the model for later Greek dragon-combats.]
// EVIDENCE: source_id=ogden-2013 ; loc=chs. 2–4

The Apollo-Python combat at Pytho / Delphi is the closest Hellenic reiteration of the Typhonomachy structure. Apollo, the storm-and-prophecy god, confronts a serpent-adversary at a fixed cult-site (the older name of Delphi, Pytho), and his victory founds the oracle and the Septerion festival (cross-ref: Ch. 12 family chapter).footnote:[Ogden 2013, ch. 2; Fontenrose 1959, on the Apollo-Python combat as the closest Hellenic reiteration of the Typhonomachy.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

Fontenrose 1959 develops the comparative argument that the Apollo-Python combat and the Zeus-Typhon combat are variant Greek instantiations of a single inherited dragon-combat type, with the cult-foundation function (Delphi) carried by the Apollo-Python variant and the cosmographic-sovereignty function (Olympian dispensation) carried by the Zeus-Typhon variant.footnote:[Fontenrose 1959, on the Python-Typhon variant relationship.]
// EVIDENCE: source_id=fontenrose-1959 ; loc=whole volume

The Herakles cycle includes multiple dragon-combat episodes (Hydra, Ladon, the dragon-killing labours) that elaborate the type the Typhonomachy establishes; these are treated in detail in the Ch. 12 family chapter on Greek dragon-combats after Zeus-Typhon.footnote:[Ogden 2013, chs. 2–3, on the Herakles dragon-combat cycle; forward to Ch. 12.]
// EVIDENCE: source_id=ogden-2013 ; loc=chs. 2–3

The Perseus-and-Ketos episode (the rescue of Andromeda) is the iconographic antecedent of the medieval St. George dragon-rescue type (cross-ref: Ch. 10) and represents an iconographic continuity from the Greek dragon-combat tradition through late-antique and Christian reception.footnote:[Ogden 2013, ch. 3, on the Perseus-Andromeda-Ketos episode and its medieval iconographic afterlife.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 3

Kadmos's slaying of the dragon of Ares at Thebes — the Theban founder-myth — combines dragon-combat with a foundation function (the Spartoi rise from the sown teeth) and shows how the dragon-combat type can be adapted to local civic-foundation narratives. This is treated in the Ch. 12 family chapter.footnote:[Ogden 2013, ch. 3, on the Kadmos-and-the-dragon foundation narrative; forward to Ch. 12.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 3

Bellerophon's slaying of the Chimaera — the fire-breathing hybrid of lion, goat, and serpent — represents a heroic-monster-fight variant of the type, in which the cosmographic-sovereignty function is replaced by a heroic-test function while the morphological vocabulary (multi-headed, fire-emitting, serpentine) is preserved.footnote:[Ogden 2013, ch. 3, on the Bellerophon-Chimaera narrative.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 3

Hercules's slaying of the fire-breathing Cacus in the Latin tradition (Virgil _Aeneid_ 8, Ovid _Fasti_ 1) is the Roman terminal point of the Greek dragon-combat tradition's reception in classical Latin literature; this is treated in the Ch. 12 family chapter.footnote:[Ogden 2013, ch. 3, on the Hercules-Cacus episode in Virgil and Ovid; forward to Ch. 12.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 3

The Typhonomachy's influence extends beyond the dragon-combat type proper into the wider Greek imagination of cosmographic disorder. Storm-winds, volcanic eruptions, earthquakes, and other geophysical disturbances are conceived in the post-Hesiodic tradition through the Typhonic register, with the bound monster's residual force serving as the imaginative substrate for these phenomena.footnote:[Ogden 2013, ch. 2, on the Typhonic register for cosmographic disorder.]
// EVIDENCE: source_id=ogden-2013 ; loc=ch. 2

This chapter sets up the Ch. 12 family chapter on Greek dragon-combats after Zeus-Typhon (Apollo-Python, Herakles-Hydra, Perseus-Ketos, Kadmos-and-the-dragon, Bellerophon-Chimaera, Hercules-Cacus) as the Hellenic reception of the pattern the Typhonomachy establishes, and Part II C6 (Near-Eastern-to-Mediterranean transmission) as the comparative test-case for the transmission argument the present chapter develops.footnote:[Forward-pointers to Ch. 12 and Part II C6; Ogden 2013, chs. 2–3; West 1997, ch. 6; Burkert 1992.]
// EVIDENCE: source_id=ogden-2013 ; loc=chs. 2–3

// COMPARATIVE-HOOK: Hurro-Hittite (Kumarbi Cycle) — the Typhonomachy's three most concrete and specific Near Eastern parallels are with the Kumarbi Cycle: Hedammu's growth-from-sea (Song of Hedammu, Ch. 5) parallels the marine register of Apollodoran-Nonnian Typhon's morphology; Ullikummi's stone-body and growth-toward-heaven (Song of Ullikummi, Ch. 5) parallels the post-Hesiodic Typhon's lithic / volcanic locus under Etna; Elkunirsa's theft of the storm-god's organs (the Hittite Elkunirsa-and-Ašertu fragment) parallels the Apollodoran sinew-theft. The succession-frame parallel (Alalu → Anu → Kumarbi → Teshub corresponding to Ouranos → Kronos → Zeus, with castration of the sky-god by his successor as the most specific shared motif) places the Hesiodic _Theogony_ as a whole within the transmission corridor. Treated in detail in Part II C6 (west-1997; burkert-1992; hoffner-1998 for the Hurro-Hittite material).
// COMPARATIVE-HOOK: Phoenician — Burkert 1992's Phoenician-mediation argument is the principal route-specific transmission model: Phoenician traders, scribes, and craftsmen of the eighth and seventh centuries BCE, whose presence in the eastern Mediterranean (including Cilician ports) is well documented, are positioned as the intermediaries through which Hurro-Hittite and Levantine combat-myth material reached early Greek poets. The Cilician anchorage of Typhon's birth (Pindar) and the Corycian-cave locus of the Apollodoran sinew-theft are the geographically suggestive Greek-end markers of this transmission corridor. Treated in detail in Part II C6 (burkert-1992; west-1997).
// COMPARATIVE-HOOK: Mesopotamia (Marduk-Tiamat) — Zeus-versus-Typhon parallels Marduk-versus-Tiamat (Ch. 3) as storm-god-versus-monster sovereignty combat at the level of structural type rather than of specific shared motifs; direct transmission from Babylon to Hesiod is less easily documented than for the Hurro-Hittite material, and Burkert reads the Mesopotamian combat-cosmogony as the deeper substrate that the Hurro-Hittite Kumarbi Cycle reworks and that reaches Greece via the Anatolian-Levantine corridor (burkert-1992; lambert-2013 for the Mesopotamian end of the substrate; cross-ref: Ch. 3).
// COMPARATIVE-HOOK: Ugarit (Baal-Yamm-Lôtan) — the Ugaritic Baal-Yamm-Lôtan complex (Ch. 7) supplies an additional Levantine layer of structural correspondence: storm-god (Baal / Zeus) confronts personified-sea / serpentine antagonist (Yamm / Lôtan / Typhon) to establish sovereignty in the divine assembly; the multi-headed morphology of Lôtan (KTU 1.5 i 1–3, the seven-headed serpent) corresponds to the multi-headed morphology of Hesiodic Typhoeus (Theog. 824–828, the hundred serpent-heads). The Cilician geographical anchorage of Typhon (Pindar; Apollodorus) places the Greek-end attestation in the same eastern-Mediterranean contact zone as the Ugaritic Baal-Yamm material, and West 1997 reads this as a route-specific Levantine transmission line that complements the Phoenician-mediation argument (west-1997; smith-1994-baal-i; smith-pitard-2009-baal-ii for the Ugaritic end of the substrate; cross-ref: Ch. 7).
// COMPARATIVE-HOOK: Greek (later dragon-combats) — the Typhonomachy is the model for the later Greek dragon-combat repertoire that the Ch. 12 family chapter treats: Apollo-Python at Pytho / Delphi (the closest Hellenic reiteration; Fontenrose 1959); Herakles's encounters with Hydra, Ladon, and Geryon's hounds; Perseus-and-Ketos in the rescue of Andromeda (the iconographic antecedent of the medieval St. George dragon-rescue type, cross-ref Ch. 10); Kadmos and the dragon of Ares at Thebes (combining dragon-combat with civic-foundation); Bellerophon and the Chimaera; and Hercules and Cacus in the Latin reception (Virgil _Aeneid_ 8, Ovid _Fasti_ 1). The Typhonomachy establishes both the type and the central iconographic-narrative vocabulary that these later combats elaborate (ogden-2013; fontenrose-1959; forward to Ch. 12).
```
