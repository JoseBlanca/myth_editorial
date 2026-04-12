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
To `prose-factcheck`, fresh conversation, different model.
