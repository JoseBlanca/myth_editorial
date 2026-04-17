# Grammar-check diff — Chapter 17: Nanna-Suen's Journey to Nibru

Stage: 14b grammar-check
Input: `chapters/17-nannas-journey-to-nibru.resolved.adoc`
Output: `chapters/17-nannas-journey-to-nibru.grammar-checked.adoc`

## Changes

No grammar, readability, or punctuation changes were made to the main prose. Every candidate issue was reviewed and either resolved to "no change needed" by the skill's own rules or deferred to a later stage. The `.grammar-checked.adoc` file is byte-identical to the `.resolved.adoc` input.

## Reviewed and not fixed (with rationale)

### Sentence length (>50-word threshold)

- **Line 3** — `Multiple Old Babylonian copies from Nippur (Sumerian: Nibru) — the religious capital of Sumer, seat of Enlil's temple the E-kur — and from Ur scribal schools confirm its place in the _edubba_ curriculum, the standard body of texts that trainee scribes copied and studied.`
  - Length: ~42 words. Under threshold.
  - Structure: one em-dash appositive on Nippur plus one comma appositive on _edubba_ curriculum. Parsable on one read.
  - Not fixed.

- **Line 11** — `Ur (Sumerian: Urim) — the great city of southern Mesopotamia, seat of Nanna's temple the Ekishnugal — was the economic powerhouse, wealthy from trade, agriculture, and the vast canal-fed estates of its hinterland.`
  - Length: ~31 words. Well under threshold.
  - Structure: one em-dash appositive on Ur plus a trailing `wealthy from …` adjective phrase listing three sources. Parsable.
  - Not fixed.

- **Line 15** — `Nanna-Suen — the moon god, son of Enlil, king of the gods, lord of wind and command, supreme authority in Nippur — is the patron deity of Ur, and therefore the divine figure who most naturally embodies this relationship.`
  - Length: ~40 words. Under threshold.
  - Structure: the em-dash block contains an apposition list that could, on first read, ambiguously attach "king of the gods, lord of wind and command, supreme authority in Nippur" to either Nanna-Suen or Enlil. The fidelity-check stage (12) explicitly confirmed that these three phrases are glosses of Enlil pulled from the glossary, and the construction was locked as faithful. A "fix" (e.g. parentheses around the Enlil glosses inside the em-dash block) would introduce nested parentheticals — exactly the structure the skill says to flatten — and would touch a fidelity-locked construction. Readers who reach this chapter have been told earlier in the book that Enlil is the chief god and lord of Nippur, so the attachment resolves contextually.
  - Not fixed — flagged for human review only if line-edit chooses to rework.

- **Line 36** — `Each stop confirms the same proposition: the journey from Ur to Nippur is not merely a transit but a procession through a connected network of cult centres, each of which acknowledges Nanna's passage and, by extension, the legitimacy of the relationship his journey enacts.`
  - Length: ~44 words. Under threshold.
  - Structure: one `not merely X but Y` construction followed by a relative clause with a compound object (`Nanna's passage and … the legitimacy …`). Parsable on one read.
  - Not fixed.

- **Line 40** — `The text functions, among other things, as a map — not a drawn map, because the Sumerians encoded their geography in narrative rather than cartography, but a map nonetheless.`
  - Length: ~30 words. Under threshold.
  - Structure: `not X, because Y, but Z` is dense but grammatically sound; the interpolated `because` clause explains the qualification. Parsable on second read; the cadence is a style choice belonging to line-edit.
  - Not fixed.

- **Line 40** — `When a scribal student copied this text, he was learning the geography of southern Mesopotamia at the same time as he was learning its mythology.`
  - Length: ~26 words. Under threshold.
  - Pronoun `he` is generic singular for a student whose gender is unknown; consistent with the book's established register for Old Babylonian scribes.
  - Not fixed.

- **Line 57** — `The blessing encompasses agricultural abundance, commercial prosperity, and military security for Ur and its people, granted through Enlil's supreme divine authority.`
  - Length: ~23 words.
  - Trailing participial phrase `granted through …` attaches cleanly to `security … for Ur and its people` (or to the whole preceding noun phrase); no dangling-modifier issue.
  - Not fixed.

- **Line 61** — `Enlil's endorsement of Ur through Nanna validates the political and cultic pre-eminence of Ur within the Sumerian city-state system.`
  - Length: ~20 words. Under threshold.
  - Not fixed.

- **Line 72** — `The royal-legitimation function operates through the reciprocal logic of the journey itself: Ur sends offerings to Nippur and receives Enlil's blessing in return, encoding the dependence of secular power on religious sanction.`
  - Length: ~33 words. Under threshold.
  - Structure: colon introduces an explanatory clause followed by a participial gloss. Parsable.
  - Not fixed.

- **Line 75** — `The divine statues may have been aboard — the evidence is suggestive though not conclusive — and the cities they passed through would have marked their transit with offerings and ceremonies of their own.`
  - Length: ~34 words. Under threshold.
  - Structure: em-dash aside on the evidence, then a coordinated main clause. Parsable.
  - Not fixed.

- **Line 82** — `Where Enki's journey proceeds directly from Eridu to Nippur without lingering on intermediate stops, Nanna's journey maps the entire canal corridor between Ur and Nippur, naming each city and cult centre along the route.`
  - Length: ~34 words. Under threshold.
  - Structure: one `where …, Nanna's journey …` contrast plus one participial tail (`naming …`). Parsable.
  - Not fixed.

- **Line 97** — `They were learning how their world worked: the canals that connected its cities, the offerings that maintained its temples, the blessings that legitimated its rulers, and the reciprocal logic that held the whole structure together.`
  - Length: ~35 words. Under threshold.
  - Structure: a parallel four-item list of noun phrases with matching relative clauses. Parsable as deliberate anaphora.
  - Not fixed.

### Nested / em-dash parentheticals

- **Lines 3 and 11** — `Nippur (Sumerian: Nibru) — the religious capital …` and `Ur (Sumerian: Urim) — the great city …`
  - Technically a parenthesis `(Sumerian: …)` sits adjacent to an em-dash appositive on the same noun, giving a near-nested feel. The parenthesis carries a separate informational unit (the Sumerian-name gloss) that the book uses throughout as a fixed house style. Flattening it would require either deleting the Sumerian name (loss of content) or hoisting it to a separate sentence (style change). The parenthesis and em-dash operate at different semantic levels (language gloss vs. descriptive apposition), so there is no true nesting of asides.
  - Not fixed.

- **Line 15** — em-dash block on Nanna-Suen containing a comma-separated apposition list: see the sentence-length entry above.
  - Not fixed.

### Subordinate-clause density

- **Line 97** — `The entire system — religious, political, economic — is visible in these three hundred and fifty lines.` and the surrounding paragraph of short declarative fragments (`A god loads a barge. A barge travels a canal. A father blesses a son. A city receives divine favour in exchange for material offerings.`)
  - The short declarative fragments are a clearly intentional rhetorical cadence closing the chapter. The skill explicitly exempts fragments used for effect.
  - Not fixed.

### Punctuation and mechanics

- **Line 11** — `The axis between these two cities was central to Ur III royal ideology: Ur supplied the wealth, Nippur supplied the sanction.`
  - The two short independent clauses after the colon are joined by a comma rather than a semicolon. This is an accepted post-colon pattern for short parallel clauses and is common in British academic prose. Not a comma splice in the proscribed sense.
  - Not fixed.

- **Line 36** — `The repetition is not monotony — it is structure.`
  - Em-dash joining two independent clauses: idiomatic emphatic use. Parsable.
  - Not fixed.

- **Line 64** — `Goods went up the canal from Ur to Nippur. Blessing came back down the canal from Nippur to Ur. The system works.`
  - Three short declarative sentences forming the paragraph close. Style choice; no fix needed.
  - Not fixed.

### Marker-resolved passages (hard rule 4)

The following blocks are italicised marker-resolved asides and footnote text. Hard rule 4 forbids edits to these, and the user's directive also lists "marker-resolved passages" and "footnote content" as out of scope. The `..` double-period artefacts below are noted for the pipeline record but not touched.

- **Line 26** — `_(The detailed gift catalogue closely parallels real cultic offerings documented in administrative tablets, suggesting the composition served as a mythic charter for actual barge processions and offering deliveries between Ur and Nippur..footnote:[Inference: Administrative texts from the Ur III period attest to regular deliveries of goods from Ur to Nippur's Ekur temple.. Risk: Direct correspondence between literary and administrative texts cannot be proven; the literary list may be idealised..])_`
  - Contains `..` at `Nippur..footnote:[…]`, at `Ekur temple..`, and at `idealised..])_`. These are residues from the inference/risk marker-resolution stage. Marker-resolved block; not fixed.

- **Line 38** — `_[At this point the tablet breaks. Several lines (approximately lines 170–195) describing stops along the canal route are partially damaged.. Partial; overlapping manuscripts restore most of the itinerary, but some station names and gift descriptions remain uncertain..]_`
  - Contains `..` at `damaged..` and at `uncertain..]_`. Marker-resolved lacuna block; not fixed.

- **Line 51** — `ETCSL 1.5.1, gift-catalogue and blessing formulae as rendered in the ETCSL composite.footnote:[An alternate tradition gives: "Black et al. 2004, pp. 152–154, minor editorial choices in rendering the gift-catalogue and blessing formulae". The prevalent version is chosen here because ETCSL composite represents broad manuscript agreement and is the standard scholarly text..]`
  - Line reads as a sentence fragment / source-selection stub; the footnote inside it has `..]` at `text..]`. Marker-resolved version-choice block; not fixed.

- **All `footnote:[…]` bodies** — per the user's directive ("Don't fix: … footnote content") and the skill's hard rule 2.
  - Not fixed.

### AsciiDoc structure

- All `== `, `'''`, `//` directives, `footnote:[…]`, `// EVIDENCE:`, and `// COMPARATIVE-HOOK:` markers preserved unchanged (hard rule 5).

## Self-check

1. No factual content changed — file is byte-identical to the resolved input.
2. Footnote count unchanged: 19 `footnote:[…]` occurrences in both files.
3. AsciiDoc structure intact: heading, section breaks (`'''`), EVIDENCE tokens (22), COMPARATIVE-HOOK tokens (2) all preserved.
4. Every reviewed candidate is logged above with a rationale; no silent changes.
