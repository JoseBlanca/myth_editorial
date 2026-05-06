---
name: story-inventory
description: Produces a structured list of every story the book will cover, each with verifiable scholarly references. Best run with a research-capable AI (Gemini Deep Research or equivalent) that can search many sources at once. Output is inventory.yaml.
---

# story-inventory

## For the human

This step produces what is essentially the book's table of contents — the list of stories it will cover. All the research happens here, not during writing. Everything that follows depends on this list being accurate and staying within the book's scope.

The main risk is invented stories: the AI producing entries for stories that sound plausible for the culture but aren't actually documented in real sources, or confusing stories from one culture with those of a neighboring one. (AI models do this regularly — they "know" enough about a mythology to produce convincing-sounding entries that don't correspond to any real text.)

The defense is strict sourcing. Every story in the list must carry a verifiable reference — not a generic web link (which can be a dead link or a homepage), but something a scholar could look up: a catalogue number (like ETCSL 1.4.1), a museum tablet number (like BM 92687), an ISBN, or a DOI. Entries where no such reference can be found are flagged as uncertain rather than silently included or dropped.

Best run with a research-capable AI (like Gemini Deep Research) that can search many scholarly databases in one pass.

## Inputs
- `scope.md`, `sources.yaml`

## Agent instructions

Using deep research and web search over the whitelisted sources and scholarly surveys, enumerate the major narrative cycles and individual stories of the scope mythology. Group stories by cycle: cosmogony, theogony, major heroic cycles, minor narratives, eschatology, etc. — adjusted to fit the culture (some have no cosmogony, some are organized by hero rather than cycle).

### Genre breadth — narrative is not just myth and heroic epic
Cultures encode cultural knowledge in many narrative forms beyond cosmogony, theogony, and heroic epic. The inventory must take in any text that *tells a story* in order to transmit cultural knowledge — even when it would not be classified as "myth" in a narrow sense. In particular, look for and include:

- **Disputation and debate poems** — personified objects, plants, animals, trades, or seasons argue out their relative usefulness (e.g., the Akkadian *Tamarisk and Date Palm*, the Sumerian *Hoe and Plough*, *Winter and Summer*). These encode agronomy, animal husbandry, and the social hierarchy of the trades.
- **Animal fables** — animals act out social dramas with ethical or political payload (e.g., the Akkadian *Series of the Fox*; many cultures have analogues).
- **Practical instruction literature** — a sage or father transmits ethical and social knowledge as connected counsel rather than as a dialogue (e.g., the Akkadian *Counsels of Wisdom* and *Šimâ milka*; Egyptian *Instruction* genre; the Hebrew *Proverbs* tradition; the Vedic and Avestan *Yasna* counsel literature). Include these when they carry continuous narrative or sustained quasi-narrative voice; pure proverb-collections without narrative frame are out.
- **Etiological narratives embedded in incantations, rituals, and medical texts** — short freestanding cosmogonies and origin stories that explain how a particular ill came to be (e.g., the Akkadian *Worm and the Toothache*; Egyptian *Isis and the Name of Ra*). These are often the oldest layer of a culture's narrative tradition.
- **Visionary and dream narratives** — first-person otherworld journeys (e.g., the Akkadian *Underworld Vision of an Assyrian Prince*).
- **Folktales, comic narratives, and satirical pieces** — narrative compositions outside the elite heroic register (e.g., the Akkadian *Poor Man of Nippur*).
- **Narrative hymns** — hymns that tell a story rather than only praise (e.g., the Akkadian *Agushaya Hymn*, where Ishtar creates Saltu; many Vedic hymns).
- **Pseudo-prophecies, *naru* literature, royal legends** — texts in the voice of a king or sage that narrate past or claimed-future events with cosmic and political payload.

The principle: any text that transmits cultural knowledge in narrative form is a candidate for inclusion. When in doubt about a borderline genre (instructions, narrative hymns, ritual prologues), include the entry and let the human reviewer decide whether it earns a chapter, an appendix entry, or removal — leaving it out at the inventory stage means it is silently lost.

### Sourcing rule
Every story entry must carry at least one verifiable identifier. A verifiable identifier is one of:
- **DOI** (for journal articles or modern books with DOIs).
- **ISBN** (for printed critical editions).
- **Tablet/manuscript museum number** (e.g., BM 92687, CBS 14061).
- **Corpus text identifier** (e.g., ETCSL 1.4.1, Perseus urn:cts:greekLit:...).
- **Stable archival URL** to a scholarly repository (not a generic homepage, not Wikipedia).

Entries lacking any verifiable identifier are flagged `identifier_missing: true` rather than silently omitted.

### Contamination refusal
If a story is attested only in a culture listed under "Excluded adjacent cultures" in `scope.md`, omit it. If it is attested in both the scope culture and an excluded culture, include it but check whether the specific *plot details* you've found come from the scope culture's attestations or the excluded culture's. Flag `scope_uncertain: true` for anything you cannot clearly assign.

### Scope of entries
Aim for comprehensiveness within the scope, not exhaustiveness. Include every story with a recognized scholarly attestation in the culture's major reference works. A story mentioned in one footnote of one monograph does not belong in the inventory; a story covered in Black et al. 2004 or equivalent does.

## Output: `inventory.yaml`

```yaml
cycles:
  - id: cosmogony
    name: "Cosmogonic cycle"
    stories:
      - id: <slug>
        title: "<English working title>"
        native_title: "<if applicable>"
        sources:
          - id: <source_id from sources.yaml whitelist>
            loc: "<tablet/line/page reference>"
            identifier: "<DOI, ISBN, museum number, or corpus identifier>"
        date_range: "<approximate date of composition>"
        summary: "<two sentences>"
        variants: [<brief notes if multiple versions exist within the scope culture>]
        scope_uncertain: false
        identifier_missing: false
        notes: "<lacunae, textual issues, anything the auditor should know>"
```

## Self-check before returning
1. Every entry has at least one `identifier` that could be verified by a third party.
2. No entries rely on Wikipedia as authority (acceptable as lead only, not as `source`).
3. Every `scope_uncertain: true` entry has a note explaining the uncertainty.
4. Internal variants (multiple in-scope sources giving different versions) are recorded in the `variants` field, not flagged as problems.

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
To `inventory-audit`, which must be run in a fresh conversation — preferably with a different AI model, but the same model in a fresh conversation is acceptable if a different one is impractical.
