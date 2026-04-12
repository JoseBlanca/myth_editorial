# Stage 9 of 17: claims-factcheck
# Book: sumer
# Generated: 2026-04-12T17:54:33Z

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

# Input file: chapters/14-inannas-descent.claims.adoc

```
== Inanna's Descent to the Nether World — Claims

// This is a claims document, not final prose. Each paragraph is one verifiable claim.

=== Setting and context

The Sumerian composition "Inanna's Descent to the Nether World" is catalogued as ETCSL 1.4.1 and comprises approximately 415 lines in the composite text.footnote:[ETCSL 1.4.1, composite text, lines 1–415.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1

Over forty Old Babylonian tablets and fragments preserve portions of this composition, making it the most extensively attested Sumerian literary text.footnote:[ETCSL 1.4.1, manuscript list; Sladek 1974, full philological study.]
// EVIDENCE: source_id=sladek-1974 ; loc=full study

The text is classified as composite-editorial: the ETCSL composite draws on these 40+ Old Babylonian fragments to produce the standard scholarly text.footnote:[ETCSL 1.4.1, apparatus.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1

Sladek's 1974 Johns Hopkins dissertation provides the foundational philological study of the composition, collating manuscript witnesses and establishing the text.footnote:[Sladek 1974 (PhD diss., Johns Hopkins).]
// EVIDENCE: source_id=sladek-1974 ; loc=full study

This is a distinct composition from the Akkadian "Descent of Ishtar" (a shorter, adapted version); the two must be treated as separate works despite shared narrative elements.footnote:[Sladek 1974; Black et al. 2004, pp. 52–53 (introduction).]
// EVIDENCE: source_id=sladek-1974 ; loc=full study

The composition undergirds the seasonal cult of Dumuzid and the wailing rites attested in the Ur III and Old Babylonian periods.footnote:[Jacobsen 1987, pp. 205–207.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 205–207

=== Inanna's preparation and decision

Inanna, queen of heaven, goddess of love, war, and political power, resolves to descend to the _kur_ — the nether world, realm of the dead beneath the earth — the domain of her elder sister Ereshkigal.footnote:[ETCSL 1.4.1, lines 1–13; Black et al. 2004, pp. 52–53.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1, lines 1–13

Inanna abandons heaven and earth and her seven cities and temples to go to the nether world; the text enumerates the holy places she forsakes.footnote:[ETCSL 1.4.1, lines 1–13; Jacobsen 1987, pp. 207–208.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 207–208

Inanna gathers the seven _me_ of the divine office and transforms them into physical adornments: she places the _shugurra_ (crown of the steppe) on her head, takes the measuring rod and line of lapis lazuli in her hand, fastens small lapis lazuli beads around her neck, sets twin egg-shaped beads upon her breast, places a gold ring on her hand, binds a breastplate called "Come, man, come" on her chest, and covers her body with the _pala_-garment of ladyship.footnote:[ETCSL 1.4.1, lines 14–25; Black et al. 2004, pp. 53–54; Jacobsen 1987, pp. 208–209.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1, lines 14–25

Inanna instructs her minister Ninshubur (her faithful sukkal) with detailed contingency plans: if she does not return within three days, Ninshubur must go to the temples of Enlil, Nanna-Suen, and Enki and plead for help.footnote:[ETCSL 1.4.1, lines 26–67; Black et al. 2004, pp. 54–55.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1, lines 26–67

Inanna specifies the order of appeal: first Enlil in Nippur (Sumerian: Nibru), then Nanna-Suen in Ur, then Enki in Eridu.footnote:[ETCSL 1.4.1, lines 30–67; Black et al. 2004, pp. 54–55.]
// EVIDENCE: source_id=black-2004 ; loc=pp. 54–55

=== Arrival at the nether world gates

Inanna arrives at the outer gate of the nether world (the palace Ganzer) and demands entry.footnote:[ETCSL 1.4.1, lines 68–80; Black et al. 2004, p. 55.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1, lines 68–80

Inanna tells the gatekeeper Neti that she has come for the funeral rites of Gugalanna (the Bull of Heaven), the husband of Ereshkigal.footnote:[ETCSL 1.4.1, lines 80–90; Black et al. 2004, p. 55.]
// EVIDENCE: source_id=black-2004 ; loc=p. 55

[INFERENCE: Whether Inanna's stated reason — funeral rites for Gugalanna — is sincere or a pretext is debated; the text does not resolve her actual motivation for descending. | basis: The narrative provides no other explicit motive, but the pretext may be a ruse. | risk: Scholarly opinions diverge on whether Inanna aims to conquer the underworld or whether her motivation is left deliberately ambiguous.]

Neti the gatekeeper reports Inanna's arrival to Ereshkigal, queen of the nether world and Inanna's elder sister.footnote:[ETCSL 1.4.1, lines 90–115; Black et al. 2004, p. 55.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1, lines 90–115

Ereshkigal is angered by Inanna's arrival and instructs Neti to bolt the seven gates of the nether world and then open them one by one, applying "the rules of the nether world" at each gate.footnote:[ETCSL 1.4.1, lines 115–130; Black et al. 2004, pp. 55–56.]
// EVIDENCE: source_id=black-2004 ; loc=pp. 55–56

=== The seven gates and the stripping

At the first gate, the _shugurra_ (crown) is removed from Inanna's head; when she asks why, she is told: "Be silent, Inanna. The powers of the nether world are perfect. The rites of the nether world must not be questioned."footnote:[ETCSL 1.4.1, lines 130–145; Black et al. 2004, p. 56; Jacobsen 1987, pp. 210–211.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1, lines 130–145

At the second gate, the measuring rod and line of lapis lazuli are removed from her hand.footnote:[ETCSL 1.4.1; Black et al. 2004, p. 56.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1

At the third gate, the small lapis lazuli beads are removed from her neck.footnote:[ETCSL 1.4.1; Black et al. 2004, p. 56.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1

At the fourth gate, the twin egg-shaped beads are removed from her breast.footnote:[ETCSL 1.4.1; Black et al. 2004, p. 56.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1

At the fifth gate, the gold ring is removed from her hand.footnote:[ETCSL 1.4.1; Black et al. 2004, p. 56.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1

At the sixth gate, the breastplate "Come, man, come" is removed from her chest.footnote:[ETCSL 1.4.1; Black et al. 2004, p. 56.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1

At the seventh gate, the _pala_-garment of ladyship is removed from her body; Inanna enters the throne room of the nether world naked and stripped of all divine power.footnote:[ETCSL 1.4.1, lines 160–170; Black et al. 2004, p. 56; Jacobsen 1987, pp. 210–211.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 210–211

At each gate, the same formula is repeated: Inanna questions the removal and is given the same answer about the perfection of the nether world's powers.footnote:[ETCSL 1.4.1, gate sequence; Black et al. 2004, p. 56.]
// EVIDENCE: source_id=black-2004 ; loc=p. 56

[INFERENCE: The seven-gate stripping structure maps the progressive removal of divine status; the seven adornments correspond to the seven _me_ Inanna gathered at the outset, so each gate reverses one element of her divine preparation. | basis: The composition explicitly pairs the gathering and the stripping. | risk: Not all scholars agree on a one-to-one correspondence between specific _me_ and specific gates.]

=== Death and judgment

Inanna enters the throne room and Ereshkigal rises from her throne in anger.footnote:[ETCSL 1.4.1, lines 170–175; Black et al. 2004, p. 56.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1, lines 170–175

The seven judges of the nether world, the Annunaki, fix their eyes upon Inanna — the "eyes of death."footnote:[ETCSL 1.4.1, lines 164–172; Black et al. 2004, p. 57; Jacobsen 1987, p. 212.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=p. 212

Ereshkigal pronounces the word of wrath against Inanna; Inanna is struck dead and her corpse is hung on a hook on the wall.footnote:[ETCSL 1.4.1, lines 168–172; Black et al. 2004, p. 57.]
// EVIDENCE: source_id=black-2004 ; loc=p. 57

The fundamental law of the nether world is stated: no one who enters the nether world may leave it freely; a substitute must be found.footnote:[ETCSL 1.4.1; Jacobsen 1987, pp. 212–213.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 212–213

=== Ninshubur's appeal and Enki's intervention

After three days and three nights, when Inanna does not return, Ninshubur carries out the contingency instructions.footnote:[ETCSL 1.4.1, lines 173–200; Black et al. 2004, pp. 57–58.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1, lines 173–200

Ninshubur goes first to Enlil in Nippur, who refuses to help, saying Inanna's ambition brought this upon her.footnote:[ETCSL 1.4.1; Black et al. 2004, p. 57.]
// EVIDENCE: source_id=black-2004 ; loc=p. 57

Ninshubur goes next to Nanna-Suen in Ur, who also refuses, with the same reasoning.footnote:[ETCSL 1.4.1; Black et al. 2004, p. 57.]
// EVIDENCE: source_id=black-2004 ; loc=p. 57

Ninshubur goes finally to Enki in Eridu, who is troubled and agrees to help.footnote:[ETCSL 1.4.1; Black et al. 2004, p. 58.]
// EVIDENCE: source_id=black-2004 ; loc=p. 58

Enki creates two beings from the dirt under his fingernails: the _kurgarra_ and the _galatur_ (or _kalaturru_), small sexless creatures who can slip into the nether world unnoticed.footnote:[ETCSL 1.4.1, lines 220–235; Black et al. 2004, p. 58; Sladek 1974.]
// EVIDENCE: source_id=sladek-1974 ; loc=full study

Enki gives the _kurgarra_ the "food of life" and the _galatur_ the "water of life" and instructs them to revive Inanna.footnote:[ETCSL 1.4.1, lines 235–245; Black et al. 2004, p. 58.]
// EVIDENCE: source_id=black-2004 ; loc=p. 58

=== Revival of Inanna

The _kurgarra_ and _galatur_ enter the nether world and find Ereshkigal in the throes of distress (whether birthing pains or mourning groans is debated); they commiserate with her suffering, and in gratitude she offers them a gift.footnote:[ETCSL 1.4.1, lines 245–260; Black et al. 2004, p. 58; Jacobsen 1987, pp. 214–216.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 214–216

They request the corpse hanging on the wall; the _kurgarra_ sprinkles the food of life on Inanna's corpse and the _galatur_ sprinkles the water of life, and Inanna revives.footnote:[ETCSL 1.4.1, lines 260–280; Black et al. 2004, pp. 58–59.]
// EVIDENCE: source_id=black-2004 ; loc=pp. 58–59

[LACUNA: Lines 255–270 (various manuscripts): the transition between Inanna's revival and the search for a substitute is partially damaged in several witnesses. | source: etcsl 1.4.1 | scholarly_reconstruction: overlap among 40+ tablets allows reconstruction of most gaps.]

=== The law of the substitute

The Annunaki decree that Inanna may ascend but must provide a substitute to take her place in the nether world.footnote:[ETCSL 1.4.1, lines 280–295; Black et al. 2004, p. 59.]
// EVIDENCE: source_id=black-2004 ; loc=p. 59

The _galla_ demons — underworld demons — accompany Inanna as she ascends, acting as enforcers who will seize whomever she designates.footnote:[ETCSL 1.4.1, lines 285–300; Black et al. 2004, p. 59; Jacobsen 1987, pp. 217–218.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 217–218

=== The search for a substitute

As Inanna returns to the upper world accompanied by the _galla_ demons, she encounters various deities at each of her cities.footnote:[ETCSL 1.4.1, lines 300–340; Black et al. 2004, pp. 59–60.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1, lines 300–340

At each city, Inanna finds a god or goddess in mourning, dressed in sackcloth and covered in dust, grieving for her; she refuses to hand over any of these mourners to the _galla_ demons.footnote:[ETCSL 1.4.1; Black et al. 2004, pp. 59–60.]
// EVIDENCE: source_id=black-2004 ; loc=pp. 59–60

Ninshubur, who carried out the rescue, is the first deity the _galla_ attempt to seize; Inanna refuses, honouring Ninshubur's faithfulness.footnote:[ETCSL 1.4.1; Black et al. 2004, p. 59.]
// EVIDENCE: source_id=black-2004 ; loc=p. 59

Similarly, the gods Shara and Lulal are found mourning and are spared by Inanna.footnote:[ETCSL 1.4.1; Black et al. 2004, pp. 59–60.]
// EVIDENCE: source_id=black-2004 ; loc=pp. 59–60

=== Dumuzid as substitute

Inanna arrives at Uruk and finds Dumuzid, her consort — the shepherd-god — seated on a magnificent throne, dressed in splendid garments, not mourning her absence at all.footnote:[ETCSL 1.4.1, lines 340–355; Black et al. 2004, p. 60; Jacobsen 1987, pp. 219–221.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 219–221

Inanna is enraged at Dumuzid's lack of grief and fixes upon him the "eye of death"; she hands him over to the _galla_ demons as her substitute.footnote:[ETCSL 1.4.1, lines 348–356; Black et al. 2004, p. 60.]
// EVIDENCE: source_id=black-2004 ; loc=p. 60

Dumuzid is seized by the _galla_ demons and weeps; he appeals to the sun god Utu, his brother-in-law, to transform him so he can escape.footnote:[ETCSL 1.4.1, lines 356–375; Black et al. 2004, pp. 60–61.]
// EVIDENCE: source_id=etcsl ; loc=1.4.1, lines 356–375

Utu transforms Dumuzid's hands and feet into the hands and feet of a snake (or gazelle, depending on manuscript), allowing him to flee from the _galla_.footnote:[ETCSL 1.4.1; Black et al. 2004, p. 60; Sladek 1974.]
// EVIDENCE: source_id=sladek-1974 ; loc=full study

[VARIANT: primary=ETCSL 1.4.1, "snake" transformation in some manuscripts | alt=other manuscripts read "gazelle" | chosen: composite retains both | reason: Sladek documents the variant witnesses; the ETCSL composite reflects the manuscript variation.]

Dumuzid flees but is ultimately recaptured by the _galla_ demons.footnote:[ETCSL 1.4.1; Black et al. 2004, pp. 60–61.]
// EVIDENCE: source_id=black-2004 ; loc=pp. 60–61

=== The fly and the search for Dumuzid

[VARIANT: primary=Some manuscripts include a passage in which a fly reveals Dumuzid's hiding place to Inanna | alt=Other manuscripts omit the fly episode entirely | chosen: Include with note | reason: Sladek 1974 documents that the fly's role appears in some manuscripts only; it is part of the ETCSL composite but not universal across witnesses.]

In the manuscripts that include the episode, a fly tells Inanna where Dumuzid is hiding, and she blesses the fly in return.footnote:[ETCSL 1.4.1; Sladek 1974.]
// EVIDENCE: source_id=sladek-1974 ; loc=full study

=== Geshtinanna and the seasonal alternation

Geshtinanna, the divine sister of Dumuzid, weeps bitterly for her brother and offers to take his place in the underworld.footnote:[ETCSL 1.4.1, lines 380–400; Black et al. 2004, pp. 61–62.]
// EVIDENCE: source_id=black-2004 ; loc=pp. 61–62

Inanna decrees a compromise: Dumuzid will spend half the year in the nether world, and Geshtinanna will spend the other half; each takes the other's place in alternation.footnote:[ETCSL 1.4.1, lines 400–415; Black et al. 2004, p. 62; Jacobsen 1987, pp. 225–228.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 225–228

[LACUNA: The seasonal alternation ending (lines 358–415) is not present in all manuscripts; final lines vary across witnesses. The composite relies on a subset of manuscripts for this conclusion. | source: etcsl 1.4.1 | scholarly_reconstruction: partial; some manuscripts end before the alternation sequence.]

This alternation provides the aetiological basis for the seasonal death and return of Dumuzid, grounding the wailing cult and the pastoral cycle of the agricultural year.footnote:[ETCSL 1.4.1, lines 400–415; Jacobsen 1987, pp. 225–228; Kramer 1961, pp. 83–96.]
// EVIDENCE: source_id=kramer-1961 ; loc=pp. 83–96

Ningishzida is mentioned alongside Dumuzid in some underworld passages as a chthonic deity who dwells below.footnote:[ETCSL 1.4.1; Jacobsen 1987, pp. 225–228.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 225–228

=== Underworld geography and laws

The composition provides the fullest Sumerian account of underworld geography: seven gates, the throne room of Ereshkigal, the Annunaki judges, and the fundamental law that no one leaves without a substitute.footnote:[ETCSL 1.4.1, lines 1–170; Jacobsen 1987, pp. 205–215.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 205–215

The nether world is presented as a place of immutable laws: its powers are "perfect" and its rites "must not be questioned," a formula repeated at each of the seven gates.footnote:[ETCSL 1.4.1, gate sequence; Black et al. 2004, p. 56.]
// EVIDENCE: source_id=black-2004 ; loc=p. 56

The dead in the underworld eat dust and clay and are clothed in feathered garments like birds — standard Mesopotamian underworld imagery shared with other compositions.footnote:[ETCSL 1.4.1; Jacobsen 1987, pp. 210–211.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 210–211

=== Theological and literary significance

The composition is the most important single Sumerian text for understanding Mesopotamian eschatology: the nature of death, the geography of the afterlife, and the impossibility of free return.footnote:[Sladek 1974; Jacobsen 1987, pp. 205–232.]
// EVIDENCE: source_id=sladek-1974 ; loc=full study

Sladek's full philological study and continuous scholarly engagement since Kramer confirm the text's canonical status in Sumerology.footnote:[Sladek 1974; Kramer 1961, pp. 83–96.]
// EVIDENCE: source_id=kramer-1961 ; loc=pp. 83–96

Jacobsen's literary translation in _The Harps That Once..._ (1987) smooths over line-level variants for narrative coherence but remains an influential reading.footnote:[Jacobsen 1987, pp. 205–232.]
// EVIDENCE: source_id=jacobsen-1987 ; loc=pp. 205–232

The _kurgarra_ and _galatur_ created by Enki are understood as a-sexual or trans-gender cultic functionaries in some scholarly interpretations, connecting the text to the broader Mesopotamian tradition of liminal ritual personnel.footnote:[Sladek 1974; Black et al. 2004, pp. 52–53 (introduction).]
// EVIDENCE: source_id=sladek-1974 ; loc=full study

[INFERENCE: The composition functions simultaneously as eschatological charter (establishing underworld law), ritual aetiology (grounding the Dumuzid wailing cult in narrative), and psychological drama (Inanna's ambition, Ereshkigal's grief, Dumuzid's betrayal through complacency). | basis: All three functions are directly supported by the text and scholarly commentary. | risk: Prioritising one function over others is a scholarly choice, not a textual given.]

// COMPARATIVE-HOOK: Greek — Persephone's descent and seasonal return from Hades mirrors the Dumuzid/Geshtinanna alternation (kramer-1961).
// COMPARATIVE-HOOK: Egyptian — Osiris's death, dismemberment, and cyclical resurrection echo the dying-god pattern (jacobsen-1987).
// COMPARATIVE-HOOK: Akkadian — The Descent of Ishtar is a shorter, adapted version and must be treated as a distinct composition (sladek-1974).
// COMPARATIVE-HOOK: Worldwide (seasonal myth) — Death-and-rebirth of a vegetation deity tied to seasonal cycles appears in many traditions globally (kramer-1961).
// COMPARATIVE-HOOK: Japanese — Izanagi's descent to Yomi to retrieve Izanami; the prohibition against looking, the rotting corpse, the flight and pursuit, the establishment of death's permanence.
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
