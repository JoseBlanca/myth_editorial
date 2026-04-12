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

# Input file: chapters/24-enmerkar-and-the-lord-of-aratta.claims.adoc

```
== Enmerkar and the Lord of Aratta — Claims

// This is a claims document, not final prose. Each paragraph is one verifiable claim.
// Source: ETCSL 1.8.2.3; Vanstiphout 2003, pp. 1–95; Black et al. 2004, pp. 236–251
// Classification: single-prevalent (ETCSL composite from multiple OB manuscripts)
// Composition length: ~636 lines

=== Setting and context

Enmerkar is presented as lord of Uruk (Sumerian: Unug) and son of the sun god Utu, a legendary king of the first dynasty of Uruk who seeks to make Aratta submit to his authority.footnote:[ETCSL 1.8.2.3, lines 1–10; Black et al. 2004, pp. 236–237.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 1–10

Aratta is described as a distant, wealthy city located beyond seven mountain ranges, famed as a source of precious stones (lapis lazuli, carnelian) and metals.footnote:[ETCSL 1.8.2.3, lines 10–20; Vanstiphout 2003, pp. 15–17.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 10–20

Inanna is the patron goddess of Uruk and the pivotal figure whose favor both Enmerkar and the lord of Aratta seek; the contest between the two kings is fundamentally a contest for her divine endorsement.footnote:[ETCSL 1.8.2.3, lines 1–30; Vanstiphout 2003, pp. 1–10.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 1–30

=== Inanna's endorsement of Enmerkar

Enmerkar prays to Inanna, asking her to compel Aratta to deliver precious stones and metals for the construction of her temple, the E-ana in Uruk.footnote:[ETCSL 1.8.2.3, lines 28–55; Black et al. 2004, p. 237.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 28–55

Inanna endorses Enmerkar's claim and instructs him to send a messenger across the mountains to demand Aratta's submission.footnote:[ETCSL 1.8.2.3, lines 56–100; Vanstiphout 2003, pp. 20–25.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 56–100

The goddess's endorsement establishes the ideological framework of the entire poem: Uruk's claim to supremacy rests on divine backing, not military force.footnote:[Vanstiphout 2003, pp. 1–10 (introduction).]
// EVIDENCE: source_id=vanstiphout-2003 ; loc=pp. 1–10

[LACUNA: Transition passage between Inanna's endorsement and the first messenger dispatch | source: etcsl 1.8.2.3, lines 136–155 | scholarly_reconstruction: composite reconstruction from multiple OB manuscripts restores most of the passage]

=== First messenger exchange

Enmerkar dispatches a messenger across the seven mountain ranges to Aratta, carrying an oral demand that the lord of Aratta submit and send tribute of precious stones and metals to Uruk.footnote:[ETCSL 1.8.2.3, lines 100–170; Black et al. 2004, pp. 238–239.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 100–170

The messenger travels the long road over the mountains and delivers Enmerkar's demand verbatim to the lord of Aratta, preserving the speech exactly as formulated.footnote:[ETCSL 1.8.2.3, lines 170–200; Vanstiphout 2003, pp. 28–32.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 170–200

The lord of Aratta refuses submission, asserting that Aratta too is beloved of Inanna and that the goddess resides with him as well.footnote:[ETCSL 1.8.2.3, lines 200–240; Vanstiphout 2003, pp. 32–36.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 200–240

The lord of Aratta issues a counter-challenge, proposing a trial to determine which king Inanna truly favors.footnote:[ETCSL 1.8.2.3, lines 240–260; Black et al. 2004, p. 240.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 240–260

=== Second messenger exchange and grain challenge

The messenger returns to Uruk with Aratta's response, and Enmerkar formulates a new, escalated demand.footnote:[ETCSL 1.8.2.3, lines 260–290; Vanstiphout 2003, pp. 36–40.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 260–290

Enmerkar sends the messenger back with a challenge involving grain: he fills nets with grain and sends them to Aratta, demanding that the lord of Aratta respond in kind with precious materials.footnote:[ETCSL 1.8.2.3, lines 290–330; Black et al. 2004, pp. 240–241.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 290–330

[INFERENCE: The grain challenge functions as a display of Uruk's agricultural abundance, asserting economic superiority over Aratta's mineral wealth. | basis: The text pairs agricultural produce against precious stones as competing claims to divine favor. | risk: The symbolic reading is widely accepted but the text does not make the economic argument explicit.]

The lord of Aratta is troubled by the challenge but refuses to capitulate, sending the messenger back with further counter-arguments.footnote:[ETCSL 1.8.2.3, lines 330–370; Vanstiphout 2003, pp. 42–48.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 330–370

=== Third messenger exchange and riddle challenges

Enmerkar escalates further, sending the messenger with a riddle-challenge to the lord of Aratta: he demands that Aratta send tribute carried by a donkey that is neither black nor white nor brown nor dappled — an impossible condition.footnote:[ETCSL 1.8.2.3, lines 370–410; Black et al. 2004, pp. 242–243.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 370–410

The riddle challenges represent a genre of wisdom contest in which rhetorical skill and intellectual superiority replace direct military conflict.footnote:[Vanstiphout 2003, pp. 5–8 (introduction).]
// EVIDENCE: source_id=vanstiphout-2003 ; loc=pp. 5–8

The lord of Aratta answers with his own counter-riddle, maintaining the escalating pattern of diplomatic exchange.footnote:[ETCSL 1.8.2.3, lines 410–450; Vanstiphout 2003, pp. 52–58.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 410–450

Each round of exchanges intensifies the demands and the rhetorical complexity, with the messenger serving as the sole conduit of these increasingly elaborate verbal contests.footnote:[Vanstiphout 2003, pp. 1–10 (introduction on messenger structure).]
// EVIDENCE: source_id=vanstiphout-2003 ; loc=pp. 1–10

=== Fourth and fifth exchanges: escalation

The exchanges continue through additional rounds, with Enmerkar and the lord of Aratta each attempting to outdo the other in the ingenuity and impossibility of their demands.footnote:[ETCSL 1.8.2.3, lines 450–500; Black et al. 2004, pp. 244–246.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 450–500

Inanna's favor begins to tip visibly toward Enmerkar as the exchanges proceed; divine signs and portents indicate that Uruk holds the goddess's preference.footnote:[ETCSL 1.8.2.3, lines 480–510; Vanstiphout 2003, pp. 60–66.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 480–510

[LACUNA: Several of the lord of Aratta's responses in lines 500–530 are partially damaged or unclear | source: etcsl 1.8.2.3, lines 500–530 | scholarly_reconstruction: overlapping manuscripts clarify some lines, but the lord of Aratta's counter-arguments remain fragmentary in places]

[VARIANT: primary=etcsl 1.8.2.3, lines 500–530, ETCSL composite follows majority manuscript readings | alt=Vanstiphout 2003, pp. 66–72, occasionally favors different manuscript readings in the Aratta response sections | chosen: A | reason: ETCSL composite is the standard scholarly text across multiple OB manuscripts]

=== The confusion of tongues

The poem contains a passage stating that once upon a time all lands spoke a single language in unison to Enlil, but that this linguistic unity was disrupted — the tongues of humanity were confused.footnote:[ETCSL 1.8.2.3, lines 136–155 (some scholars place it at lines 500–540 depending on interpretation); Kramer 1961, pp. 232–234.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 136–155

[VARIANT: primary=ETCSL 1.8.2.3, lines 136–155, passage placed early in the narrative as a mythological aside | alt=Some scholars interpret the confusion-of-tongues passage as occurring later in the narrative context, around lines 500–540 | chosen: A | reason: ETCSL composite placement; exact position debated but ETCSL is the standard reference]

The confusion of tongues is attributed to the god Enki, who is said to have changed the speech of humanity from one language into many.footnote:[ETCSL 1.8.2.3, lines 141–155; Vanstiphout 2003, pp. 22–26.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 141–155

Before the confusion, "the whole universe, the people in unison," spoke to Enlil in a single tongue; afterward, linguistic diversity became the norm.footnote:[ETCSL 1.8.2.3, lines 136–140, "the whole universe, the well-guarded people — may they all address Enlil together in a single language"; Kramer 1961, pp. 232–234.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 136–140

This passage has been compared to the Tower of Babel narrative in Genesis 11:1–9, where a primordial linguistic unity is disrupted by divine intervention; Kramer was among the first to note this parallel.footnote:[Kramer 1961, pp. 232–234.]
// EVIDENCE: source_id=kramer-1961 ; loc=pp. 232–234

[INFERENCE: The confusion of tongues functions within the narrative as context for the communication difficulties between Uruk and Aratta — it is the mythological backdrop to the need for messengers and ultimately for writing. | basis: The passage is situated in a composition centrally concerned with the difficulty of long-distance communication. | risk: The causal connection between the confusion motif and the writing-invention passage is inferred by scholars but not stated explicitly in the text.]

=== The invention of writing

The poem reaches a climactic moment when Enmerkar's message becomes too complex for the messenger to carry in his memory; the messenger cannot repeat it accurately.footnote:[ETCSL 1.8.2.3, lines 500–540; Vanstiphout 2003, pp. 72–78.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 500–540

In response to this limitation, Enmerkar takes a lump of clay and "puts words on it as on a tablet" — he invents the technology of writing to overcome the failure of oral communication.footnote:[ETCSL 1.8.2.3, lines 540–548; Black et al. 2004, pp. 247–248.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 540–548

The text presents writing as a practical invention born of necessity: the escalating complexity of the diplomatic exchanges between Uruk and Aratta exceeds human memory, forcing a technological solution.footnote:[Vanstiphout 2003, pp. 72–78; Black et al. 2004, pp. 247–248.]
// EVIDENCE: source_id=vanstiphout-2003 ; loc=pp. 72–78

The lord of Aratta receives the clay tablet but is unable to read it, highlighting the novelty of the technology and Uruk's innovation.footnote:[ETCSL 1.8.2.3, lines 548–560; Vanstiphout 2003, pp. 78–80.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 548–560

This passage is one of the most celebrated in Sumerian literature: it presents an aetiology for the invention of cuneiform writing, attributing it to Enmerkar of Uruk in the context of diplomatic communication.footnote:[Black et al. 2004, pp. 236–237 (introduction to the composition).]
// EVIDENCE: source_id=black-2004 ; loc=pp. 236–237

=== Divine intervention and resolution

After the writing episode, the goddess Inanna intervenes decisively in favor of Enmerkar and Uruk.footnote:[ETCSL 1.8.2.3, lines 560–590; Vanstiphout 2003, pp. 80–85.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 560–590

Ishkur, the storm god, sends rain upon Aratta, and the city produces wild grain, which is taken as a sign that the gods favor trade and communication rather than continued resistance.footnote:[ETCSL 1.8.2.3, lines 590–615; Black et al. 2004, pp. 249–250.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 590–615

[INFERENCE: The rain and grain episode may signal a shift toward peaceful exchange rather than one-sided submission — the resolution gestures toward mutual trade rather than outright conquest. | basis: The text describes both cities benefiting from the exchange of goods. | risk: Whether the ending represents genuine reciprocity or mere Uruk propaganda is debated.]

The lord of Aratta appears to accept a form of accommodation with Uruk, though the precise terms of the resolution are debated among scholars.footnote:[ETCSL 1.8.2.3, lines 615–636; Vanstiphout 2003, pp. 85–90.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 615–636

=== Structure and literary significance

The composition is structured around a series of escalating messenger exchanges between the two kings, with the messenger himself serving as the narrative vehicle — the poem never depicts the two kings meeting face to face.footnote:[Vanstiphout 2003, pp. 1–10 (introduction).]
// EVIDENCE: source_id=vanstiphout-2003 ; loc=pp. 1–10

The messenger structure is the defining literary feature: each exchange follows a pattern of dispatch, journey, delivery, response, and return, with rhetorical escalation at each round.footnote:[Vanstiphout 2003, pp. 5–8.]
// EVIDENCE: source_id=vanstiphout-2003 ; loc=pp. 5–8

The poem encodes Uruk's ideological claims to regional hegemony through Enmerkar's demands for tribute and labor from Aratta, backed by Inanna's divine favor.footnote:[Black et al. 2004, pp. 236–237 (introduction).]
// EVIDENCE: source_id=black-2004 ; loc=pp. 236–237

The composition survives across multiple Old Babylonian manuscripts from Nippur and other scribal centers, attesting to wide circulation as a curriculum text in the _edubba_ tradition.footnote:[ETCSL 1.8.2.3, manuscript list.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, manuscript list

At approximately 636 lines, this is one of the longest and most complex Sumerian narrative poems, representing a peak of the genre's rhetorical sophistication.footnote:[Vanstiphout 2003, pp. 1–10.]
// EVIDENCE: source_id=vanstiphout-2003 ; loc=pp. 1–10

=== Messenger as narrative device

The messenger crosses the seven mountain ranges between Uruk and Aratta repeatedly, and the text describes this journey in formulaic terms that recur with each exchange.footnote:[ETCSL 1.8.2.3, passim; Vanstiphout 2003, pp. 5–8.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, passim

The messenger must memorize and reproduce the kings' speeches verbatim; the fidelity of oral transmission is a central concern of the poem, setting up the climactic failure that necessitates writing.footnote:[ETCSL 1.8.2.3, lines 500–548; Vanstiphout 2003, pp. 72–78.]
// EVIDENCE: source_id=vanstiphout-2003 ; loc=pp. 72–78

The messenger never editorializes or alters the messages he carries; he is presented as a neutral conduit, reinforcing the poem's interest in the reliability and limits of communication.footnote:[Vanstiphout 2003, pp. 5–8.]
// EVIDENCE: source_id=vanstiphout-2003 ; loc=pp. 5–8

=== Riddle-contest tradition

The riddle exchanges between Enmerkar and the lord of Aratta belong to a broader ancient Near Eastern wisdom-contest genre in which intellectual prowess substitutes for military conflict.footnote:[Vanstiphout 2003, pp. 5–8.]
// EVIDENCE: source_id=vanstiphout-2003 ; loc=pp. 5–8

The impossible conditions imposed by each king — demands that cannot literally be met — function as tests of ingenuity and divine backing rather than practical ultimatums.footnote:[ETCSL 1.8.2.3, lines 370–500; Vanstiphout 2003, pp. 48–66.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 370–500

=== Royal legitimation function

The composition functions as royal legitimation literature: it establishes Uruk's supremacy over Aratta through a divinely backed diplomatic contest, presenting Enmerkar as the rightful hegemon.footnote:[ETCSL 1.8.2.3, lines 1–30; Black et al. 2004, pp. 236–237.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 1–30

The text's didactic function is evidenced by its wide _edubba_ circulation: the confusion-of-tongues passage and the writing-invention passage encode cultural memory about the origins of literate civilization.footnote:[ETCSL 1.8.2.3, lines 500–548; Black et al. 2004, pp. 236–237.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 500–548

Enmerkar's genealogical connection to Utu (the sun god) reinforces his legitimacy — he is not merely a powerful king but a figure of divine descent.footnote:[ETCSL 1.8.2.3, lines 1–5; Vanstiphout 2003, pp. 15–17.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 1–5

=== Aratta as symbolic other

Aratta functions in the text as the exotic, wealthy other — the distant source of luxury materials that Uruk desires and claims the right to command.footnote:[Black et al. 2004, pp. 236–237.]
// EVIDENCE: source_id=black-2004 ; loc=pp. 236–237

The geographical remoteness of Aratta (beyond seven mountain ranges) is emphasized repeatedly; the difficulty of the journey is part of the narrative's dramatic structure.footnote:[ETCSL 1.8.2.3, passim; Vanstiphout 2003, pp. 15–17.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, passim

Despite its subordination in the narrative, Aratta is portrayed as a sophisticated civilization with its own claims to divine favor — the lord of Aratta is not a barbarian but a worthy adversary.footnote:[ETCSL 1.8.2.3, lines 200–260; Vanstiphout 2003, pp. 32–40.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, lines 200–260

=== Textual transmission

The poem is attested in multiple Old Babylonian manuscripts, predominantly from Nippur, with the ETCSL composite representing the standard scholarly reconstruction.footnote:[ETCSL 1.8.2.3, manuscript list.]
// EVIDENCE: source_id=etcsl ; loc=1.8.2.3, manuscript list

Vanstiphout's 2003 critical edition devotes nearly one hundred pages to the text with philological commentary and is the primary scholarly treatment.footnote:[Vanstiphout 2003, pp. 1–95.]
// EVIDENCE: source_id=vanstiphout-2003 ; loc=pp. 1–95

This composition is the first and longest in the Aratta cycle, which also includes Enmerkar and En-suhgir-ana, Lugalbanda in the Mountain Cave, and Lugalbanda and the Anzud Bird.footnote:[Black et al. 2004, pp. 236–237.]
// EVIDENCE: source_id=black-2004 ; loc=pp. 236–237

// COMPARATIVE-HOOK: Confusion of tongues — Tower of Babel (Genesis 11:1–9); primordial linguistic unity disrupted by divine act (kramer-1961)
// COMPARATIVE-HOOK: Riddle contest between rival kings — Oedipus and Sphinx, ANE wisdom-contest traditions (vanstiphout-2003)
// COMPARATIVE-HOOK: Invention of writing as narrative aetiology — cultural-hero origin stories for technologies across traditions
// COMPARATIVE-HOOK: Diplomatic messenger exchanges as literary structure — parallels in El-Amarna correspondence tradition
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
