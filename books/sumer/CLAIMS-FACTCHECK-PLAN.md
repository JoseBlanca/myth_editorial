# Claims Factcheck Execution Plan

Run claims-factcheck on all 36 story chapters in 6 batches of 6 chapters each.
Each batch is independent — if a conversation runs out of tokens, only that batch needs re-running.

## Important constraints

- **Different AI from the claims writer.** The claims were written by Claude Opus. Ideally, factcheck with GPT or Gemini. If using Claude, it must be a **fresh conversation** with no memory of the writing.
- **Completion protocol.** Each factcheck agent must write a `.done.yaml` file per the skill instructions. Check `books/sumer/completions/` after each batch.

## Batches

### Batch 1: Enki Cycle (chapters 01-06)

Chapters: `01-enki-and-ninhursaja`, `02-enki-and-ninmah`, `03-enki-and-the-world-order`, `04-enkis-journey-to-nibru`, `05-enlil-and-ninlil`, `06-enlil-and-sud`

Prompt files (in `prompts/claims-factcheck/`):
- `01-enki-and-ninhursaja.prompt.md`
- `02-enki-and-ninmah.prompt.md`
- `03-enki-and-the-world-order.prompt.md`
- `04-enkis-journey-to-nibru.prompt.md`
- `05-enlil-and-ninlil.prompt.md`
- `06-enlil-and-sud.prompt.md`

Output files to save:
- `chapters/01-enki-and-ninhursaja.claims.factcheck.yaml`
- `chapters/02-enki-and-ninmah.claims.factcheck.yaml`
- `chapters/03-enki-and-the-world-order.claims.factcheck.yaml`
- `chapters/04-enkis-journey-to-nibru.claims.factcheck.yaml`
- `chapters/05-enlil-and-ninlil.claims.factcheck.yaml`
- `chapters/06-enlil-and-sud.claims.factcheck.yaml`

Claims in batch: 29 + 20 + 29 + 15 + 23 + 18 = **134 claims**

---

### Batch 2: Ninurta + Inanna Cycle (chapters 07-13)

Chapters: `07-lugal-e`, `08-angim`, `09-ninurta-and-the-turtle`, `10-inanna-and-enki`, `11-inanna-and-ebih`, `12-inanna-and-shu-kale-tuda`, `13-inanna-and-gudam`

Prompt files: `07-lugal-e.prompt.md` through `13-inanna-and-gudam.prompt.md`

Claims in batch: 34 + 22 + 14 + 28 + 23 + 21 + 8 = **150 claims**

---

### Batch 3: Inanna-Dumuzid + Nanna + Other (chapters 14-18)

Chapters: `14-inannas-descent`, `15-dumuzids-dream`, `16-inanna-and-bilulu`, `17-nannas-journey-to-nibru`, `18-marriage-of-martu`

Prompt files: `14-inannas-descent.prompt.md` through `18-marriage-of-martu.prompt.md`

Claims in batch: 58 + 26 + 17 + 18 + 12 = **131 claims**

Note: Inanna's Descent alone has 58 claims — the largest single chapter.

---

### Batch 4: Gilgamesh Poems (chapters 19-23)

Chapters: `19-gilgamesh-and-aga`, `20-gilgamesh-and-the-bull-of-heaven`, `21-gilgamesh-and-huwawa`, `22-gilgamesh-enkidu-and-the-nether-world`, `23-death-of-gilgamesh`

Prompt files: `19-gilgamesh-and-aga.prompt.md` through `23-death-of-gilgamesh.prompt.md`

Claims in batch: 21 + 8 + 28 + 34 + 12 = **103 claims**

---

### Batch 5: Enmerkar-Lugalbanda + Underworld (chapters 24-30)

Chapters: `24-enmerkar-and-the-lord-of-aratta`, `25-enmerkar-and-en-suhgir-ana`, `26-lugalbanda-in-the-mountain-cave`, `27-lugalbanda-and-the-anzud-bird`, `28-eridu-flood-story`, `29-ningishzidas-journey`, `30-death-of-ur-namma`

Prompt files: `24-enmerkar-and-the-lord-of-aratta.prompt.md` through `30-death-of-ur-namma.prompt.md`

Claims in batch: 50 + 22 + 19 + 25 + 16 + 10 + 22 = **164 claims**

Note: Enmerkar and the Lord of Aratta has 50 claims — second largest.

---

### Batch 6: Debate Poems (chapters 31-36)

Chapters: `31-debate-hoe-and-plough`, `32-debate-ewe-and-grain`, `33-debate-winter-and-summer`, `34-debate-bird-and-fish`, `35-debate-copper-and-silver`, `36-debate-date-palm-and-tamarisk`

Prompt files: `31-debate-hoe-and-plough.prompt.md` through `36-debate-date-palm-and-tamarisk.prompt.md`

Claims in batch: 21 + 18 + 19 + 19 + 11 + 11 = **99 claims** (lightest batch)

---

## How to run each batch

In a new Claude Code conversation (or other AI), say:

```
Run claims-factcheck on chapters NN through MM for the sumer book.

The individual prompt files are in books/sumer/prompts/claims-factcheck/.
Read each prompt file and produce the corresponding .claims.factcheck.yaml
output in books/sumer/chapters/.

Process them one at a time. For each chapter:
1. Read the prompt from prompts/claims-factcheck/<slug>.prompt.md
2. Run the factcheck per the skill instructions in the prompt
3. Write the output to chapters/<slug>.claims.factcheck.yaml
4. Write completion record to completions/09-claims-factcheck-<slug>.done.yaml

After all chapters in this batch are done, report a summary.
```

## Verification after all batches

```bash
# Check all 36 factcheck files exist
ls books/sumer/chapters/*.claims.factcheck.yaml | wc -l
# Should be 36

# Check all completion records
ls books/sumer/completions/09-claims-factcheck-*.done.yaml | wc -l
# Should be 36

# Quick summary of findings
grep -h "high:" books/sumer/chapters/*.claims.factcheck.yaml
```

## Total claims: 752 across 36 chapters
