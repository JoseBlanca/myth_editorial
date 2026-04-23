# Mythology Book Pipeline

A step-by-step process for producing mythology books in the style of Isaac Asimov's non-fiction: clear, plain-English retellings of myths, one culture per book, with every factual claim traced to a scholarly source. The process uses AI agents (Claude, GPT, Gemini, etc.) working in sequence, each doing one job and checked in a fresh conversation with no memory of the writing — ideally by a different AI model, but the same model is acceptable when running a different one is impractical. It handles the hard parts of mythology writing: gaps in ancient texts, contradictory versions of the same story, and the constant risk of mixing up material from neighboring cultures.

## Core principles

1. **The checker must have no memory of the writing.** Every check runs in a fresh conversation (or a fresh process, for autonomous runs) so the checker cannot rely on anything but the artefacts in front of it. Using a different AI model for the check is preferred — two models make independent mistakes — but the same model in a fresh conversation is acceptable when a second model is not available. What never works is self-review in the same conversation: it catches almost nothing.

2. **Three files govern the entire book.** Three files are created early and must be read by every AI and every human before starting any later stage:
   - `scope.md` — what culture, period, and sources the book covers, and what it explicitly excludes.
   - `sources.yaml` — the approved list of scholarly sources (whitelist) and banned popularizations (blacklist).
   - `glossary.yaml` — the locked English translations for key terms (created after the scope, before any writing begins).

   These are the single source of truth. If an AI or human is unsure whether something belongs in the book, these files have the answer.

3. **Cite only sources you can see.** When writing, the AI may only cite sources whose text has been pasted into the conversation or retrieved during it. No citing from the AI's training memory, even for famous texts. This is the main defense against fabricated references — a common AI failure mode.

4. **Contradictions between sources are normal, not errors.** Ancient mythologies have multiple versions of the same story. Two legitimate sources disagreeing is part of the record, not a mistake. The pipeline handles this explicitly: when one version dominates the scholarly record, it goes in the main text with alternatives in footnotes. When versions are roughly equal, they are presented side by side. The key is to never silently pick one and ignore the others.

5. **Check the document, not the deity.** When checking whether something belongs in the book, the question is: "Does this specific story detail appear in a document from within our scope?" — not "Does this god belong to our culture?" Gods and heroes cross cultural boundaries; specific narrative details are tied to specific texts. A detail found only in a Babylonian tablet does not belong in a Sumerian book, even if the god is originally Sumerian.

6. **Chapter length follows the evidence.** A myth preserved on a single broken tablet gets a short chapter. A richly-documented cycle gets a long one. Chapters are never padded to reach a target length.

7. **Human edits are validated before proceeding.** Every time a human reviews and modifies a file, the result must pass a validation step (`post-human-normalize`) before it becomes input for the next stage. Human edits are one of the main ways that the pipeline's structural guarantees can break — merged claims, removed markers, altered citations. The validator catches these before they propagate.

8. **Comparison metadata is not comparison prose.** Cross-cultural notes may exist in planning files and comments throughout the pipeline, but reader-facing comparison prose is confined to the comparative chapter. This distinction — noting a parallel vs. writing about it — must be enforced.

## Global contracts

These rules apply across all stages. They are not repeated in each skill, but every skill must comply.

**Provenance metadata.** Every machine-generated file must include a metadata block recording: the stage that produced it, the AI model used, and a timestamp. For YAML files, use a `meta:` section. For AsciiDoc files, use a comment block at the top. This makes model-separation auditable rather than trust-based.

**Canonical anchors.** Every chapter has a stable anchor ID defined in its brief (e.g., `ch-01-descent-of-inanna`). All cross-references use this anchor, never auto-generated section IDs. Anchors survive marker-resolve and line-edit unchanged.

**Evidence tokens.** Every factual claim carries both a reader-facing AsciiDoc footnote AND a machine-readable evidence token in a comment. The token format is: `// EVIDENCE: source_id=<id> ; loc=<tablet/line/page>`. The `format-finalize` stage builds the bibliography from these tokens (not from parsing footnote prose), which eliminates ambiguity between bibliographic and editorial footnotes.

**Negative-evidence discipline.** When a source does not attest something (e.g., no physical description survives), this must be stated explicitly and scoped: "No physical description survives in the in-scope sources" — not "No description exists." Absence of evidence in the in-scope corpus is not the same as universal absence.

**Template discipline.** Any skill that tells an agent to render a marker, claim, footnote, or other structured element into prose using a template with `<placeholder>` slots must follow three rules:

1. *Every template ships with at least one worked input→output example.* A template without an example is a specification, not an instruction — agents will guess at the slot-filling rule and guess differently each time.
2. *Every template specifies a trailing-punctuation rule.* If a slot value may end with `.`, `?`, `!`, or `…`, the template must say explicitly whether to suppress its own following separator. Past runs have shipped "..]_" and ".. Risk:" into the final PDF because this was implicit.
3. *Every template specifies fallback behaviour for empty, missing, or sentinel-valued slots* (`none`, `n/a`, `—`, etc.). The renderer must never emit a literal `<placeholder>` token, an empty paren `(. [n])`, or a leaked sentinel word. When a required slot is missing, the skill must describe a concrete fallback (e.g. "render the claim as plain prose without a footnote") rather than letting the agent improvise.

The corresponding skill's self-check must include grep-based anti-pattern checks for each of the three failure modes (placeholder leaks, empty slots, sentinel leaks), and the downstream stage that assembles final artefacts must mirror those checks as a safety net.

## Stage order

The book is built in stages. Each stage produces a file that the next stage consumes. `[HUMAN]` marks points where you review and approve before continuing. The arrows show what feeds into what:

```
scope-lock → story-inventory → inventory-audit →
  [HUMAN] → post-human-normalize(inventory) →
  chapter-briefs → glossary-lock →
  intro-chapter → prose-factcheck(intro) →
  [HUMAN] → post-human-normalize(intro) →
  [per chapter:
    chapter-claims → claims-factcheck →
    [HUMAN] → post-human-normalize(claims) →
    chapter-draft → narrative-fidelity →
    [HUMAN if REVISE] → post-human-normalize(narrative if revised)] →
  comparative-chapter → prose-factcheck(comparative) →
  [HUMAN] → post-human-normalize(comparative) →
  marker-resolve → line-edit →
  character-appendix → prose-factcheck(appendix) →
  [HUMAN] → post-human-normalize(appendix) →
  format-finalize
```

**In plain English:** First you define what the book covers and what sources are allowed (scope-lock). Then an AI researches all the stories (story-inventory), and the list is checked in a fresh conversation (inventory-audit) — ideally by a different AI, but the same model in a fresh conversation is fine. You review, the result is validated (post-human-normalize), then turned into one planning document per chapter (chapter-briefs) and a locked glossary (glossary-lock). An introductory chapter on cultural context is written and fact-checked in a fresh conversation (prose-factcheck); you review; the result is validated. Then, for each story chapter: the facts are written out one by one (chapter-claims), checked in a fresh conversation (claims-factcheck), you review, the result is validated, then the facts are turned into narrative prose (chapter-draft), and a fresh conversation confirms the prose faithfully represents the facts (narrative-fidelity) — if it finds problems, you review and the result is validated. After all story chapters are done, a cross-cultural comparison chapter is written and fact-checked (prose-factcheck); you review; validated. Then all chapters get their placeholder markers converted to final text (marker-resolve) and a prose-quality polish (line-edit). A character reference appendix is compiled and fact-checked (prose-factcheck); you review; validated. Finally, everything is assembled into a book with a bibliography and validated (format-finalize).

## Artifact layout per book

```
<book-name>/
  cover.jpg                          (provided by user — JPG or PNG)
  scope.md
  sources.yaml
  inventory.yaml
  inventory-audit.yaml
  inventory.approved.yaml
  briefs/
    01-<slug>.yaml
    ...
  toc.yaml
  glossary.yaml
  chapters/
    00-introduction.adoc          (intro chapter — cultural relevance)
    00-introduction.factcheck.yaml
    00-introduction.resolved.adoc
    00-introduction.edited.adoc
    00-introduction.diff.md
    01-<slug>.claims.adoc         (factual skeleton — one claim per paragraph)
    01-<slug>.claims.factcheck.yaml (claims audited)
    01-<slug>.claims.approved.adoc  (after human review)
    01-<slug>.adoc                (Asimov narrative from verified claims)
    01-<slug>.fidelity.yaml       (narrative-vs-claims fidelity review)
    01-<slug>.resolved.adoc       (markers resolved)
    01-<slug>.edited.adoc         (line-edited)
    01-<slug>.diff.md             (line-edit diff for review)
    ...
  comparative.adoc                   (drafted)
  comparative.factcheck.yaml         (audited)
  comparative.resolved.adoc          (markers resolved)
  comparative.edited.adoc            (line-edited)
  comparative.diff.md                (line-edit diff)
  character-appendix.adoc            (character reference)
  character-appendix.factcheck.yaml  (audited)
  book.adoc                          (master)
  bibliography.bib
  validation-report.md
```

## Output format

AsciiDoc, rendered via Asciidoctor (not Pandoc) to PDF and EPUB. Pandoc is still useful for DOCX export if needed.

## What changed from v1

See `CHANGELOG.md`.
