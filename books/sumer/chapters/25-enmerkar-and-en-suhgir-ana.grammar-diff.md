# Grammar-check diff — Chapter 25: Enmerkar and En-suhgir-ana

Source: `25-enmerkar-and-en-suhgir-ana.resolved.adoc`
Output: `25-enmerkar-and-en-suhgir-ana.grammar-checked.adoc`

## Changes

### 1. Split 56-word sentence (line 58, commentary paragraph following the five-rounds passage)

**Original:**
> The sorcerer from Hamazu, the rootless professional with his formidable reputation, discovers that he has been outmatched not by a more powerful version of his own methods but by a different kind of power entirely -- one that draws on local knowledge, divine backing, and the capacity to subvert the very categories on which his sorcery depends.

**Corrected:**
> The sorcerer from Hamazu, the rootless professional with his formidable reputation, discovers that he has been outmatched. He has been defeated not by a more powerful version of his own methods but by a different kind of power entirely -- one that draws on local knowledge, divine backing, and the capacity to subvert the very categories on which his sorcery depends.

**Rationale:** Original ran 56 words and stacked three subordinate clauses after the main verb "discovers." Split at the natural pivot between the bare finding ("he has been outmatched") and the contrastive elaboration ("not by... but by..."). Meaning preserved; "discovers" retained. No factual content affected.

---

### 2. Split 56-word sentence with nested parenthetical (line 76, cycle-summary paragraph)

**Original:**
> The cycle has traced a complete arc: from Enmerkar's initial prayer to Inanna demanding Aratta's submission, through the messenger exchanges and riddle contests, through the invention of writing, and now to this final proof -- conducted not through words but through conjured animals on a riverbank in Eresh -- that Uruk's supremacy is divinely ordained and practically unassailable.

**Corrected:**
> The cycle has traced a complete arc: from Enmerkar's initial prayer to Inanna demanding Aratta's submission, through the messenger exchanges and riddle contests, through the invention of writing, and now to this final proof that Uruk's supremacy is divinely ordained and practically unassailable. That proof is conducted not through words but through conjured animals on a riverbank in Eresh.

**Rationale:** Original ran 56 words and embedded an em-dash aside ("conducted not through words but through conjured animals on a riverbank in Eresh") between "proof" and its "that"-clause, forcing the reader to hold the main clause open across a digression. Moved the aside to a follow-up sentence so the main proof-clause completes cleanly. No factual content affected.

---

### 3. Split 59-word sentence with embedded list and nested em-dash aside (line 88, closing paragraph)

**Original:**
> Between thirty-two and thirty-seven manuscript witnesses preserve the composition in the scribal curriculum, copied by students who understood that the story was an argument about the nature of legitimate power -- an argument that Uruk won on every available field of competition, from rhetoric to riddles to writing to sorcery, and that it won for the same reason every time.

**Corrected:**
> Between thirty-two and thirty-seven manuscript witnesses preserve the composition in the scribal curriculum, copied by students who understood that the story was an argument about the nature of legitimate power. Uruk won that argument on every available field of competition -- from rhetoric to riddles to writing to sorcery -- and it won for the same reason every time.

**Rationale:** Original ran 59 words with four clauses and an inner list. Split at the em-dash into two sentences; promoted the inner list to a genuine em-dash parenthetical around the cleaner predicate. "Thirty-two and thirty-seven" figure retained verbatim; factual claims unchanged.

---

## Self-check

1. Factual content unchanged — names, numbers (thirty-two to thirty-seven witnesses, five rounds, five animal pairs), ETCSL IDs, page references, Sumerian terms, and every quoted passage are identical to the source.
2. Footnote count and content unchanged — all 16 footnotes present and unmodified.
3. AsciiDoc structure intact — heading, section separators (`'''`), `// EVIDENCE:` and `// COMPARATIVE-HOOK:` comment lines, `_edubba_` italics, em-dash and en-dash conventions all preserved.
4. Every change is logged above; no silent edits.
5. No changes were made to the source-overview paragraphs (lines 3--13), to any sentence carrying a footnote/EVIDENCE marker (resolved passages), or to the En-suhgir-ana direct quotation.
