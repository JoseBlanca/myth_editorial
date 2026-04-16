# Runbook: How to Execute the Pipeline

Step-by-step operational instructions. For each stage: what to run, which AI to use, what to paste, and where to save the output.

## General workflow

1. Run `python assemble_prompt.py <stage> <book> [input-files...]` to generate the prompt
2. Open a conversation with the appropriate AI
3. Paste the prompt (it's already on your clipboard)
4. For some stages, also paste primary source texts into the conversation
5. Collect the output and save it to the right file in `books/<book>/`
6. Move to the next stage

## Which AI for which stage?

The rule is: **the writer and the checker must be different AIs.** Beyond that, use whatever works best. A reasonable default rotation:

| Role | Suggested AI | Why |
|------|-------------|-----|
| Research (story-inventory) | Gemini Deep Research | Best at searching many sources |
| Interactive (scope-lock, glossary-lock) | Any — your preference | These are conversations with you |
| Writing (intro-chapter, chapter-claims, chapter-draft, comparative, character-appendix) | Claude | Strong at structured writing |
| Checking (inventory-audit, claims-factcheck, prose-factcheck, narrative-fidelity) | GPT | Different model from writer |
| Mechanical (post-human-normalize, marker-resolve, line-edit, format-finalize) | Any | No audit independence needed |

The key constraint: the AI that **produced** content must not be the AI that **checks** it, and the check must be in a **fresh conversation** (no memory of the writing).

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
- **Must be a different AI than story-inventory, fresh conversation**
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
- **Different AI from intro-chapter writer, fresh conversation**
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

- **Different AI, fresh conversation**
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

- **Different AI, fresh conversation**
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
- Then run prose-factcheck on it (different AI), HUMAN REVIEW, post-human-normalize

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
- Then run prose-factcheck (different AI), HUMAN REVIEW, post-human-normalize

---

### 18. format-finalize

**Goal:** Assemble the book and build the bibliography.

```
python assemble_prompt.py format-finalize sumer
```

Paste all final files.

- Any AI
- **Save to:** `books/sumer/book.adoc`, `books/sumer/bibliography.bib`, `books/sumer/validation-report.md`
- Run the asciidoctor commands to produce `book.pdf` and `book.epub`

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
                  → book.adoc + book.pdf/epub     ← format-finalize
```
