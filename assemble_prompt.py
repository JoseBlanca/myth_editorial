#!/usr/bin/env python3
"""
Assembles a ready-to-paste prompt for a pipeline stage.

Usage:
    python assemble_prompt.py <stage> <book> [extra-input-files...]

Examples:
    python assemble_prompt.py scope-lock sumer
    python assemble_prompt.py inventory-audit sumer
    python assemble_prompt.py chapter-claims sumer briefs/01-descent-of-inanna.yaml
    python assemble_prompt.py claims-factcheck sumer chapters/01-descent-of-inanna.claims.adoc

Output:
    Writes the assembled prompt to books/<book>/prompts/<NN>-<stage>[<modifier>][<chapter>].prompt.md
    If xclip/xsel/wl-copy is available, also copies to clipboard.

    The output filename is derived from the inputs:
      - Chapter suffix: input filenames matching `^NN-` (e.g. `briefs/21-gonggong.yaml`)
        contribute `-chNN`. Up to 2 unique chapter numbers are kept, sorted, e.g.
        `04-post-human-normalize-claims-ch21-ch22.prompt.md`. More than 2 (e.g.
        comparative-chapter taking every story chapter as input) → no suffix.
      - Modifier suffix: post-human-normalize is reused for four artifacts
        (inventory / intro / claims / fidelity) — the modifier is inferred from
        the input filenames so parallel cycles don't collide.

    Without these, parallel runs of the same stage on different chapters
    overwrite each other's prompt files mid-pipeline.

The assembled prompt contains:
    1. The governing files (scope.md, sources.yaml, glossary.yaml) if they exist
    2. The skill instructions
    3. Any extra input files passed as arguments
"""

import os
import re
import sys
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


PIPELINE_DIR = Path(__file__).resolve().parent
SKILLS_DIR = PIPELINE_DIR / "skills"
BOOKS_DIR = PIPELINE_DIR / "books"

GOVERNING_FILES = ["scope.md", "sources.yaml", "glossary.yaml", "toc.yaml"]


def find_skill_file(stage: str) -> tuple[Path, int] | tuple[None, None]:
    """Find a skill file matching the stage name, ignoring the NN- prefix.
    Returns (path, stage_number) or (None, None)."""
    for path in sorted(SKILLS_DIR.glob("*.md")):
        parts = path.stem.split("-", 1)
        number = int(parts[0]) if parts[0].isdigit() else 0
        name = parts[1] if len(parts) > 1 else path.stem
        if name == stage:
            return path, number
    return None, None


def total_stages() -> int:
    return len(list(SKILLS_DIR.glob("*.md")))


def list_stages() -> list[str]:
    stages = []
    for path in sorted(SKILLS_DIR.glob("*.md")):
        parts = path.stem.split("-", 1)
        number = parts[0] if parts[0].isdigit() else "?"
        name = parts[1] if len(parts) > 1 else path.stem
        stages.append(f"{number}. {name}")
    return stages


def list_books() -> list[str]:
    return [d.name for d in sorted(BOOKS_DIR.iterdir()) if d.is_dir()]


CHAPTER_NUM_RE = re.compile(r"(?:^|/)(\d+)-")


def detect_chapter_suffix(extra_files: list[str]) -> str:
    """Build a ``-chNN[-chNN]`` suffix from chapter numbers found in input
    filenames matching ``NN-...``. Returns ``""`` if no chapters are found
    or if more than two unique chapter numbers are present (avoids
    multi-chapter stages like comparative-chapter producing absurdly long
    filenames)."""
    nums: list[int] = []
    for f in extra_files:
        m = CHAPTER_NUM_RE.search(f)
        if m:
            n = int(m.group(1))
            if n not in nums:
                nums.append(n)
    if not nums or len(nums) > 2:
        return ""
    nums.sort()
    return "".join(f"-ch{n:02d}" for n in nums)


def detect_normalize_modifier(stage: str, extra_files: list[str]) -> str:
    """For ``post-human-normalize``, infer which artifact is being normalized
    from the input filenames and return ``-claims`` / ``-fidelity`` /
    ``-intro`` / ``-inventory`` (or ``""`` if unrecognized). The same skill
    is reused for four distinct artifacts; without a modifier their prompt
    files collide. ``intro`` and ``inventory`` are checked before the
    chapter-based modifiers because they live at fixed paths that the
    chapter-suffix logic would otherwise also match."""
    if stage != "post-human-normalize":
        return ""
    files_str = " ".join(extra_files)
    if "00-introduction" in files_str:
        return "-intro"
    if "inventory" in files_str:
        return "-inventory"
    if ".fidelity.yaml" in files_str:
        return "-fidelity"
    if ".claims.factcheck.yaml" in files_str or ".claims.adoc" in files_str:
        return "-claims"
    return ""


def copy_to_clipboard(text: str) -> str | None:
    """Try to copy text to clipboard. Returns the tool name used, or None.

    Skipped entirely when no display server is detected. Without an X11
    DISPLAY or Wayland session, xsel falls back to dumping its stdin to
    stdout while still exiting 0 — that pollutes the script's stdout
    (with up to several hundred KB of prompt text) and produces a
    misleading "Copied to clipboard" message. Stdout/stderr from the
    clipboard tool are also redirected to DEVNULL as belt-and-suspenders."""
    if not (os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY")):
        return None
    for tool, args in [
        ("xclip", ["xclip", "-selection", "clipboard"]),
        ("xsel", ["xsel", "--clipboard"]),
        ("wl-copy", ["wl-copy"]),
    ]:
        if shutil.which(tool):
            try:
                subprocess.run(
                    args,
                    input=text.encode(),
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                return tool
            except subprocess.CalledProcessError:
                continue
    return None


def assemble(stage: str, book: str, extra_files: list[str]) -> None:
    skill_file, stage_number = find_skill_file(stage)
    if skill_file is None:
        print(f"Error: no skill file found for stage '{stage}'")
        print(f"Available stages:\n  " + "\n  ".join(list_stages()))
        sys.exit(1)

    total = total_stages()

    book_dir = BOOKS_DIR / book
    if not book_dir.is_dir():
        print(f"Error: book directory '{book_dir}' not found")
        print(f"Available books: {', '.join(list_books())}")
        sys.exit(1)

    parts: list[str] = []

    # Header
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    parts.append(f"# Stage {stage_number} of {total}: {stage}")
    parts.append(f"# Book: {book}")
    parts.append(f"# Generated: {now}")
    parts.append("")

    # Governing files (if they exist — they won't for scope-lock, which creates them)
    for gov_file in GOVERNING_FILES:
        gov_path = book_dir / gov_file
        if gov_path.exists():
            content = gov_path.read_text()
            parts.append("---")
            parts.append("")
            parts.append(f"# Governing file: {gov_file}")
            parts.append("")
            parts.append("```")
            parts.append(content.rstrip())
            parts.append("```")
            parts.append("")

    # Skill instructions
    skill_content = skill_file.read_text()
    parts.append("---")
    parts.append("")
    parts.append(f"# Skill instructions: {stage}")
    parts.append("")
    parts.append(skill_content.rstrip())
    parts.append("")

    # Extra input files
    for extra in extra_files:
        filepath = book_dir / extra
        if filepath.exists():
            content = filepath.read_text()
            parts.append("---")
            parts.append("")
            parts.append(f"# Input file: {extra}")
            parts.append("")
            parts.append("```")
            parts.append(content.rstrip())
            parts.append("```")
            parts.append("")
        else:
            parts.append(f"# WARNING: input file not found: {extra}")
            parts.append("")

    prompt_text = "\n".join(parts)

    # Write to file
    prompts_dir = book_dir / "prompts"
    prompts_dir.mkdir(exist_ok=True)
    padded = f"{stage_number:02d}"
    modifier = detect_normalize_modifier(stage, extra_files)
    chapter_suffix = "" if modifier in ("-intro", "-inventory") else detect_chapter_suffix(extra_files)
    output_path = prompts_dir / f"{padded}-{stage}{modifier}{chapter_suffix}.prompt.md"
    output_path.write_text(prompt_text)

    line_count = prompt_text.count("\n")
    print(f"Assembled: {output_path} ({line_count} lines)")
    print(f"  Stage {stage_number} of {total}: {stage}")

    # Try clipboard
    tool = copy_to_clipboard(prompt_text)
    if tool:
        print(f"Copied to clipboard ({tool})")
    else:
        print(f"No clipboard tool found — paste from {output_path} manually")


def main():
    if len(sys.argv) < 3:
        print("Usage: python assemble_prompt.py <stage> <book> [extra-input-files...]")
        print()
        print("Available stages:")
        for s in list_stages():
            print(f"  {s}")
        print()
        print(f"Available books: {', '.join(list_books())}")
        sys.exit(1)

    stage = sys.argv[1]
    book = sys.argv[2]
    extra_files = sys.argv[3:]

    assemble(stage, book, extra_files)


if __name__ == "__main__":
    main()
