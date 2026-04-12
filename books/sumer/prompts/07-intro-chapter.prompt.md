# Stage 7 of 17: intro-chapter
# Book: sumer
# Generated: 2026-04-12T15:28:02Z

---

# Governing file: scope.md

```
# Scope: Sumerian Mythology

## Culture
Sumerians (self-designation: *saĝ-gig-ga*, "black-headed people"). Southern Mesopotamian alluvial plain — the city-states of Eridu, Ur, Uruk, Nippur, Lagash, Umma, Shuruppag, Isin, Larsa, and their hinterlands. The culture that produced Sumerian-language literary compositions, preserved primarily through the scribal school (*edubba*) tradition.

## Period
ca. 2600 BCE (earliest attested literary fragments, Early Dynastic period: Abu Salabikh and Fara tablets) — ca. 1600 BCE (end of the Old Babylonian scribal copying tradition).

## Languages of primary sources
- Sumerian (Emegir, main dialect)
- Sumerian (Emesal, liturgical/feminine dialect, used in some compositions — e.g., Inanna's speeches)
- Sumerian-Akkadian bilingual tablets: only the Sumerian text is in scope.

## Excluded adjacent cultures (contamination risks)
- **Akkadian/Babylonian literary tradition**: Shares geographic space and many deities, but compositions in Akkadian are a distinct literary tradition. Excludes: Standard Babylonian *Epic of Gilgamesh* (*Sha naqba imuru*), *Enuma Elish*, *Atrahasis*, Akkadian *Descent of Ishtar*. The Sumerian Gilgamesh poems, Inanna's Descent, and the Eridu Flood Story are separate compositions and remain in scope.
- **Elamite literary tradition**: Eastern neighbor (southwestern Iran). Elamite mythological texts, even when featuring shared deities or motifs, are a separate corpus in a separate language. Aratta narratives are in scope (Sumerian compositions *about* a distant land, not Elamite texts).
- **Hurrian/Hittite literary tradition**: Northern Mesopotamia and Anatolia. The Hurrian *Song of Kumarbi* and Hittite mythological cycles draw on Mesopotamian themes but are distinct traditions in distinct languages. Excluded even when they retell recognizably Sumerian-origin stories.
- **Neo-Assyrian and later recensions**: First-millennium library copies (e.g., Ashurbanipal's Nineveh library) often rework earlier material. Excluded unless a Sumerian original is independently attested from OB or earlier tablets. The Adapa narrative (ETCSL 1.8.3.1) is excluded — it survives almost exclusively in Akkadian fragments.
- **Post-OB Sumerian liturgical tradition**: After 1600 BCE, Sumerian continued as a liturgical/scholarly language, but new compositions from this period reflect Kassite and later Babylonian theological developments, not the original Sumerian literary tradition.

## Reconstruction policy
When a primary source has a physical lacuna, content may be reconstructed from:
- **Parallel recensions of the same composition** from different sites (e.g., a Nippur tablet filling a gap in a Ur tablet of the same text) — always permitted.
- **A different composition within the same thematic cycle** (e.g., using *Dumuzid's Dream* to fill a gap in *Inanna's Descent*) — permitted only when strictly necessary; the donor text must be named in the marker.
- All reconstructed material must be flagged with `[RECONSTRUCTION:]` markers that identify the donor source. Reconstructions must appear explicitly in the claims stage and in the final text — they are never silent fills.
- **Not permitted**: Akkadian-language versions of the "same" story (e.g., Akkadian *Descent of Ishtar* to fill a gap in Sumerian *Inanna's Descent*). These belong to the excluded tradition.
- In-tradition means: Sumerian language (Emegir or Emesal), attested on tablets from ca. 2600–1600 BCE, originating from the southern Mesopotamian scribal tradition.

## In-scope corpus (broad)
- ETCSL categories 1.x (narrative and mythological compositions) and 5.3.x (debate poems)
- Sumerian heroic narratives: Gilgamesh poems, Enmerkar cycle, Lugalbanda cycle
- Sumerian divine narratives: Enki cycle, Enlil cycle, Inanna/Dumuzid cycle
- Underworld/eschatological narratives: Inanna's Descent, Ningishzida's Journey, the Eridu Flood Story, The Death of Ur-Namma
- Debate poems with mythological framing: Hoe and Plough, Ewe and Grain, Winter and Summer, Bird and Fish, Copper and Silver
- Early Dynastic literary fragments (Abu Salabikh, Fara) where identifiable as precursors to OB compositions

## Out-of-scope (explicit)
- Standard Babylonian *Epic of Gilgamesh* (*Sha naqba imuru*)
- *Enuma Elish*, *Atrahasis*, Akkadian *Descent of Ishtar*
- The Adapa narrative (ETCSL 1.8.3.1 — surviving texts overwhelmingly Akkadian)
- Elamite, Hurrian, and Hittite mythological compositions
- Neo-Assyrian library recensions without independently attested Sumerian originals
- Post-1600 BCE Sumerian liturgical compositions reflecting Kassite/later theology
- Royal hymns, temple hymns, and lamentations unless they contain substantial embedded narrative (e.g., The Death of Ur-Namma is in scope for its underworld narrative)
- Administrative, legal, and epistolary texts

## Book register
Asimov-style retelling. Narrative prose in the body. Citations in AsciiDoc footnotes. Inferences, lacunae, reconstructions, and variants flagged inline with explicit markers.

## Variant presentation policy
- If one variant is clearly prevalent in the scholarly corpus: present it in the body, with minor variants in footnotes.
- If several variants are roughly co-equal: present them inline in the chapter body, introducing each with its source.
```

---

# Governing file: sources.yaml

```
registry:
  # ── Primary / Primary-translation tier ──────────────────────────────

  - id: etcsl
    source_tier: primary
    in_scope: true
    author: "Black, Jeremy; Cunningham, Graham; Flückiger-Hawker, Esther; Robson, Eleanor; Zólyomi, Gábor"
    title: "The Electronic Text Corpus of Sumerian Literature"
    year: 1998–2006
    full_citation: "Black, J.A., Cunningham, G., Flückiger-Hawker, E., Robson, E., and Zólyomi, G., The Electronic Text Corpus of Sumerian Literature (https://etcsl.orinst.ox.ac.uk/), Oxford, 1998–2006."
    short_citation: "ETCSL"
    identifier_type: stable-url
    identifier_value: "https://etcsl.orinst.ox.ac.uk/"
    access_url: "https://etcsl.orinst.ox.ac.uk/"
    notes: "Standard digital corpus of transliterated and translated Sumerian literary texts. Primary reference for composition numbers (e.g., ETCSL 1.4.1)."

  - id: black-2004
    source_tier: primary-translation
    in_scope: true
    author: "Black, Jeremy; Cunningham, Graham; Robson, Eleanor; Zólyomi, Gábor"
    title: "The Literature of Ancient Sumer"
    year: 2004
    full_citation: "Black, J.A., Cunningham, G., Robson, E., and Zólyomi, G., *The Literature of Ancient Sumer* (Oxford: Oxford University Press, 2004)."
    short_citation: "Black et al. 2004"
    identifier_type: ISBN
    identifier_value: "9780199296330"
    notes: "Most comprehensive single-volume English anthology of Sumerian literary texts."

  - id: kramer-1961
    source_tier: secondary
    in_scope: true
    author: "Kramer, Samuel Noah"
    title: "Sumerian Mythology: A Study of Spiritual and Literary Achievement in the Third Millennium B.C."
    year: 1961
    full_citation: "Kramer, S.N., *Sumerian Mythology: A Study of Spiritual and Literary Achievement in the Third Millennium B.C.*, rev. ed. (New York: Harper & Row, 1961)."
    short_citation: "Kramer 1961"
    identifier_type: ISBN
    identifier_value: "9780812210477"
    notes: "Foundational but dated. Useful for orientation; must be cross-checked against ETCSL for textual accuracy. Never cite alone for textual claims."

  - id: jacobsen-1987
    source_tier: primary-translation
    in_scope: true
    author: "Jacobsen, Thorkild"
    title: "The Harps That Once…: Sumerian Poetry in Translation"
    year: 1987
    full_citation: "Jacobsen, T., *The Harps That Once…: Sumerian Poetry in Translation* (New Haven: Yale University Press, 1987)."
    short_citation: "Jacobsen 1987"
    identifier_type: ISBN
    identifier_value: "9780300072785"
    notes: "Literary translations with extensive commentary. Standard reference for narrative interpretations."

  - id: george-2003
    source_tier: reference
    in_scope: true
    author: "George, Andrew R."
    title: "The Babylonian Gilgamesh Epic: Introduction, Critical Edition and Cuneiform Texts"
    year: 2003
    full_citation: "George, A.R., *The Babylonian Gilgamesh Epic: Introduction, Critical Edition and Cuneiform Texts*, 2 vols. (Oxford: Oxford University Press, 2003)."
    short_citation: "George 2003"
    identifier_type: ISBN
    identifier_value: "9780199278985"
    notes: "Critical for distinguishing Sumerian Gilgamesh poems from the Akkadian epic. In scope only for its treatment of the Sumerian poems."

  # ── Secondary / Reference tier ──────────────────────────────────────

  - id: cdli
    source_tier: reference
    in_scope: true
    author: "Cuneiform Digital Library Initiative"
    title: "Cuneiform Digital Library Initiative"
    year: 2000–present
    full_citation: "Cuneiform Digital Library Initiative (https://cdli.ucla.edu/)."
    short_citation: "CDLI"
    identifier_type: stable-url
    identifier_value: "https://cdli.ucla.edu/"
    access_url: "https://cdli.ucla.edu/"
    notes: "Primary database for tablet identification, P-numbers, museum numbers, and physical descriptions."

  - id: attinger-glossaire
    source_tier: reference
    in_scope: true
    author: "Attinger, Pascal"
    title: "Glossaire sumérien–français"
    year: 2021
    full_citation: "Attinger, P., *Glossaire sumérien–français* (online, updated), Bern, 2021."
    short_citation: "Attinger 2021"
    identifier_type: stable-url
    identifier_value: "http://www.iaw.unibe.ch/attinger"
    access_url: "http://www.iaw.unibe.ch/attinger"
    notes: "Standard Sumerian philological reference. Continuously updated."

  - id: civil-1994
    source_tier: secondary
    in_scope: true
    author: "Civil, Miguel"
    title: "The Farmer's Instructions: A Sumerian Agricultural Manual"
    year: 1994
    full_citation: "Civil, M., *The Farmer's Instructions: A Sumerian Agricultural Manual*, Aula Orientalis Supplementa 5 (Barcelona: Editorial AUSA, 1994)."
    short_citation: "Civil 1994"
    identifier_type: ISBN
    identifier_value: "9788486695569"
    notes: "Critical edition relevant to debate poems and agricultural compositions."

  - id: vanstiphout-2003
    source_tier: primary-translation
    in_scope: true
    author: "Vanstiphout, Herman L.J."
    title: "Epics of Sumerian Kings: The Matter of Aratta"
    year: 2003
    full_citation: "Vanstiphout, H.L.J., *Epics of Sumerian Kings: The Matter of Aratta*, Writings from the Ancient World 20 (Atlanta: Society of Biblical Literature, 2003)."
    short_citation: "Vanstiphout 2003"
    identifier_type: ISBN
    identifier_value: "9781589830837"
    notes: "Critical editions of the Enmerkar and Lugalbanda cycles."

  - id: alster-1972
    source_tier: primary-translation
    in_scope: true
    author: "Alster, Bendt"
    title: "Dumuzi's Dream: Aspects of Oral Poetry in a Sumerian Myth"
    year: 1972
    full_citation: "Alster, B., *Dumuzi's Dream: Aspects of Oral Poetry in a Sumerian Myth*, Mesopotamia 1 (Copenhagen: Akademisk Forlag, 1972)."
    short_citation: "Alster 1972"
    identifier_type: ISBN
    identifier_value: "9788750015536"
    notes: "Critical edition of the Dumuzid cycle texts."

  - id: sladek-1974
    source_tier: secondary
    in_scope: true
    author: "Sladek, William R."
    title: "Inanna's Descent to the Netherworld"
    year: 1974
    full_citation: "Sladek, W.R., *Inanna's Descent to the Netherworld* (PhD diss., Johns Hopkins University, 1974)."
    short_citation: "Sladek 1974"
    identifier_type: corpus-id
    identifier_value: "JHU-diss-1974-Sladek"
    notes: "Most detailed philological study of the Sumerian Descent text."

  - id: fluckiger-hawker-1999
    source_tier: primary-translation
    in_scope: true
    author: "Flückiger-Hawker, Esther"
    title: "Urnamma of Ur in Sumerian Literary Tradition"
    year: 1999
    full_citation: "Flückiger-Hawker, E., *Urnamma of Ur in Sumerian Literary Tradition*, Orbis Biblicus et Orientalis 166 (Fribourg: University Press / Göttingen: Vandenhoeck & Ruprecht, 1999)."
    short_citation: "Flückiger-Hawker 1999"
    identifier_type: ISBN
    identifier_value: "9783727812446"
    notes: "Critical edition relevant to The Death of Ur-Namma and royal underworld narratives."

blacklist:
  - pattern: "wikipedia.org"
    reason: "Unvetted; mixes Sumerian and Akkadian material freely."
  - pattern: "worldhistory.org"
    reason: "Popular summaries; frequent conflation of Sumerian and Babylonian traditions."
  - pattern: "ancient.eu"
    reason: "Redirects to worldhistory.org. Same conflation issues."
  - pattern: "mythopedia.com"
    reason: "No philological rigor; treats pan-Mesopotamian as a single tradition."
  - pattern: "theoi.com"
    reason: "Greco-Roman focus; Mesopotamian content is shallow and conflated."
  - pattern: "Sitchin"
    reason: "Pseudoscholarship (*The 12th Planet* and related works)."
  - pattern: "Any source citing Enuma Elish or Atrahasis as 'Sumerian'"
    reason: "Misattribution signals the source does not distinguish the traditions."
  - pattern: "Kramer 1961 cited without ETCSL cross-check"
    reason: "Readings superseded by 40+ years of collation; never cite Kramer alone for textual claims."

triangulation_databases:
  - id: ETCSL
    url: "https://etcsl.orinst.ox.ac.uk/"
    covers: "Sumerian literary texts — transliterations and translations"
  - id: CDLI
    url: "https://cdli.ucla.edu/"
    covers: "Tablet catalog — P-numbers, museum numbers, physical metadata"
  - id: ORACC
    url: "http://oracc.museum.upenn.edu/"
    covers: "Open Richly Annotated Cuneiform Corpus — multiple sub-projects with Sumerian texts"
  - id: BDTNS
    url: "http://bdtns.filol.csic.es/"
    covers: "Database of Neo-Sumerian Texts — administrative texts, useful for cross-referencing names and dates"
```

---

# Governing file: glossary.yaml

```
terms:
  # ── Deities ──────────────────────────────────────────────────────────

  - native: "Inanna"
    renderings_considered:
      - { form: "Inanna", source: "ETCSL, Black 2004, Jacobsen 1987" }
      - { form: "Innin", source: "archaic variant in some hymns" }
    chosen: "Inanna"
    rationale: "Universal in scholarship, no ambiguity."
    first_mention_gloss: "goddess of love, war, and the morning and evening star"
    never_use: ["Ishtar"]

  - native: "Enki"
    renderings_considered:
      - { form: "Enki", source: "ETCSL, Black 2004, Jacobsen 1987" }
      - { form: "Ea", source: "Akkadian equivalent" }
    chosen: "Enki"
    rationale: "Standard Sumerian form."
    first_mention_gloss: "god of wisdom, fresh water, and cunning, lord of the abzu beneath Eridu"
    never_use: ["Ea"]

  - native: "Enlil"
    renderings_considered:
      - { form: "Enlil", source: "ETCSL, Black 2004, Jacobsen 1987" }
      - { form: "Ellil", source: "variant transliteration" }
    chosen: "Enlil"
    rationale: "Standard in all major editions."
    first_mention_gloss: "king of the gods, lord of wind and command, supreme authority in Nippur"
    never_use: []

  - native: "Ninurta"
    renderings_considered:
      - { form: "Ninurta", source: "ETCSL, Black 2004" }
      - { form: "Ningirsu", source: "related but distinct deity in Lagash tradition" }
    chosen: "Ninurta"
    rationale: "Ningirsu is a separate deity; Ninurta is the standard form for these narratives."
    first_mention_gloss: "warrior god, son of Enlil, champion of the gods"
    never_use: ["Ningirsu"]

  - native: "Ereshkigal"
    renderings_considered:
      - { form: "Ereshkigal", source: "ETCSL, Black 2004" }
      - { form: "Ereškigal", source: "diacritical transliteration" }
    chosen: "Ereshkigal"
    rationale: "Anglicized without diacritics for readability."
    first_mention_gloss: "queen of the underworld, elder sister of Inanna"
    never_use: []

  - native: "Ninhursaja"
    renderings_considered:
      - { form: "Ninhursaja", source: "ETCSL" }
      - { form: "Ninhursag", source: "older anglicization (Kramer 1961)" }
      - { form: "Ninḫursaĝa", source: "full diacritical" }
    chosen: "Ninhursaja"
    rationale: "ETCSL standard form."
    first_mention_gloss: "mother goddess, lady of the mountain"
    never_use: ["Ninhursag"]

  - native: "Dumuzid"
    renderings_considered:
      - { form: "Dumuzid", source: "ETCSL, Black 2004" }
      - { form: "Tammuz", source: "Akkadian/biblical form" }
      - { form: "Dumuzi", source: "shortened form in some scholarship" }
    chosen: "Dumuzid"
    rationale: "Sumerian form for a Sumerian book; Tammuz is Akkadian."
    first_mention_gloss: "shepherd-god, consort of Inanna"
    never_use: ["Tammuz"]

  - native: "Nanna-Suen"
    renderings_considered:
      - { form: "Nanna", source: "short Sumerian form" }
      - { form: "Suen", source: "short form, basis of 'Sin'" }
      - { form: "Nanna-Suen", source: "full double name" }
    chosen: "Nanna-Suen"
    rationale: "Full form on first mention, then 'Nanna' in subsequent references."
    first_mention_gloss: "moon god, son of Enlil and Ninlil, patron of Ur"
    never_use: ["Sin"]

  - native: "Geshtinanna"
    renderings_considered:
      - { form: "Geshtinanna", source: "ETCSL, Black 2004" }
      - { form: "Geštinanna", source: "diacritical" }
    chosen: "Geshtinanna"
    rationale: "Anglicized without diacritics."
    first_mention_gloss: "goddess, sister of Dumuzid, who shares his time in the underworld"
    never_use: []

  - native: "Ningishzida"
    renderings_considered:
      - { form: "Ningishzida", source: "ETCSL" }
      - { form: "Ningišzida", source: "diacritical" }
    chosen: "Ningishzida"
    rationale: "Anglicized."
    first_mention_gloss: "god of the underworld, a judge among the dead"
    never_use: []

  - native: "Ninlil"
    renderings_considered:
      - { form: "Ninlil", source: "ETCSL, standard" }
      - { form: "Sud", source: "pre-marriage name in Enlil and Sud" }
    chosen: "Ninlil"
    rationale: "Standard name; Sud noted only in chapter 06 where the naming occurs."
    first_mention_gloss: "queen of the gods, wife of Enlil"
    never_use: []

  # ── Heroes ───────────────────────────────────────────────────────────

  - native: "Gilgamesh"
    renderings_considered:
      - { form: "Gilgamesh", source: "conventional anglicization" }
      - { form: "Bilgames", source: "Sumerian form (ETCSL)" }
    chosen: "Gilgamesh"
    rationale: "Universally recognized; note Bilgames as Sumerian form on first mention."
    first_mention_gloss: "king of Uruk, two-thirds divine hero (Sumerian: Bilgames)"
    never_use: []

  - native: "Enkidu"
    renderings_considered:
      - { form: "Enkidu", source: "ETCSL, standard" }
    chosen: "Enkidu"
    rationale: "No variation."
    first_mention_gloss: "companion and servant of Gilgamesh"
    never_use: []

  - native: "Enmerkar"
    renderings_considered:
      - { form: "Enmerkar", source: "ETCSL, standard" }
    chosen: "Enmerkar"
    rationale: "No variation."
    first_mention_gloss: "king of Uruk, rival of Aratta, credited with the invention of writing"
    never_use: []

  - native: "Lugalbanda"
    renderings_considered:
      - { form: "Lugalbanda", source: "ETCSL, standard" }
    chosen: "Lugalbanda"
    rationale: "No variation."
    first_mention_gloss: "soldier and later king of Uruk, father of Gilgamesh in tradition"
    never_use: []

  - native: "Huwawa"
    renderings_considered:
      - { form: "Huwawa", source: "Sumerian form (ETCSL)" }
      - { form: "Humbaba", source: "Akkadian form" }
    chosen: "Huwawa"
    rationale: "Sumerian form for a Sumerian book."
    first_mention_gloss: "guardian of the Cedar Forest, appointed by Enlil"
    never_use: ["Humbaba"]

  # ── Places ───────────────────────────────────────────────────────────

  - native: "Nippur"
    renderings_considered:
      - { form: "Nippur", source: "conventional anglicization" }
      - { form: "Nibru", source: "Sumerian form (ETCSL)" }
    chosen: "Nippur"
    rationale: "Universally known; note Nibru as Sumerian form on first mention."
    first_mention_gloss: "religious capital of Sumer, seat of Enlil's temple the E-kur (Sumerian: Nibru)"
    never_use: []

  - native: "Uruk"
    renderings_considered:
      - { form: "Uruk", source: "conventional anglicization" }
      - { form: "Unug", source: "Sumerian form (ETCSL)" }
    chosen: "Uruk"
    rationale: "Universally known; note Unug as Sumerian form on first mention."
    first_mention_gloss: "great walled city of southern Mesopotamia, seat of Inanna's temple the E-ana (Sumerian: Unug)"
    never_use: []

  - native: "Eridu"
    renderings_considered:
      - { form: "Eridu", source: "standard" }
    chosen: "Eridu"
    rationale: "No variation."
    first_mention_gloss: "oldest city in Sumerian tradition, seat of Enki's temple the E-abzu"
    never_use: []

  - native: "Dilmun"
    renderings_considered:
      - { form: "Dilmun", source: "standard" }
      - { form: "Tilmun", source: "variant transliteration" }
    chosen: "Dilmun"
    rationale: "Standard in scholarship."
    first_mention_gloss: "paradisal land associated with purity, trade, and immortality"
    never_use: []

  - native: "Aratta"
    renderings_considered:
      - { form: "Aratta", source: "standard" }
    chosen: "Aratta"
    rationale: "No variation."
    first_mention_gloss: "distant, fabulously wealthy city beyond the mountains, rival of Uruk"
    never_use: []

  - native: "Kish"
    renderings_considered:
      - { form: "Kish", source: "standard" }
    chosen: "Kish"
    rationale: "No variation."
    first_mention_gloss: "city in northern Sumer, seat of early kingship"
    never_use: []

  # ── Technical / Ritual Terms ─────────────────────────────────────────

  - native: "me"
    renderings_considered:
      - { form: "divine powers", source: "Kramer 1961" }
      - { form: "cosmic ordinances", source: "Jacobsen 1987" }
      - { form: "divine properties", source: "Black 2004" }
      - { form: "me (untranslated)", source: "ETCSL transliterations" }
    chosen: "me"
    rationale: "No English word captures the concept. Left untranslated and italicized, glossed on first mention."
    first_mention_gloss: "the me — the divine powers and cultural blueprints that govern civilization"
    never_use: ["cosmic ordinances"]

  - native: "kur"
    renderings_considered:
      - { form: "mountain", source: "geographic sense" }
      - { form: "netherworld", source: "underworld sense" }
      - { form: "foreign land", source: "political sense" }
      - { form: "kur (untranslated)", source: "ETCSL transliterations" }
    chosen: "kur"
    rationale: "Left untranslated and italicized. Glossed on first mention with all three senses; context makes the intended meaning clear."
    first_mention_gloss: "the kur — a word meaning mountain, netherworld, or foreign land depending on context"
    never_use: []

  - native: "abzu"
    renderings_considered:
      - { form: "underground waters", source: "descriptive" }
      - { form: "abyss", source: "false cognate with Greek abyssos" }
      - { form: "freshwater deep", source: "Jacobsen 1987" }
      - { form: "abzu (untranslated)", source: "ETCSL" }
    chosen: "abzu"
    rationale: "Left untranslated and italicized, glossed on first mention."
    first_mention_gloss: "the abzu — the underground freshwater ocean beneath Eridu, Enki's domain"
    never_use: ["abyss"]

  - native: "galla"
    renderings_considered:
      - { form: "demons", source: "generic" }
      - { form: "constables of the underworld", source: "Jacobsen 1987" }
      - { form: "underworld officers", source: "descriptive" }
      - { form: "galla demons", source: "hybrid" }
    chosen: "galla demons"
    rationale: "Retains the Sumerian term while making the category clear to readers."
    first_mention_gloss: "the galla — underworld demons who enforce the laws of the dead"
    never_use: []

  - native: "me-lam"
    renderings_considered:
      - { form: "divine radiance", source: "Black 2004" }
      - { form: "terrifying splendor", source: "Jacobsen 1987" }
      - { form: "aura", source: "popular usage" }
      - { form: "me-lam (untranslated)", source: "ETCSL transliterations" }
    chosen: "me-lam"
    rationale: "Left untranslated and italicized, like me, kur, and abzu. Glossed on first mention."
    first_mention_gloss: "the me-lam — the terrifying divine radiance that emanates from gods, monsters, and sacred objects"
    never_use: ["aura"]

  - native: "edubba"
    renderings_considered:
      - { form: "scribal school", source: "descriptive" }
      - { form: "tablet house", source: "literal translation" }
      - { form: "edubba (untranslated)", source: "ETCSL" }
    chosen: "edubba"
    rationale: "Left untranslated and italicized, glossed on first mention."
    first_mention_gloss: "the edubba — the scribal school where these texts were copied and taught"
    never_use: []

  - native: "Anzud"
    renderings_considered:
      - { form: "Anzud", source: "Sumerian form (ETCSL)" }
      - { form: "Anzu", source: "Akkadian form" }
    chosen: "Anzud"
    rationale: "Sumerian form for a Sumerian book."
    first_mention_gloss: "divine lion-headed eagle"
    never_use: ["Anzu"]

  - native: "huluppu"
    renderings_considered:
      - { form: "willow", source: "conjectural identification" }
      - { form: "poplar", source: "conjectural identification" }
      - { form: "huluppu (untranslated)", source: "ETCSL" }
    chosen: "huluppu"
    rationale: "Species identification is uncertain; left untranslated."
    first_mention_gloss: "the huluppu — a tree of uncertain species, sacred to Inanna"
    never_use: []
```

---

# Skill instructions: intro-chapter

---
name: intro-chapter
description: Produces the introductory chapter that frames the cultural relevance of every myth covered in the book. For each myth: was it central or marginal? What function did it serve? How does it resonate across cultures?
---

# intro-chapter

## For the human

This chapter is the reader's first encounter with the mythology as a living cultural system — not yet the stories themselves, but the frame that makes them intelligible. Without it, the reader goes into a retelling of, say, the Descent of Inanna without knowing whether Sumerians treated this as a central cosmological narrative or a minor literary curiosity. That context changes how the retelling lands.

The chapter answers three questions for each myth, based on scholarly evidence:

1. **How important was it?** A creation myth recited at the New Year festival is not the same as a scribal exercise preserved in one school tablet. The evidence comes from: how many copies survive, whether it was used in rituals, whether it shows up in art (cylinder seals, reliefs), whether kings invoked it, and how much scholarly attention it has received.

2. **What did it do?** Myths are not just stories — they legitimate kingship, explain rituals, encode how the world works, teach students, mark seasonal transitions. Knowing that a myth was recited at a political ceremony changes how you read it. The reader should know this before encountering the retelling.

3. **Where else does this theme appear?** A brief preview — not the full analysis, which comes in the comparative chapter at the end — of where this myth's themes show up in other cultures. This gives the reader something to watch for as they read, and prepares them for the cross-cultural discussion later.

This chapter makes factual claims about cultural significance, so it goes through the same fact-checking process as any other chapter: a different AI checks every claim against sources.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- All `briefs/*.yaml` (especially the `cultural_relevance` fields)
- `toc.yaml`
- Primary and secondary sources — pasted into the conversation or accessible via fetch

## Agent instructions

### Structure

The chapter opens with a brief overview of the culture's mythological corpus as a whole — its size, state of preservation, and the scholarly tradition around it. Then one section per myth (or per cycle, if the book groups stories into cycles), following `toc.yaml` order. A closing section synthesizes patterns: which types of myth were most important to this culture, what that reveals about its worldview, and a forward pointer to the comparative chapter.

### Per-myth section

For each myth or cycle, address three questions:

**1. Centrality in the culture**
How important was this myth? Evidence types, in order of strength:
- **Attestation volume**: how many copies survive? A myth preserved on dozens of tablets was widely copied; one preserved on a single fragment was not.
- **Ritual context**: was the myth recited, performed, or enacted in known rituals? (e.g., the Enuma Elish at the Akitu festival)
- **Iconographic record**: does the myth appear in visual art — cylinder seals, reliefs, pottery?
- **Royal appropriation**: did kings cite or invoke the myth in inscriptions?
- **Scholarly discussion**: how much attention has the myth received in the academic literature?

Classify as **central**, **significant**, or **marginal**, with explicit evidence. Do not guess — if the evidence is thin, say so.

**2. Function in the culture**
What role did the myth serve? Common functions (adapt to the culture):
- **Cosmological**: explains the origin or structure of the world.
- **Theogonic**: establishes the divine hierarchy.
- **Royal-legitimation**: grounds political authority in divine action.
- **Ritual-aetiological**: explains the origin of a rite or festival.
- **Didactic**: teaches moral or social norms (common in scribal-school contexts).
- **Eschatological**: addresses death, the afterlife, or cosmic endings.
- **Entertainment/literary**: valued primarily as narrative art.

A myth may serve multiple functions. Cite the scholarly basis for each attribution.

**3. Cross-cultural resonance (preview)**
In 2–4 sentences, note the most striking parallels in other traditions. This is a preview, not the analysis — the comparative chapter handles depth. The goal is to plant a seed: "When you read this retelling, notice X, because you will encounter something remarkably similar in Y tradition."

Cite both the in-scope source and the out-of-scope parallel. Use `// COMPARATIVE-HOOK:` comments for anything that should be expanded in the comparative chapter.

### Style

Asimov register, same as the rest of the book. The reader is intelligent and uninformed. No reverence, no mystification. Plain, clear prose that treats mythology as evidence about a culture, not as sacred text.

Same forbidden-words list as `chapter-draft`. Same glossary discipline: use `glossary.yaml` renderings, gloss on first mention.

### Citations

Same rules as `chapter-draft`: cite only sources provided in the conversation or fetched via tool use. AsciiDoc footnotes. Every claim about centrality, function, or cross-cultural resonance needs a citation.

### Markers

Same marker discipline as `chapter-draft`:
- `[INFERENCE:]` for claims about function or centrality that go beyond what sources explicitly state.
- `[LACUNA:]` if evidence for a myth's cultural role is missing due to gaps in the record.
- No `[RECONSTRUCTION:]` or `[VARIANT:]` — these apply to narrative content, not to cultural-relevance framing.

### Length

Scale to the number of myths. For a book with 8–12 chapters: 3000–6000 words. For a larger book (15+ chapters): 6000–10000 words. Do not pad.

## Output: `chapters/00-introduction.adoc`

```asciidoc
== Introduction: The Myths and Their World

<Opening — the mythology as a corpus: size, preservation, scholarly tradition.>

=== <Myth/Cycle Title>

<Centrality — evidence-based assessment.>

<Function — what role it served, with citations.>

<Cross-cultural resonance — brief preview, 2–4 sentences.>

// COMPARATIVE-HOOK: <detail for comparative chapter>

=== <Next Myth/Cycle Title>
...

=== Patterns and Worldview

<Synthesis — what the distribution of central vs marginal myths reveals about this culture. Forward pointer to comparative chapter.>
```

## Self-check before returning
1. Every centrality claim cites evidence (attestation count, ritual context, iconography, or scholarship).
2. Every function attribution cites a scholarly source. No function assigned by vibes.
3. Cross-cultural previews cite both the in-scope and out-of-scope source.
4. Glossary renderings match `glossary.yaml`. First-mention glosses present.
5. No forbidden words. No reverence. Asimov register throughout.
6. Length proportional to the number of myths — not padded, not skeletal.
7. Every marker has all required sub-fields.
8. `// COMPARATIVE-HOOK:` comments present for every cross-cultural note.

## Handoff
To `prose-factcheck`, fresh conversation, different model.

---

# Input file: toc.yaml

```
chapters:
  - number: 0
    slug: introduction
    title: "Introduction: The Literature of the Black-Headed People"
    anchor: "ch-00-introduction"
    cycle: ~

  # ── Enki Cycle ──
  - number: 1
    slug: enki-and-ninhursaja
    title: "Enki and Ninhursaja: The Paradise of Dilmun"
    anchor: "ch-01-enki-and-ninhursaja"
    cycle: enki-cycle
  - number: 2
    slug: enki-and-ninmah
    title: "Enki and Ninmah: The Creation of Humanity"
    anchor: "ch-02-enki-and-ninmah"
    cycle: enki-cycle
  - number: 3
    slug: enki-and-the-world-order
    title: "Enki and the World Order: The Decrees of Destiny"
    anchor: "ch-03-enki-and-the-world-order"
    cycle: enki-cycle
  - number: 4
    slug: enkis-journey-to-nibru
    title: "Enki's Journey to Nibru"
    anchor: "ch-04-enkis-journey-to-nibru"
    cycle: enki-cycle

  # ── Enlil Cycle ──
  - number: 5
    slug: enlil-and-ninlil
    title: "Enlil and Ninlil: Exile of the Great Mountain"
    anchor: "ch-05-enlil-and-ninlil"
    cycle: enlil-cycle
  - number: 6
    slug: enlil-and-sud
    title: "Enlil and Sud: The Courtship in Shuruppag"
    anchor: "ch-06-enlil-and-sud"
    cycle: enlil-cycle

  # ── Ninurta Cycle ──
  - number: 7
    slug: lugal-e
    title: "Ninurta's Exploits: The Battle with Asag"
    anchor: "ch-07-lugal-e"
    cycle: ninurta-cycle
  - number: 8
    slug: angim
    title: "Ninurta's Return to Nibru"
    anchor: "ch-08-angim"
    cycle: ninurta-cycle
  - number: 9
    slug: ninurta-and-the-turtle
    title: "Ninurta and the Turtle: Enki's Trick"
    anchor: "ch-09-ninurta-and-the-turtle"
    cycle: ninurta-cycle

  # ── Inanna Cycle ──
  - number: 10
    slug: inanna-and-enki
    title: "Inanna and Enki: The Theft of the ME"
    anchor: "ch-10-inanna-and-enki"
    cycle: inanna-cycle
  - number: 11
    slug: inanna-and-ebih
    title: "Inanna and Ebih: The Destruction of the Mountain"
    anchor: "ch-11-inanna-and-ebih"
    cycle: inanna-cycle
  - number: 12
    slug: inanna-and-shu-kale-tuda
    title: "Inanna and Shu-kale-tuda: The Gardener's Crime"
    anchor: "ch-12-inanna-and-shu-kale-tuda"
    cycle: inanna-cycle
  - number: 13
    slug: inanna-and-gudam
    title: "Inanna and Gudam"
    anchor: "ch-13-inanna-and-gudam"
    cycle: inanna-cycle

  # ── Inanna and Dumuzid Cycle ──
  - number: 14
    slug: inannas-descent
    title: "Inanna's Descent to the Nether World"
    anchor: "ch-14-inannas-descent"
    cycle: inanna-dumuzid-cycle
  - number: 15
    slug: dumuzids-dream
    title: "Dumuzid's Dream"
    anchor: "ch-15-dumuzids-dream"
    cycle: inanna-dumuzid-cycle
  - number: 16
    slug: inanna-and-bilulu
    title: "Inanna and Bilulu: Vengeance for the Shepherd"
    anchor: "ch-16-inanna-and-bilulu"
    cycle: inanna-dumuzid-cycle

  # ── Nanna/Suen Cycle ──
  - number: 17
    slug: nannas-journey-to-nibru
    title: "Nanna-Suen's Journey to Nibru"
    anchor: "ch-17-nannas-journey-to-nibru"
    cycle: nanna-cycle

  # ── Other Divine Narratives ──
  - number: 18
    slug: marriage-of-martu
    title: "The Marriage of Martu"
    anchor: "ch-18-marriage-of-martu"
    cycle: other-divine-narratives

  # ── Sumerian Gilgamesh Poems ──
  - number: 19
    slug: gilgamesh-and-aga
    title: "Gilgamesh and Aga: The Siege of Uruk"
    anchor: "ch-19-gilgamesh-and-aga"
    cycle: gilgamesh-poems
  - number: 20
    slug: gilgamesh-and-the-bull-of-heaven
    title: "Gilgamesh and the Bull of Heaven"
    anchor: "ch-20-gilgamesh-and-the-bull-of-heaven"
    cycle: gilgamesh-poems
  - number: 21
    slug: gilgamesh-and-huwawa
    title: "Gilgamesh and Huwawa: The Cedar Forest"
    anchor: "ch-21-gilgamesh-and-huwawa"
    cycle: gilgamesh-poems
  - number: 22
    slug: gilgamesh-enkidu-and-the-nether-world
    title: "Gilgamesh, Enkidu, and the Nether World"
    anchor: "ch-22-gilgamesh-enkidu-and-the-nether-world"
    cycle: gilgamesh-poems
  - number: 23
    slug: death-of-gilgamesh
    title: "The Death of Gilgamesh"
    anchor: "ch-23-death-of-gilgamesh"
    cycle: gilgamesh-poems

  # ── Enmerkar and Lugalbanda Cycle ──
  - number: 24
    slug: enmerkar-and-the-lord-of-aratta
    title: "Enmerkar and the Lord of Aratta"
    anchor: "ch-24-enmerkar-and-the-lord-of-aratta"
    cycle: enmerkar-lugalbanda-cycle
  - number: 25
    slug: enmerkar-and-en-suhgir-ana
    title: "Enmerkar and En-suhgir-ana: The Sorcery Contest"
    anchor: "ch-25-enmerkar-and-en-suhgir-ana"
    cycle: enmerkar-lugalbanda-cycle
  - number: 26
    slug: lugalbanda-in-the-mountain-cave
    title: "Lugalbanda in the Mountain Cave"
    anchor: "ch-26-lugalbanda-in-the-mountain-cave"
    cycle: enmerkar-lugalbanda-cycle
  - number: 27
    slug: lugalbanda-and-the-anzud-bird
    title: "Lugalbanda and the Anzud Bird"
    anchor: "ch-27-lugalbanda-and-the-anzud-bird"
    cycle: enmerkar-lugalbanda-cycle

  # ── Underworld and Eschatological Narratives ──
  - number: 28
    slug: eridu-flood-story
    title: "The Flood Story: The Eridu Genesis"
    anchor: "ch-28-eridu-flood-story"
    cycle: underworld-eschatology
  - number: 29
    slug: ningishzidas-journey
    title: "Ningishzida's Journey to the Nether World"
    anchor: "ch-29-ningishzidas-journey"
    cycle: underworld-eschatology
  - number: 30
    slug: death-of-ur-namma
    title: "The Death of Ur-Namma"
    anchor: "ch-30-death-of-ur-namma"
    cycle: underworld-eschatology

  # ── Debate Poems ──
  - number: 31
    slug: debate-hoe-and-plough
    title: "The Debate between Hoe and Plough"
    anchor: "ch-31-debate-hoe-and-plough"
    cycle: debate-poems
  - number: 32
    slug: debate-ewe-and-grain
    title: "The Debate between Ewe and Grain"
    anchor: "ch-32-debate-ewe-and-grain"
    cycle: debate-poems
  - number: 33
    slug: debate-winter-and-summer
    title: "The Debate between Winter and Summer"
    anchor: "ch-33-debate-winter-and-summer"
    cycle: debate-poems
  - number: 34
    slug: debate-bird-and-fish
    title: "The Debate between Bird and Fish"
    anchor: "ch-34-debate-bird-and-fish"
    cycle: debate-poems
  - number: 35
    slug: debate-copper-and-silver
    title: "The Debate between Copper and Silver"
    anchor: "ch-35-debate-copper-and-silver"
    cycle: debate-poems
  - number: 36
    slug: debate-date-palm-and-tamarisk
    title: "The Debate between Date Palm and Tamarisk"
    anchor: "ch-36-debate-date-palm-and-tamarisk"
    cycle: debate-poems
```

---

# Input file: briefs/01-enki-and-ninhursaja.yaml

```
chapter_number: 1
slug: "enki-and-ninhursaja"
title: "Enki and Ninhursaja: The Paradise of Dilmun"
chapter_anchor: "ch-01-enki-and-ninhursaja"

sources:
  primary:
    - id: etcsl
      loc: "1.1.1, composite text, lines 1–278"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.1.1"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.1.1"
    - id: black-2004
      loc: "pp. 38–50"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
    - id: jacobsen-1987
      loc: "pp. 181–204"
      translator_edition: "Jacobsen 1987"
      identifier: "ISBN 9780300072785"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 54–59 (Dilmun and paradise motif)" }

lacunae:
  - source: etcsl
    location: "lines 1–13 (Nippur manuscripts)"
    what_is_missing: "Opening invocation partially damaged; initial description of Dilmun's pristine state fragmentary"
    in_tradition_fills_available: "yes, Ur manuscripts preserve portions of the opening"
  - source: etcsl
    location: "lines 64–78 (Nippur manuscripts)"
    what_is_missing: "Transition between water-provision and first plant-eating episode partially broken"
    in_tradition_fills_available: "partial, Ur manuscripts overlap but diverge in the tribute section"

variants:
  classification: co-equal
  prevalent_version:
    source: etcsl
    why_prevalent: "ETCSL composite draws on both Nippur and Ur manuscripts but follows the Nippur recension as base"
  alternates:
    - source: jacobsen-1987
      difference: "Ur manuscripts include an extended tribute passage (Dilmun trade goods) absent from Nippur recension"

entities_glossary:
  - name: "Enki (𒂗𒆠)"
    role: deity
    first_mention_gloss_candidate: "god of wisdom, freshwater, and cunning, lord of the abzu"
  - name: "Ninhursaja (𒊩𒌆𒄯𒊕)"
    role: deity
    first_mention_gloss_candidate: "great mother goddess of the stony ground, also called Nintur"
  - name: "Dilmun (𒉌𒌇)"
    role: place
    first_mention_gloss_candidate: "paradise land east of Sumer, identified with modern Bahrain"
  - name: "abzu (𒍪𒀊)"
    role: place
    first_mention_gloss_candidate: "subterranean freshwater ocean beneath the earth, Enki's domain"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Multiple Old Babylonian copies from Nippur and Ur scribal schools attest wide circulation"
      source: "etcsl 1.1.1, manuscript list"
    - kind: scholarly-attention
      detail: "Jacobsen and Kramer both devote sustained analyses to the text's paradise motif and botanical imagery"
      source: "jacobsen-1987 pp. 181–204"
  function:
    - role: cosmological
      basis: "Establishes Dilmun as a primordial pure land where sun and freshwater are granted by divine decree"
      source: "etcsl 1.1.1, lines 1–30"
    - role: ritual-aetiological
      basis: "Explains the origin of healing deities through Ninhursaja's curing of Enki's eight ailments"
      source: "etcsl 1.1.1, lines 230–278"
  cross_cultural_parallels:
    - other_culture: "Hebrew Bible"
      parallel: "Eden/paradise garden with forbidden fruit, expulsion, and divine curse echoes the Dilmun paradise with forbidden plants and Enki's curse"
      source: "kramer-1961"
    - other_culture: "Greek (Hesiod)"
      parallel: "Golden age of effortless plenty and divine proximity parallels Dilmun's initial state of no sickness, no old age"
      source: "jacobsen-1987"

comparative_hooks:
  - other_culture: "Hebrew Bible"
    parallel: "Paradise garden, forbidden consumption, divine curse and healing"
    source: "kramer-1961"
  - other_culture: "Greek (Hesiod)"
    parallel: "Golden age myth of primordial perfection and divine proximity"
    source: "jacobsen-1987"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 3000

special_instructions: "Treat Nippur and Ur versions as co-equal witnesses. Present the tribute insertion from the Ur manuscripts in a clearly marked inset rather than merging silently into the Nippur base text. Flag the Dilmun–Eden parallel but do not overstate direct borrowing."
```

---

# Input file: briefs/02-enki-and-ninmah.yaml

```
chapter_number: 2
slug: "enki-and-ninmah"
title: "Enki and Ninmah: The Creation of Humanity"
chapter_anchor: "ch-02-enki-and-ninmah"

sources:
  primary:
    - id: etcsl
      loc: "1.1.2, composite text, lines 1–139"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.1.2"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.1.2"
    - id: black-2004
      loc: "pp. 30–37"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
    - id: kramer-1961
      loc: "pp. 68–72"
      translator_edition: "Kramer 1961"
      identifier: "ISBN 9780812210477"
      url_or_file: ~
  secondary:
    - { id: jacobsen-1987, loc: "pp. 151–166 (discussion of creation motifs)" }

lacunae:
  - source: etcsl
    location: "lines 1–6"
    what_is_missing: "Opening lines fragmentary; divine setting before the creation contest partially lost"
    in_tradition_fills_available: "no, only Nippur manuscripts known"
  - source: etcsl
    location: "lines 68–76"
    what_is_missing: "Approximately nine lines damaged in the middle of the impaired-humans sequence"
    in_tradition_fills_available: "no, no parallel witnesses fill this gap"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "Only Nippur Old Babylonian copies are attested; ETCSL composite is the sole reconstructable version"
  alternates:
    - source: kramer-1961
      difference: "Kramer's earlier translation differs in the reading of several creation verbs, now superseded by ETCSL collations"

entities_glossary:
  - name: "Enki (𒂗𒆠)"
    role: deity
    first_mention_gloss_candidate: "god of wisdom and freshwater who devises humanity's creation from clay"
  - name: "Ninmah (𒊩𒌆𒈤)"
    role: deity
    first_mention_gloss_candidate: "great mother goddess who shapes humans from clay over the abzu"
  - name: "Umul"
    role: hero
    first_mention_gloss_candidate: "Enki's helpless creation, a being unable to function, fashioned to stump Ninmah"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: scholarly-attention
      detail: "Foundational creation narrative widely discussed in every major survey of Sumerian literature"
      source: "kramer-1961 pp. 68–72"
    - kind: attestation-volume
      detail: "Multiple OB Nippur copies indicate its place in the scribal curriculum"
      source: "etcsl 1.1.2, manuscript list"
  function:
    - role: theogonic
      basis: "Explains how the gods decided to create humanity to relieve their labour burden"
      source: "etcsl 1.1.2, lines 1–20"
    - role: cosmological
      basis: "Establishes the divine origin of human physical diversity and social roles through the contest"
      source: "etcsl 1.1.2, lines 30–120"
  cross_cultural_parallels:
    - other_culture: "Greek"
      parallel: "Prometheus shaping humans from clay and divine contest over human destiny parallels the Enki-Ninmah competition"
      source: "kramer-1961"
    - other_culture: "Vedic (Rig Veda)"
      parallel: "Divine crafting of beings from primordial substance echoes the Purusha Sukta's cosmic sacrifice and creation"
      source: "jacobsen-1987"

comparative_hooks:
  - other_culture: "Greek"
    parallel: "Clay creation of humans and divine contest over human form (Prometheus tradition)"
    source: "kramer-1961"
  - other_culture: "Vedic (Rig Veda)"
    parallel: "Divine crafting from primordial substance"
    source: "jacobsen-1987"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2500

special_instructions: "Emphasise the social-integration theme: each impaired human is given a role in society. Distinguish clearly from the Akkadian Atrahasis creation account, which is a separate tradition. Mark the ~15-line lacunae without speculative reconstruction."
```

---

# Input file: briefs/03-enki-and-the-world-order.yaml

```
chapter_number: 3
slug: "enki-and-the-world-order"
title: "Enki and the World Order: The Decrees of Destiny"
chapter_anchor: "ch-03-enki-and-the-world-order"

sources:
  primary:
    - id: etcsl
      loc: "1.1.3, composite text, lines 1–473"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.1.3"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.1.3"
    - id: black-2004
      loc: "pp. 215–225"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
    - id: kramer-1961
      loc: "pp. 59–62"
      translator_edition: "Kramer 1961"
      identifier: "ISBN 9780812210477"
      url_or_file: ~
  secondary:
    - { id: jacobsen-1987, loc: "pp. 151–166 (cosmic ordering and divine delegation)" }

lacunae:
  - source: etcsl
    location: "lines 141–147"
    what_is_missing: "Gap in the blessing of Meluhha; details of trade goods and divine favour partially lost"
    in_tradition_fills_available: "no, no duplicate manuscripts fill this passage"
  - source: etcsl
    location: "lines 318–324"
    what_is_missing: "Transition passage between appointment of river deities and marsh deities damaged"
    in_tradition_fills_available: "no, single composite tradition"
  - source: etcsl
    location: "scattered gaps of 3–7 lines throughout"
    what_is_missing: "Minor damage throughout the tablets; individual deity-appointment passages occasionally incomplete"
    in_tradition_fills_available: "no, no parallel witnesses"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "Single composite text reconstructed from OB Nippur manuscripts; no competing recension known"
  alternates:
    - source: kramer-1961
      difference: "Kramer's earlier reading of Inanna's complaint section differs in emphasis; ETCSL collations provide the current standard"

entities_glossary:
  - name: "Enki (𒂗𒆠)"
    role: deity
    first_mention_gloss_candidate: "god of wisdom who organises the cosmos by decreeing destinies and assigning divine offices"
  - name: "Inanna (𒈹)"
    role: deity
    first_mention_gloss_candidate: "goddess of love and war who protests that Enki has given her no clear domain"
  - name: "ME (𒈨)"
    role: ritual-term
    first_mention_gloss_candidate: "divine powers or cultural blueprints that govern civilisation's arts and institutions"
  - name: "Tigris (Idigna)"
    role: place
    first_mention_gloss_candidate: "great river of Mesopotamia, filled with life-giving water by Enki's decree"
  - name: "Euphrates (Buranuna)"
    role: place
    first_mention_gloss_candidate: "great river of Mesopotamia, paired with the Tigris in Enki's ordering of the land"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: scholarly-attention
      detail: "Reveals the Sumerian conception of cosmic bureaucracy more fully than any other single text"
      source: "black-2004 pp. 215–225"
    - kind: attestation-volume
      detail: "Long composition (~470 lines) with multiple OB manuscript witnesses from Nippur"
      source: "etcsl 1.1.3, manuscript list"
    - kind: ritual-context
      detail: "The ME assignments mirror temple-administrative hierarchies attested in royal inscriptions"
      source: "kramer-1961 pp. 59–62"
  function:
    - role: cosmological
      basis: "Systematically maps the entire known world—lands, rivers, crafts, agriculture—under divine jurisdiction"
      source: "etcsl 1.1.3, lines 50–400"
    - role: theogonic
      basis: "Defines the portfolios of major deities as delegated by Enki, structuring the divine hierarchy"
      source: "etcsl 1.1.3, lines 250–470"
  cross_cultural_parallels:
    - other_culture: "Greek"
      parallel: "Division of cosmic domains among Zeus, Poseidon, and Hades parallels Enki's systematic assignment of divine offices"
      source: "kramer-1961"
    - other_culture: "Egyptian"
      parallel: "The Ennead's structured assignment of divine roles (Shu, Tefnut, Geb, Nut) echoes Enki's hierarchical delegation"
      source: "jacobsen-1987"

comparative_hooks:
  - other_culture: "Greek"
    parallel: "Division of divine domains among Olympians after the Titanomachy"
    source: "kramer-1961"
  - other_culture: "Egyptian"
    parallel: "Ennead role assignments and cosmic ordering at creation"
    source: "jacobsen-1987"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 4000

special_instructions: "This is the longest chapter brief. Preserve the encyclopaedic sweep of the original: do not collapse the land-by-land and craft-by-craft sections. Give Inanna's complaint at the close its full weight as it sets up later Inanna-cycle chapters. Clearly distinguish the ME concept from Akkadian parsu."
```

---

# Input file: briefs/04-enkis-journey-to-nibru.yaml

```
chapter_number: 4
slug: "enkis-journey-to-nibru"
title: "Enki's Journey to Nibru"
chapter_anchor: "ch-04-enkis-journey-to-nibru"

sources:
  primary:
    - id: etcsl
      loc: "1.1.4, composite text"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.1.4"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.1.4"
  secondary:
    - { id: black-2004, loc: "pp. 330–333 (summary and context)" }
    - { id: kramer-1961, loc: "pp. 62–64 (Enki and Eridu)" }

lacunae:
  - source: etcsl
    location: "lines 1–8"
    what_is_missing: "Opening lines describing Enki's temple construction partially damaged"
    in_tradition_fills_available: "no, limited manuscript witnesses"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Standard OB curriculum text with well-preserved fragments; no competing recension"
  alternates:
    - source: kramer-1961
      difference: "Kramer's paraphrase differs in minor details of the journey itinerary, superseded by ETCSL readings"

entities_glossary:
  - name: "Enki (𒂗𒆠)"
    role: deity
    first_mention_gloss_candidate: "god of wisdom and freshwater who builds his temple in Eridu and journeys to Nippur"
  - name: "Enlil (𒂗𒇸)"
    role: deity
    first_mention_gloss_candidate: "king of the gods, supreme authority in Nippur whose blessing Enki seeks"
  - name: "Eridu (𒉣𒆠)"
    role: place
    first_mention_gloss_candidate: "Enki's cult city in the deep south of Sumer, oldest city in Mesopotamian tradition"
  - name: "Nibru / Nippur (𒂗𒆤𒆠)"
    role: place
    first_mention_gloss_candidate: "religious capital of Sumer, seat of Enlil and the divine assembly"
  - name: "E-abzu"
    role: place
    first_mention_gloss_candidate: "Enki's temple in Eridu, 'House of the Abzu'"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Attested as a standard OB curriculum text, indicating wide scribal familiarity"
      source: "etcsl 1.1.4, manuscript list"
    - kind: royal-inscription
      detail: "The Eridu temple-building motif resonates with royal inscriptions legitimating temple construction"
      source: "cdli (Eridu-related royal inscriptions)"
  function:
    - role: ritual-aetiological
      basis: "Provides the mythological foundation for the E-abzu temple at Eridu and its ritual importance"
      source: "etcsl 1.1.4, opening sections"
    - role: royal-legitimation
      basis: "The barge journey and Enlil's blessing model the pattern of southern rulers seeking Nippur's sanction"
      source: "kramer-1961 pp. 62–64"
  cross_cultural_parallels:
    - other_culture: "Ugaritic"
      parallel: "Divine temple-building in the Baal Cycle, where Baal constructs his palace and seeks El's permission, mirrors Enki's journey for Enlil's blessing"
      source: "black-2004"

comparative_hooks:
  - other_culture: "Ugaritic"
    parallel: "Divine temple-building and seeking the supreme god's blessing (Baal Cycle)"
    source: "black-2004"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 1500

special_instructions: "Short chapter. Emphasise the political geography: the Eridu-to-Nippur axis as a model of southern-city-seeks-central-authority. Note the barge journey as a ritual procession prototype."
```

---

# Input file: briefs/05-enlil-and-ninlil.yaml

```
chapter_number: 5
slug: "enlil-and-ninlil"
title: "Enlil and Ninlil: Exile of the Great Mountain"
chapter_anchor: "ch-05-enlil-and-ninlil"

sources:
  primary:
    - id: etcsl
      loc: "1.2.1, composite text, lines 1–152"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.2.1"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.2.1"
    - id: black-2004
      loc: "pp. 100–107"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
    - id: jacobsen-1987
      loc: "pp. 167–180"
      translator_edition: "Jacobsen 1987"
      identifier: "ISBN 9780300072785"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 43–47 (Enlil and Ninlil summary)" }

lacunae:
  - source: etcsl
    location: "lines 77–85"
    what_is_missing: "Portions of the pursuit sequence damaged; Enlil's second disguise encounter partially broken"
    in_tradition_fills_available: "partial, minor overlapping fragments help but gaps remain"
  - source: etcsl
    location: "lines 118–123"
    what_is_missing: "Transition to the third chthonic deity birth partially lost"
    in_tradition_fills_available: "no, no complete parallel fills this gap"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Heavily attested curriculum text from Nippur; minor word-level variants across fragments do not constitute a separate recension"
  alternates:
    - source: jacobsen-1987
      difference: "Jacobsen interprets Enlil's acts as a progressive mythological descent rather than repeated seduction; translation choices reflect this reading"

entities_glossary:
  - name: "Enlil (𒂗𒇸)"
    role: deity
    first_mention_gloss_candidate: "king of the gods, called 'Great Mountain,' ruler of Nippur and head of the divine assembly"
  - name: "Ninlil (𒊩𒌆𒇸)"
    role: deity
    first_mention_gloss_candidate: "queen of the gods, young grain goddess who follows Enlil into exile"
  - name: "Nanna / Suen (𒀭𒋀𒆠)"
    role: deity
    first_mention_gloss_candidate: "moon god, firstborn of Enlil and Ninlil, destined for heaven rather than the underworld"
  - name: "Nibru / Nippur (𒂗𒆤𒆠)"
    role: place
    first_mention_gloss_candidate: "religious capital of Sumer where the divine assembly convenes and banishes Enlil"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: attestation-volume
      detail: "One of the most heavily attested Sumerian narrative compositions, with numerous OB Nippur copies"
      source: "etcsl 1.2.1, manuscript list"
    - kind: scholarly-attention
      detail: "Extensively studied by Jacobsen, Kramer, and subsequent Sumerologists for its theogonic and ethical dimensions"
      source: "jacobsen-1987 pp. 167–180"
    - kind: ritual-context
      detail: "The birth of Nanna connects to the lunar cult cycle central to Ur III and OB Nippur religion"
      source: "black-2004 pp. 100–107"
  function:
    - role: theogonic
      basis: "Explains the birth of the moon god Nanna and three chthonic deities who serve as his underworld substitutes"
      source: "etcsl 1.2.1, lines 100–152"
    - role: cosmological
      basis: "Maps the vertical cosmos: Enlil's descent from Nippur toward the underworld generates deities for each cosmic level"
      source: "jacobsen-1987 pp. 167–180"
  cross_cultural_parallels:
    - other_culture: "Greek"
      parallel: "Divine exile and punishment by a divine assembly echoes Zeus's overthrow of Kronos and the Titanomachy exile sequences"
      source: "jacobsen-1987"
    - other_culture: "Hindu"
      parallel: "Divine transformation and disguise during pursuit parallels Shiva's forms and appearances in Puranic narratives"
      source: "black-2004"

comparative_hooks:
  - other_culture: "Greek"
    parallel: "Divine exile by assembly decree and generative consequences (Kronos/Zeus cycle)"
    source: "jacobsen-1987"
  - other_culture: "Hindu"
    parallel: "God in disguise during amorous pursuit; transformation births"
    source: "black-2004"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 3000

special_instructions: "Handle the sexual-violence dimension with scholarly precision: the divine assembly's judgement frames the act as transgressive within the narrative's own ethics. Do not euphemise, but contextualise within Sumerian literary convention. Highlight the substitution logic (three underworld gods born so Nanna can ascend) as the narrative's theological core."
```

---

# Input file: briefs/06-enlil-and-sud.yaml

```
chapter_number: 6
slug: "enlil-and-sud"
title: "Enlil and Sud: The Courtship in Shuruppag"
chapter_anchor: "ch-06-enlil-and-sud"

sources:
  primary:
    - id: etcsl
      loc: "1.2.2, composite text, lines 1–170"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.2.2"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.2.2"
    - id: black-2004
      loc: "pp. 108–115"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 43–47 (Enlil marriage traditions)" }
    - { id: jacobsen-1987, loc: "pp. 167–168 (context of Enlil's marriages)" }

lacunae:
  - source: etcsl
    location: "lines 55–62"
    what_is_missing: "Portion of the bridal negotiation dialogue between Enlil's envoy and Nisaba partially damaged"
    in_tradition_fills_available: "no, single manuscript tradition"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Well-preserved OB composition with no competing recension; minor scribal variants only"
  alternates:
    - source: black-2004
      difference: "Black et al. restore a few damaged signs differently from ETCSL default readings, but differences are minor"

entities_glossary:
  - name: "Enlil (𒂗𒇸)"
    role: deity
    first_mention_gloss_candidate: "king of the gods who undertakes a formal courtship journey to Shuruppag"
  - name: "Sud / Ninlil (𒊩𒌆𒇸)"
    role: deity
    first_mention_gloss_candidate: "young goddess of Shuruppag, renamed Ninlil upon her marriage to Enlil"
  - name: "Nisaba (𒀭𒊺𒉀)"
    role: deity
    first_mention_gloss_candidate: "goddess of grain and writing, mother of Sud, who negotiates the marriage terms"
  - name: "Shuruppag (𒋢𒆳𒊒𒂡𒆠)"
    role: place
    first_mention_gloss_candidate: "ancient Sumerian city, home of Sud and her mother Nisaba"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: ritual-context
      detail: "The courtship protocol mirrors attested Sumerian marriage customs including bridal gifts, envoy negotiations, and formal renaming"
      source: "black-2004 pp. 108–115"
    - kind: scholarly-attention
      detail: "Studied as a primary source for reconstructing OB marriage ritual and gender norms in divine narrative"
      source: "etcsl 1.2.2, commentary"
  function:
    - role: theogonic
      basis: "Explains how Sud became Ninlil, queen of the gods, establishing her divine status through marriage"
      source: "etcsl 1.2.2, lines 140–170"
    - role: ritual-aetiological
      basis: "Models the ideal divine marriage protocol that earthly ceremonies reflect, including bride-price and naming ceremony"
      source: "black-2004 pp. 108–115"
  cross_cultural_parallels:
    - other_culture: "Hindu"
      parallel: "Shiva's courtship of Parvati through formal negotiation with her family parallels Enlil's structured approach through envoys to Nisaba"
      source: "jacobsen-1987"
    - other_culture: "Cross-cultural (Ancient Near East)"
      parallel: "Bride-price customs attested across Mesopotamian, Hittite, and biblical traditions echo the detailed gift exchanges in Enlil's courtship"
      source: "black-2004"

comparative_hooks:
  - other_culture: "Hindu"
    parallel: "Formal divine courtship with family negotiation (Shiva-Parvati cycle)"
    source: "jacobsen-1987"
  - other_culture: "Ancient Near East broadly"
    parallel: "Bride-price and marriage-negotiation customs across Mesopotamian and biblical traditions"
    source: "black-2004"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2500

special_instructions: "Contrast explicitly with the preceding chapter (Enlil and Ninlil): this text presents the orderly, sanctioned courtship that chapter 5's transgressive encounter inverts. Highlight the renaming of Sud to Ninlil as a theological act, not merely a name change. Note the role of Nisaba as both mother and literate goddess."
```

---

# Input file: briefs/07-lugal-e.yaml

```
chapter_number: 7
slug: "lugal-e"
title: "Ninurta's Exploits: The Battle with Asag"
chapter_anchor: "ch-07-lugal-e"

sources:
  primary:
    - id: etcsl
      loc: "1.6.2, composite text, lines 1–729"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.6.2"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.6.2"
    - id: black-2004
      loc: "pp. 163–191"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
    - id: jacobsen-1987
      loc: "pp. 233–272"
      translator_edition: "Jacobsen 1987"
      identifier: "ISBN 9780300072785"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 80–83 (Ninurta myths overview)" }

lacunae:
  - source: etcsl
    location: "lines 1–20"
    what_is_missing: "Opening lines partially damaged in several witnesses; invocation and initial battle context fragmentary"
    in_tradition_fills_available: "yes, composite reconstruction from multiple OB manuscripts restores most of the opening"
  - source: etcsl
    location: "lines 330–370"
    what_is_missing: "Portions of the stone-fate assignment section damaged, with gaps in the individual verdicts for some stones"
    in_tradition_fills_available: "partial, overlapping manuscripts cover different subsections but no single witness is complete"
  - source: etcsl
    location: "lines 680–729"
    what_is_missing: "Closing hymnic section has minor gaps in the praise formula and the mother-renaming passage"
    in_tradition_fills_available: "yes, multiple manuscripts preserve the ending with minor variation"

variants:
  classification: composite-editorial
  prevalent_version:
    source: etcsl
    why_prevalent: "Standard composite text assembled from numerous OB manuscripts with wide attestation"
  alternates:
    - source: jacobsen-1987
      difference: "Jacobsen's literary translation smooths over gaps and occasionally follows different manuscript readings in the stone-fate section"

entities_glossary:
  - name: "Ninurta (𒀭𒊩𒌆𒅁)"
    role: deity
    first_mention_gloss_candidate: "warrior god, champion of the gods, son of Enlil"
  - name: "Asag (𒀀𒊻𒀝)"
    role: deity
    first_mention_gloss_candidate: "monstrous demon of sickness born of An and Ki, who raised a stone army against the gods"
  - name: "Ninhursaja (𒊩𒌆𒄯𒊕)"
    role: deity
    first_mention_gloss_candidate: "great mother goddess, originally called Ninmah, renamed by Ninurta after his victory"
  - name: "šar-ur (𒊬𒌨)"
    role: artifact
    first_mention_gloss_candidate: "Ninurta's sentient mace and battlefield counselor, literally 'smiter of thousands'"
  - name: "kur (𒆳)"
    role: place
    first_mention_gloss_candidate: "the mountain, foreign land, or netherworld — the hostile territory where Ninurta battles Asag"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: attestation-volume
      detail: "One of the longest and most copied Sumerian literary compositions, attested in numerous OB manuscripts from Nippur and elsewhere"
      source: "etcsl 1.6.2, manuscript list"
    - kind: scholarly-attention
      detail: "Jacobsen devotes forty pages to the text and its cosmological implications; standard reference in all surveys of Sumerian literature"
      source: "jacobsen-1987 pp. 233–272"
    - kind: ritual-context
      detail: "The stone-fate assignments suggest connection to mineralogical lore and temple-building ritual knowledge"
      source: "black-2004 pp. 163–164 (introduction)"
  function:
    - role: cosmological
      basis: "Ninurta's damming of the primeval waters and reorganization of the landscape explains the creation of the Tigris river system and the fertile plains"
      source: "etcsl 1.6.2, lines 400–460"
    - role: theogonic
      basis: "Ninurta's mother Ninmah is elevated and renamed Ninhursaja, establishing a new divine identity and the 'Lady of the Mountain' epithet"
      source: "etcsl 1.6.2, lines 690–729"
  cross_cultural_parallels:
    - other_culture: "Babylonian (Enuma Elish)"
      parallel: "Chaoskampf pattern: a young warrior god defeats a primordial chaos being to organize the cosmos, closely paralleled by Marduk vs. Tiamat"
      source: "jacobsen-1987"
    - other_culture: "Greek"
      parallel: "Zeus vs. Typhon — storm god battles a monstrous chthonic adversary to secure divine sovereignty"
      source: "kramer-1961"
    - other_culture: "Vedic"
      parallel: "Indra vs. Vrtra — warrior god slays a serpentine demon blocking the waters, releasing them to flow and fertilize the land"
      source: "jacobsen-1987"

comparative_hooks:
  - other_culture: "Babylonian (Enuma Elish)"
    parallel: "Chaoskampf: young warrior god defeats chaos being and reshapes the cosmos"
    source: "jacobsen-1987"
  - other_culture: "Greek"
    parallel: "Zeus vs. Typhon — storm god battles chthonic monster for cosmic order"
    source: "kramer-1961"
  - other_culture: "Vedic"
    parallel: "Indra vs. Vrtra — warrior god releases dammed waters by slaying a blocking demon"
    source: "jacobsen-1987"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 8000

special_instructions: "Very long composition — organize the retelling into clear subsections (battle, damming of waters, stone-fate assignments, mother's renaming). The stone-fate catalogue is extensive; present representative examples rather than exhaustive listing, but note the full scope. Flag the Chaoskampf parallel but emphasize that Lugal-e predates Enuma Elish and should not be read as derivative."
```

---

# Input file: briefs/08-angim.yaml

```
chapter_number: 8
slug: "angim"
title: "Ninurta's Return to Nibru"
chapter_anchor: "ch-08-angim"

sources:
  primary:
    - id: etcsl
      loc: "1.6.1, composite text, lines 1–206"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.6.1"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.6.1"
    - id: black-2004
      loc: "pp. 192–198"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: jacobsen-1987, loc: "pp. 233–234 (contextual discussion as sequel to Lugal-e)" }
    - { id: kramer-1961, loc: "pp. 80–83 (Ninurta myths overview)" }

lacunae:
  - source: etcsl
    location: "lines 80–100"
    what_is_missing: "Portions of Ninurta's triumphal procession description damaged, details of trophy display fragmentary"
    in_tradition_fills_available: "partial, Akkadian bilingual version preserves some corresponding passages but is out of scope"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Sumerian text is the primary composition; the bilingual Akkadian version is secondary and out of scope"
  alternates:
    - source: black-2004
      difference: "Minor translation differences in the rendering of Ninurta's epithets and the gods' fearful reactions"

entities_glossary:
  - name: "Ninurta (𒀭𒊩𒌆𒅁)"
    role: deity
    first_mention_gloss_candidate: "warrior god returning in terrifying martial glory after his victory over Asag"
  - name: "Enlil (𒀭𒂗𒆤)"
    role: deity
    first_mention_gloss_candidate: "king of the gods, father of Ninurta, who must pacify his son's battle-fury"
  - name: "Ninlil (𒀭𒊩𒌆𒆤)"
    role: deity
    first_mention_gloss_candidate: "queen of the gods, consort of Enlil, who welcomes and soothes Ninurta"
  - name: "Nibru/Nippur (𒂗𒆤𒆠)"
    role: place
    first_mention_gloss_candidate: "sacred city of Enlil, religious capital of Sumer, destination of Ninurta's triumphal return"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Attested in multiple OB manuscripts and known through the bilingual tradition, indicating sustained scribal interest"
      source: "etcsl 1.6.1, manuscript list"
    - kind: scholarly-attention
      detail: "Recognized as a standard OB curriculum text and companion piece to Lugal-e"
      source: "black-2004 pp. 192 (introduction)"
  function:
    - role: theogonic
      basis: "Explores the problem of divine martial power that threatens cosmic order — the gods themselves fear Ninurta's return"
      source: "etcsl 1.6.1, lines 1–50"
    - role: literary
      basis: "A sustained exploration of martial excess and its reintegration into civilized order through parental authority"
      source: "black-2004 pp. 192–193 (introduction)"
  cross_cultural_parallels:
    - other_culture: "Greek (Homer)"
      parallel: "Achilles' rage and its threat to both enemies and allies echoes Ninurta's martial fury that alarms even the gods"
      source: "black-2004"
    - other_culture: "Norse"
      parallel: "Berserker battle-fury that must be calmed after combat parallels the pattern of divine warrior needing pacification"
      source: "jacobsen-1987"

comparative_hooks:
  - other_culture: "Greek (Homer)"
    parallel: "Warrior's homecoming rage threatening cosmic or social order (Achilles' wrath)"
    source: "black-2004"
  - other_culture: "Norse"
    parallel: "Berserker fury that endangers allies and must be ritually pacified"
    source: "jacobsen-1987"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2000

special_instructions: "Note bilingual nature — only Sumerian text in scope. Present as a companion piece to Lugal-e (chapter 7), with cross-references to that chapter. Emphasize the psychological dimension: the gods' fear of their own champion."
```

---

# Input file: briefs/09-ninurta-and-the-turtle.yaml

```
chapter_number: 9
slug: "ninurta-and-the-turtle"
title: "Ninurta and the Turtle: Enki's Trick"
chapter_anchor: "ch-09-ninurta-and-the-turtle"

sources:
  primary:
    - id: etcsl
      loc: "1.6.3, composite text (fragmentary)"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.6.3"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.6.3"
  secondary:
    - { id: black-2004, loc: "pp. 199–201 (summary reference)" }
    - { id: kramer-1961, loc: "pp. 82–83 (brief discussion of Ninurta–Anzu episode)" }

lacunae:
  - source: etcsl
    location: "lines 1–15"
    what_is_missing: "Opening section heavily damaged; context for the theft of the Tablet of Destinies and Ninurta's recovery largely lost"
    in_tradition_fills_available: "partial, Akkadian Anzu myth provides a parallel narrative of the tablet theft but is out of scope"
  - source: etcsl
    location: "lines 50–80"
    what_is_missing: "Middle section fragmentary; details of the turtle's creation by Enki and the mechanism of the trap partially lost"
    in_tradition_fills_available: "no, no other Sumerian witness fills these gaps"
  - source: etcsl
    location: "lines 100–end"
    what_is_missing: "Conclusion damaged; final judgment or resolution unclear"
    in_tradition_fills_available: "no"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "Only known Sumerian version; reconstructed from limited fragmentary witnesses"
  alternates:
    - source: kramer-1961
      difference: "Kramer's early summary fills narrative gaps with interpretive inference that goes beyond the preserved text"

entities_glossary:
  - name: "Ninurta (𒀭𒊩𒌆𒅁)"
    role: deity
    first_mention_gloss_candidate: "warrior god who recovers the Tablet of Destinies but is humbled by Enki's cunning"
  - name: "Enki (𒂗𒆠)"
    role: deity
    first_mention_gloss_candidate: "god of wisdom and cunning, lord of the abzu, who devises the turtle trap"
  - name: "Anzud (𒀭𒅎𒂂)"
    role: deity
    first_mention_gloss_candidate: "divine lion-headed eagle that stole the Tablet of Destinies from Enlil"
  - name: "tup šimāti / Tablet of Destinies"
    role: artifact
    first_mention_gloss_candidate: "tablet conferring supreme cosmic authority on its possessor, stolen by Anzud and recovered by Ninurta"

cultural_relevance:
  centrality: marginal
  centrality_evidence:
    - kind: attestation-volume
      detail: "Few copies survive and the text is heavily damaged, indicating limited circulation compared to Lugal-e and Angim"
      source: "etcsl 1.6.3, manuscript list"
    - kind: scholarly-attention
      detail: "Receives brief treatment in surveys as a comic counterpoint to the heroic Ninurta cycle"
      source: "black-2004 pp. 199–201"
  function:
    - role: literary
      basis: "Functions as a comic or satirical counterpoint to the heroic Ninurta narratives, deflating martial pride through trickster cleverness"
      source: "etcsl 1.6.3"
    - role: didactic
      basis: "Punishes hubris: Ninurta's arrogance after recovering the Tablet of Destinies is checked by Enki's superior cunning"
      source: "etcsl 1.6.3"
  cross_cultural_parallels:
    - other_culture: "Norse"
      parallel: "Trickster defeats warrior pattern: Loki outsmarts Thor in several Eddaic episodes through cunning rather than force"
      source: "kramer-1961"
    - other_culture: "West African (Akan)"
      parallel: "Anansi the spider-trickster defeats stronger opponents through wit and traps, a widespread trickster-vs-warrior motif"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Norse"
    parallel: "Trickster god humbles warrior god through cunning (Loki vs. Thor)"
    source: "kramer-1961"
  - other_culture: "West African (Akan)"
    parallel: "Anansi trickster defeats powerful opponents through wit and traps"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 1000

special_instructions: "Fragmentary text — be transparent about gaps and do not invent content to fill them. Present what survives clearly and note where the narrative is lost. The comic/ironic tone is distinctive within the Ninurta cycle and should be preserved in the retelling."
```

---

# Input file: briefs/10-inanna-and-enki.yaml

```
chapter_number: 10
slug: "inanna-and-enki"
title: "Inanna and Enki: The Theft of the ME"
chapter_anchor: "ch-10-inanna-and-enki"

sources:
  primary:
    - id: etcsl
      loc: "1.3.1, composite text"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.3.1"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.3.1"
    - id: black-2004
      loc: "pp. 63–70"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 64–68 (Inanna and the ME)" }
    - { id: jacobsen-1987, loc: "pp. 112–113 (brief contextual discussion)" }

lacunae:
  - source: etcsl
    location: "ME lists (repeated catalogue sections)"
    what_is_missing: "The lengthy catalogues of ME are fragmentary in multiple places; individual ME names are broken or illegible across several passages"
    in_tradition_fills_available: "partial, overlapping manuscripts restore some items but the full list of approximately one hundred ME cannot be completely reconstructed"
  - source: etcsl
    location: "lines 1–20"
    what_is_missing: "Opening partially damaged; Inanna's initial preparations for the journey to Eridu fragmentary"
    in_tradition_fills_available: "partial, other manuscripts preserve portions of the opening"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "ETCSL composite is the standard reconstruction; gaps in the ME lists remain unfilled across all known witnesses"
  alternates:
    - source: black-2004
      difference: "Black et al. condense or summarize the ME lists where the text is too fragmentary to translate fully"

entities_glossary:
  - name: "Inanna (𒀭𒈹)"
    role: deity
    first_mention_gloss_candidate: "goddess of love, war, and political power, patroness of Uruk"
  - name: "Enki (𒂗𒆠)"
    role: deity
    first_mention_gloss_candidate: "god of wisdom, freshwater, and cunning, lord of Eridu, guardian of the ME"
  - name: "ME (𒈨)"
    role: ritual-term
    first_mention_gloss_candidate: "divine powers or cultural norms underpinning all aspects of civilization — kingship, priesthood, crafts, truth, descent to the underworld, and dozens more"
  - name: "E-ana (𒂍𒀭𒈾)"
    role: place
    first_mention_gloss_candidate: "the House of Heaven, Inanna's great temple in Uruk, destination of the stolen ME"
  - name: "Eridu (𒉣𒆠)"
    role: place
    first_mention_gloss_candidate: "the most ancient of Sumerian cities, Enki's cult center, where the ME were kept"
  - name: "Uruk/Unug (𒌷𒀕)"
    role: place
    first_mention_gloss_candidate: "great city of Inanna, rival of Eridu, recipient of the transferred ME"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: attestation-volume
      detail: "Widely copied in OB scribal schools; the ME concept is central to Sumerian intellectual tradition"
      source: "etcsl 1.3.1, manuscript list"
    - kind: ritual-context
      detail: "The ME catalogue constitutes a comprehensive taxonomy of Sumerian civilization, reflecting temple and royal ideology"
      source: "black-2004 pp. 63–64 (introduction)"
    - kind: scholarly-attention
      detail: "Kramer devoted extensive analysis to the ME concept as the foundation of Sumerian cultural self-understanding"
      source: "kramer-1961 pp. 64–68"
  function:
    - role: cosmological
      basis: "Explains the transfer of civilizational powers from Eridu to Uruk, mapping a shift in religious and political centrality"
      source: "etcsl 1.3.1"
    - role: ritual-aetiological
      basis: "Provides an aetiology for the presence of the ME in Uruk's E-ana temple and legitimates Uruk's cultural supremacy"
      source: "black-2004 pp. 63–64 (introduction)"
  cross_cultural_parallels:
    - other_culture: "Greek"
      parallel: "Prometheus stealing fire from the gods and bringing it to humanity — a culture hero's transgressive theft that establishes civilization"
      source: "kramer-1961"
    - other_culture: "Polynesian"
      parallel: "Maui stealing fire from the underworld — trickster figure acquires civilizational knowledge through cunning and daring"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Greek"
    parallel: "Prometheus stealing fire — transgressive theft that founds civilization"
    source: "kramer-1961"
  - other_culture: "Polynesian"
    parallel: "Maui's theft of fire from the underworld — culture hero acquires knowledge through daring"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 3000

special_instructions: "The ME lists are central to the text's significance but fragmentary. Present a representative selection of the ME with clear indication of which are securely read and where gaps exist. Do not silently reconstruct broken items. The Eridu–Uruk rivalry subtext is important theological context."
```

---

# Input file: briefs/11-inanna-and-ebih.yaml

```
chapter_number: 11
slug: "inanna-and-ebih"
title: "Inanna and Ebih: The Destruction of the Mountain"
chapter_anchor: "ch-11-inanna-and-ebih"

sources:
  primary:
    - id: etcsl
      loc: "1.3.2, composite text, lines 1–184"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.3.2"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.3.2"
    - id: black-2004
      loc: "pp. 71–77"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 83–85 (Inanna as warrior goddess)" }
    - { id: jacobsen-1987, loc: "pp. 112–114 (brief contextual discussion of Inanna's martial aspect)" }

lacunae:
  - source: etcsl
    location: "lines 140–155"
    what_is_missing: "Minor gaps in the description of Inanna's assault on the mountain; some details of the destruction sequence broken"
    in_tradition_fills_available: "yes, the numerous manuscript copies allow near-complete restoration; only isolated words remain uncertain"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Numerous consistent OB copies produce a stable composite text with minimal significant variation"
  alternates:
    - source: black-2004
      difference: "Minor translation choices in rendering Inanna's epithets and the intensity of the destruction imagery"

entities_glossary:
  - name: "Inanna (𒀭𒈹)"
    role: deity
    first_mention_gloss_candidate: "goddess of love and war, whose martial fury is the driving force of the narrative"
  - name: "An/Anu (𒀭)"
    role: deity
    first_mention_gloss_candidate: "sky god, father of the gods, who warns Inanna against attacking Ebih but cannot dissuade her"
  - name: "Ebih (𒂊𒁉)"
    role: place
    first_mention_gloss_candidate: "a great mountain in the eastern ranges (identified with the Jebel Hamrin) that refuses to bow before Inanna"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: attestation-volume
      detail: "Exceptionally well-preserved in numerous OB copies, part of the standard scribal curriculum"
      source: "etcsl 1.3.2, manuscript list"
    - kind: scholarly-attention
      detail: "Frequently cited as a key text for understanding Inanna's martial aspect and the 'deity vs. mountain' topos in Sumerian literature"
      source: "black-2004 pp. 71 (introduction)"
    - kind: royal-inscription
      detail: "The motif of Inanna as irresistible destroyer is echoed in royal hymns invoking her patronage in warfare"
      source: "etcsl 1.3.2"
  function:
    - role: theogonic
      basis: "Demonstrates Inanna's supremacy even over An's counsel — she acts independently and triumphs, asserting her rank among the gods"
      source: "etcsl 1.3.2, lines 50–75"
    - role: literary
      basis: "A sustained exercise in divine martial rhetoric and sublime destructive imagery, showcasing the hymnic-narrative genre"
      source: "black-2004 pp. 71–72 (introduction)"
  cross_cultural_parallels:
    - other_culture: "Ugaritic/Canaanite"
      parallel: "Baal's conflict with mountains and his storm-god destruction motif echoes the deity-vs-landscape pattern, though the targets and theology differ"
      source: "jacobsen-1987"
    - other_culture: "Greek"
      parallel: "Athena's martial independence and defiance of other Olympians parallels Inanna's refusal to heed An's warning"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Ugaritic/Canaanite"
    parallel: "Deity vs. mountain — Baal's storm-god destruction of landscape features"
    source: "jacobsen-1987"
  - other_culture: "Greek"
    parallel: "Athena's martial independence — goddess defies patriarchal counsel and triumphs"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2500

special_instructions: "The text's rhetorical power lies in its escalation: Inanna's self-praise, An's futile warning, and the overwhelming destruction. Preserve this rhetorical structure in the retelling. The hymnic opening and closing frame the narrative and should not be truncated."
```

---

# Input file: briefs/12-inanna-and-shu-kale-tuda.yaml

```
chapter_number: 12
slug: "inanna-and-shu-kale-tuda"
title: "Inanna and Shu-kale-tuda: The Gardener's Crime"
chapter_anchor: "ch-12-inanna-and-shu-kale-tuda"

sources:
  primary:
    - id: etcsl
      loc: "1.3.3, composite text"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.3.3"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.3.3"
    - id: black-2004
      loc: "pp. 78–84"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 83–85 (Inanna narratives overview)" }

lacunae:
  - source: etcsl
    location: "plague description sections (multiple passages)"
    what_is_missing: "Significant portions of the three plague descriptions are broken; the specific nature and effects of the first and second plagues are only partially recoverable"
    in_tradition_fills_available: "no, the Nippur tablets that preserve this text do not offer sufficient overlap to fully restore the plague passages"
  - source: etcsl
    location: "lines 1–15"
    what_is_missing: "Opening lines damaged; initial context for the gardener's circumstances partially lost"
    in_tradition_fills_available: "partial, some manuscripts preserve fragments of the opening"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "ETCSL composite is the only standard reconstruction; gaps in the plague sections remain across all witnesses"
  alternates:
    - source: black-2004
      difference: "Black et al. mark the plague sections as heavily fragmentary and offer cautious partial translation where ETCSL gives transliteration only"

entities_glossary:
  - name: "Inanna (𒀭𒈹)"
    role: deity
    first_mention_gloss_candidate: "goddess of love and war, victim of the gardener's crime, who sends devastating plagues to find the culprit"
  - name: "Shu-kale-tuda"
    role: hero
    first_mention_gloss_candidate: "a mortal gardener who rapes the sleeping goddess and hides among humanity to escape her wrath"
  - name: "Enki (𒂗𒆠)"
    role: deity
    first_mention_gloss_candidate: "god of wisdom whom Shu-kale-tuda consults for advice on evading Inanna's pursuit"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Attested in the OB scribal curriculum from Nippur tablets, indicating recognized pedagogical value"
      source: "etcsl 1.3.3, manuscript list"
    - kind: scholarly-attention
      detail: "Discussed in surveys of Inanna literature as a distinctive narrative combining sexual violence, divine pursuit, and cosmic justice"
      source: "black-2004 pp. 78 (introduction)"
  function:
    - role: literary
      basis: "A sustained narrative of pursuit and divine justice with distinctive structure: crime, three escalating plagues, judgment"
      source: "etcsl 1.3.3"
    - role: didactic
      basis: "Demonstrates that crimes against the divine cannot be hidden — even Enki's counsel cannot ultimately protect the guilty"
      source: "etcsl 1.3.3"
  cross_cultural_parallels:
    - other_culture: "Greek"
      parallel: "Artemis and Actaeon — divine vengeance for transgression against a goddess's body, with the mortal hunted and destroyed"
      source: "kramer-1961"
    - other_culture: "Hebrew Bible"
      parallel: "Plagues sent to compel revelation or punish wrongdoing echo the pattern of escalating divine afflictions on the land"
      source: "black-2004"

comparative_hooks:
  - other_culture: "Greek"
    parallel: "Divine vengeance for transgression against a goddess (Artemis and Actaeon)"
    source: "kramer-1961"
  - other_culture: "Hebrew Bible"
    parallel: "Escalating plagues sent upon the land as divine punishment and compulsion"
    source: "black-2004"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2000

special_instructions: "Handle the sexual violence in the narrative with appropriate gravity and scholarly framing. The plague sections are heavily fragmentary — mark gaps clearly and do not fabricate details. The paradox of the ending (Shu-kale-tuda is condemned but his name is preserved) deserves attention as a literary device."
```

---

# Input file: briefs/13-inanna-and-gudam.yaml

```
chapter_number: 13
slug: "inanna-and-gudam"
title: "Inanna and Gudam"
chapter_anchor: "ch-13-inanna-and-gudam"

sources:
  primary:
    - id: etcsl
      loc: "1.3.4, composite text (very fragmentary)"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.3.4"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.3.4"
  secondary:
    - { id: black-2004, loc: "pp. 85 (brief summary reference)" }
    - { id: kramer-1961, loc: "pp. 83–85 (Inanna myths overview, brief mention)" }

lacunae:
  - source: etcsl
    location: "lines 1–20"
    what_is_missing: "Opening heavily damaged; the origin and nature of Gudam only partially described"
    in_tradition_fills_available: "no, too few manuscripts survive to restore the opening"
  - source: etcsl
    location: "middle sections"
    what_is_missing: "Central narrative substantially broken; details of Gudam's rampage and the confrontation with Inanna largely lost"
    in_tradition_fills_available: "no"
  - source: etcsl
    location: "closing lines"
    what_is_missing: "Conclusion fragmentary; the resolution and any hymnic closing are mostly lost"
    in_tradition_fills_available: "no"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "Only known version; reconstructed from very limited fragmentary witnesses"
  alternates:
    - source: black-2004
      difference: "Black et al. provide only a brief summary given the extreme fragmentary state"

entities_glossary:
  - name: "Inanna (𒀭𒈹)"
    role: deity
    first_mention_gloss_candidate: "goddess of love and war, patroness and protector of Uruk"
  - name: "Gudam"
    role: deity
    first_mention_gloss_candidate: "a fearsome monster or creature that terrorizes Uruk, devouring its food and drink"
  - name: "Uruk/Unug (𒌷𒀕)"
    role: place
    first_mention_gloss_candidate: "great city under Inanna's protection, terrorized by the monster Gudam"

cultural_relevance:
  centrality: marginal
  centrality_evidence:
    - kind: attestation-volume
      detail: "Very few copies survive and all are heavily damaged, indicating limited circulation or poor preservation"
      source: "etcsl 1.3.4, manuscript list"
    - kind: scholarly-attention
      detail: "Receives only brief mention in surveys due to fragmentary state; insufficient text for sustained analysis"
      source: "black-2004 pp. 85"
  function:
    - role: literary
      basis: "Patron deity defeats a city-threatening monster — a basic pattern of divine protection of the urban center"
      source: "etcsl 1.3.4"
  cross_cultural_parallels:
    - other_culture: "Mesopotamian (general)"
      parallel: "City patron deity slays a threatening monster — a widespread Near Eastern motif seen in Marduk vs. Tiamat and other traditions"
      source: "kramer-1961"
    - other_culture: "Greek"
      parallel: "Monster-slaying by a city's patron (Athena and various monsters in the Athenian tradition)"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Mesopotamian (general)"
    parallel: "Patron deity protects city by slaying a monstrous threat"
    source: "kramer-1961"
  - other_culture: "Greek"
    parallel: "City patron defeats threatening monster (widespread Hellenic pattern)"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 600

special_instructions: "Very fragmentary — chapter may be brief. Note gaps honestly; do not invent content. Present what survives clearly and indicate the overall narrative shape that can be inferred from the fragments. This is the shortest and most damaged text in the Inanna cycle; the retelling should be transparent about how little is securely readable."
```

---

# Input file: briefs/14-inannas-descent.yaml

```
chapter_number: 14
slug: "inannas-descent"
title: "Inanna's Descent to the Nether World"
chapter_anchor: "ch-14-inannas-descent"

sources:
  primary:
    - id: etcsl
      loc: "1.4.1, composite text, lines 1–415"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.4.1"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.4.1"
    - id: black-2004
      loc: "pp. 52–62"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
    - id: jacobsen-1987
      loc: "pp. 205–232"
      translator_edition: "Jacobsen 1987"
      identifier: "ISBN 9780300072785"
      url_or_file: ~
    - id: sladek-1974
      loc: "full philological study"
      translator_edition: "Sladek 1974 (PhD diss., Johns Hopkins)"
      identifier: "JHU-diss-1974-Sladek"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 83–96 (Inanna's descent and the dying-god cycle)" }

lacunae:
  - source: etcsl
    location: "lines 255–270 (various manuscripts)"
    what_is_missing: "Transition between Inanna's revival and the search for a substitute partially damaged in several witnesses"
    in_tradition_fills_available: "yes, overlap among 40+ tablets allows reconstruction of most gaps"
  - source: etcsl
    location: "lines 358–415 (seasonal alternation ending)"
    what_is_missing: "Seasonal alternation between Dumuzid and Geshtinanna not present in all manuscripts; final lines vary"
    in_tradition_fills_available: "partial, some manuscripts end before the alternation; composite relies on a subset of witnesses"

variants:
  classification: composite-editorial
  prevalent_version:
    source: etcsl
    why_prevalent: "ETCSL composite draws on 40+ Old Babylonian fragments to produce the standard scholarly text"
  alternates:
    - source: sladek-1974
      difference: "Fly's role in locating Dumuzid appears in some manuscripts only; Sladek documents the variant witnesses"
    - source: jacobsen-1987
      difference: "Jacobsen's literary translation smooths over line-level variants for narrative coherence"

entities_glossary:
  - name: "Inanna (𒀭𒈹)"
    role: deity
    first_mention_gloss_candidate: "queen of heaven, goddess of love, war, and political power"
  - name: "Ereshkigal (𒀭𒊩𒌆𒆠𒃲)"
    role: deity
    first_mention_gloss_candidate: "queen of the nether world, Inanna's elder sister and ruler of the dead"
  - name: "Dumuzid (𒌉𒍣)"
    role: deity
    first_mention_gloss_candidate: "shepherd-god and consort of Inanna, also known as Tammuz"
  - name: "Geshtinanna (𒄑𒌅𒀭𒈾)"
    role: deity
    first_mention_gloss_candidate: "divine sister of Dumuzid, who takes his place in the underworld for half the year"
  - name: "galla (𒃲𒆷)"
    role: deity
    first_mention_gloss_candidate: "underworld demons who accompany Inanna back and seize her substitute"
  - name: "kur / ki-gal"
    role: place
    first_mention_gloss_candidate: "the nether world, realm of the dead beneath the earth"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: attestation-volume
      detail: "Over 40 Old Babylonian tablets and fragments make this the most extensively attested Sumerian literary composition"
      source: "etcsl 1.4.1, manuscript list"
    - kind: ritual-context
      detail: "The text undergirds the seasonal cult of Dumuzid and the wailing rites attested in Ur III and OB periods"
      source: "jacobsen-1987 pp. 205–207"
    - kind: scholarly-attention
      detail: "Sladek's full philological study and continuous scholarly engagement since Kramer confirm its canonical status"
      source: "sladek-1974"
  function:
    - role: eschatological
      basis: "Provides the fullest Sumerian account of underworld geography, the laws of the dead, and the impossibility of free return"
      source: "etcsl 1.4.1, lines 1–170"
    - role: ritual-aetiological
      basis: "Explains the origin of the seasonal alternation in which Dumuzid dies and returns, grounding the wailing cult"
      source: "etcsl 1.4.1, lines 358–415"
  cross_cultural_parallels:
    - other_culture: "Greek"
      parallel: "Persephone's descent and seasonal return from Hades mirrors the Dumuzid/Geshtinanna alternation"
      source: "kramer-1961"
    - other_culture: "Egyptian"
      parallel: "Osiris's death, dismemberment, and cyclical resurrection echo the dying-god pattern"
      source: "jacobsen-1987"
    - other_culture: "Worldwide (seasonal myth)"
      parallel: "Death-and-rebirth of a vegetation deity tied to seasonal cycles appears in many traditions globally"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Greek"
    parallel: "Persephone's descent and seasonal return from Hades"
    source: "kramer-1961"
  - other_culture: "Egyptian"
    parallel: "Osiris death and cyclical resurrection as dying-god archetype"
    source: "jacobsen-1987"
  - other_culture: "Akkadian"
    parallel: "Descent of Ishtar is a shorter, adapted version; must be treated as a distinct composition"
    source: "sladek-1974"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 6000

special_instructions: "Preserve the seven-gate stripping structure. Distinct from Akkadian Descent of Ishtar."
```

---

# Input file: briefs/15-dumuzids-dream.yaml

```
chapter_number: 15
slug: "dumuzids-dream"
title: "Dumuzid's Dream"
chapter_anchor: "ch-15-dumuzids-dream"

sources:
  primary:
    - id: etcsl
      loc: "1.4.3, composite text, lines 1–260"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.4.3"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.4.3"
    - id: black-2004
      loc: "pp. 71–77"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
    - id: alster-1972
      loc: "full critical edition"
      translator_edition: "Alster 1972"
      identifier: "ISBN 9788750015536"
      url_or_file: ~
  secondary:
    - { id: jacobsen-1987, loc: "pp. 28–55 (discussion of Dumuzid cycle and pastoral imagery)" }

lacunae:
  - source: etcsl
    location: "lines 45–55"
    what_is_missing: "Several lines in the dream-interpretation sequence partially damaged"
    in_tradition_fills_available: "yes, Alster 1972 collates multiple witnesses that fill most gaps"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Well-preserved composite text with broad manuscript agreement; Alster's critical edition confirms stability"
  alternates:
    - source: alster-1972
      difference: "Minor orthographic variants among manuscripts; no substantive narrative divergence"

entities_glossary:
  - name: "Dumuzid (𒌉𒍣)"
    role: deity
    first_mention_gloss_candidate: "shepherd-god and consort of Inanna, doomed to the underworld"
  - name: "Geshtinanna (𒄑𒌅𒀭𒈾)"
    role: deity
    first_mention_gloss_candidate: "divine sister of Dumuzid who shelters and mourns him"
  - name: "galla (𒃲𒆷)"
    role: deity
    first_mention_gloss_candidate: "underworld demons who pursue Dumuzid across the steppe"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Well-attested in OB copies; part of the broader Dumuzid dying-god tradition in the scribal curriculum"
      source: "alster-1972 pp. 7–15"
    - kind: scholarly-attention
      detail: "Alster's monograph established this as a key text for Sumerian oral-poetic technique"
      source: "alster-1972"
  function:
    - role: eschatological
      basis: "Dramatises the inevitability of death through a prophetic dream that unfolds exactly as foretold"
      source: "etcsl 1.4.3, lines 1–50"
    - role: literary
      basis: "Outstanding psychological narrative exploring fate, flight, transformation, and sibling loyalty"
      source: "alster-1972 pp. 40–60"
  cross_cultural_parallels:
    - other_culture: "Ancient Near Eastern (widespread)"
      parallel: "Prophetic dreams foretelling inescapable death appear across ANE literature, including the Gilgamesh epic"
      source: "alster-1972"
    - other_culture: "Greek"
      parallel: "Tragic foreknowledge of doom echoes Greek tragic heroes (Cassandra, Oedipus) who cannot escape their fates"
      source: "jacobsen-1987"

comparative_hooks:
  - other_culture: "Ancient Near Eastern (widespread)"
    parallel: "Prophetic dream foretelling inescapable death"
    source: "alster-1972"
  - other_culture: "Greek"
    parallel: "Tragic hero foreknowledge and futile flight from fate"
    source: "jacobsen-1987"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2500

special_instructions: "Emphasise the dream-symbolism and the transformations during flight. Keep close to Alster's critical edition as the philological anchor."
```

---

# Input file: briefs/16-inanna-and-bilulu.yaml

```
chapter_number: 16
slug: "inanna-and-bilulu"
title: "Inanna and Bilulu: Vengeance for the Shepherd"
chapter_anchor: "ch-16-inanna-and-bilulu"

sources:
  primary:
    - id: etcsl
      loc: "1.4.4, composite text, lines 1–190"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.4.4"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.4.4"
    - id: jacobsen-1987
      loc: "pp. 315–325"
      translator_edition: "Jacobsen 1987"
      identifier: "ISBN 9780300072785"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 97–101 (Inanna and Dumuzid cycle overview)" }

lacunae:
  - source: etcsl
    location: "lines 1–20"
    what_is_missing: "Opening lines heavily damaged; context for Inanna's mourning partially lost"
    in_tradition_fills_available: "no, very few manuscript witnesses survive"
  - source: etcsl
    location: "lines 95–130"
    what_is_missing: "Central section describing the encounter with Bilulu fragmentary; transformation scene partly broken"
    in_tradition_fills_available: "no, insufficient parallel witnesses"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "Only a small number of fragmentary witnesses survive; ETCSL composite is the best available reconstruction"
  alternates:
    - source: jacobsen-1987
      difference: "Jacobsen's literary translation fills narrative gaps interpretively where the text is broken"

entities_glossary:
  - name: "Inanna (𒀭𒈹)"
    role: deity
    first_mention_gloss_candidate: "goddess who avenges the death of her consort Dumuzid"
  - name: "Dumuzid (𒌉𒍣)"
    role: deity
    first_mention_gloss_candidate: "shepherd-god whose death Inanna mourns and avenges"
  - name: "Bilulu"
    role: deity
    first_mention_gloss_candidate: "old woman transformed by Inanna into a waterskin for desert libations"
  - name: "Girgire"
    role: deity
    first_mention_gloss_candidate: "son of Bilulu, transformed alongside his mother"

cultural_relevance:
  centrality: marginal
  centrality_evidence:
    - kind: attestation-volume
      detail: "Very few manuscript copies survive, indicating limited circulation compared to other Inanna texts"
      source: "etcsl 1.4.4, manuscript list"
    - kind: scholarly-attention
      detail: "Jacobsen's treatment remains the most detailed study; interpretation of the transformation is still debated"
      source: "jacobsen-1987 pp. 315–325"
  function:
    - role: ritual-aetiological
      basis: "Explains the origin of desert libation practice through the transformation of Bilulu into a waterskin"
      source: "jacobsen-1987 pp. 320–325"
    - role: eschatological
      basis: "Continues the Dumuzid dying-god cycle with divine vengeance for his death"
      source: "etcsl 1.4.4, lines 140–190"
  cross_cultural_parallels:
    - other_culture: "Greek/Roman (Ovid)"
      parallel: "Divine transformation as punishment echoes Metamorphoses patterns, though Ovid is much later"
      source: "jacobsen-1987"

comparative_hooks:
  - other_culture: "Greek/Roman (Ovid)"
    parallel: "Divine vengeance through transformation of offenders into objects"
    source: "jacobsen-1987"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 1500

special_instructions: "Be transparent about the fragmentary state. Do not over-reconstruct. Flag Jacobsen's interpretive fills clearly."
```

---

# Input file: briefs/17-nannas-journey-to-nibru.yaml

```
chapter_number: 17
slug: "nannas-journey-to-nibru"
title: "Nanna-Suen's Journey to Nibru"
chapter_anchor: "ch-17-nannas-journey-to-nibru"

sources:
  primary:
    - id: etcsl
      loc: "1.5.1, composite text, lines 1–350"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.5.1"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.5.1"
    - id: black-2004
      loc: "pp. 147–155"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 47–49 (Nanna and the Ur-Nippur connection)" }

lacunae:
  - source: etcsl
    location: "lines 170–195"
    what_is_missing: "Several lines describing stops along the canal route partially damaged"
    in_tradition_fills_available: "partial, overlapping manuscripts restore most of the itinerary"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Well-preserved OB text with broad manuscript agreement; ETCSL composite is standard"
  alternates:
    - source: black-2004
      difference: "Minor editorial choices in rendering the gift-catalogue and blessing formulae"

entities_glossary:
  - name: "Nanna / Suen (𒀭𒋀𒆠)"
    role: deity
    first_mention_gloss_candidate: "moon god, patron deity of Ur, son of Enlil"
  - name: "Enlil (𒀭𒂗𒆤)"
    role: deity
    first_mention_gloss_candidate: "chief god of the Sumerian pantheon, lord of Nippur"
  - name: "Urim / Ur (𒋀𒀕𒆠)"
    role: place
    first_mention_gloss_candidate: "major Sumerian city, seat of Nanna's temple, the Ekishnugal"
  - name: "Nibru / Nippur (𒂗𒆤𒆠)"
    role: place
    first_mention_gloss_candidate: "religious capital of Sumer, seat of Enlil's temple, the Ekur"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Multiple OB copies from Nippur and Ur scribal schools confirm its place in the curriculum"
      source: "etcsl 1.5.1, manuscript list"
    - kind: ritual-context
      detail: "Reflects actual barge processions and offering deliveries between Ur and Nippur attested in administrative texts"
      source: "cdli"
    - kind: royal-inscription
      detail: "The Ur-Nippur political axis validated by this text mirrors Ur III royal ideology"
      source: "black-2004 pp. 147–148"
  function:
    - role: ritual-aetiological
      basis: "Provides a mythic charter for the regular delivery of offerings from Ur to Nippur's Ekur temple"
      source: "etcsl 1.5.1, lines 1–100"
    - role: royal-legitimation
      basis: "Enlil's blessing of Ur through Nanna legitimises Ur's political and cultic pre-eminence"
      source: "etcsl 1.5.1, lines 300–350"
  cross_cultural_parallels:
    - other_culture: "Egyptian"
      parallel: "The barque of Ra's daily solar journey along the river parallels the divine barge procession"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Egyptian"
    parallel: "Divine river journey by barque as ritual and cosmic act"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2500

special_instructions: "Highlight the detailed itinerary and gift catalogue as evidence for real cultic practice. Note the political subtext of the Ur-Nippur relationship."
```

---

# Input file: briefs/18-marriage-of-martu.yaml

```
chapter_number: 18
slug: "marriage-of-martu"
title: "The Marriage of Martu"
chapter_anchor: "ch-18-marriage-of-martu"

sources:
  primary:
    - id: etcsl
      loc: "1.7.1, composite text, lines 1–155"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.7.1"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.7.1"
    - id: black-2004
      loc: "pp. 156–162"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 101–103 (Martu and Amorite traditions)" }

lacunae:
  - source: etcsl
    location: "lines 120–140"
    what_is_missing: "Portions of the friend's warning speech about nomadic life partially broken"
    in_tradition_fills_available: "partial, overlapping manuscripts restore most of the speech"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Reasonably well-preserved OB text with consistent manuscript tradition"
  alternates:
    - source: black-2004
      difference: "Minor editorial choices in rendering the ethnographic catalogue of nomadic habits"

entities_glossary:
  - name: "Martu / Amurru"
    role: deity
    first_mention_gloss_candidate: "divine personification of the Amorite west, god of the nomadic peoples"
  - name: "Numushda (𒀭𒉡𒈲𒁕)"
    role: deity
    first_mention_gloss_candidate: "local deity, father of the bride in the narrative"
  - name: "Shuruppag (𒋢𒆳𒊒𒉺𒂵𒆠)"
    role: place
    first_mention_gloss_candidate: "ancient Sumerian city, setting for the festival and marriage"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Several OB copies survive; the text's ethnographic content attracted consistent scholarly interest"
      source: "etcsl 1.7.1, manuscript list"
    - kind: scholarly-attention
      detail: "Valued as a rare Sumerian literary witness to Amorite cultural perception from the urban Sumerian viewpoint"
      source: "black-2004 pp. 156–157"
  function:
    - role: literary
      basis: "A comedic narrative of cultural encounter between settled Sumerian civilisation and nomadic Amorite life"
      source: "etcsl 1.7.1, lines 100–155"
    - role: didactic
      basis: "The bride's willing acceptance despite warnings conveys a message about integration across cultural boundaries"
      source: "black-2004 pp. 156–162"
  cross_cultural_parallels:
    - other_culture: "Ancient Near Eastern (widespread)"
      parallel: "Civilised/nomadic bride narratives and cultural-encounter texts appear across ANE literary traditions"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Ancient Near Eastern (widespread)"
    parallel: "Civilised/nomadic encounter and intermarriage as literary theme"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 1500

special_instructions: "Foreground the ethnographic value of the friend's speech describing Amorite customs. Avoid projecting modern ethnic categories onto the text."
```

---

# Input file: briefs/19-gilgamesh-and-aga.yaml

```
chapter_number: 19
slug: "gilgamesh-and-aga"
title: "Gilgamesh and Aga: The Siege of Uruk"
chapter_anchor: "ch-19-gilgamesh-and-aga"

sources:
  primary:
    - id: etcsl
      loc: "1.8.1.1, composite text, lines 1–115"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.8.1.1"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.8.1.1"
    - id: black-2004
      loc: "pp. 279–284"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
    - id: george-2003
      loc: "vol. 1, pp. 141–148"
      translator_edition: "George 2003"
      identifier: "ISBN 9780199278985"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 187–190 (early analysis of the Gilgamesh-Aga conflict)" }

lacunae:
  - source: etcsl
    location: "lines 85–95"
    what_is_missing: "Portions of the siege climax and Aga's response partially damaged"
    in_tradition_fills_available: "partial, manuscript overlap restores most of the sequence"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Mostly complete OB text with consistent manuscript tradition; the shortest and most cohesive Gilgamesh poem"
  alternates:
    - source: george-2003
      difference: "George offers minor variant readings in the assembly speeches based on collation of additional fragments"

entities_glossary:
  - name: "Gilgamesh / Bilgames (𒄑𒉈𒂵𒈩)"
    role: hero
    first_mention_gloss_candidate: "king of Uruk, semi-divine hero who defies Kish's demand for submission"
  - name: "Aga (𒀀𒂵)"
    role: hero
    first_mention_gloss_candidate: "king of Kish who besieges Uruk and is ultimately captured and released"
  - name: "Enkidu (𒂗𒆠𒆕)"
    role: hero
    first_mention_gloss_candidate: "companion and adviser of Gilgamesh during the siege"
  - name: "Unug / Uruk (𒌷𒀕)"
    role: place
    first_mention_gloss_candidate: "great walled city of Gilgamesh in southern Mesopotamia"
  - name: "Kish (𒆧𒆠)"
    role: place
    first_mention_gloss_candidate: "rival city whose hegemony Gilgamesh challenges"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: attestation-volume
      detail: "Well-attested in OB copies; the only Gilgamesh poem without supernatural elements, valued for its historical kernel"
      source: "etcsl 1.8.1.1, manuscript list"
    - kind: scholarly-attention
      detail: "Widely discussed as evidence for early political assemblies and proto-democratic institutions in Sumer"
      source: "george-2003 vol. 1, pp. 141–142"
    - kind: royal-inscription
      detail: "The bicameral assembly (elders vs. young men) has been compared to early political structures attested in royal inscriptions"
      source: "kramer-1961 pp. 187–190"
  function:
    - role: royal-legitimation
      basis: "Establishes Uruk's independence from Kish and Gilgamesh's authority as divinely favoured ruler"
      source: "etcsl 1.8.1.1, lines 1–30"
    - role: literary
      basis: "A tightly constructed political narrative exploring the tension between assembly counsel and royal initiative"
      source: "black-2004 pp. 279–280"
  cross_cultural_parallels:
    - other_culture: "Greek"
      parallel: "Siege narratives and assembly debates echo Homeric Troy and the Greek polis model of political decision-making"
      source: "george-2003"
    - other_culture: "Greek"
      parallel: "The bicameral structure (elders vs. fighting men) parallels the Homeric assembly in the Iliad"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Greek"
    parallel: "Siege narrative and political assembly as literary motif (Troy, Iliad)"
    source: "george-2003"
  - other_culture: "Greek"
    parallel: "Bicameral deliberation (elders vs. young warriors) as proto-political institution"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2000

special_instructions: "Emphasise the unique absence of supernatural elements. Foreground the bicameral assembly as politically significant. Note that Aga's release is a gesture of magnanimity, not weakness."
```

---

# Input file: briefs/20-gilgamesh-and-the-bull-of-heaven.yaml

```
chapter_number: 20
slug: "gilgamesh-and-the-bull-of-heaven"
title: "Gilgamesh and the Bull of Heaven"
chapter_anchor: "ch-20-gilgamesh-and-the-bull-of-heaven"

sources:
  primary:
    - id: etcsl
      loc: "1.8.1.2, composite text (heavily damaged)"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.8.1.2"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.8.1.2"
  secondary:
    - { id: george-2003, loc: "vol. 1, pp. 10–12 (Sumerian Bull of Heaven tradition vs. Akkadian Tablet VI)" }
    - { id: kramer-1961, loc: "pp. 192–193 (early summary of the bull-slaying episode)" }

lacunae:
  - source: etcsl
    location: "throughout; majority of lines"
    what_is_missing: "Heavily damaged composition; large portions of the narrative are lost, including much of the battle sequence"
    in_tradition_fills_available: "no, insufficient Sumerian witnesses survive; Akkadian Gilgamesh Tablet VI is a separate tradition and must not be used to fill gaps"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "ETCSL composite is the only available reconstruction from heavily damaged Sumerian witnesses"
  alternates:
    - source: george-2003
      difference: "George discusses the Sumerian fragments in the context of the Akkadian tradition but does not conflate them"

entities_glossary:
  - name: "Gilgamesh / Bilgames (𒄑𒉈𒂵𒈩)"
    role: hero
    first_mention_gloss_candidate: "king of Uruk who slays the Bull of Heaven with Enkidu"
  - name: "Enkidu (𒂗𒆠𒆕)"
    role: hero
    first_mention_gloss_candidate: "companion of Gilgamesh who assists in slaying the bull"
  - name: "Inanna (𒀭𒈹)"
    role: deity
    first_mention_gloss_candidate: "goddess who sends the Bull of Heaven against Uruk"
  - name: "gudanna (𒄞𒀭𒈾)"
    role: artifact
    first_mention_gloss_candidate: "the Bull of Heaven, a cosmic beast unleashed as divine weapon"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: iconography
      detail: "The bull-slaying motif is widely attested on cylinder seals from the Early Dynastic through Old Babylonian periods"
      source: "cdli"
    - kind: scholarly-attention
      detail: "Despite textual damage, the motif's prominence in visual art confirms its importance in the tradition"
      source: "george-2003 vol. 1, pp. 10–12"
  function:
    - role: literary
      basis: "A divine-human conflict narrative in which heroes challenge a beast sent by an offended deity"
      source: "etcsl 1.8.1.2"
    - role: theogonic
      basis: "Dramatises the limits of divine power when mortal heroes defeat a divine weapon"
      source: "george-2003 vol. 1, pp. 10–12"
  cross_cultural_parallels:
    - other_culture: "Roman (Mithraic)"
      parallel: "Mithras's tauroctony (ritual bull-slaying) echoes the cosmic bull-killing motif"
      source: "kramer-1961"
    - other_culture: "Greek"
      parallel: "Heracles and the Cretan Bull / Theseus and the Minotaur share the hero-vs-divine-bull pattern"
      source: "george-2003"

comparative_hooks:
  - other_culture: "Roman (Mithraic)"
    parallel: "Cosmic bull-slaying as ritual and mythic act"
    source: "kramer-1961"
  - other_culture: "Greek"
    parallel: "Hero vs. divine bull (Cretan Bull, Minotaur)"
    source: "george-2003"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 1000

special_instructions: "Heavily damaged — be honest about gaps. Do not fill from Akkadian Gilgamesh Tablet VI."
```

---

# Input file: briefs/21-gilgamesh-and-huwawa.yaml

```
chapter_number: 21
slug: "gilgamesh-and-huwawa"
title: "Gilgamesh and Huwawa: The Cedar Forest"
chapter_anchor: "ch-21-gilgamesh-and-huwawa"

sources:
  primary:
    - id: etcsl
      loc: "1.8.1.5 (Version A), composite text, lines 1–197; 1.8.1.5.1 (Version B), composite text, lines 1–160"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.8.1.5 and 1.8.1.5.1"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.8.1.5"
    - id: black-2004
      loc: "pp. 269–278"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
    - id: george-2003
      loc: "vol. 1, pp. 149–174"
      translator_edition: "George 2003"
      identifier: "ISBN 9780199278985"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 190–196 (Gilgamesh and the Land of the Living)" }

lacunae:
  - source: etcsl
    location: "Version A, lines 140–160"
    what_is_missing: "Portions of the trick with the seven auras partially damaged in some manuscripts"
    in_tradition_fills_available: "yes, overlapping manuscripts for Version A allow reconstruction of most gaps"
  - source: etcsl
    location: "Version B, lines 80–110"
    what_is_missing: "Central section emphasising fear and hesitation before the forest partially broken"
    in_tradition_fills_available: "partial, fewer manuscripts for Version B leave some lines unrestored"

variants:
  classification: co-equal
  prevalent_version:
    source: etcsl
    why_prevalent: "Version A is longer, better preserved, and more widely attested in OB copies; used as the primary presentation"
  alternates:
    - source: etcsl
      difference: "Version B is a shorter, distinct composition emphasising fear and the psychological dimension of the quest, well-attested in its own right"

entities_glossary:
  - name: "Gilgamesh / Bilgames (𒄑𒉈𒂵𒈩)"
    role: hero
    first_mention_gloss_candidate: "king of Uruk who journeys to the Cedar Forest seeking eternal fame"
  - name: "Enkidu (𒂗𒆠𒆕)"
    role: hero
    first_mention_gloss_candidate: "companion of Gilgamesh and guide through the mountain passes"
  - name: "Huwawa / Humbaba (𒄷𒉿𒉿)"
    role: deity
    first_mention_gloss_candidate: "fearsome guardian of the Cedar Forest, appointed by Enlil"
  - name: "me-lam (𒈨𒀭)"
    role: ritual-term
    first_mention_gloss_candidate: "divine aura or radiance, the seven supernatural terrors wielded by Huwawa"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: attestation-volume
      detail: "Numerous OB copies of Version A make it one of the best-attested Gilgamesh poems in the scribal curriculum"
      source: "etcsl 1.8.1.5, manuscript list"
    - kind: scholarly-attention
      detail: "George devotes extensive discussion to distinguishing the two Sumerian versions from the Akkadian Cedar Forest episode"
      source: "george-2003 vol. 1, pp. 149–174"
  function:
    - role: literary
      basis: "A quest narrative exploring heroic ambition, the desire for lasting fame, and the confrontation with the monstrous"
      source: "etcsl 1.8.1.5, lines 1–50"
    - role: didactic
      basis: "Raises the question of mortality and the compensatory value of fame — central to Sumerian wisdom thought"
      source: "black-2004 pp. 269–270"
  cross_cultural_parallels:
    - other_culture: "Anglo-Saxon"
      parallel: "Hero versus forest guardian echoes Beowulf's encounter with Grendel in his lair"
      source: "george-2003"
    - other_culture: "Greek"
      parallel: "Quest for immortal fame (kleos) as the hero's driving motivation parallels Achilles' choice in the Iliad"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Anglo-Saxon"
    parallel: "Hero vs. monstrous forest guardian (Beowulf and Grendel)"
    source: "george-2003"
  - other_culture: "Greek"
    parallel: "Quest for immortal fame overcoming mortality (kleos in the Iliad)"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 3500

special_instructions: "Present Version A as primary, Version B inline as distinct composition. Both are Sumerian, independent of Akkadian."
```

---

# Input file: briefs/22-gilgamesh-enkidu-and-the-nether-world.yaml

```
chapter_number: 22
slug: "gilgamesh-enkidu-and-the-nether-world"
title: "Gilgamesh, Enkidu, and the Nether World"
chapter_anchor: "ch-22-gilgamesh-enkidu-and-the-nether-world"

sources:
  primary:
    - id: etcsl
      loc: "1.8.1.4, composite text, lines 1–303"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.8.1.4"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.8.1.4"
    - id: black-2004
      loc: "pp. 285–296"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
    - id: george-2003
      loc: "vol. 1, pp. 175–195"
      translator_edition: "George 2003"
      identifier: "ISBN 9780199278985"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 196–205 (Gilgamesh and the huluppu tree, underworld vision)" }
    - { id: jacobsen-1987, loc: "pp. 233–240 (cosmogonic prologue and afterlife vision)" }

lacunae:
  - source: etcsl
    location: "lines 150–175"
    what_is_missing: "Portions of Enkidu's taboo-breaking instructions and descent sequence partially damaged"
    in_tradition_fills_available: "yes, numerous OB tablets overlap and allow reconstruction of most gaps"
  - source: etcsl
    location: "lines 240–270"
    what_is_missing: "Parts of Enkidu's ghost's report on afterlife conditions fragmentary in some witnesses"
    in_tradition_fills_available: "partial, manuscript overlap covers most but not all of the catalogue of the dead"

variants:
  classification: composite-editorial
  prevalent_version:
    source: etcsl
    why_prevalent: "ETCSL composite draws on numerous OB tablets to produce the standard scholarly text"
  alternates:
    - source: george-2003
      difference: "George discusses the relationship between this Sumerian composition and Akkadian Tablet XII, which is a partial translation, not a variant"

entities_glossary:
  - name: "Gilgamesh / Bilgames (𒄑𒉈𒂵𒈩)"
    role: hero
    first_mention_gloss_candidate: "king of Uruk who loses his ritual objects to the nether world"
  - name: "Enkidu (𒂗𒆠𒆕)"
    role: hero
    first_mention_gloss_candidate: "companion who descends to the nether world and returns as a ghost to report on the afterlife"
  - name: "Inanna (𒀭𒈹)"
    role: deity
    first_mention_gloss_candidate: "goddess who plants and later abandons the huluppu tree"
  - name: "huluppu"
    role: artifact
    first_mention_gloss_candidate: "sacred tree planted by Inanna, from which Gilgamesh fashions his ritual objects"
  - name: "ellag / ekidma (pukku / mekku)"
    role: artifact
    first_mention_gloss_candidate: "ritual objects (possibly a ball and stick or drum and drumstick) that fall into the nether world"
  - name: "kur (𒆳)"
    role: place
    first_mention_gloss_candidate: "the nether world, realm of the dead"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: attestation-volume
      detail: "Widely attested in numerous OB tablets from Nippur and elsewhere; a major curriculum text"
      source: "etcsl 1.8.1.4, manuscript list"
    - kind: scholarly-attention
      detail: "George's extensive treatment and its status as the basis for Akkadian Tablet XII confirm its canonical importance"
      source: "george-2003 vol. 1, pp. 175–195"
  function:
    - role: eschatological
      basis: "Provides the most detailed Sumerian catalogue of afterlife conditions, organised by manner of death and social status"
      source: "etcsl 1.8.1.4, lines 240–303"
    - role: cosmological
      basis: "The cosmogonic prologue describes the separation of heaven and earth and the primordial ordering of the world"
      source: "etcsl 1.8.1.4, lines 1–26"
  cross_cultural_parallels:
    - other_culture: "Greek"
      parallel: "Odyssey Book 11 (Nekyia) presents a catalogue of the dead consulted by a living hero, closely paralleling Enkidu's ghost report"
      source: "george-2003"
    - other_culture: "Roman"
      parallel: "Virgil's Aeneid Book 6 underworld journey continues the classical tradition of living heroes visiting the dead"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Greek"
    parallel: "Living hero consults the dead for knowledge of the afterlife (Odyssey Book 11)"
    source: "george-2003"
  - other_culture: "Roman"
    parallel: "Hero's underworld journey as cosmological revelation (Aeneid Book 6)"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 4000

special_instructions: "Treat the cosmogonic prologue as integral, not a later addition. Clearly distinguish this Sumerian composition from Akkadian Tablet XII, which is a partial translation appended to the standard Babylonian epic."
```

---

# Input file: briefs/23-death-of-gilgamesh.yaml

```
chapter_number: 23
slug: "death-of-gilgamesh"
title: "The Death of Gilgamesh"
chapter_anchor: "ch-23-death-of-gilgamesh"

sources:
  primary:
    - id: etcsl
      loc: "1.8.1.3, composite text (fragmentary)"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.8.1.3"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.8.1.3"
    - id: george-2003
      loc: "vol. 1, pp. 195–208 (Nippur and Tell Haddad versions)"
      translator_edition: "George 2003"
      identifier: "ISBN 9780199278985"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 205–207 (early discussion of Gilgamesh's death and afterlife)" }

lacunae:
  - source: etcsl
    location: "throughout; multiple large gaps"
    what_is_missing: "Extensive damage to the Nippur manuscripts; funeral preparations and underworld reception sequences heavily broken"
    in_tradition_fills_available: "partial, Tell Haddad version provides significant new material not in Nippur witnesses, but the two do not fully overlap"
  - source: george-2003
    location: "Tell Haddad tablets, col. ii–iv"
    what_is_missing: "Ritual content in the Tell Haddad version partially damaged; divine judgement scene incomplete"
    in_tradition_fills_available: "no, the Tell Haddad version is the only witness for its distinctive ritual content"

variants:
  classification: co-equal
  prevalent_version:
    source: etcsl
    why_prevalent: "Nippur version has been known longer and forms the basis of the ETCSL composite, but Tell Haddad is equally authoritative"
  alternates:
    - source: george-2003
      difference: "Tell Haddad version includes significantly more ritual and funerary content, expanding the underworld reception scene"

entities_glossary:
  - name: "Gilgamesh / Bilgames (𒄑𒉈𒂵𒈩)"
    role: hero
    first_mention_gloss_candidate: "king of Uruk who confronts his mortality and is received as a judge among the dead"
  - name: "Ereshkigal (𒀭𒊩𒌆𒆠𒃲)"
    role: deity
    first_mention_gloss_candidate: "queen of the nether world who receives Gilgamesh after death"
  - name: "Ningishzida (𒀭𒊩𒌆𒄑𒍣𒁕)"
    role: deity
    first_mention_gloss_candidate: "underworld deity who serves as judge of the dead alongside Gilgamesh"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Fragmentary but attested at multiple sites; the Tell Haddad discovery significantly expanded knowledge of the text"
      source: "george-2003 vol. 1, pp. 195–196"
    - kind: scholarly-attention
      detail: "George's treatment of the two versions revitalised scholarly discussion of the hero's death and afterlife status"
      source: "george-2003 vol. 1, pp. 195–208"
  function:
    - role: eschatological
      basis: "Explores the universal human confrontation with mortality through the death of the greatest hero"
      source: "etcsl 1.8.1.3"
    - role: royal-legitimation
      basis: "Gilgamesh is elevated to divine status as a judge in the underworld, legitimising the cult of dead kings"
      source: "george-2003 vol. 1, pp. 200–208"
  cross_cultural_parallels:
    - other_culture: "Greek"
      parallel: "Heracles' death and apotheosis on Olympus mirrors Gilgamesh's elevation to judge of the dead"
      source: "george-2003"
    - other_culture: "Norse"
      parallel: "Heroes received in Valhalla after death parallel the honoured reception of Gilgamesh in the nether world"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Greek"
    parallel: "Hero's death and apotheosis (Heracles on Olympus)"
    source: "george-2003"
  - other_culture: "Norse"
    parallel: "Heroic afterlife reception (Valhalla)"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 1500

special_instructions: "Present both Nippur and Tell Haddad versions as co-equal witnesses. Be transparent about extensive damage. Highlight the Tell Haddad ritual content as a major addition to the tradition."
```

---

# Input file: briefs/24-enmerkar-and-the-lord-of-aratta.yaml

```
chapter_number: 24
slug: "enmerkar-and-the-lord-of-aratta"
title: "Enmerkar and the Lord of Aratta"
chapter_anchor: "ch-24-enmerkar-and-the-lord-of-aratta"

sources:
  primary:
    - id: etcsl
      loc: "1.8.2.3, composite text, lines 1–636"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.8.2.3"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.8.2.3"
    - id: vanstiphout-2003
      loc: "pp. 1–95"
      translator_edition: "Vanstiphout 2003"
      identifier: "ISBN 9781589830837"
      url_or_file: ~
    - id: black-2004
      loc: "pp. 236–251"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 232–234 (Enmerkar cycle overview)" }

lacunae:
  - source: etcsl
    location: "lines 500–530 (Aratta's responses)"
    what_is_missing: "Several of Aratta's lord's responses to Enmerkar's escalating demands are partially damaged or unclear"
    in_tradition_fills_available: "partial, overlapping manuscripts clarify some lines but the lord of Aratta's counter-arguments remain fragmentary in places"
  - source: etcsl
    location: "lines 136–155"
    what_is_missing: "Transition passage between Inanna's initial endorsement of Enmerkar and the first messenger dispatch partially broken"
    in_tradition_fills_available: "yes, composite reconstruction from multiple OB manuscripts restores most of the passage"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Mostly preserved across multiple OB manuscripts; ETCSL composite is the standard scholarly text"
  alternates:
    - source: vanstiphout-2003
      difference: "Vanstiphout's critical edition occasionally favors different manuscript readings in the Aratta response sections"

entities_glossary:
  - name: "Enmerkar (𒂗𒈨𒅕𒃸)"
    role: hero
    first_mention_gloss_candidate: "legendary king of Uruk, son of Utu, who sought to subjugate Aratta"
  - name: "lord of Aratta"
    role: hero
    first_mention_gloss_candidate: "unnamed rival king of the distant city of Aratta, Enmerkar's adversary in diplomatic contest"
  - name: "Inanna (𒀭𒈹)"
    role: deity
    first_mention_gloss_candidate: "queen of heaven, patron goddess of Uruk whose favor Enmerkar and the lord of Aratta both seek"
  - name: "Aratta"
    role: place
    first_mention_gloss_candidate: "distant wealthy city beyond seven mountain ranges, source of precious stones and metals"
  - name: "Uruk / Unug (𒌷𒀕)"
    role: place
    first_mention_gloss_candidate: "great city of southern Mesopotamia, Enmerkar's seat of power and Inanna's cult center"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: attestation-volume
      detail: "Multiple Old Babylonian manuscripts from Nippur and other scribal centers attest wide circulation as a curriculum text"
      source: "etcsl 1.8.2.3, manuscript list"
    - kind: scholarly-attention
      detail: "Vanstiphout devotes nearly a hundred pages to the critical edition; the composition is a standard reference in all surveys of Sumerian narrative poetry"
      source: "vanstiphout-2003 pp. 1–95"
    - kind: royal-inscription
      detail: "The text encodes Uruk's ideological claims to regional hegemony through Enmerkar's demands for tribute and labor from Aratta"
      source: "black-2004 pp. 236–237 (introduction)"
  function:
    - role: royal-legitimation
      basis: "Establishes Uruk's supremacy over Aratta through divinely backed diplomatic contest, legitimating Uruk hegemony"
      source: "etcsl 1.8.2.3, lines 1–30"
    - role: literary
      basis: "Peak of Sumerian narrative poetry: complex messenger structure, riddle exchanges, and rhetorical escalation"
      source: "vanstiphout-2003 pp. 1–10 (introduction)"
    - role: didactic
      basis: "The confusion of tongues passage and the invention of writing passage encode cultural memory about the origins of literate civilization"
      source: "etcsl 1.8.2.3, lines 500–540"
  cross_cultural_parallels:
    - other_culture: "Hebrew Bible"
      parallel: "The confusion of tongues motif directly parallels the Tower of Babel narrative (Genesis 11:1–9)"
      source: "kramer-1961"
    - other_culture: "Greek"
      parallel: "Riddle contests echo the Oedipus and Sphinx tradition and broader ANE wisdom-contest genres"
      source: "vanstiphout-2003"

comparative_hooks:
  - other_culture: "Hebrew Bible"
    parallel: "Confusion of tongues — Tower of Babel (Genesis 11)"
    source: "kramer-1961"
  - other_culture: "Greek"
    parallel: "Riddle contest between rivals — Oedipus and Sphinx, ANE wisdom traditions"
    source: "vanstiphout-2003"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 6000

special_instructions: "Preserve the messenger structure and the escalating exchanges. The confusion of tongues passage and writing invention passage are pivotal."
```

---

# Input file: briefs/25-enmerkar-and-en-suhgir-ana.yaml

```
chapter_number: 25
slug: "enmerkar-and-en-suhgir-ana"
title: "Enmerkar and En-suhgir-ana: The Sorcery Contest"
chapter_anchor: "ch-25-enmerkar-and-en-suhgir-ana"

sources:
  primary:
    - id: etcsl
      loc: "1.8.2.4, composite text"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.8.2.4"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.8.2.4"
    - id: vanstiphout-2003
      loc: "pp. 97–169"
      translator_edition: "Vanstiphout 2003"
      identifier: "ISBN 9781589830837"
      url_or_file: ~
    - id: black-2004
      loc: "pp. 252–261"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 234–235 (Aratta cycle overview)" }

lacunae:
  - source: etcsl
    location: "lines 200–220"
    what_is_missing: "Transition between the sorcery challenge and the dispatch of Urgirinuna partially damaged"
    in_tradition_fills_available: "yes, overlapping OB manuscripts restore most of the passage"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Generally well-preserved across OB manuscripts; ETCSL composite provides a coherent text"
  alternates:
    - source: vanstiphout-2003
      difference: "Vanstiphout's edition includes fuller philological notes on minor variant readings in the sorcery-contest sequence"

entities_glossary:
  - name: "Enmerkar (𒂗𒈨𒅕𒃸)"
    role: hero
    first_mention_gloss_candidate: "king of Uruk, protagonist who prevails through wisdom rather than direct combat"
  - name: "En-suhgir-ana"
    role: hero
    first_mention_gloss_candidate: "lord of Aratta who challenges Enmerkar to a contest of sorcery"
  - name: "Urgirinuna"
    role: being
    first_mention_gloss_candidate: "witch dispatched from Aratta to defeat Uruk through magic"
  - name: "Sagburu"
    role: being
    first_mention_gloss_candidate: "old woman of Uruk who defeats Urgirinuna's sorcery with superior cunning"
  - name: "Inanna (𒀭𒈹)"
    role: deity
    first_mention_gloss_candidate: "patron goddess of Uruk whose favor ensures Enmerkar's ultimate victory"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Well-preserved OB manuscripts attest its place in the Aratta cycle curriculum"
      source: "etcsl 1.8.2.4, manuscript list"
    - kind: scholarly-attention
      detail: "Vanstiphout provides a full critical edition with seventy pages of text and commentary"
      source: "vanstiphout-2003 pp. 97–169"
  function:
    - role: literary
      basis: "Showcases the magical-contest genre and the motif of humble wisdom triumphing over foreign sorcery"
      source: "vanstiphout-2003 pp. 97–105 (introduction)"
    - role: royal-legitimation
      basis: "Affirms Uruk's supremacy over Aratta: even Aratta's sorcery cannot overcome Uruk's divinely protected wisdom"
      source: "etcsl 1.8.2.4, concluding lines"
  cross_cultural_parallels:
    - other_culture: "Hebrew Bible"
      parallel: "Magical contest recalls Moses vs. Egyptian magicians (Exodus 7–8) and Elijah vs. prophets of Baal (1 Kings 18)"
      source: "vanstiphout-2003"
    - other_culture: "Worldwide (folklore)"
      parallel: "The old-woman-defeats-witch motif appears in many traditions as the triumph of humble wisdom over foreign magic"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Hebrew Bible"
    parallel: "Magical contest — Moses vs. Egyptian magicians, Elijah vs. Baal priests"
    source: "vanstiphout-2003"
  - other_culture: "Worldwide (folklore)"
    parallel: "Humble old woman defeats powerful foreign sorcerer through cunning"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2500

special_instructions: "Emphasize the contest structure and the role of Sagburu as the unlikely champion. This is the final composition in the Aratta diplomatic cycle."
```

---

# Input file: briefs/26-lugalbanda-in-the-mountain-cave.yaml

```
chapter_number: 26
slug: "lugalbanda-in-the-mountain-cave"
title: "Lugalbanda in the Mountain Cave"
chapter_anchor: "ch-26-lugalbanda-in-the-mountain-cave"

sources:
  primary:
    - id: etcsl
      loc: "1.8.2.1, composite text"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.8.2.1"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.8.2.1"
    - id: vanstiphout-2003
      loc: "pp. 171–213"
      translator_edition: "Vanstiphout 2003"
      identifier: "ISBN 9781589830837"
      url_or_file: ~
    - id: black-2004
      loc: "pp. 262–268"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 236–237 (Lugalbanda myths overview)" }

lacunae:
  - source: etcsl
    location: "lines 1–30"
    what_is_missing: "Opening lines describing the army's march and Lugalbanda's initial illness partially damaged in Nippur manuscripts"
    in_tradition_fills_available: "partial, Ur fragments preserve some of the opening but with divergent wording"
  - source: etcsl
    location: "lines 280–320"
    what_is_missing: "Sections describing divine healing interventions unclear; transitions between Utu, Inanna, and Suen episodes fragmentary"
    in_tradition_fills_available: "partial, composite reconstruction from Nippur and Ur fragments covers most gaps but some lines remain uncertain"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "ETCSL composite reconstructed from Nippur and Ur fragments provides the most complete available text"
  alternates:
    - source: vanstiphout-2003
      difference: "Vanstiphout's edition notes divergences between Nippur and Ur fragments in the healing sequence and wilderness-survival sections"

entities_glossary:
  - name: "Lugalbanda"
    role: hero
    first_mention_gloss_candidate: "soldier in Enmerkar's army and future king of Uruk, left for dead in a mountain cave"
  - name: "Enmerkar (𒂗𒈨𒅕𒃸)"
    role: hero
    first_mention_gloss_candidate: "king of Uruk who leads the army toward Aratta; Lugalbanda serves under him"
  - name: "Utu / Shamash (𒀭𒌓)"
    role: deity
    first_mention_gloss_candidate: "sun god who aids Lugalbanda's healing in the wilderness"
  - name: "Inanna (𒀭𒈹)"
    role: deity
    first_mention_gloss_candidate: "goddess who contributes to Lugalbanda's divine restoration"
  - name: "Suen / Nanna (𒀭𒋀𒆠)"
    role: deity
    first_mention_gloss_candidate: "moon god who participates in healing Lugalbanda"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Fragments from both Nippur and Ur scribal schools indicate it circulated as a curriculum text in the linked Lugalbanda pair"
      source: "etcsl 1.8.2.1, manuscript list"
    - kind: scholarly-attention
      detail: "Vanstiphout's critical edition and extensive commentary confirm sustained scholarly engagement with the text"
      source: "vanstiphout-2003 pp. 171–213"
  function:
    - role: literary
      basis: "Explores the theme of individual endurance and isolation in a sophisticated narrative of abandonment and survival"
      source: "vanstiphout-2003 pp. 171–175 (introduction)"
    - role: theogonic
      basis: "The divine healing sequence demonstrates the collaborative intervention of Utu, Inanna, and Suen, illustrating individual piety rewarded"
      source: "etcsl 1.8.2.1, healing sections"
  cross_cultural_parallels:
    - other_culture: "Hebrew Bible"
      parallel: "Hero abandoned in wilderness and sustained by divine providence recalls Moses in the desert and Hagar's ordeal (Genesis 21)"
      source: "kramer-1961"
    - other_culture: "Roman"
      parallel: "Foundling hero left to die and miraculously preserved echoes Romulus and Remus"
      source: "jacobsen-1987"

comparative_hooks:
  - other_culture: "Hebrew Bible"
    parallel: "Hero abandoned in wilderness, sustained by divine providence — Moses, Hagar"
    source: "kramer-1961"
  - other_culture: "Roman"
    parallel: "Foundling hero left to die and miraculously preserved — Romulus and Remus"
    source: "jacobsen-1987"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2500

special_instructions: "This is the first half of a linked pair with Lugalbanda and the Anzud Bird. Flag the fragmentary state honestly. Emphasize Lugalbanda's isolation and the piety theme."
```

---

# Input file: briefs/27-lugalbanda-and-the-anzud-bird.yaml

```
chapter_number: 27
slug: "lugalbanda-and-the-anzud-bird"
title: "Lugalbanda and the Anzud Bird"
chapter_anchor: "ch-27-lugalbanda-and-the-anzud-bird"

sources:
  primary:
    - id: etcsl
      loc: "1.8.2.2, composite text"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.8.2.2"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.8.2.2"
    - id: vanstiphout-2003
      loc: "pp. 215–275"
      translator_edition: "Vanstiphout 2003"
      identifier: "ISBN 9781589830837"
      url_or_file: ~
    - id: black-2004
      loc: "pp. 12–22"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
    - id: jacobsen-1987
      loc: "pp. 320–344"
      translator_edition: "Jacobsen 1987"
      identifier: "ISBN 9780300072785"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 236–238 (Lugalbanda and the Anzud bird)" }

lacunae:
  - source: etcsl
    location: "lines 1–15"
    what_is_missing: "Opening lines partially damaged; initial context for Lugalbanda's separation from the army fragmentary"
    in_tradition_fills_available: "yes, multiple OB manuscripts overlap to restore most of the opening"
  - source: etcsl
    location: "lines 350–380"
    what_is_missing: "Minor gaps in the passage where Lugalbanda delivers Enmerkar's message to Inanna"
    in_tradition_fills_available: "yes, composite reconstruction from heavily attested manuscripts covers the gaps"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Substantially intact across numerous OB manuscripts; ETCSL composite is the standard scholarly text"
  alternates:
    - source: jacobsen-1987
      difference: "Jacobsen's literary translation emphasizes poetic rhythm and occasionally paraphrases where the composite has minor damage"
    - source: vanstiphout-2003
      difference: "Vanstiphout's critical edition documents minor variant readings in the Anzud-encounter and gift-granting scenes"

entities_glossary:
  - name: "Lugalbanda"
    role: hero
    first_mention_gloss_candidate: "pious soldier and future king of Uruk who wins supernatural speed by honoring the Anzud bird's chick"
  - name: "Anzud / Anzu"
    role: being
    first_mention_gloss_candidate: "enormous divine eagle whose nest Lugalbanda discovers in the mountains"
  - name: "Inanna (𒀭𒈹)"
    role: deity
    first_mention_gloss_candidate: "patron goddess of Uruk to whom Lugalbanda delivers Enmerkar's message"
  - name: "Enmerkar (𒂗𒈨𒅕𒃸)"
    role: hero
    first_mention_gloss_candidate: "king of Uruk whose stalled campaign depends on Lugalbanda's speed as messenger"
  - name: "Uruk / Unug (𒌷𒀕)"
    role: place
    first_mention_gloss_candidate: "great city of southern Mesopotamia, seat of Enmerkar's kingship"
  - name: "Aratta"
    role: place
    first_mention_gloss_candidate: "distant wealthy city that Enmerkar's army is campaigning against"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: attestation-volume
      detail: "Heavily attested in OB scribal curricula from Nippur and other centers, one of the most copied Sumerian narrative poems"
      source: "etcsl 1.8.2.2, manuscript list"
    - kind: scholarly-attention
      detail: "Jacobsen devotes twenty-five pages to a literary translation; Vanstiphout provides sixty pages of critical edition and commentary"
      source: "jacobsen-1987 pp. 320–344; vanstiphout-2003 pp. 215–275"
  function:
    - role: literary
      basis: "Masterful narrative of encounter, reciprocity, and reward — among the finest examples of Sumerian storytelling"
      source: "vanstiphout-2003 pp. 215–220 (introduction)"
    - role: didactic
      basis: "Demonstrates that piety and reciprocity toward the divine are rewarded with supernatural gifts; Lugalbanda's humility contrasts with martial valor"
      source: "etcsl 1.8.2.2, Anzud-encounter sequence"
  cross_cultural_parallels:
    - other_culture: "Arabic (1001 Nights)"
      parallel: "Hero befriends a magical bird of enormous size — Sinbad and the Roc"
      source: "vanstiphout-2003"
    - other_culture: "Hindu"
      parallel: "Divine eagle granting boons parallels Garuda, the solar eagle-mount of Vishnu"
      source: "jacobsen-1987"

comparative_hooks:
  - other_culture: "Arabic (1001 Nights)"
    parallel: "Hero befriends enormous magical bird — Sinbad and the Roc"
    source: "vanstiphout-2003"
  - other_culture: "Hindu"
    parallel: "Divine eagle granting supernatural boons — Garuda tradition"
    source: "jacobsen-1987"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 3000

special_instructions: "This is the second half of a linked pair with Lugalbanda in the Mountain Cave. Emphasize the reciprocity theme: Lugalbanda's care for the chick earns the Anzud's gift of speed. The narrative arc from abandoned soldier to indispensable messenger should be clear."
```

---

# Input file: briefs/28-eridu-flood-story.yaml

```
chapter_number: 28
slug: "eridu-flood-story"
title: "The Flood Story: The Eridu Genesis"
chapter_anchor: "ch-28-eridu-flood-story"

sources:
  primary:
    - id: etcsl
      loc: "1.7.4, composite text (fragmentary)"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.7.4"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.7.4"
    - id: jacobsen-1987
      loc: "pp. 145–150"
      translator_edition: "Jacobsen 1987"
      identifier: "ISBN 9780300072785"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 97–101 (Sumerian flood story and paradise motif)" }
    - { id: black-2004, loc: "pp. 284–285 (brief discussion of Eridu Genesis)" }

lacunae:
  - source: etcsl
    location: "columns i–ii (opening)"
    what_is_missing: "Creation of humans, establishment of cities, and institution of kingship largely lost; only fragments of the antediluvian section survive"
    in_tradition_fills_available: "no, sole manuscript CBS 10673 is the only Sumerian witness; Akkadian Atrahasis is a distinct tradition and must not be used to fill gaps"
  - source: etcsl
    location: "column iii (flood narrative)"
    what_is_missing: "The divine decision to destroy humanity and Enki's warning to Ziusudra survive only in broken passages; details of the boat and the flood itself are largely lost"
    in_tradition_fills_available: "no, no other Sumerian manuscripts preserve these sections"
  - source: etcsl
    location: "column vi (ending)"
    what_is_missing: "Ziusudra's apotheosis and settlement in Dilmun fragmentary; the concluding lines are damaged"
    in_tradition_fills_available: "no, sole manuscript only"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "Sole manuscript CBS 10673 is the only Sumerian witness; all editions depend on this single tablet"
  alternates:
    - source: jacobsen-1987
      difference: "Jacobsen's literary translation bridges gaps with interpretive paraphrase more freely than ETCSL's conservative rendering"

entities_glossary:
  - name: "Ziusudra"
    role: hero
    first_mention_gloss_candidate: "pious king who survives the flood by building a boat at Enki's instruction, granted immortality"
  - name: "Enki (𒂗𒆠)"
    role: deity
    first_mention_gloss_candidate: "god of wisdom and freshwater who warns Ziusudra of the coming flood through a reed wall"
  - name: "Enlil (𒀭𒂗𒆤)"
    role: deity
    first_mention_gloss_candidate: "chief god of the pantheon who decrees the flood to destroy humanity"
  - name: "Dilmun (𒉌𒌇)"
    role: place
    first_mention_gloss_candidate: "paradise land where Ziusudra is settled after the flood, granted eternal life"

cultural_relevance:
  centrality: central
  centrality_evidence:
    - kind: scholarly-attention
      detail: "Despite extreme fragmentation, the text has received massive scholarly attention as the earliest known flood narrative"
      source: "jacobsen-1987 pp. 145–150"
    - kind: attestation-volume
      detail: "Sole manuscript CBS 10673 (Nippur), but its uniqueness as the Sumerian flood account gives it outsized importance"
      source: "etcsl 1.7.4, manuscript note"
  function:
    - role: cosmological
      basis: "Describes the divine destruction and renewal of the world, establishing the flood as a cosmological boundary event"
      source: "etcsl 1.7.4, column iii"
    - role: eschatological
      basis: "Ziusudra's translation to immortal life in Dilmun provides the Sumerian template for the exceptional human who escapes death"
      source: "jacobsen-1987 pp. 148–150"
  cross_cultural_parallels:
    - other_culture: "Hebrew Bible"
      parallel: "Noah's flood (Genesis 6–9): divine decision to destroy, one righteous man warned, boat survival, covenant afterward"
      source: "kramer-1961"
    - other_culture: "Akkadian"
      parallel: "Utnapishtim in Gilgamesh XI and Atrahasis epic — comparative only, these are distinct Akkadian traditions not to be conflated with the Sumerian text"
      source: "george-2003"
    - other_culture: "Greek"
      parallel: "Deucalion and Pyrrha: divine flood sent to destroy humanity, single pious couple survives by boat"
      source: "jacobsen-1987"

comparative_hooks:
  - other_culture: "Hebrew Bible"
    parallel: "Noah's flood — divine destruction, righteous survivor, boat, renewal"
    source: "kramer-1961"
  - other_culture: "Akkadian"
    parallel: "Utnapishtim and Atrahasis — comparative only, distinct traditions"
    source: "george-2003"
  - other_culture: "Greek"
    parallel: "Deucalion flood — divine destruction, pious survivor by boat"
    source: "jacobsen-1987"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 1200

special_instructions: "Very fragmentary. Do not reconstruct from Akkadian Atrahasis or Gilgamesh XI — those are out of scope. Be transparent about what is missing."
```

---

# Input file: briefs/29-ningishzidas-journey.yaml

```
chapter_number: 29
slug: "ningishzidas-journey"
title: "Ningishzida's Journey to the Nether World"
chapter_anchor: "ch-29-ningishzidas-journey"

sources:
  primary:
    - id: etcsl
      loc: "1.7.3, composite text (fragmentary)"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 1.7.3"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.7.3"
  secondary:
    - { id: jacobsen-1987, loc: "pp. 56–63 (Ningishzida and underworld deities)" }
    - { id: kramer-1961, loc: "pp. 90–92 (underworld journey motifs)" }
    - { id: black-2004, loc: "pp. 280–282 (brief discussion)" }

lacunae:
  - source: etcsl
    location: "opening columns"
    what_is_missing: "Context for Ningishzida's seizure by the galla demons largely lost; circumstances of his descent unclear"
    in_tradition_fills_available: "no, OB Nippur manuscripts are the only witnesses and they are highly fragmentary"
  - source: etcsl
    location: "central section (lamentation passages)"
    what_is_missing: "Sister's and mother's laments through the stations of descent substantially broken; only fragments of individual lament stanzas survive"
    in_tradition_fills_available: "no, no overlapping manuscripts fill the gaps"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "Fragmentary OB Nippur manuscripts are the sole witnesses; ETCSL composite represents the best available reconstruction"
  alternates:
    - source: jacobsen-1987
      difference: "Jacobsen provides interpretive context and paraphrases the fragmentary passages more freely to extract narrative continuity"

entities_glossary:
  - name: "Ningishzida (𒀭𒊩𒌆𒄑𒍣𒁕)"
    role: deity
    first_mention_gloss_candidate: "underworld god, lord of the good tree, seized by demons and dragged to the nether world"
  - name: "galla (𒃲𒆷)"
    role: being
    first_mention_gloss_candidate: "underworld demons who seize Ningishzida and escort him to the land of the dead"

cultural_relevance:
  centrality: marginal
  centrality_evidence:
    - kind: attestation-volume
      detail: "Fewer manuscript copies survive compared to major underworld compositions; fragmentary state limits scholarly reconstruction"
      source: "etcsl 1.7.3, manuscript list"
    - kind: scholarly-attention
      detail: "Receives occasional treatment in discussions of underworld journey texts but lacks a dedicated critical edition"
      source: "jacobsen-1987 pp. 56–63"
  function:
    - role: eschatological
      basis: "Depicts a god's forced journey to the underworld, contributing to the Sumerian understanding of the nether world as inescapable even for deities"
      source: "etcsl 1.7.3"
    - role: ritual-aetiological
      basis: "The lamentation structure suggests connection to ritual wailing for dying gods, paralleling the Dumuzid and Inanna traditions"
      source: "jacobsen-1987 pp. 56–58"
  cross_cultural_parallels:
    - other_culture: "Sumerian (internal)"
      parallel: "Divine descent parallels Inanna's own Descent to the Nether World, with similar galla-demon seizure and lamentation motifs"
      source: "etcsl"
    - other_culture: "Greek"
      parallel: "Forced journey to the underworld with lamentation echoes Orpheus's descent and Persephone's abduction"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Sumerian (internal)"
    parallel: "Galla-demon seizure and descent — mirrors Inanna's Descent structure"
    source: "etcsl"
  - other_culture: "Greek"
    parallel: "Divine descent to underworld with lamentation — Orpheus, Persephone"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 800

special_instructions: "Highly fragmentary — be transparent about gaps and do not over-reconstruct. Note structural parallels to Inanna's Descent but avoid conflating the two traditions."
```

---

# Input file: briefs/30-death-of-ur-namma.yaml

```
chapter_number: 30
slug: "death-of-ur-namma"
title: "The Death of Ur-Namma"
chapter_anchor: "ch-30-death-of-ur-namma"

sources:
  primary:
    - id: etcsl
      loc: "2.4.1.1, composite text"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 2.4.1.1"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.2.4.1.1"
    - id: fluckiger-hawker-1999
      loc: "full critical edition"
      translator_edition: "Flückiger-Hawker 1999"
      identifier: "ISBN 9783727812446"
      url_or_file: ~
  secondary:
    - { id: jacobsen-1987, loc: "pp. 380–385 (underworld geography and royal afterlife)" }
    - { id: kramer-1961, loc: "pp. 128–131 (Ur-Namma and the underworld)" }
    - { id: black-2004, loc: "pp. 56–60 (brief discussion of royal underworld texts)" }

lacunae:
  - source: etcsl
    location: "lines 1–30"
    what_is_missing: "Opening section describing Ur-Namma's death in battle partially damaged; circumstances of the king's fall fragmentary"
    in_tradition_fills_available: "partial, Flückiger-Hawker's reconstruction from Nippur tablets restores most of the sequence"
  - source: etcsl
    location: "lines 100–140"
    what_is_missing: "Details of the journey to the underworld and arrival at the gates have minor gaps"
    in_tradition_fills_available: "yes, overlapping Nippur manuscripts allow reconstruction of most of the passage"

variants:
  classification: single-prevalent
  prevalent_version:
    source: fluckiger-hawker-1999
    why_prevalent: "Flückiger-Hawker's critical edition provides the most thorough philological treatment, reconstructed from Nippur tablets"
  alternates:
    - source: etcsl
      difference: "ETCSL composite follows Flückiger-Hawker closely but presents a slightly more conservative text in damaged passages"

entities_glossary:
  - name: "Ur-Namma"
    role: hero
    first_mention_gloss_candidate: "king of Ur and founder of the Third Dynasty of Ur, who dies in battle and descends to the underworld"
  - name: "Ereshkigal (𒀭𒊩𒌆𒆠𒃲)"
    role: deity
    first_mention_gloss_candidate: "queen of the underworld to whom Ur-Namma presents gifts upon his arrival"
  - name: "Gilgamesh (𒄑𒂆𒈦)"
    role: hero
    first_mention_gloss_candidate: "legendary king of Uruk who serves as a judge in the underworld"
  - name: "Ningishzida (𒀭𒊩𒌆𒄑𒍣𒁕)"
    role: deity
    first_mention_gloss_candidate: "underworld deity who serves as a judge of the dead alongside Gilgamesh"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: scholarly-attention
      detail: "Flückiger-Hawker's full critical edition and sustained scholarly interest in the text's unique genre confirm its importance"
      source: "fluckiger-hawker-1999"
    - kind: attestation-volume
      detail: "Multiple Nippur tablets preserve the text, attesting its place in the scribal tradition"
      source: "etcsl 2.4.1.1, manuscript list"
  function:
    - role: eschatological
      basis: "Provides the most detailed Sumerian account of a king's entry into the underworld, gift-giving to its rulers, and posthumous status"
      source: "etcsl 2.4.1.1, underworld-arrival sections"
    - role: royal-legitimation
      basis: "Elevates Ur-Namma's status after death: even in the underworld, the king retains dignity and is honored by its rulers"
      source: "fluckiger-hawker-1999, commentary"
  cross_cultural_parallels:
    - other_culture: "Egyptian"
      parallel: "Royal afterlife judgment and status in the underworld parallels the Egyptian Book of the Dead and royal mortuary texts"
      source: "jacobsen-1987"
    - other_culture: "Greek"
      parallel: "King encountering the dead and receiving status in the underworld echoes Odyssey Book 11, where Agamemnon retains royal identity in Hades"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Egyptian"
    parallel: "Royal afterlife — king judged and honored among the dead, Book of the Dead"
    source: "jacobsen-1987"
  - other_culture: "Greek"
    parallel: "Royal shade in the underworld — Agamemnon in Odyssey Book 11"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2000

special_instructions: "ETCSL section 2 (royal) — included per scope policy for substantial underworld narrative."
```

---

# Input file: briefs/31-debate-hoe-and-plough.yaml

```
chapter_number: 31
slug: "debate-hoe-and-plough"
title: "The Debate between Hoe and Plough"
chapter_anchor: "ch-31-debate-hoe-and-plough"

sources:
  primary:
    - id: etcsl
      loc: "5.3.1, composite text, lines 1–190"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 5.3.1"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.5.3.1"
    - id: black-2004
      loc: "pp. 210–218"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: civil-1994, loc: "passim (agricultural terminology and tool vocabulary)" }
    - { id: kramer-1961, loc: "pp. 72–73 (overview of debate genre)" }

lacunae:
  - source: etcsl
    location: "lines 1–10"
    what_is_missing: "Minor damage to the cosmogonic prologue opening"
    in_tradition_fills_available: "yes, multiple Nippur school copies overlap and restore the prologue nearly completely"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Nearly complete composite text assembled from numerous Nippur school copies with strong agreement"
  alternates:
    - source: black-2004
      difference: "Minor rendering differences in the verdict formula; no substantive narrative divergence"

entities_glossary:
  - name: "al/Hoe (𒀠)"
    role: artifact
    first_mention_gloss_candidate: "the hoe, essential agricultural tool for digging irrigation channels and breaking ground"
  - name: "apin/Plough (𒀳)"
    role: artifact
    first_mention_gloss_candidate: "the seeder-plough, prestige implement of large-scale cereal agriculture"
  - name: "Enlil (𒀭𒂗𒆤)"
    role: deity
    first_mention_gloss_candidate: "king of the gods, lord of the wind and authority, who renders the final verdict"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Numerous copies recovered from Nippur and other OB school sites confirm its place in the scribal curriculum"
      source: "etcsl 5.3.1, manuscript list"
    - kind: scholarly-attention
      detail: "Civil's agricultural studies and Black's anthology both treat the text as a canonical example of the debate genre"
      source: "civil-1994 passim"
  function:
    - role: didactic
      basis: "Teaches scribal students through competitive argument the merits and social roles of two key agricultural tools"
      source: "etcsl 5.3.1, lines 50–170"
    - role: cosmological
      basis: "The prologue establishes a hierarchy of created things, situating tools within the divine order of civilisation"
      source: "etcsl 5.3.1, lines 1–20"
  cross_cultural_parallels:
    - other_culture: "Medieval European"
      parallel: "Debate poems such as The Owl and the Nightingale use the same adversarial structure with a judge rendering a verdict"
      source: "black-2004"
    - other_culture: "Latin/Medieval"
      parallel: "The conflictus genre (e.g., Conflictus Veris et Hiemis) shares the pattern of personified entities arguing before a divine or royal arbiter"
      source: "black-2004"

comparative_hooks:
  - other_culture: "Medieval European"
    parallel: "Adversarial debate poem with judicial verdict (The Owl and the Nightingale)"
    source: "black-2004"
  - other_culture: "Latin/Medieval"
    parallel: "Conflictus genre of personified seasonal or material disputes"
    source: "black-2004"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2000

special_instructions: "Preserve the dialogue/debate structure. Note the cosmogonic prologue if present."
```

---

# Input file: briefs/32-debate-ewe-and-grain.yaml

```
chapter_number: 32
slug: "debate-ewe-and-grain"
title: "The Debate between Ewe and Grain"
chapter_anchor: "ch-32-debate-ewe-and-grain"

sources:
  primary:
    - id: etcsl
      loc: "5.3.2, composite text, lines 1–192"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 5.3.2"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.5.3.2"
    - id: black-2004
      loc: "pp. 219–225"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 72–73 (cosmogonic prologue and primitive humanity motif)" }
    - { id: jacobsen-1987, loc: "pp. 155–160 (discussion of early humanity without divine gifts)" }

lacunae:
  - source: etcsl
    location: "lines 100–115"
    what_is_missing: "Some lines in the central exchange partially damaged"
    in_tradition_fills_available: "yes, overlapping Nippur manuscripts restore most of the passage"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Well-preserved composite from multiple OB school tablets with consistent text across witnesses"
  alternates:
    - source: black-2004
      difference: "Minor translational choices in the cosmogonic prologue; no substantive narrative divergence"

entities_glossary:
  - name: "Lahar/Ewe (𒇻)"
    role: deity
    first_mention_gloss_candidate: "divine personification of pastoralism and livestock, created by the gods for humanity's benefit"
  - name: "Ashnan/Grain (𒀭𒀊𒉣)"
    role: deity
    first_mention_gloss_candidate: "divine personification of cereal agriculture, created by the gods to nourish humanity"
  - name: "Enlil (𒀭𒂗𒆤)"
    role: deity
    first_mention_gloss_candidate: "king of the gods who participates in the creation of Ewe and Grain"
  - name: "Enki (𒂗𒆠)"
    role: deity
    first_mention_gloss_candidate: "god of wisdom and craft who helps fashion the conditions for agriculture and herding"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Multiple OB copies from Nippur scribal schools confirm wide circulation as a standard curriculum text"
      source: "etcsl 5.3.2, manuscript list"
    - kind: scholarly-attention
      detail: "The cosmogonic prologue describing primitive humanity before divine gifts is one of the most cited passages in Sumerological literature"
      source: "kramer-1961 pp. 72–73"
  function:
    - role: didactic
      basis: "Teaches through competitive argument the relative merits of pastoralism and agriculture as pillars of civilisation"
      source: "etcsl 5.3.2, lines 80–180"
    - role: cosmological
      basis: "The prologue describes an era when humans lived like animals, before the gods created Ewe and Grain to sustain them"
      source: "etcsl 5.3.2, lines 1–40"
  cross_cultural_parallels:
    - other_culture: "Hebrew Bible"
      parallel: "Cain (farmer) and Abel (shepherd) conflict in Genesis 4 mirrors the pastoral-vs-agricultural tension, though with a reversed outcome"
      source: "kramer-1961"
    - other_culture: "Global (widespread)"
      parallel: "Debates between nomadic pastoralism and settled farming recur across world mythologies and wisdom traditions"
      source: "black-2004"

comparative_hooks:
  - other_culture: "Hebrew Bible"
    parallel: "Cain and Abel: shepherd vs. farmer conflict with divine judgement"
    source: "kramer-1961"
  - other_culture: "Global (widespread)"
    parallel: "Pastoral vs. agricultural debates as a universal myth motif"
    source: "black-2004"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2000

special_instructions: "The cosmogonic prologue describing humanity before divine gifts is crucial — do not truncate it."
```

---

# Input file: briefs/33-debate-winter-and-summer.yaml

```
chapter_number: 33
slug: "debate-winter-and-summer"
title: "The Debate between Winter and Summer"
chapter_anchor: "ch-33-debate-winter-and-summer"

sources:
  primary:
    - id: etcsl
      loc: "5.3.3, composite text, lines 1–310"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 5.3.3"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.5.3.3"
    - id: black-2004
      loc: "pp. 226–233"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: civil-1994, loc: "passim (agricultural calendar and seasonal terminology)" }
    - { id: kramer-1961, loc: "pp. 72–73 (overview of the debate genre)" }

lacunae:
  - source: etcsl
    location: "lines 140–155"
    what_is_missing: "Several lines in the central exchange partially broken"
    in_tradition_fills_available: "yes, overlapping Nippur school tablets restore the passage in large part"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Mostly complete composite text from frequent Nippur school copies with good inter-manuscript agreement"
  alternates:
    - source: black-2004
      difference: "Minor rendering differences in seasonal epithets; no substantive narrative divergence"

entities_glossary:
  - name: "Enten (𒂗𒋼𒀭)"
    role: deity
    first_mention_gloss_candidate: "divine personification of Winter, associated with rain, floods, and the fertile season"
  - name: "Emesh (𒂍𒈩)"
    role: deity
    first_mention_gloss_candidate: "divine personification of Summer, associated with harvest, heat, and ripening"
  - name: "Enlil (𒀭𒂗𒆤)"
    role: deity
    first_mention_gloss_candidate: "king of the gods who created the seasons and renders the final verdict in favour of Winter"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Frequent in Nippur school tablets, confirming its standard place in the OB scribal curriculum"
      source: "etcsl 5.3.3, manuscript list"
    - kind: scholarly-attention
      detail: "Regularly cited in studies of Mesopotamian agricultural religion and the debate genre"
      source: "civil-1994 passim"
  function:
    - role: didactic
      basis: "Teaches the relative contributions of the wet and dry seasons to agricultural productivity through competitive argument"
      source: "etcsl 5.3.3, lines 50–280"
    - role: cosmological
      basis: "Frames the seasonal cycle as a deliberate divine creation with each season assigned specific duties by Enlil"
      source: "etcsl 5.3.3, lines 1–30"
  cross_cultural_parallels:
    - other_culture: "Greek"
      parallel: "The Demeter/Persephone myth explains seasonal cycles through divine narrative, as does the Enten/Emesh contest"
      source: "black-2004"
    - other_culture: "Medieval European"
      parallel: "The Conflictus Veris et Hiemis (Debate of Spring and Winter) preserves an almost identical literary structure"
      source: "black-2004"

comparative_hooks:
  - other_culture: "Greek"
    parallel: "Seasonal-cycle myth (Demeter/Persephone) as divine explanation for agricultural rhythm"
    source: "black-2004"
  - other_culture: "Medieval European"
    parallel: "Conflictus Veris et Hiemis: personified seasonal debate with verdict"
    source: "black-2004"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2000

special_instructions: "Clarify the Sumerian seasonal calendar (Enten = wet/winter, Emesh = dry/summer) for readers unfamiliar with southern Mesopotamian agriculture. The verdict favours Winter because rain and flooding are the basis of irrigation farming."
```

---

# Input file: briefs/34-debate-bird-and-fish.yaml

```
chapter_number: 34
slug: "debate-bird-and-fish"
title: "The Debate between Bird and Fish"
chapter_anchor: "ch-34-debate-bird-and-fish"

sources:
  primary:
    - id: etcsl
      loc: "5.3.5, composite text, lines 1–190"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 5.3.5"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.5.3.5"
    - id: black-2004
      loc: "pp. 234–240"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 72–73 (overview of the debate genre)" }
    - { id: civil-1994, loc: "passim (vocabulary of fauna and natural resources)" }

lacunae:
  - source: etcsl
    location: "lines 85–90"
    what_is_missing: "Minor damage to a few lines in the central exchange"
    in_tradition_fills_available: "yes, the text is exceptionally well-preserved and overlapping copies fill almost all gaps"

variants:
  classification: single-prevalent
  prevalent_version:
    source: etcsl
    why_prevalent: "Exceptionally well-preserved composite text with strong manuscript agreement across witnesses"
  alternates:
    - source: black-2004
      difference: "Minor translational choices in animal epithets; no substantive narrative divergence"

entities_glossary:
  - name: "Mušen/Bird (𒄷)"
    role: deity
    first_mention_gloss_candidate: "divine personification of Bird, who claims superiority through flight and song"
  - name: "Ku₆/Fish (𒄩)"
    role: deity
    first_mention_gloss_candidate: "divine personification of Fish, who claims superiority through purity and abundance in the waters"
  - name: "Enki (𒂗𒆠)"
    role: deity
    first_mention_gloss_candidate: "god of wisdom and freshwater who renders the final verdict in favour of Bird"

cultural_relevance:
  centrality: significant
  centrality_evidence:
    - kind: attestation-volume
      detail: "Well-preserved with multiple copies, indicating active use in OB scribal schools"
      source: "etcsl 5.3.5, manuscript list"
    - kind: scholarly-attention
      detail: "Praised for its rich vocabulary of natural history and its vivid portrayal of animal behaviour"
      source: "black-2004 pp. 234–240"
  function:
    - role: didactic
      basis: "Teaches scribal students through competitive argument about the natural hierarchy and the merits of different creatures"
      source: "etcsl 5.3.5, lines 30–170"
    - role: literary
      basis: "Outstanding literary composition with vivid imagery, escalating rhetoric, and dramatic action (Bird destroys Fish's eggs)"
      source: "etcsl 5.3.5, lines 140–170"
  cross_cultural_parallels:
    - other_culture: "Greek (Aesop)"
      parallel: "Animal fable debates where creatures argue their merits, with a moral or judicial resolution"
      source: "black-2004"
    - other_culture: "Indian (Panchatantra)"
      parallel: "Animal contest narratives that teach through the personification of natural creatures"
      source: "black-2004"

comparative_hooks:
  - other_culture: "Greek (Aesop)"
    parallel: "Animal fable with moral judgement and hierarchy among creatures"
    source: "black-2004"
  - other_culture: "Indian (Panchatantra)"
    parallel: "Didactic animal contest narratives"
    source: "black-2004"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 2000

special_instructions: "Highlight the escalation from verbal argument to physical aggression (Bird destroys Fish's eggs). Note Enki as judge rather than Enlil, reflecting the aquatic domain of the dispute."
```

---

# Input file: briefs/35-debate-copper-and-silver.yaml

```
chapter_number: 35
slug: "debate-copper-and-silver"
title: "The Debate between Copper and Silver"
chapter_anchor: "ch-35-debate-copper-and-silver"

sources:
  primary:
    - id: etcsl
      loc: "5.3.6, composite text, fragmentary"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 5.3.6"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.5.3.6"
    - id: black-2004
      loc: "pp. 241–243"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 72–73 (overview of the debate genre)" }

lacunae:
  - source: etcsl
    location: "final section (verdict)"
    what_is_missing: "The verdict and conclusion of the debate are entirely lost"
    in_tradition_fills_available: "no, no known manuscript preserves the ending"
  - source: etcsl
    location: "multiple passages throughout"
    what_is_missing: "Significant breaks and gaps across the surviving tablets"
    in_tradition_fills_available: "no, fewer copies survive than for other debate poems"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "Only available composite, reconstructed from limited fragmentary witnesses"
  alternates:
    - source: black-2004
      difference: "Translation covers only the preserved portions; no additional witnesses available"

entities_glossary:
  - name: "Urudu/Copper (𒌑𒆕)"
    role: artifact
    first_mention_gloss_candidate: "personified Copper, who argues superiority through practical utility in weapons and tools"
  - name: "Ku-babbar/Silver (𒆬𒌈)"
    role: artifact
    first_mention_gloss_candidate: "personified Silver, who argues superiority through prestige, beauty, and exchange value"

cultural_relevance:
  centrality: marginal
  centrality_evidence:
    - kind: attestation-volume
      detail: "Fewer copies survive than for other debate poems, suggesting more limited circulation"
      source: "etcsl 5.3.6, manuscript list"
    - kind: scholarly-attention
      detail: "Receives less scholarly treatment than the major debates, though noted for its economic theme"
      source: "black-2004 pp. 241–243"
  function:
    - role: didactic
      basis: "Explores the tension between practical utility and prestige value — a question central to Mesopotamian economic life"
      source: "etcsl 5.3.6, surviving lines"
  cross_cultural_parallels:
    - other_culture: "Classical/Modern economic thought"
      parallel: "The use-value vs. exchange-value distinction (Adam Smith, Marx) is prefigured in Copper's utility argument vs. Silver's prestige claim"
      source: "black-2004"
    - other_culture: "Ancient Near Eastern (widespread)"
      parallel: "Metal hierarchy debates reflect the same material ranking found in Hesiod's Ages of Man (gold, silver, bronze, iron)"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Classical/Modern economic thought"
    parallel: "Use-value vs. exchange-value debate prefigured in Copper vs. Silver"
    source: "black-2004"
  - other_culture: "Greek (Hesiod)"
    parallel: "Metal hierarchy in the Ages of Man myth"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 800

special_instructions: "Verdict is missing — note this honestly. Do not invent an outcome."
```

---

# Input file: briefs/36-debate-date-palm-and-tamarisk.yaml

```
chapter_number: 36
slug: "debate-date-palm-and-tamarisk"
title: "The Debate between Date Palm and Tamarisk"
chapter_anchor: "ch-36-debate-date-palm-and-tamarisk"

sources:
  primary:
    - id: etcsl
      loc: "5.3.7, composite text, fragmentary"
      translator_edition: "ETCSL transliteration and translation"
      identifier: "ETCSL 5.3.7"
      url_or_file: "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.5.3.7"
    - id: black-2004
      loc: "pp. 244–246"
      translator_edition: "Black et al. 2004"
      identifier: "ISBN 9780199296330"
      url_or_file: ~
  secondary:
    - { id: kramer-1961, loc: "pp. 72–73 (overview of the debate genre)" }

lacunae:
  - source: etcsl
    location: "multiple passages throughout"
    what_is_missing: "Substantial gaps across the surviving tablets; much of the central argument is lost"
    in_tradition_fills_available: "no, fewer copies survive and no known manuscript fills the major gaps"
  - source: etcsl
    location: "final section"
    what_is_missing: "Verdict and conclusion poorly preserved or lost"
    in_tradition_fills_available: "no, the ending is not securely attested"

variants:
  classification: single-prevalent-reconstructed
  prevalent_version:
    source: etcsl
    why_prevalent: "Only available composite, reconstructed from limited fragmentary witnesses"
  alternates:
    - source: black-2004
      difference: "Translation covers only the preserved portions; no additional witnesses expand the text"

entities_glossary:
  - name: "Gišimmar/Date Palm (𒄑𒈠)"
    role: artifact
    first_mention_gloss_candidate: "personified Date Palm, the cultivated tree that provides fruit, syrup, and fibre — the supreme domesticated tree of Mesopotamia"
  - name: "Šinig/Tamarisk (𒄑𒆜)"
    role: artifact
    first_mention_gloss_candidate: "personified Tamarisk, the hardy wild tree used for ritual purification and fuel"

cultural_relevance:
  centrality: marginal
  centrality_evidence:
    - kind: attestation-volume
      detail: "Fewer copies survive than for the major debate poems, indicating more limited circulation in scribal schools"
      source: "etcsl 5.3.7, manuscript list"
    - kind: scholarly-attention
      detail: "Receives less independent scholarly treatment, though noted as part of the broader ANE tree-debate tradition"
      source: "black-2004 pp. 244–246"
  function:
    - role: didactic
      basis: "Explores the tension between cultivated and wild nature, domesticated utility versus natural resilience"
      source: "etcsl 5.3.7, surviving lines"
  cross_cultural_parallels:
    - other_culture: "Ancient Near Eastern (widespread)"
      parallel: "Tree debates between cultivated and wild species appear in Akkadian and later ANE wisdom literature, forming a recognisable sub-genre"
      source: "black-2004"
    - other_culture: "Global (widespread)"
      parallel: "The cultivated-vs-wild opposition recurs in fable and wisdom traditions worldwide (e.g., the oak and the reed in Aesop)"
      source: "kramer-1961"

comparative_hooks:
  - other_culture: "Ancient Near Eastern (widespread)"
    parallel: "ANE tree-debate tradition in Akkadian and later wisdom literature"
    source: "black-2004"
  - other_culture: "Greek (Aesop)"
    parallel: "Cultivated vs. wild tree fable (the oak and the reed)"
    source: "kramer-1961"

triangulation_databases:
  - ETCSL
  - CDLI
  - ORACC

target_length_words: 800

special_instructions: "Fragmentary — be transparent about gaps. Note the broader ANE tree-debate tradition that includes Akkadian parallels."
```
