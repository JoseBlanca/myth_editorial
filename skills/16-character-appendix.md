---
name: character-appendix
description: Produces a reference appendix listing every named character in the book — who they are, where they appear, what they look like (only if the sources actually say so), and how important they are. Runs after all chapters are finished. Goes through fact-checking before the book is assembled.
---

# character-appendix

## For the human

This appendix is the reader's reference companion. Halfway through a chapter on Gilgamesh, the reader encounters Siduri and wants to know: who is she, where else does she appear, what does she look like? This appendix answers that — and only what the sources actually say.

The hardest discipline here is restraint on physical descriptions. AI models asked to describe a mythological character will readily produce vivid physical portraits drawn from cultural stereotypes, later artistic traditions, or pure invention. For most ancient characters, the sources say very little about physical appearance — sometimes nothing at all. The correct entry is an honest "No physical description survives in the in-scope sources," not a fabricated portrait. Accuracy is more important than completeness: it is better to leave a field empty than to fill it with something the sources don't support.

This step runs after all chapters are finalized because it needs the final text to build accurate cross-references ("Siduri appears in Chapter 5, where she..."). It goes through fact-checking by a different AI before the book is assembled.

**Note on markers and line-edit:** The character appendix is a reference section, not narrative prose. It does not use `[INFERENCE:]`, `[LACUNA:]`, or other markers — all claims must be directly sourced or explicitly noted as absent. It does not go through `marker-resolve` or `line-edit`. The Asimov register and citation discipline are enforced at writing time; the factcheck catches any problems.

## Cardinal rule

**Never fabricate or infer physical descriptions.** If no in-scope source describes a character's appearance, the entry says so explicitly. Later artistic depictions, out-of-scope literary traditions, and modern illustrations are not evidence for how the culture described the character. A missing physical description is not a gap to fill — it is information about what the sources contain.

## Inputs
- `scope.md`, `sources.yaml`, `glossary.yaml`
- All `chapters/NN-<slug>.edited.adoc` (final prose, for cross-referencing)
- `chapters/00-introduction.edited.adoc`
- `comparative.adoc` (edited)
- All `briefs/*.yaml` (for source pointers)
- Primary source translations — pasted or accessible via fetch

## Agent instructions

### Step 1: Character extraction

Scan all edited chapters (including introduction and comparative chapter) for every named character. A character is any named entity that acts or is acted upon in the narrative: deities, heroes, creatures, notable mortals, personified concepts. Places and artifacts are excluded (they belong in the glossary).

For each character, record every chapter in which they appear and the AsciiDoc section anchor or heading under which they appear.

### Step 2: Entry composition

For each character, compose an entry with these fields:

**1. Name and identification**
- Use the `glossary.yaml` rendering. If the character is in the glossary, use the locked form. If not, use the most common scholarly transliteration and note it.
- One-sentence identification: role (deity, hero, mortal, creature), domain or function, and relationship to other characters. Sourced.

**2. Physical description**
This is the most audit-sensitive field. Rules:
- **Include only** descriptions explicitly attested in in-scope primary sources. Quote or closely paraphrase the source, with a footnote citation.
- **Acceptable evidence**: direct textual description ("Enkidu was hairy-bodied, with hair like a woman's"), iconographic conventions described in scholarly sources ("Consistently depicted with horned crown in Ur III cylinder seals, per Collon 1987"), or epithets that imply physical traits ("the wild bull" — note this is an epithet, not a literal description).
- **Not acceptable**: descriptions from out-of-scope traditions, later artistic traditions, modern illustrations, inferences from the character's role ("as a sun god, he was likely depicted as radiant"), or generic cultural assumptions.
- **If no physical description survives**: write exactly: "No physical description survives in the in-scope sources." Do not soften this ("little is known about...") — the absence is the fact.
- **Partial descriptions**: if the sources describe one aspect (e.g., a distinctive garment or attribute) but not the full figure, report what exists and note what is absent.

**3. Myths and appearances**
A list of every myth/story in which the character appears, cross-referenced to the chapter where the reader can find it. For each appearance, one sentence on the character's role in that story. Use AsciiDoc cross-references (`<<anchor, display text>>`) to link to chapters.

Order: by narrative chronology within the mythology (cosmogonic appearances first, then theogonic, heroic, etc.), not by chapter number — though chapter numbers should be noted.

**4. Relevance in the mythology**
2–4 sentences on the character's overall importance: how central they are to the mythological corpus, whether they appear across many stories or only one, what scholarly consensus says about their significance. Cite sources. This overlaps with the introduction chapter's centrality assessment but is focused on the individual character rather than the story.

### Step 3: Organization

Sort entries alphabetically by the `glossary.yaml` English rendering (or by scholarly transliteration for characters not in the glossary).

Group into sections if the character count warrants it:
- **Deities** (subdivide by rank/domain if the culture has a clear hierarchy)
- **Heroes and mortals**
- **Creatures and monsters**
- **Personified concepts** (if applicable — e.g., Sumerian *me*, personified Fate)

If the book has fewer than ~20 characters, a single alphabetical list is cleaner than forced categories.

### Style

Same Asimov register as the rest of the book. Entries should be readable as standalone mini-profiles, not dry catalogue entries. But brevity matters — this is a reference appendix, not a chapter. Each entry should be 80–300 words depending on the character's prominence.

### Citations

Same rules as the rest of the pipeline: cite only sources provided in the conversation or fetched via tool use. AsciiDoc footnotes. Every factual claim — especially every physical description — needs a citation.

## Output: `character-appendix.adoc`

```asciidoc
[appendix]
== Characters

A reference guide to the named characters who appear in this book. Physical descriptions are included only where attested in the in-scope sources; where the sources are silent, this is noted explicitly.

=== Deities

[[char-<slug>]]
==== <Character Name>

<One-sentence identification with role and relationships.>

*Physical description.* <Attested description with citation, OR "No physical description survives in the in-scope sources." OR partial description noting what is and is not attested.>

*Appears in:*

* <<chapter-anchor, _Chapter Title_>> — <one-sentence role in that story.>
* <<chapter-anchor, _Chapter Title_>> — <one-sentence role.>

*Relevance.* <2–4 sentences on importance in the mythology, with citations.>

=== Heroes and Mortals

...

=== Creatures and Monsters

...
```

## Self-check before returning
1. Every physical description cites an in-scope primary source. No exceptions. Grep for any physical-appearance language without a footnote — that is a fabrication risk.
2. No entry contains the phrases "likely appeared", "was probably depicted", "would have looked", "may have been described as", or similar hedged fabrications. If the source doesn't describe it, the entry says so flatly.
3. Every chapter cross-reference resolves to an actual chapter anchor.
4. Every character who appears in any chapter is in the appendix. Grep all chapter files for proper nouns and compare against the appendix entry list.
5. Glossary renderings match `glossary.yaml`.
6. Entries are sorted alphabetically within their category.
7. No out-of-scope source cited for physical descriptions or character details.

## Handoff
To `prose-factcheck` (fresh conversation, different model) for a factcheck pass focused on:
- Fabricated or unsourced physical descriptions (the primary risk).
- Cross-reference accuracy.
- Claims about mythological relevance.

After factcheck passes, to `format-finalize`.
