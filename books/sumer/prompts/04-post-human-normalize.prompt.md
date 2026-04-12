# Stage 4 of 17: post-human-normalize
# Book: sumer
# Generated: 2026-04-12T15:07:20Z

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

# Skill instructions: post-human-normalize

---
name: post-human-normalize
description: Validates and normalizes any file that has been modified by a human reviewer before it becomes input for the next stage. Ensures that human edits have not broken the structural contracts that downstream stages depend on. Runs after every [HUMAN] review checkpoint.
---

# post-human-normalize

## For the human

Every time you review and edit a file — approving factcheck findings, fixing claims, resolving audit issues — there is a risk that your edits break something the next stage depends on. You might merge two claims into one paragraph, accidentally delete a marker, change a citation format, or remove a field from a YAML file. These are easy mistakes to make, and the next AI stage will silently produce wrong output rather than catching the problem.

This step is a quick automated check that catches these problems before they propagate. It runs after every human review point and validates that the edited file still meets the structural requirements for the next stage.

This step does not change the meaning of anything you wrote. It only checks structure, reformats where necessary, and flags violations that need your attention before proceeding.

## When to run

After every `[HUMAN]` checkpoint in the stage order:
- After inventory-audit human review → validates `inventory.approved.yaml`
- After intro-chapter factcheck human review → validates `chapters/00-introduction.adoc`
- After claims-factcheck human review → validates `chapters/NN-<slug>.claims.approved.adoc`
- After narrative-fidelity human review (if REVISE) → validates `chapters/NN-<slug>.adoc`
- After comparative-chapter factcheck human review → validates `comparative.adoc`
- After character-appendix factcheck human review → validates `character-appendix.adoc`

## Checks performed

### For YAML files (`inventory.approved.yaml`, factcheck outputs)
1. All required fields present per the schema defined in the producing skill.
2. No empty required fields.
3. All `source_id` values resolve to entries in `sources.yaml` registry.
4. No YAML syntax errors.

### For claims documents (`*.claims.approved.adoc`)
1. One claim per paragraph — no merged or bundled claims.
2. Every claim paragraph has a footnote citation.
3. Every evidence token (`// EVIDENCE: ...`) is syntactically valid and references a `source_id` in `sources.yaml`.
4. All markers (`[INFERENCE:]`, `[LACUNA:]`, `[RECONSTRUCTION:]`, `[VARIANT:]`) have all required sub-fields.
5. `glossary.yaml` renderings used consistently.

### For prose documents (intro, comparative, character-appendix, narrative chapters)
1. All markers syntactically valid with required sub-fields.
2. All evidence tokens syntactically valid.
3. Canonical chapter anchors present and unchanged.
4. `glossary.yaml` renderings used consistently.
5. No `never_use` glossary terms present.

## Output

The validated file, with a provenance comment block appended:
```
// Validated by post-human-normalize
// Timestamp: <UTC>
// Checks passed: <list>
// Warnings: <any non-blocking issues>
```

If any check fails, the file is returned to the human with a specific error report. The pipeline does not proceed until all checks pass.

## Handoff
The validated file proceeds to the next stage as defined in the stage order.

---

# Input file: inventory.approved.yaml

```
cycles:
  # ═══════════════════════════════════════════════════════════════════
  # ENKI CYCLE
  # ═══════════════════════════════════════════════════════════════════
  - id: enki-cycle
    name: "Enki Cycle"
    stories:
      - id: enki-and-ninhursaja
        title: "Enki and Ninhursaja"
        native_title: "en-ki-ga-ke₄ kuru₇-ba"
        sources:
          - id: etcsl
            loc: "ETCSL 1.1.1"
            identifier: "ETCSL 1.1.1"
          - id: black-2004
            loc: "pp. 38–50"
            identifier: "ISBN 9780199296330"
          - id: jacobsen-1987
            loc: "pp. 181–204"
            identifier: "ISBN 9780300072785"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE; composition possibly earlier"
        summary: "In the paradisal land of Dilmun, Enki provides fresh water and engenders a chain of divine births by consuming forbidden plants. Cursed by Ninhursaja, he is eventually healed through her creation of eight deities corresponding to his afflicted body parts."
        variants:
          - "Ur manuscripts include an insertion of international tributes to Dilmun not found in the Nippur versions."
          - "Gaps in the Dilmun description and dialogue vary across manuscripts."
        scope_uncertain: false
        identifier_missing: false
        notes: "Reconstructed from Nippur and Ur fragments. Contains gaps in the Dilmun description and dialogue."

      - id: enki-and-ninmah
        title: "Enki and Ninmah"
        native_title: "u₄ re-a an ki-bi-ta"
        sources:
          - id: etcsl
            loc: "ETCSL 1.1.2"
            identifier: "ETCSL 1.1.2"
          - id: black-2004
            loc: "pp. 30–37"
            identifier: "ISBN 9780199296330"
          - id: kramer-1961
            loc: "pp. 68–72"
            identifier: "ISBN 9780812210477"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "At a divine feast, Ninmah and Enki engage in a creation contest: Ninmah fashions physically impaired humans and challenges Enki to find each a social role. Enki succeeds every time but wins when his own creation, Umul, proves beyond Ninmah's ability to place."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Largely intact but with fragmentary sections in the middle (~6 lines) and end (~9 lines). Primarily attested in OB Nippur scribal copies. Also functions as a creation-of-humanity narrative."

      - id: enki-and-the-world-order
        title: "Enki and the World Order"
        native_title: "en mah-di an ki-bi-ta"
        sources:
          - id: etcsl
            loc: "ETCSL 1.1.3"
            identifier: "ETCSL 1.1.3"
          - id: black-2004
            loc: "pp. 215–225"
            identifier: "ISBN 9780199296330"
          - id: kramer-1961
            loc: "pp. 59–62"
            identifier: "ISBN 9780812210477"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Enki travels across the known world decreeing the fates of lands and appointing deities to oversee specific domains — sea, agriculture, brick-making, and more. The narrative concludes with Inanna's complaint that she was neglected in the divine distribution of powers."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Well-preserved in sections of hymn and list, but with significant internal gaps of up to 7 missing lines. A long composition (~470 lines)."

      - id: enkis-journey-to-nibru
        title: "Enki's Journey to Nibru"
        native_title: "en-ki-ga-ke₄ e₂-a-ni mu-un-du₃"
        sources:
          - id: etcsl
            loc: "ETCSL 1.1.4"
            identifier: "ETCSL 1.1.4"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Enki constructs his temple in Eridu and travels by barge to Nippur to receive Enlil's blessing for the house. The story legitimates Eridu's ritual status through Nippur's acknowledgement of its supreme authority."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Reconstructed from substantial fragments; generally well-preserved. Standard OB curriculum text."

  # ═══════════════════════════════════════════════════════════════════
  # ENLIL CYCLE
  # ═══════════════════════════════════════════════════════════════════
  - id: enlil-cycle
    name: "Enlil Cycle"
    stories:
      - id: enlil-and-ninlil
        title: "Enlil and Ninlil"
        native_title: "uru-bi na-nam"
        sources:
          - id: etcsl
            loc: "ETCSL 1.2.1"
            identifier: "ETCSL 1.2.1"
          - id: black-2004
            loc: "pp. 100–107"
            identifier: "ISBN 9780199296330"
          - id: jacobsen-1987
            loc: "pp. 167–180"
            identifier: "ISBN 9780300072785"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Enlil seduces the young Ninlil and is banished from Nippur by the assembly of gods for his transgression. He follows her into exile disguised as various underworld figures, begetting three chthonic deities to serve as substitutes so their son Nanna may ascend to the sky."
        variants:
          - "Minor word variants across Nippur fragments."
        scope_uncertain: false
        identifier_missing: false
        notes: "Mostly complete narrative with some damage in the pursuit sequences and ending."

      - id: enlil-and-sud
        title: "Enlil and Sud"
        native_title: "ni₂-te-a-ni-še₃ i₃-hu-luh"
        sources:
          - id: etcsl
            loc: "ETCSL 1.2.2"
            identifier: "ETCSL 1.2.2"
          - id: black-2004
            loc: "pp. 108–115"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE; rooted in Early Dynastic traditions of Shuruppag"
        summary: "Enlil falls in love with the goddess Sud in Shuruppag and, after a formal courtship involving a bridal gift and negotiations with her mother Nisaba, weds her. Upon marriage Sud is renamed Ninlil and established as Queen of the gods."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Generally well-preserved narrative of divine romance and legal status."

  # ═══════════════════════════════════════════════════════════════════
  # NINURTA CYCLE
  # ═══════════════════════════════════════════════════════════════════
  - id: ninurta-cycle
    name: "Ninurta Cycle"
    stories:
      - id: lugal-e
        title: "Ninurta's Exploits (Lugal-e)"
        native_title: "lugal-e u₄ me-lám-bi nir-ĝál-la"
        sources:
          - id: etcsl
            loc: "ETCSL 1.6.2"
            identifier: "ETCSL 1.6.2"
          - id: black-2004
            loc: "pp. 163–191"
            identifier: "ISBN 9780199296330"
          - id: jacobsen-1987
            loc: "pp. 233–272"
            identifier: "ISBN 9780300072785"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE; possibly composed in the Ur III period"
        summary: "Ninurta battles the demon Asag and its stone army in the mountains, then reorganizes the landscape by damming the primeval waters and assigning fates to each stone that fought for or against him. His mother Ninmah is honored with a new name, Ninhursaja."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "A very long composition (~730 lines). Well-attested in numerous OB manuscripts. One of the most important Sumerian mythological narratives. Also known as 'Lugal-e' from its incipit."

      - id: angim
        title: "Ninurta's Return to Nibru (Angim)"
        native_title: "an-gim dím-ma"
        sources:
          - id: etcsl
            loc: "ETCSL 1.6.1"
            identifier: "ETCSL 1.6.1"
          - id: black-2004
            loc: "pp. 192–198"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "After his military triumph, Ninurta returns in fearsome glory to Nippur, where his excess martial fury alarms even the gods. Enlil and Ninlil welcome him, and his destructive energy is channeled back into cosmic order."
        variants:
          - "Also attested in an Akkadian bilingual version; only the Sumerian text is in scope."
        scope_uncertain: false
        identifier_missing: false
        notes: "Substantially preserved. Sometimes considered a sequel or companion piece to Lugal-e."

      - id: ninurta-and-the-turtle
        title: "Ninurta and the Turtle"
        native_title: ""
        sources:
          - id: etcsl
            loc: "ETCSL 1.6.3"
            identifier: "ETCSL 1.6.3"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "After Ninurta recovers the stolen Tablet of Destinies, Enki tricks him with a turtle that drags him into a pit, punishing Ninurta's arrogance. The story reveals the tension between Ninurta's martial heroism and Enki's cunning supremacy."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Fragmentary. Added per inventory-audit finding (MEDIUM/MISSING). A comic counterpoint to the heroic Lugal-e and Angim."

  # ═══════════════════════════════════════════════════════════════════
  # INANNA CYCLE (divine exploits, excluding Dumuzid-focused narratives)
  # ═══════════════════════════════════════════════════════════════════
  - id: inanna-cycle
    name: "Inanna Cycle"
    stories:
      - id: inanna-and-enki
        title: "Inanna and Enki"
        native_title: "i₃-ne-eš₂ ki-še₃"
        sources:
          - id: etcsl
            loc: "ETCSL 1.3.1"
            identifier: "ETCSL 1.3.1"
          - id: black-2004
            loc: "pp. 63–70"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Inanna visits Enki in Eridu, gets him drunk at a feast, and secures the transfer of the hundred ME — the divine powers underpinning civilization — to her city Uruk. Despite Enki's attempts to recover them once sober, Inanna transports the ME to the E-ana temple."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Fragmentary in the long lists of the ME; narrative structure is otherwise clear. A central text in the Uruk/Eridu rivalry tradition."

      - id: inanna-and-ebih
        title: "Inanna and Ebih"
        native_title: "in-nin me-ḫuš-a"
        sources:
          - id: etcsl
            loc: "ETCSL 1.3.2"
            identifier: "ETCSL 1.3.2"
          - id: black-2004
            loc: "pp. 71–77"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Inanna seeks An's permission to destroy the mountain Ebih, which refuses to show her proper reverence. Despite An's warning, she unleashes a devastating storm of fire and arrows, obliterating the mountain."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Exceptionally well-preserved in numerous copies; part of the standard OB curriculum."

      - id: inanna-and-shu-kale-tuda
        title: "Inanna and Shu-kale-tuda"
        native_title: "u₄-ri-a"
        sources:
          - id: etcsl
            loc: "ETCSL 1.3.3"
            identifier: "ETCSL 1.3.3"
          - id: black-2004
            loc: "pp. 78–84"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 1900–1600 BCE"
        summary: "After being raped by the gardener Shu-kale-tuda while she sleeps beneath a poplar tree, Inanna sends three plagues upon the land to find him. He is eventually captured, judged, and condemned, though his name is paradoxically preserved in memory."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Contains significant fragmentary sections, particularly during the description of the plagues. Known from Nippur tablets."

      - id: inanna-and-gudam
        title: "Inanna and Gudam"
        native_title: ""
        sources:
          - id: etcsl
            loc: "ETCSL 1.3.4"
            identifier: "ETCSL 1.3.4"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "The fearsome creature Gudam terrorizes the city of Uruk, devouring its food and drink. Inanna confronts and defeats the creature, restoring order to her city."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Very fragmentary. Short composition with significant gaps. Auditor should assess whether enough text survives to sustain a retelling in the book."

  # ═══════════════════════════════════════════════════════════════════
  # INANNA AND DUMUZID CYCLE
  # ═══════════════════════════════════════════════════════════════════
  - id: inanna-dumuzid-cycle
    name: "Inanna and Dumuzid Cycle"
    stories:
      - id: inannas-descent
        title: "Inanna's Descent to the Nether World"
        native_title: "an-gal-ta ki-gal-še₃"
        sources:
          - id: etcsl
            loc: "ETCSL 1.4.1"
            identifier: "ETCSL 1.4.1"
          - id: black-2004
            loc: "pp. 52–62"
            identifier: "ISBN 9780199296330"
          - id: jacobsen-1987
            loc: "pp. 205–232"
            identifier: "ISBN 9780300072785"
          - id: sladek-1974
            loc: "Full text and philological commentary"
            identifier: "JHU-diss-1974-Sladek"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Inanna descends through the seven gates of the underworld to challenge her sister Ereshkigal, being stripped of a divine power at each gate until she arrives naked and is killed. She is revived by Enki's creatures but must provide a substitute; she chooses Dumuzid, who ultimately alternates with his sister Geshtinanna in the underworld."
        variants:
          - "Some manuscripts add extra lines regarding the fly's role in locating Dumuzid."
          - "The ending with the seasonal alternation between Dumuzid and Geshtinanna is not present in all manuscripts."
        scope_uncertain: false
        identifier_missing: false
        notes: "Reconstructed from over 40 tablets and fragments, including CBS 12638 and HS 1480. The most extensively attested Sumerian literary composition. Distinct from the Akkadian Descent of Ishtar."

      - id: dumuzids-dream
        title: "Dumuzid's Dream"
        native_title: "šag₄-bi-ta a-še-er"
        sources:
          - id: etcsl
            loc: "ETCSL 1.4.3"
            identifier: "ETCSL 1.4.3"
          - id: black-2004
            loc: "pp. 71–77"
            identifier: "ISBN 9780199296330"
          - id: alster-1972
            loc: "Full text and commentary"
            identifier: "ISBN 9788750015536"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Dumuzid dreams of his own capture by underworld demons and flees through the steppe, repeatedly transforming and hiding with the help of his sister Geshtinanna. He is ultimately caught and taken to the underworld, confirming the grim fate predicted in his dream."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Generally well-preserved. Narratively linked to Inanna's Descent. Critical edition by Alster (1972)."

      - id: inanna-and-bilulu
        title: "Inanna and Bilulu"
        native_title: "uru₂ am₃-ma-ir-ra-bi"
        sources:
          - id: etcsl
            loc: "ETCSL 1.4.4"
            identifier: "ETCSL 1.4.4"
          - id: jacobsen-1987
            loc: "pp. 315–325"
            identifier: "ISBN 9780300072785"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Inanna mourns Dumuzid's death and seeks vengeance against the old woman Bilulu and her son Girgire, who are implicated in his fate. She transforms them into waterskins used in desert libation rituals, linking Dumuzid's death to pastoral cult practice."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Fragmentary in places. Provides a conclusion to the Dumuzid death cycle. Some scholars debate whether Bilulu is directly responsible for Dumuzid's death or whether this is a separate aetiological narrative."

  # ═══════════════════════════════════════════════════════════════════
  # NANNA/SUEN CYCLE
  # ═══════════════════════════════════════════════════════════════════
  - id: nanna-cycle
    name: "Nanna/Suen Cycle"
    stories:
      - id: nannas-journey-to-nibru
        title: "Nanna-Suen's Journey to Nibru"
        native_title: "šeš-ki a-a-ni-ir"
        sources:
          - id: etcsl
            loc: "ETCSL 1.5.1"
            identifier: "ETCSL 1.5.1"
          - id: black-2004
            loc: "pp. 147–155"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "The moon god Nanna loads a barge with trees, animals, and other gifts and travels from Ur to Nippur to visit his father Enlil. Enlil receives the gifts and in return blesses Ur with prosperity and abundance."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Generally well-preserved. Parallels the structure of Enki's Journey to Nibru. Celebrates the Ur-Nippur religious axis."

  # ═══════════════════════════════════════════════════════════════════
  # SUMERIAN GILGAMESH POEMS
  # ═══════════════════════════════════════════════════════════════════
  - id: gilgamesh-poems
    name: "Sumerian Gilgamesh Poems"
    stories:
      - id: gilgamesh-and-aga
        title: "Gilgamesh and Aga"
        native_title: "lu₂-me-en-re₂-e-ne"
        sources:
          - id: etcsl
            loc: "ETCSL 1.8.1.1"
            identifier: "ETCSL 1.8.1.1"
          - id: black-2004
            loc: "pp. 279–284"
            identifier: "ISBN 9780199296330"
          - id: george-2003
            loc: "Vol. 1, pp. 141–148"
            identifier: "ISBN 9780199278985"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE; may reflect Ur III composition"
        summary: "King Aga of Kish demands Uruk's submission; Gilgamesh defies the counsel of the elders and, with the support of the city's young men, successfully resists the siege. He captures Aga but releases him in a gesture of magnanimity, establishing Uruk's independence."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Mostly complete. The only Sumerian Gilgamesh poem without a clear supernatural element — uniquely 'political.' Significant for depicting early Mesopotamian political assemblies (bicameral: elders + young men)."

      - id: gilgamesh-and-the-bull-of-heaven
        title: "Gilgamesh and the Bull of Heaven"
        native_title: ""
        sources:
          - id: etcsl
            loc: "ETCSL 1.8.1.2"
            identifier: "ETCSL 1.8.1.2"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Inanna sends the celestial Bull of Heaven to ravage Uruk after Gilgamesh offends her. Gilgamesh and Enkidu slay the beast, protecting the city but provoking divine consequences."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Heavily damaged, especially in sections describing the confrontation with the bull. The Sumerian original of what became Tablet VI of the Akkadian epic."

      - id: death-of-gilgamesh
        title: "The Death of Gilgamesh"
        native_title: ""
        sources:
          - id: etcsl
            loc: "ETCSL 1.8.1.3"
            identifier: "ETCSL 1.8.1.3"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Gilgamesh confronts the inevitability of his death, reflects on his deeds, and prepares a magnificent funeral for himself and his retinue. He is received in the underworld not as a common ghost but as a judge among the gods of the dead."
        variants:
          - "Tell Haddad (ancient Me-Turan) version offers significant ritualistic variants compared to the Nippur manuscripts."
        scope_uncertain: false
        identifier_missing: false
        notes: "Fragmentary; portions recovered from both Nippur and Tell Haddad."

      - id: gilgamesh-enkidu-and-the-nether-world
        title: "Gilgamesh, Enkidu, and the Nether World"
        native_title: "u₄ re-a u₄ sud-rá re-a"
        sources:
          - id: etcsl
            loc: "ETCSL 1.8.1.4"
            identifier: "ETCSL 1.8.1.4"
          - id: black-2004
            loc: "pp. 285–296"
            identifier: "ISBN 9780199296330"
          - id: george-2003
            loc: "Vol. 1, pp. 175–195"
            identifier: "ISBN 9780199278985"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "After Inanna's huluppu tree is cleared of its supernatural inhabitants, Gilgamesh fashions ritual objects that fall into the underworld. Enkidu descends to retrieve them but breaks the underworld's taboos and is trapped; his ghost returns to describe the grim fate of the dead."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Reconstructed from numerous OB tablets. Opens with a cosmogonic prologue. The basis for Tablet XII of the Akkadian Gilgamesh, though the Sumerian version is an independent composition."

      - id: gilgamesh-and-huwawa
        title: "Gilgamesh and Huwawa"
        native_title: "en-e kur lu₂ ti-la-še₃ (Version A)"
        sources:
          - id: etcsl
            loc: "ETCSL 1.8.1.5 (Version A); ETCSL 1.8.1.5.1 (Version B)"
            identifier: "ETCSL 1.8.1.5"
          - id: black-2004
            loc: "pp. 269–278"
            identifier: "ISBN 9780199296330"
          - id: george-2003
            loc: "Vol. 1, pp. 149–174"
            identifier: "ISBN 9780199278985"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Gilgamesh journeys to the Cedar Forest to establish his name by confronting the guardian Huwawa. He tricks the monster into surrendering his seven magical 'auras' through gifts and flattery before decapitating him."
        variants:
          - "Version A (ETCSL 1.8.1.5): longer, well-preserved, focuses on the trick with the auras and the repetitive exchange."
          - "Version B (ETCSL 1.8.1.5.1): shorter, distinct composition emphasizing Gilgamesh's fear and Enkidu's more prominent role."
        scope_uncertain: false
        identifier_missing: false
        notes: "Both versions are Sumerian compositions independent of the Akkadian Cedar Forest episode. Version A is the better-attested."

  # ═══════════════════════════════════════════════════════════════════
  # ENMERKAR AND LUGALBANDA CYCLE
  # ═══════════════════════════════════════════════════════════════════
  - id: enmerkar-lugalbanda-cycle
    name: "Enmerkar and Lugalbanda Cycle"
    stories:
      - id: enmerkar-and-the-lord-of-aratta
        title: "Enmerkar and the Lord of Aratta"
        native_title: "en-me-er-kar₂ dumu utu-ke₄"
        sources:
          - id: etcsl
            loc: "ETCSL 1.8.2.3"
            identifier: "ETCSL 1.8.2.3"
          - id: vanstiphout-2003
            loc: "pp. 1–95"
            identifier: "ISBN 9781589830837"
          - id: black-2004
            loc: "pp. 236–251"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE; composition possibly Ur III"
        summary: "Enmerkar of Uruk demands materials from the distant city of Aratta to build temples; the two kings exchange riddles, threats, and challenges through messengers. The story includes the famous passage on the 'confusion of tongues' and Enmerkar's invention of writing on clay."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Mostly preserved, though some descriptions of the Aratta response are unclear. A peak achievement of Sumerian narrative poetry (~630 lines)."

      - id: enmerkar-and-en-suhgir-ana
        title: "Enmerkar and En-suhgir-ana"
        native_title: "en-me-er-kar₂-re"
        sources:
          - id: etcsl
            loc: "ETCSL 1.8.2.4"
            identifier: "ETCSL 1.8.2.4"
          - id: vanstiphout-2003
            loc: "pp. 97–169"
            identifier: "ISBN 9781589830837"
          - id: black-2004
            loc: "pp. 252–261"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "The lord of Aratta, En-suhgir-ana, challenges Enmerkar to a sorcery contest. A witch from Aratta is sent to Uruk, but her magic is defeated by an old woman of Uruk, and Aratta's challenge collapses."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Generally well-preserved. Also known as 'Enmerkar and Ensuhkeshdanna' in older literature. Features a magical contest rather than the riddle-exchange of the other Enmerkar poem."

      - id: lugalbanda-in-the-mountain-cave
        title: "Lugalbanda in the Mountain Cave"
        native_title: "u₄ re-a an ki-bi-ta"
        sources:
          - id: etcsl
            loc: "ETCSL 1.8.2.1"
            identifier: "ETCSL 1.8.2.1"
          - id: vanstiphout-2003
            loc: "pp. 171–213"
            identifier: "ISBN 9781589830837"
          - id: black-2004
            loc: "pp. 262–268"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "During Enmerkar's military expedition against Aratta, the soldier Lugalbanda falls gravely ill and is left for dead in a mountain cave. He is healed by the gods Utu, Inanna, and Suen, and survives in the wilderness through ingenuity and divine favor."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Reconstructed from Nippur and Ur fragments; some segments remain unclear. Part of a linked pair with Lugalbanda and the Anzud Bird."

      - id: lugalbanda-and-the-anzud-bird
        title: "Lugalbanda and the Anzud Bird"
        native_title: "lugal-ba-an-da kaskal-še₃"
        sources:
          - id: etcsl
            loc: "ETCSL 1.8.2.2"
            identifier: "ETCSL 1.8.2.2"
          - id: vanstiphout-2003
            loc: "pp. 215–275"
            identifier: "ISBN 9781589830837"
          - id: black-2004
            loc: "pp. 12–22"
            identifier: "ISBN 9780199296330"
          - id: jacobsen-1987
            loc: "pp. 320–344"
            identifier: "ISBN 9780300072785"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Lugalbanda discovers the nest of the divine Anzud bird and treats its chick with great honor — feeding, anointing, and decorating it. In gratitude the bird grants him supernatural speed, which he uses to rejoin Enmerkar's army and deliver a vital message to Inanna in Uruk."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Substantially intact. Standard in the OB Isin-Larsa period curriculum."

  # ═══════════════════════════════════════════════════════════════════
  # OTHER DIVINE NARRATIVES
  # ═══════════════════════════════════════════════════════════════════
  - id: other-divine-narratives
    name: "Other Divine Narratives"
    stories:
      - id: marriage-of-martu
        title: "The Marriage of Martu"
        native_title: "u₄ ul-e"
        sources:
          - id: etcsl
            loc: "ETCSL 1.7.1"
            identifier: "ETCSL 1.7.1"
          - id: black-2004
            loc: "pp. 156–162"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "The god Martu attends a festival and falls in love with the daughter of the god Numushda. Despite her friend's warnings that Martu is an uncivilized nomad who eats raw meat and has no house, the bride accepts him."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Provides a Sumerian perspective on the Amorite ('Martu') people. The comic warnings about nomadic life are ethnographically significant."

  # ═══════════════════════════════════════════════════════════════════
  # UNDERWORLD AND ESCHATOLOGICAL NARRATIVES
  # ═══════════════════════════════════════════════════════════════════
  - id: underworld-eschatology
    name: "Underworld and Eschatological Narratives"
    stories:
      - id: eridu-flood-story
        title: "The Flood Story (Eridu Genesis)"
        native_title: ""
        sources:
          - id: etcsl
            loc: "ETCSL 1.7.4"
            identifier: "ETCSL 1.7.4"
          - id: jacobsen-1987
            loc: "pp. 145–150"
            identifier: "ISBN 9780300072785"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE; the sole known manuscript is from Nippur"
        summary: "The gods decide to destroy mankind with a great flood, but Enki warns the pious king Ziusudra, who survives in a large boat. After the flood Ziusudra is granted immortality and transported to Dilmun."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Fragmentary — the creation of man and the boat-building details are largely missing. Preserved primarily on CBS 10673. This is the Sumerian flood narrative, distinct from the Akkadian Atrahasis."

      - id: ningishzidas-journey
        title: "Ningishzida's Journey to the Nether World"
        native_title: ""
        sources:
          - id: etcsl
            loc: "ETCSL 1.7.3"
            identifier: "ETCSL 1.7.3"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "The god Ningishzida is seized by demons and taken to the underworld. His sister and mother follow, offering laments as they pass through the stations of descent."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Generally fragmentary but vital for understanding underworld ritual and lamentation. OB Nippur tradition."

      - id: death-of-ur-namma
        title: "The Death of Ur-Namma"
        native_title: ""
        sources:
          - id: etcsl
            loc: "ETCSL 2.4.1.1"
            identifier: "ETCSL 2.4.1.1"
          - id: fluckiger-hawker-1999
            loc: "Full text and commentary"
            identifier: "ISBN 9783727812446"
        date_range: "Ur III / Old Babylonian period, ca. 2000–1800 BCE"
        summary: "King Ur-Namma of Ur dies on the battlefield and enters the underworld, where he offers gifts to Ereshkigal and the seven judges of the dead. He is received with honor and assigned a role among the underworld gods."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "ETCSL section 2 (royal compositions), included per scope policy because it contains substantial underworld narrative. Reconstructed from several Nippur tablets. Hybrid genre combining history with underworld myth."

  # ═══════════════════════════════════════════════════════════════════
  # DEBATE POEMS (DISPUTATIONS)
  # ═══════════════════════════════════════════════════════════════════
  - id: debate-poems
    name: "Debate Poems (Disputations)"
    stories:
      - id: debate-hoe-and-plough
        title: "The Debate between Hoe and Plough"
        native_title: "al-e šu mu-ni-ni-ib-gar"
        sources:
          - id: etcsl
            loc: "ETCSL 5.3.1"
            identifier: "ETCSL 5.3.1"
          - id: black-2004
            loc: "pp. 210–218"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "The humble Hoe and the prestigious Plough argue their relative importance to agriculture and civilization. Enlil judges in favor of the Hoe, whose year-round utility and accessibility to the poor outweigh the Plough's seasonal power."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Nearly complete. Standard Nippur and Ur curriculum text."

      - id: debate-ewe-and-grain
        title: "The Debate between Ewe and Grain"
        native_title: "hur-sag an ki-bi-da-ke₄"
        sources:
          - id: etcsl
            loc: "ETCSL 5.3.2"
            identifier: "ETCSL 5.3.2"
          - id: black-2004
            loc: "pp. 219–225"
            identifier: "ISBN 9780199296330"
          - id: kramer-1961
            loc: "pp. 72–73"
            identifier: "ISBN 9780812210477"
        date_range: "Old Babylonian period, ca. 1900–1600 BCE"
        summary: "Beginning with a cosmogonic prologue describing the world before agriculture, the personified Ewe (pastoralism) and Grain (farming) debate which is more essential to civilization. Grain is declared the winner."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Generally well-preserved. The cosmogonic prologue on the 'primitive' state of humanity makes this relevant beyond the debate genre."

      - id: debate-winter-and-summer
        title: "The Debate between Winter and Summer"
        native_title: ""
        sources:
          - id: etcsl
            loc: "ETCSL 5.3.3"
            identifier: "ETCSL 5.3.3"
          - id: black-2004
            loc: "pp. 226–233"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "The personified seasons Enten (Winter) and Emesh (Summer) compete over who produces more bounty for the gods. Enlil judges that Winter is the 'farmer of the gods,' essential for growth."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Mostly complete. Also known as 'Emesh and Enten.' Frequent in Nippur school tablets."

      - id: debate-bird-and-fish
        title: "The Debate between Bird and Fish"
        native_title: ""
        sources:
          - id: etcsl
            loc: "ETCSL 5.3.5"
            identifier: "ETCSL 5.3.5"
          - id: black-2004
            loc: "pp. 234–240"
            identifier: "ISBN 9780199296330"
        date_range: "Old Babylonian period, ca. 1800 BCE"
        summary: "The Bird and Fish argue their relative merits and ritual purity. After escalating insults and the Bird's destruction of the Fish's eggs, Enki intervenes to judge in the Bird's favor."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Exceptionally well-preserved. Contains rich technical vocabulary for fauna."

      - id: debate-copper-and-silver
        title: "The Debate between Copper and Silver"
        native_title: ""
        sources:
          - id: etcsl
            loc: "ETCSL 5.3.6"
            identifier: "ETCSL 5.3.6"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "Copper and Silver argue their relative worth: Copper emphasizes its utility in weapons, tools, and agriculture, while Silver boasts of its prestige and ritual value."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Fragmentary — the verdict and several central sections are missing. Less common than the biological/agricultural debates."

      - id: debate-date-palm-and-tamarisk
        title: "The Debate between Date Palm and Tamarisk"
        native_title: ""
        sources:
          - id: etcsl
            loc: "ETCSL 5.3.7"
            identifier: "ETCSL 5.3.7"
        date_range: "Old Babylonian period, ca. 2000–1600 BCE"
        summary: "The cultivated Date Palm and the wild Tamarisk argue their relative worth, each claiming superiority in usefulness and prestige. The debate explores the tension between domesticated abundance and wild resilience."
        variants: []
        scope_uncertain: false
        identifier_missing: false
        notes: "Fragmentary. Added per inventory-audit finding (MEDIUM/MISSING)."
```
