# Prompt for: scope-lock
# Book: sumer
# Generated: 2026-04-12T14:26:07Z

---

# Skill instructions: scope-lock

---
name: scope-lock
description: Interactive conversation run once at the start of each book. Produces scope.md and sources.yaml — the two files that define what belongs in the book and what doesn't. Every later stage reads them.
---

# scope-lock

## For the human

This is where you define what the book is and, equally importantly, what it is not. A Sumerian book is not a Mesopotamian book. A Norse book is not a Germanic book. Without a locked scope, the research, drafting, and checking stages drift: material from neighboring cultures seeps in, and by the time anyone notices, it's woven through every chapter.

This step runs once, at the very start. It produces two files — `scope.md` (what the book covers and excludes) and `sources.yaml` (which scholarly sources are approved and which are banned). Every AI working on every later stage reads these two files before doing anything. They are the rulebook for the entire book.

This step is a conversation between you and the AI. The AI will ask you questions about the book's boundaries. Don't accept vague answers from yourself — the more specific you are here, the fewer problems you'll have later. Three decisions matter most:

1. **Which neighboring cultures to exclude.** For a Sumerian book, the main risk is Akkadian/Babylonian material leaking in. For a Norse book, it's continental Germanic and Christianized sagas. The AI will propose specific exclusions with reasons; you confirm or adjust.

2. **What counts as a legitimate gap-fill.** Ancient texts have physical gaps — broken tablets, lost pages. The pipeline allows filling those gaps from other texts in the same tradition, clearly marked. You need to define what "same tradition" means for this book (e.g., "any Sumerian literary text from within 400 years of the damaged one").

3. **Which sources are approved.** The AI will propose 8–15 scholarly sources (critical editions, standard reference works) and a blacklist of popularizations that should never be cited. You approve or edit the lists.

## Inputs
- Target mythology (e.g., "Sumerian", "Norse", "Yoruba")
- User's goals and any hard exclusions they already have in mind

## Agent instructions

Run an interactive dialogue. Work through the template below with the user, question by question. Propose defaults drawn from scholarly consensus when the user doesn't know, and confirm their choice.

Pay particular attention to three sections that the rest of the pipeline depends on:

**1. Excluded adjacent cultures.** Name the specific cultures most likely to contaminate this book. For Sumerian, this is Akkadian/Babylonian. For Norse, it is continental Germanic and later Christianized sagas. Propose at least three specific contamination risks per book (more if the culture sits in a dense neighborhood), with a one-line rationale for each, and have the user confirm.

**2. Reconstruction policy.** When a primary source has a physical gap (tablet broken, manuscript leaf lost), the chapter-draft stage is allowed to fill that gap from another in-tradition source, flagged with a `[RECONSTRUCTION:]` marker. Ask the user to define precisely what counts as "in-tradition" for this book. Propose a default: same culture, same language of composition, within ±N centuries of the gap-bearing source. The user confirms or narrows.

**3. Source whitelist and blacklist.** Propose 8–15 whitelisted academic sources (critical editions, standard reference works, peer-reviewed corpora) and a blacklist of common contaminating popularizations. The user approves or edits.

## Outputs

### `scope.md`

```markdown
# Scope: <Mythology Name>

## Culture
<Name, self-designation, geographic extent>

## Period
<Earliest attested in-scope source — latest in-scope source>

## Languages of primary sources
<List>

## Excluded adjacent cultures (contamination risks)
- **<Culture A>**: <one-line reason, e.g., "Shares pantheon but distinct literary tradition; covered in separate book.">
- **<Culture B>**: <reason>
- **<Culture C>**: <reason>

## Reconstruction policy
When a primary source has a physical lacuna, content may be reconstructed from:
- <Defined in-tradition corpus, e.g., "Any Sumerian literary composition from the Old Babylonian scribal tradition, ca. 2000–1600 BCE">
- Reconstructions must be flagged with [RECONSTRUCTION:] markers; they are not silent fills.

## In-scope corpus (broad)
<Text collections, tablet series, manuscript traditions>

## Out-of-scope (explicit)
<Specific texts a naive researcher would wrongly include>

## Book register
Asimov-style retelling. Narrative prose in the body. Citations in AsciiDoc footnotes. Inferences, lacunae, reconstructions, and variants flagged inline with explicit markers.

## Variant presentation policy
- If one variant is clearly prevalent in the scholarly corpus: present it in the body, with minor variants in footnotes.
- If several variants are roughly co-equal: present them inline in the chapter body, introducing each with its source.
```

### `sources.yaml`

This file is a real source registry, not just a whitelist. Later stages use it for citation normalization, bibliography generation, and disambiguation. Every field marked (required) must be present.

```yaml
registry:
  - id: <short_id>                              # (required) unique key, used in all citations
    source_tier: primary | primary-translation | secondary | reference | comparative
    in_scope: true | false                       # false for comparative-only sources
    author: <last, first>                        # (required)
    title: <title>                               # (required)
    year: <year>                                 # (required)
    translator_editor: <name, if applicable>
    container_title: <journal or edited volume, if applicable>
    full_citation: <complete bibliographic string>  # (required) — used in first footnote mention
    short_citation: <author year>                   # (required) — used in subsequent footnote mentions
    identifier_type: DOI | ISBN | corpus-id | museum-number | stable-url
    identifier_value: <the identifier>              # (required)
    access_url: <where to retrieve the text, if online>
    notes: <any caveats — e.g., "translation only, no original-language text">

blacklist:
  - pattern: <URL pattern or citation pattern>
    reason: <why excluded>

triangulation_databases:
  # Culture-appropriate databases for verifying tablet/manuscript references
  - id: ETCSL
    url: https://etcsl.orinst.ox.ac.uk/
    covers: Sumerian literary texts
  # ...
```

The `full_citation` and `short_citation` fields are used directly by `format-finalize` to build the bibliography — no parsing of free-text footnotes required.

## Handoff
Pass `scope.md` and `sources.yaml` to `story-inventory`. These files are re-read by every subsequent skill.
