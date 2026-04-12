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

# Input file: chapters/04-enkis-journey-to-nibru.claims.adoc

```
== Enki's Journey to Nibru — Claims

// This is a claims document, not final prose. Each paragraph is one verifiable claim.
// Source: ETCSL 1.1.4, composite text. Single-prevalent.
// Variant classification: single-prevalent

=== Setting and context

The composition "Enki's Journey to Nibru" is catalogued as ETCSL 1.1.4 and survives as a standard Old Babylonian curriculum text with well-preserved fragments.footnote:[ETCSL 1.1.4, composite text.]
// EVIDENCE: source_id=etcsl ; loc=1.1.4, composite text

No competing recension of the text is known; the ETCSL composite represents the sole reconstructable version.footnote:[ETCSL 1.1.4, editorial notes; Black et al. 2004, pp. 330–333.]
// EVIDENCE: source_id=etcsl ; loc=1.1.4, editorial notes

=== Enki's temple in Eridu

Enki constructs (or adorns) his temple, the E-abzu ("House of the _abzu_"), in Eridu — the oldest city in Mesopotamian tradition and the seat of Enki's cult.footnote:[ETCSL 1.1.4, opening section; Kramer 1961, pp. 62–64.]
// EVIDENCE: source_id=etcsl ; loc=1.1.4, opening section

[LACUNA: Opening lines (1–8) describing Enki's temple construction partially damaged | source: etcsl 1.1.4 | scholarly_reconstruction: none — limited manuscript witnesses]

The temple is described in terms of cosmic grandeur: it is compared to a mountain rising from the earth, its foundations set in the _abzu_, the underground freshwater ocean that is Enki's domain.footnote:[ETCSL 1.1.4, lines 1–20 (partially reconstructed); Kramer 1961, pp. 62–63.]
// EVIDENCE: source_id=etcsl ; loc=1.1.4, lines 1–20

Eridu is presented as the primal city of Sumer, located in the deep south of the alluvial plain, the place where civilisation began in Sumerian tradition.footnote:[Kramer 1961, pp. 62–64; CDLI Eridu-related entries.]
// EVIDENCE: source_id=kramer-1961 ; loc=pp. 62–64

=== Narrative sequence: The barge journey

Enki loads his barge with provisions and precious goods and sets out on a journey up the waterways from Eridu to Nippur (Sumerian: Nibru).footnote:[ETCSL 1.1.4, middle section; Black et al. 2004, pp. 330–331.]
// EVIDENCE: source_id=etcsl ; loc=1.1.4, middle section

The barge journey follows the canal and river network northward, stopping at cities along the way; each city is named and blessed as Enki passes.footnote:[ETCSL 1.1.4, journey section; Kramer 1961, pp. 63–64.]
// EVIDENCE: source_id=etcsl ; loc=1.1.4, journey section

[INFERENCE: The barge journey models the pattern of ritual processions between southern cult cities, with the waterway route functioning as both literal geography and sacred itinerary | basis: Royal inscriptions from Ur III attest to similar divine-statue barge processions between Eridu and Nippur | risk: The text does not explicitly name a ritual occasion; the connection to actual processions is scholarly inference]

The journey traces the political geography of Sumer: the Eridu-to-Nippur axis represents a southern cult city seeking the blessing and sanction of the central religious authority.footnote:[Kramer 1961, pp. 62–64.]
// EVIDENCE: source_id=kramer-1961 ; loc=pp. 62–64

=== Arrival at Nippur and Enlil's blessing

Enki arrives at Nippur, the religious capital of Sumer and seat of Enlil, king of the gods and head of the divine assembly.footnote:[ETCSL 1.1.4, arrival section; Black et al. 2004, pp. 331–332.]
// EVIDENCE: source_id=etcsl ; loc=1.1.4, arrival section

Enki prepares a lavish banquet for Enlil, presenting offerings and gifts from the goods carried on his barge.footnote:[ETCSL 1.1.4, banquet section; Black et al. 2004, pp. 332–333.]
// EVIDENCE: source_id=etcsl ; loc=1.1.4, banquet section

Enlil receives Enki with approval and pronounces a blessing upon him and upon the E-abzu temple in Eridu, formally sanctioning Enki's cult and his domain over the freshwater.footnote:[ETCSL 1.1.4, closing section; Kramer 1961, pp. 63–64.]
// EVIDENCE: source_id=etcsl ; loc=1.1.4, closing section

The blessing from Enlil functions as divine legitimation: Enki's authority over the _abzu_ and his cult at Eridu require ratification by the supreme god at Nippur, reflecting the Sumerian political theology in which local power requires central sanction.footnote:[Kramer 1961, pp. 62–64; Black et al. 2004, pp. 330–333.]
// EVIDENCE: source_id=black-2004 ; loc=pp. 330–333

=== Cultural and ritual function

The composition provides the mythological foundation for the E-abzu temple at Eridu, establishing its ritual importance through the narrative of divine construction and subsequent divine approval.footnote:[ETCSL 1.1.4, opening sections.]
// EVIDENCE: source_id=etcsl ; loc=1.1.4, opening sections

The barge journey and Enlil's blessing model the pattern of southern rulers seeking Nippur's sanction — a pattern attested in royal inscriptions throughout the Ur III and early Old Babylonian periods.footnote:[Kramer 1961, pp. 62–64; CDLI Eridu-related royal inscriptions.]
// EVIDENCE: source_id=kramer-1961 ; loc=pp. 62–64

The text was attested as a standard OB curriculum text, indicating wide scribal familiarity.footnote:[ETCSL 1.1.4, manuscript list.]
// EVIDENCE: source_id=etcsl ; loc=1.1.4, manuscript list

// COMPARATIVE-HOOK: Divine temple-building and seeking the supreme god's blessing (Ugaritic: Baal Cycle — Baal constructs palace and seeks El's permission); cf. black-2004.
// COMPARATIVE-HOOK: River-journey as sacred itinerary between cult centres — compare Egyptian Opet festival procession on the Nile between Karnak and Luxor.
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
