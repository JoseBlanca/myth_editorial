# Stage 9 of 17: claims-factcheck
# Book: sumer
# Generated: 2026-04-12T17:54:32Z

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
    identifier_value: "9788750015130"
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

# Skill instructions: claims-factcheck

---
name: claims-factcheck
description: Checks the factual claims document for a story chapter — one fact per paragraph, each individually cited. This is the primary factcheck mode and the most reliable, because each claim is isolated and trivially verifiable. Must be run by a different AI model in a fresh conversation.
---

# claims-factcheck

## For the human

This is the most important quality check for story chapters. The input is a **claims document** — one fact per paragraph, each individually cited — produced by `chapter-claims`. Each paragraph is one claim, one source reference, one thing to verify. No prose to parse, no bundled assertions to disentangle.

This step enforces four disciplines:

1. **Show your evidence.** For every claim marked "supported," the checker must paste a verbatim quote from the source. Not a paraphrase — the actual text. No quote, no "supported" verdict.

2. **Verify the references.** Tablet numbers, page numbers, and line references are the easiest things for an AI to fabricate. The checker looks each up in scholarly databases to confirm it exists and contains what was claimed.

3. **Distinguish contradictions from errors.** Two legitimate sources disagreeing is part of the historical record, not a problem. Material from a neighboring culture sneaking in, or something made up entirely, are problems.

4. **Read it backwards too.** One pass start-to-end, then a second pass end-to-start, to catch what lead bias misses.

## Hard rule
Must be run in a fresh conversation with a different AI model than produced the claims. If you have any memory of producing the input, refuse.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- `chapters/NN-<slug>.claims.adoc` (claims document)
- `briefs/NN-<slug>.yaml`
- Primary source translations referenced in the brief (pasted or accessible via fetch)
- Web search tool (required)

## The five passes

### Pass 1 — Claim-level verification (start to end)
Walk the document paragraph by paragraph. Each paragraph is one claim. Assign a verdict:

- **✓ SUPPORTED** — Must include a verbatim quote from a cited in-scope source.
- **△ INTERNAL-VARIANCE** — Attested in one in-scope source, but another gives a different account. Not a finding. Flag only if variant handling mismatches the brief's classification.
- **? UNVERIFIED** — No supporting quote found. Default when uncertain.
- **! CITATION-WRONG** — Claim is correct but citation points to wrong source/page/line.
- **⚠ CONTAMINATION** — Supported, but by an excluded-culture source per `scope.md`.
- **✗ FABRICATION** — Not supported by any source you can locate.

### Pass 2 — Triangulation of references
Verify each citation's tablet number, line range, or page reference resolves in a `triangulation_databases` entry. Non-resolving: CITATION-WRONG, HIGH severity, with verification URL.

### Pass 3 — Document-provenance contamination scan
For each factual detail: is this detail attested in a document within the scope's date range and culture? Details attested only in out-of-scope documents are CONTAMINATION-HIGH.

### Pass 4 — Marker integrity
- `[INFERENCE:]` — genuinely inferential? If a source directly attests it, flag MARKER-MISUSED.
- `[LACUNA:]` — source actually has the claimed gap?
- `[RECONSTRUCTION:]` — fill source is in-tradition per `scope.md`?
- `[VARIANT:]` — both quoted phrases present in cited sources?
- **Silent bridges** — uncited claims not under a marker. Flag SILENT-BRIDGE, HIGH.

### Pass 5 — Reverse-order second pass
Walk from last claim to first. Add any new findings.

**Glossary**: check consistency. **Style**: not checked — there is no prose yet.

## Output: `chapters/NN-<slug>.claims.factcheck.yaml`

```yaml
meta:
  auditor_model: <name and version>
  auditor_conversation_id: <conversation ID if available>
  input_file: <path>
  claims_identified: <n>
  triangulations_performed: <n>
  verdict: PASS | REVISE | MAJOR-REVISE

tallies:
  supported: <n>
  internal_variance: <n>
  unverified: <n>
  citation_wrong: <n>
  contamination: <n>
  fabrication: <n>
  silent_bridges: <n>
  marker_issues: <n>
  glossary_violations: <n>

supported_claims:
  - claim_number: <n>
    claim: "<the claim>"
    source_id: <from sources.yaml>
    source_loc: <tablet/line/page>
    verbatim_quote: "<exact text from source>"

findings:
  - claim_number: <n>
    kind: UNVERIFIED | CITATION-WRONG | CONTAMINATION | FABRICATION | SILENT-BRIDGE | MARKER-MISUSED | MARKER-FABRICATED | GLOSSARY-VIOLATION | VARIANT-HANDLING-MISMATCH
    severity: HIGH | MEDIUM | LOW
    claim: "<the claim>"
    issue: <one sentence>
    evidence: <verbatim quote or triangulation URL>
    recommended_fix: <concrete>
```

## Verdict rules

Apply in order (first match wins):
- **MAJOR-REVISE**: ≥ 3 HIGH findings, or any contamination, or triangulation failures indicating fabricated references.
- **REVISE**: 1–2 HIGH, or > 3 MEDIUM, or any silent bridge.
- **PASS**: zero HIGH, zero silent bridges, ≤ 3 MEDIUM.

## Honesty self-check
Answer in `meta`:
1. Did I open every cited primary source, or skim? Name any I skimmed.
2. Did I triangulate every reference, or assume some? Name any assumed.
3. For every ✓, did I paste a real quote or pattern-match? Downgrade any pattern-matched.
4. Did I distinguish internal variance from contamination?
5. Am I the same model that produced the claims? If yes, this audit is invalid.

## Human review protocol
Review HIGH findings (~10 minutes), skim MEDIUM. Apply accepted fixes to produce `chapters/NN-<slug>.claims.approved.adoc`. Run `post-human-normalize` before proceeding to `chapter-draft`.

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
After human review and normalization: `chapters/NN-<slug>.claims.approved.adoc` to `chapter-draft`.

---

# Input file: chapters/01-enki-and-ninhursaja.claims.adoc

```
== Enki and Ninhursaja: The Paradise of Dilmun — Claims

// This is a claims document, not final prose. Each paragraph is one verifiable claim.
// Source: ETCSL 1.1.1, lines 1–278. Co-equal Nippur and Ur recensions.
// Variant classification: co-equal (Nippur/Ur manuscripts)

=== Setting and context

The composition "Enki and Ninhursaja" is catalogued as ETCSL 1.1.1 and survives in multiple Old Babylonian manuscript witnesses from both Nippur and Ur scribal schools.footnote:[ETCSL 1.1.1, composite text, lines 1–278; Black et al. 2004, pp. 38–50.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, composite text, lines 1–278

The ETCSL composite text follows the Nippur recension as its base but draws on Ur manuscripts to fill gaps and provide alternative readings.footnote:[ETCSL 1.1.1, editorial notes on manuscript base.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, editorial notes

[VARIANT: primary="ETCSL composite follows Nippur recension as base" | alt="Ur manuscripts preserve extended tribute passage (Dilmun trade goods) absent from Nippur recension, per Jacobsen 1987 pp. 181–204" | chosen: Nippur as base | reason: "ETCSL editorial decision; Ur tribute passage presented separately"]

=== Dilmun as paradise

The text opens by describing Dilmun as a land that is pure, clean, and bright — a place where there is no sickness, no old age, no death, and no predatory violence.footnote:[ETCSL 1.1.1, lines 1–30; Black et al. 2004, pp. 38–39.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 1–30

[LACUNA: Opening invocation partially damaged in Nippur manuscripts (lines 1–13) | source: etcsl 1.1.1, Nippur manuscripts | scholarly_reconstruction: Ur manuscripts preserve portions of the opening and are used to supplement the composite]

Dilmun is identified in Sumerian tradition with a real place — the island or region associated with modern Bahrain — known as a trade emporium linking Mesopotamia with the lands to the east.footnote:[Kramer 1961, pp. 54–59; Black et al. 2004, pp. 38–39.]
// EVIDENCE: source_id=kramer-1961 ; loc=pp. 54–59

In its primordial state, Dilmun has no fresh water: no river flows, no well yields water, no rain falls.footnote:[ETCSL 1.1.1, lines 13–28; Black et al. 2004, p. 39.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 13–28

=== Water provision

The goddess Ninsikila (an epithet of Ninhursaja as lady of Dilmun) appeals to Enki to provide Dilmun with fresh water.footnote:[ETCSL 1.1.1, lines 29–36; Jacobsen 1987, pp. 184–186.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 29–36

Enki commands the sun god Utu to bring fresh water from the earth, filling Dilmun's wells and irrigating its fields, transforming it into a garden paradise.footnote:[ETCSL 1.1.1, lines 37–52; Black et al. 2004, pp. 39–40.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 37–52

After the water provision, Dilmun becomes a prosperous harbour and trading port, with goods flowing in from Tukrish, Meluhha, and other foreign lands.footnote:[ETCSL 1.1.1, lines 53–63; Black et al. 2004, p. 40.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 53–63

[VARIANT: primary="Nippur recension: brief mention of trade" | alt="Ur manuscripts include an extended tribute passage detailing Dilmun trade goods, absent from the Nippur recension (Jacobsen 1987, pp. 186–188)" | chosen: both presented | reason: "Co-equal witnesses; Ur tribute passage should be presented as a clearly marked inset per brief instructions"]

=== Narrative sequence: Chain of births

Enki copulates with Ninhursaja; she conceives and after a gestation of nine days (rather than nine months) gives birth to the goddess Ninsar (Lady Greenery).footnote:[ETCSL 1.1.1, lines 64–78; Jacobsen 1987, pp. 188–190.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 64–78

[LACUNA: Transition between water-provision and first plant-eating episode partially broken in Nippur manuscripts (lines 64–78) | source: etcsl 1.1.1, Nippur manuscripts | scholarly_reconstruction: Ur manuscripts overlap but diverge in the tribute section]

Enki then copulates with his daughter Ninsar, who conceives and gives birth to the goddess Ninkurra (Lady Pasture) after the same accelerated nine-day gestation.footnote:[ETCSL 1.1.1, lines 79–100; Black et al. 2004, pp. 41–42.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 79–100

Enki copulates with his granddaughter Ninkurra, who gives birth to the goddess Uttu (the spider, goddess of weaving).footnote:[ETCSL 1.1.1, lines 101–120; Black et al. 2004, p. 42.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 101–120

Ninhursaja (or Nintur, as she is sometimes called in this passage) warns Uttu not to yield to Enki unless he brings her gifts of garden produce — cucumbers, apples, and grapes.footnote:[ETCSL 1.1.1, lines 121–140; Jacobsen 1987, pp. 191–193.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 121–140

Enki brings the required garden produce and Uttu opens the door to him; he copulates with her.footnote:[ETCSL 1.1.1, lines 141–155; Black et al. 2004, pp. 42–43.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 141–155

=== The forbidden plants

Ninhursaja removes Enki's semen from Uttu's body and plants it in the ground, where eight plants grow.footnote:[ETCSL 1.1.1, lines 156–175; Black et al. 2004, p. 43.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 156–175

Enki, aided by his minister Isimud (two-faced servant of Enki), discovers the eight plants one by one, determines their nature, and eats each of them.footnote:[ETCSL 1.1.1, lines 176–215; Jacobsen 1987, pp. 194–196.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 176–215

The act of eating the plants constitutes a transgression: Enki "decrees the fates" of the plants by consuming them, an act of appropriation that enrages Ninhursaja.footnote:[ETCSL 1.1.1, lines 210–220; Black et al. 2004, pp. 44–45.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 210–220

=== Curse and illness

Ninhursaja pronounces a curse of death on Enki, declaring that she will not look upon him with the "eye of life" until he is dying, and then she vanishes.footnote:[ETCSL 1.1.1, lines 216–225; Black et al. 2004, p. 45.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 216–225

After the curse, Enki falls gravely ill; eight parts of his body sicken, one for each plant he consumed.footnote:[ETCSL 1.1.1, lines 226–240; Jacobsen 1987, pp. 197–199.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 226–240

The great gods are unable to help; Enlil himself cannot cure Enki; the situation appears hopeless.footnote:[ETCSL 1.1.1, lines 241–248; Black et al. 2004, p. 46.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 241–248

The fox offers to bring Ninhursaja back and succeeds in persuading her to return.footnote:[ETCSL 1.1.1, lines 249–255; Jacobsen 1987, pp. 199–200.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 249–255

=== Eight healing deities

Ninhursaja seats Enki beside her vulva and asks him, one by one, which part of his body hurts.footnote:[ETCSL 1.1.1, lines 256–270; Black et al. 2004, pp. 47–49.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 256–270

For each of the eight ailing body parts, Ninhursaja gives birth to a healing deity whose name puns on the body part being cured — an aetiological explanation of these deities' origins and domains.footnote:[ETCSL 1.1.1, lines 256–278; Jacobsen 1987, pp. 200–203.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 256–278

Among the eight healing deities is Ninti, whose name means both "Lady of the Rib" and "Lady of Life" — a pun that has been compared to the biblical Eve, created from Adam's rib, whose name means "living."footnote:[Kramer 1961, pp. 54–59; ETCSL 1.1.1, line ~270.]
// EVIDENCE: source_id=kramer-1961 ; loc=pp. 54–59

Each newly born deity is assigned a specific role or domain by Enki, integrating them into the divine order.footnote:[ETCSL 1.1.1, lines 270–278; Black et al. 2004, pp. 48–50.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 270–278

=== Cultural and cosmological function

The composition functions cosmologically: it establishes Dilmun as a primordial pure land where sun and fresh water are granted by divine decree, and aetologically: it explains the origin of eight healing deities through Ninhursaja's curing of Enki's ailments.footnote:[ETCSL 1.1.1, lines 1–30 (cosmological), lines 230–278 (aetiological); Jacobsen 1987, pp. 181–204.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, lines 1–30 and 230–278

The nine-day gestation period (replacing the normal nine months) marks Dilmun as a space operating under different temporal rules — a feature characteristic of paradise or otherworld narratives across cultures.footnote:[Jacobsen 1987, pp. 188–190.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 188–190

[INFERENCE: The accelerated gestation functions as a narrative marker of Dilmun's otherworldly temporal nature | basis: The pattern of nine days replacing nine months is consistent across all four generations of births in the text | risk: The text does not explicitly state the symbolic function; this is scholarly interpretation]

The chain of incestuous unions may reflect a mythological theme of divine power concentrating through successive generations rather than a narrative about kinship taboos as moderns would understand them.footnote:[Jacobsen 1987, pp. 188–195.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 188–195

=== Attestation and transmission

Multiple Old Babylonian copies from both Nippur and Ur scribal schools attest wide circulation of the composition in the _edubba_ curriculum.footnote:[ETCSL 1.1.1, manuscript list.]
// EVIDENCE: source_id=etcsl ; loc=1.1.1, manuscript list

Both Jacobsen and Kramer devote sustained analyses to the text's paradise motif and botanical imagery, making it one of the most discussed Sumerian compositions in modern scholarship.footnote:[Jacobsen 1987, pp. 181–204; Kramer 1961, pp. 54–59.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 181–204

// COMPARATIVE-HOOK: Eden/paradise garden with forbidden consumption and divine curse (Hebrew Bible, Genesis 2–3); cf. kramer-1961 pp. 54–59. Ninti "Lady of the Rib/Life" pun parallel to Eve from Adam's rib.
// COMPARATIVE-HOOK: Golden age of effortless plenty and divine proximity (Hesiod, Works and Days); cf. jacobsen-1987 pp. 181–204.
// COMPARATIVE-HOOK: Dilmun as pure land / otherworld with altered temporal rules — compare Celtic Tir na nOg, Vedic heavenly gardens.
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
