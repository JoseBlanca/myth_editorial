# Grammar-check diff: comparative chapter

Source: `books/sumer/comparative.resolved.adoc`
Output: `books/sumer/comparative.grammar-checked.adoc`

## Summary

Four mechanical punctuation fixes. All are duplicated sentence-terminal periods
at the junction between body text and a trailing `footnote:[...]` macro — a
typographic artefact of marker-resolution where a period already closing the
sentence was followed by a second period (or by a stray period with an
intervening space) before the footnote. These produced visual ". ." or ".."
sequences in the rendered text.

No grammar, syntax, clause-structure, or readability changes were made. The
chapter's sentences run long in places but their structure is either parallel
or semicolon-segmented and parses cleanly; none met the criteria for a forced
split (over 50 words *and* hard to parse *and* not already flattened by
parallelism or a semicolon). No nested parentheticals were found. No
ambiguous pronouns, subject-verb disagreement, dangling modifiers, or
tense-shift issues were detected. Em-dash, serial-comma, and non-English-term
formatting are consistent throughout.

Footnote content (including the stylistically chosen "..]" closers on the four
speculative-parallel footnotes) is unchanged per the skill's hard rule against
footnote modification. AsciiDoc structure is unchanged; file length is 211
lines before and after.

## Changes

### Change 1 — line 29 (Cosmogonic Parallels, clay-creation paragraph)

- Original: `... each child on his wheel)..footnote:[This parallel is speculative. ...`
- Corrected: `... each child on his wheel).footnote:[This parallel is speculative. ...`
- Rationale: Duplicated sentence-ending period. The closing parenthesis was
  already followed by the terminal period of the sentence; a second period
  preceded the `footnote:` macro. Punctuation fix only; no change to meaning
  or to the footnote content.

### Change 2 — line 36 (Cosmogonic Parallels, heaven-earth separation paragraph)

- Original: `... the zenith is where they are furthest apart. .footnote:[This parallel is speculative. ...`
- Corrected: `... the zenith is where they are furthest apart.footnote:[This parallel is speculative. ...`
- Rationale: Stray period preceded by a space after the sentence-terminal
  period, producing a ". ." sequence before the footnote. Punctuation fix only;
  no change to meaning or to the footnote content.

### Change 3 — line 65 (Chaoskampf, Dumézilian tripartite paragraph)

- Original: `... its appearance in Sumer is independent and typological rather than genealogical..footnote:[This parallel is speculative. ...`
- Corrected: `... its appearance in Sumer is independent and typological rather than genealogical.footnote:[This parallel is speculative. ...`
- Rationale: Duplicated sentence-ending period before the `footnote:` macro.
  Punctuation fix only; no change to meaning or to the footnote content.

### Change 4 — line 129 (Divine Kingship, city-patronage paragraph)

- Original: `... but the causal direction (did theology shape politics or did politics shape theology?) is hard to determine..footnote:[This parallel is speculative. ...`
- Corrected: `... but the causal direction (did theology shape politics or did politics shape theology?) is hard to determine.footnote:[This parallel is speculative. ...`
- Rationale: Duplicated sentence-ending period before the `footnote:` macro.
  The embedded question mark inside the parenthetical is correct and left
  untouched; only the trailing ".." was collapsed to ".". Punctuation fix
  only; no change to meaning or to the footnote content.

## Self-check

1. No factual content changed. The four edits affect punctuation only; every
   proper noun, date, citation, claim, and hedge is identical between the
   resolved and grammar-checked files.
2. Footnote count unchanged: 83 `footnote:` macros in both files. Footnote
   content unchanged (including the four speculative-parallel footnotes whose
   internal "..]" closers were not touched).
3. AsciiDoc structure intact: all five `===` section headings preserved in
   their original positions; the top-level `==` heading preserved; paragraph
   breaks unchanged; no include directives affected.
4. Every change is logged above. No silent changes were made.
