# Runbook: How to Execute the Pipeline

Step-by-step operational instructions. For each stage: what to run, which AI to use, what to paste, and where to save the output.

## Execution environment (preferred: container)

Run the pipeline **inside the myth-claude container** whenever possible. It bundles Claude Code, Python, the full Asciidoctor toolchain (including `asciidoctor-bibtex`), Pandoc, and Git, and only sees this project's directory as `/workspace` — nothing outside. That lets Claude Code run with `--dangerously-skip-permissions` without any risk of touching files elsewhere on the host.

Setup (once):

```bash
./container/build.sh
./container/run_claude.sh     # first run: authenticate via /login
```

Daily use:

| Task | Command |
|------|---------|
| Interactive Claude Code session | `./container/run_claude.sh` |
| One-off command (`python assemble_prompt.py ...`, a render, a grep) | `./container/exec_cmd.sh <cmd> [args...]` |
| Plain shell inside the container | `./container/shell.sh` |
| Render a finished book to PDF + EPUB | `./container/render_book.sh <book-dir> <slug> [--es]` |

Browser-based AI conversations (ChatGPT, Gemini Deep Research, claude.ai) still happen outside the container — they don't touch the filesystem and don't benefit from the isolation. The container only matters for locally-executed tooling: Claude Code sessions and every shell command in this runbook. Full isolation-model details and troubleshooting: [`container/README.md`](container/README.md).

The `python assemble_prompt.py ...` examples below are written in their plain form for readability; prefix them with `./container/exec_cmd.sh` (or run them from inside a `./container/shell.sh` session) when using the container.

## Parallel agents: at most two at a time

Launching sub-agents in parallel is a good way to run research or pipeline stages unattended, especially when they work inside the container. But **do not launch more than two agents at a time.** The Anthropic account's token/rate limit is shared across all concurrent agents: if the limit is hit mid-run, every in-flight agent is killed and any work that was not already written to disk is lost. Running two at a time keeps throughput reasonable while leaving headroom for the agents to actually finish and save their output.

Practical rule: queue remaining agents and start the next pair only after the previous pair has completed (and saved its files). If a batch of agents is mostly short-running research but one is unusually large, run the large one alone.

## General workflow

1. Run `python assemble_prompt.py <stage> <book> [input-files...]` to generate the prompt (via the container — see above)
2. Open a conversation with the appropriate AI
3. Paste the prompt (it's already on your clipboard)
4. For some stages, also paste primary source texts into the conversation
5. Collect the output and save it to the right file in `books/<book>/`
6. Move to the next stage

## Which AI for which stage?

The rule is: **every check runs in a fresh conversation (or fresh autonomous process) with no memory of the writing.** Using a different AI model for the check is preferred — two models make independent mistakes — but the same model in a fresh conversation is acceptable when a second model is not practical to run. The load-bearing constraint is the fresh context, not the model identity. A reasonable default rotation:

| Role | Suggested AI | Why |
|------|-------------|-----|
| Research (story-inventory) | Gemini Deep Research | Best at searching many sources |
| Interactive (scope-lock, glossary-lock) | Any — your preference | These are conversations with you |
| Writing (intro-chapter, chapter-claims, chapter-draft, comparative, character-appendix) | Claude | Strong at structured writing |
| Checking (inventory-audit, claims-factcheck, prose-factcheck, narrative-fidelity) | Ideally a different model from the writer; otherwise the same model in a fresh conversation | Independence preferred; fresh context is the hard requirement |
| Mechanical (post-human-normalize, marker-resolve, line-edit, format-finalize) | Any | No audit independence needed |

The key constraint: the check must be in a **fresh conversation** (no memory of the writing). A different AI model is preferred but not required.

---

## Stage-by-stage instructions

### 1. scope-lock

**Goal:** Define the book's boundaries. Produces `scope.md` and `sources.yaml`.

```
python assemble_prompt.py scope-lock sumer
```

**How to run:**
- Open a conversation with any AI
- Paste the prompt
- The AI will ask you questions about culture, period, excluded neighbors, sources, reconstruction policy
- Answer each question — be specific
- When done, the AI produces two files

**Save output to:**
- `books/sumer/scope.md`
- `books/sumer/sources.yaml`

**Tip for Sumer:** You already have good instincts from the Gemini prompt. Paste the Gemini research output into the conversation too, so the AI can see what stories were found and propose a realistic source whitelist.

---

### 2. story-inventory

**Goal:** List every story the book will cover. Produces `inventory.yaml`.

```
python assemble_prompt.py story-inventory sumer
```

**How to run:**
- Best with Gemini Deep Research or equivalent
- Paste the prompt (which now includes scope.md and sources.yaml)
- The AI researches and produces a structured inventory

**For Sumer:** You already have Gemini's output. You can either:
- (a) Ask an AI to convert the existing Gemini catalog into the `inventory.yaml` format defined in the skill file, or
- (b) Re-run story-inventory with the scope now locked, to get a cleaner result

**Save output to:**
- `books/sumer/inventory.yaml`

---

### 3. inventory-audit

**Goal:** Check the story inventory for errors. Produces `inventory-audit.yaml`.

```
python assemble_prompt.py inventory-audit sumer inventory.yaml
```

**How to run:**
- **Must be a fresh conversation** (ideally a different AI model than story-inventory, but the same model is acceptable if running a different one is impractical)
- Paste the prompt (includes scope.md, sources.yaml, and inventory.yaml)
- The AI checks for wrong-culture material, fake references, missing stories, merged variants
- Wait for the full audit report

**Save output to:**
- `books/sumer/inventory-audit.yaml`

---

### 4. HUMAN REVIEW (inventory)

**What to do:**
- Read the `inventory-audit.yaml` findings
- Focus on HIGH severity findings (~10 minutes)
- Skim MEDIUM, ignore LOW unless you want maximum rigor
- Edit `inventory.yaml` to fix accepted findings
- Save the fixed version as `books/sumer/inventory.approved.yaml`

---

### 5. post-human-normalize (inventory)

**Goal:** Validate that your edits didn't break the inventory structure.

```
python assemble_prompt.py post-human-normalize sumer inventory.approved.yaml
```

**How to run:**
- Any AI, any conversation
- Paste the prompt
- The AI checks YAML structure, required fields, source ID references
- If it finds problems, fix them and re-run

**Save output to:**
- Overwrite `books/sumer/inventory.approved.yaml` with the validated version

---

### 6. chapter-briefs

**Goal:** Create a planning document for each chapter. Produces `briefs/*.yaml` and `toc.yaml`.

```
python assemble_prompt.py chapter-briefs sumer inventory.approved.yaml
```

**How to run:**
- Any AI
- Paste the prompt
- The AI produces one YAML brief per story plus a table of contents

**Save output to:**
- `books/sumer/briefs/01-<slug>.yaml` (one per chapter)
- `books/sumer/toc.yaml`

---

### 7. glossary-lock

**Goal:** Lock English translations for recurring terms. Produces `glossary.yaml`.

```
python assemble_prompt.py glossary-lock sumer briefs/01-*.yaml
```

(Pass all brief files as extra inputs, or paste them manually.)

**How to run:**
- Interactive conversation with any AI
- The AI proposes terms and translation options
- You pick the translation you prefer for each term
- Usually 10-30 terms per book

**Save output to:**
- `books/sumer/glossary.yaml`

---

### 8. intro-chapter

**Goal:** Write the introductory chapter on cultural relevance. Produces `chapters/00-introduction.adoc`.

```
python assemble_prompt.py intro-chapter sumer toc.yaml
```

Also paste the relevant briefs and any primary source texts into the conversation.

**How to run:**
- Writing AI (e.g., Claude)
- Paste the prompt plus briefs and source texts
- The AI writes the introductory chapter

**Save output to:**
- `books/sumer/chapters/00-introduction.adoc`

---

### 9. prose-factcheck (intro)

**Goal:** Check the intro chapter's claims. Produces `chapters/00-introduction.factcheck.yaml`.

```
python assemble_prompt.py prose-factcheck sumer chapters/00-introduction.adoc
```

**How to run:**
- **Fresh conversation** (ideally a different AI model from the intro-chapter writer; the same model is acceptable if a different one is impractical)
- Paste the prompt
- Also paste or provide access to the primary source texts

**Save output to:**
- `books/sumer/chapters/00-introduction.factcheck.yaml`

**Then:** HUMAN REVIEW the findings, fix the intro, run post-human-normalize on it.

---

### 10-13. Per chapter (repeat for each story)

For each chapter (e.g., chapter 01, "Descent of Inanna"):

#### 10a. chapter-claims

```
python assemble_prompt.py chapter-claims sumer briefs/01-descent-of-inanna.yaml
```

- Writing AI (e.g., Claude)
- Also paste the primary source translations into the conversation
- **Save to:** `books/sumer/chapters/01-descent-of-inanna.claims.adoc`

#### 10b. claims-factcheck

```
python assemble_prompt.py claims-factcheck sumer chapters/01-descent-of-inanna.claims.adoc briefs/01-descent-of-inanna.yaml
```

- **Fresh conversation** (ideally a different AI model; the same model is acceptable if impractical)
- Also paste primary source texts
- **Save to:** `books/sumer/chapters/01-descent-of-inanna.claims.factcheck.yaml`

#### 10c. HUMAN REVIEW + post-human-normalize

- Review findings, fix the claims file
- **Save to:** `books/sumer/chapters/01-descent-of-inanna.claims.approved.adoc`
- Run post-human-normalize on it

#### 10d. chapter-draft

```
python assemble_prompt.py chapter-draft sumer chapters/01-descent-of-inanna.claims.approved.adoc briefs/01-descent-of-inanna.yaml
```

- Writing AI (e.g., Claude) — **do NOT paste primary sources** (the claims are the only input)
- **Save to:** `books/sumer/chapters/01-descent-of-inanna.adoc`

#### 10e. narrative-fidelity

```
python assemble_prompt.py narrative-fidelity sumer chapters/01-descent-of-inanna.claims.approved.adoc chapters/01-descent-of-inanna.adoc
```

- **Fresh conversation** (ideally a different AI model; the same model is acceptable if impractical)
- **Save to:** `books/sumer/chapters/01-descent-of-inanna.fidelity.yaml`
- If verdict is REVISE: review findings, fix the narrative, re-run narrative-fidelity
- If PASS: this chapter is done — move to the next one

**Repeat 10a-10e for every story chapter.**

---

### 14. comparative-chapter

**Goal:** Write the cross-cultural comparison chapter. Only after ALL story chapters are done.

```
python assemble_prompt.py comparative-chapter sumer chapters/01-*.adoc
```

Also pass the briefs (for comparative hooks).

- Writing AI
- **Save to:** `books/sumer/comparative.adoc`
- Then run prose-factcheck on it (fresh conversation, ideally a different AI model), HUMAN REVIEW, post-human-normalize

---

### 15. marker-resolve

**Goal:** Convert placeholder markers to final text. Runs on ALL chapters at once.

```
python assemble_prompt.py marker-resolve sumer
```

Paste all chapter files (intro, story chapters, comparative) into the conversation.

- Any AI
- **Save to:** `books/sumer/chapters/NN-<slug>.resolved.adoc` (for each), `books/sumer/comparative.resolved.adoc`

---

### 15b. grammar-check

**Goal:** Fix grammar errors, awkward sentences, and readability issues. Runs after marker-resolve, before line-edit.

```
python assemble_prompt.py grammar-check sumer
```

Paste all `.resolved.adoc` files.

- Any AI
- **Save to:** `books/sumer/chapters/NN-<slug>.grammar-checked.adoc` + `.grammar-diff.md`
- Skim the diffs to approve

---

### 16. line-edit

**Goal:** Final prose polish. Runs on ALL grammar-checked chapters.

```
python assemble_prompt.py line-edit sumer
```

Paste all `.resolved.adoc` files.

- Any AI
- **Save to:** `books/sumer/chapters/NN-<slug>.edited.adoc` + `.diff.md` (for each), `books/sumer/comparative.edited.adoc` + `.diff.md`
- Skim the diffs to approve

---

### 17. character-appendix

**Goal:** Compile the character reference. Only after line-edit is done.

```
python assemble_prompt.py character-appendix sumer
```

Paste all `.edited.adoc` files and briefs.

- Writing AI
- **Save to:** `books/sumer/character-appendix.adoc`
- Then run prose-factcheck (fresh conversation, ideally a different AI model), HUMAN REVIEW, post-human-normalize

---

### 18. format-finalize

**Goal:** Assemble the book, build the bibliography, and render the final PDF + EPUB.

```
python assemble_prompt.py format-finalize sumer
```

Paste all final files.

- Any AI
- The stage first fixes the book slug, either from an explicit `slug:` field in `scope.md` or by deriving it from the book title. For Sumer the slug is `the_myths_of_sumer`.
- **Save to:** `books/sumer/the_myths_of_sumer.adoc` (master) and `books/sumer/bibliography.bib` (both at the book root, so relative `include::`, `:bibtex-file:`, and cover-image paths resolve without `../` rewrites)
- Render via the container helper, from the repo root:

  ```
  ./container/render_book.sh books/sumer the_myths_of_sumer
  ```

  This produces `books/sumer/output/the_myths_of_sumer.pdf`, `books/sumer/output/the_myths_of_sumer.epub`, and `books/sumer/reports/validation-report.md`. The helper runs the asciidoctor commands with `-r asciidoctor-bibtex --verbose --failure-level=WARN`, then scans the rendered EPUB for anti-patterns (EVIDENCE/COMPARATIVE-HOOK leftovers, `(. ` empty-paren artefacts, `_(.footnote` artefacts) and exits non-zero on any WARN/ERROR or hit.

---

### 19. translate-spanish

**Goal:** Produce a parallel Spanish edition. Only after `format-finalize` — the English book must be finished.

```
python assemble_prompt.py translate-spanish sumer
```

Paste `glossary.yaml`, all `chapters/NN-*.edited.adoc`, `chapters/00-introduction.edited.adoc`, `comparative.edited.adoc`, `character-appendix.adoc`, `the_myths_of_sumer.adoc`, and `bibliography.bib` into the conversation.

**How to run:**
- Any strong writing AI with Spanish competence
- Pass 0 is **interactive**: the AI proposes `glossary.es.yaml`; you confirm each term (Sumerian deity names stay, Sumerian place names usually Akkadianized — Nippur, Uruk, Eridu — technical terms like *me* and *edubba* stay italicized)
- Passes 1–3 (draft → reflect → revise) run per chapter
- Pass 4 assembles `the_myths_of_sumer.es.adoc` at the book root
- Pass 5 renders via the same container helper with `--es`:

  ```
  ./container/render_book.sh books/sumer the_myths_of_sumer --es
  ```

**Save output to:**
- `books/sumer/glossary.es.yaml`
- `books/sumer/chapters/NN-<chapter-slug>.es.adoc` + `.es-diff.md` (one per chapter, plus intro)
- `books/sumer/comparative.es.adoc` + `.es-diff.md`
- `books/sumer/character-appendix.es.adoc` + `.es-diff.md`
- `books/sumer/the_myths_of_sumer.es.adoc` (master, at book root)
- `books/sumer/bibliography.es.bib` (only if translator-note footnotes introduced new citations)
- `books/sumer/output/the_myths_of_sumer.es.pdf`
- `books/sumer/output/the_myths_of_sumer.es.epub`
- `books/sumer/reports/validation-report.es.md`

**Skim the `.es-diff.md` files** to approve translation decisions in bulk. The diffs flag glossary terms on first mention, ambiguous passages, and translator-note footnotes.

---

## Verifying stage completion

Every skill instructs the agent to write a completion record as its very last action:

```
books/<book>/completions/<NN>-<stage-name>.done.yaml
```

After any batch run, check for truncated stages:

```bash
# List completed stages
ls books/sumer/completions/

# Find stages that ran but didn't complete (no .done.yaml)
# Compare against the stages you expected to run
```

A missing `.done.yaml` means the agent was interrupted (rate limit, timeout, context overflow). A file with `status: "partial"` means the agent knew it couldn't finish and reported what's missing. Re-run only the incomplete stages.

---

## Quick reference: file flow

```
scope.md + sources.yaml                          ← scope-lock
  → inventory.yaml                               ← story-inventory
    → inventory-audit.yaml                        ← inventory-audit
      → inventory.approved.yaml                   ← YOU + normalize
        → briefs/*.yaml + toc.yaml                ← chapter-briefs
          → glossary.yaml                         ← glossary-lock
            → chapters/00-introduction.adoc       ← intro-chapter
              → (factchecked, reviewed, normalized)
            → chapters/NN-*.claims.adoc           ← chapter-claims
              → claims.factcheck.yaml             ← claims-factcheck
                → claims.approved.adoc            ← YOU + normalize
                  → chapters/NN-*.adoc            ← chapter-draft
                    → fidelity.yaml               ← narrative-fidelity
            → comparative.adoc                    ← comparative-chapter
              → (factchecked, reviewed, normalized)
          → *.resolved.adoc                       ← marker-resolve
            → *.edited.adoc                       ← line-edit
              → character-appendix.adoc           ← character-appendix
                → (factchecked, reviewed, normalized)
                  → <slug>.adoc + output/<slug>.pdf/epub     ← format-finalize
                    → glossary.es.yaml                        ← translate-spanish (Pass 0)
                      → *.es.adoc (per chapter)               ← translate-spanish (Pass 1-3)
                        → <slug>.es.adoc + output/<slug>.es.pdf/epub  ← translate-spanish (Pass 4-5)
```
