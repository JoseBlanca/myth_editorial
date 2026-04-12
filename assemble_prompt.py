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
    Writes the assembled prompt to books/<book>/prompts/<stage>.prompt.md
    If xclip/xsel/wl-copy is available, also copies to clipboard.

The assembled prompt contains:
    1. The governing files (scope.md, sources.yaml, glossary.yaml) if they exist
    2. The skill instructions
    3. Any extra input files passed as arguments
"""

import sys
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


PIPELINE_DIR = Path(__file__).resolve().parent
SKILLS_DIR = PIPELINE_DIR / "skills"
BOOKS_DIR = PIPELINE_DIR / "books"

GOVERNING_FILES = ["scope.md", "sources.yaml", "glossary.yaml"]


def find_skill_file(stage: str) -> Path | None:
    """Find a skill file matching the stage name, ignoring the NN- prefix."""
    for path in sorted(SKILLS_DIR.glob("*.md")):
        # e.g. "01-scope-lock.md" -> "scope-lock"
        name = path.stem.split("-", 1)[1] if "-" in path.stem else path.stem
        if name == stage:
            return path
    return None


def list_stages() -> list[str]:
    stages = []
    for path in sorted(SKILLS_DIR.glob("*.md")):
        name = path.stem.split("-", 1)[1] if "-" in path.stem else path.stem
        stages.append(name)
    return stages


def list_books() -> list[str]:
    return [d.name for d in sorted(BOOKS_DIR.iterdir()) if d.is_dir()]


def copy_to_clipboard(text: str) -> str | None:
    """Try to copy text to clipboard. Returns the tool name used, or None."""
    for tool, args in [
        ("xclip", ["xclip", "-selection", "clipboard"]),
        ("xsel", ["xsel", "--clipboard"]),
        ("wl-copy", ["wl-copy"]),
    ]:
        if shutil.which(tool):
            try:
                subprocess.run(args, input=text.encode(), check=True)
                return tool
            except subprocess.CalledProcessError:
                continue
    return None


def assemble(stage: str, book: str, extra_files: list[str]) -> None:
    skill_file = find_skill_file(stage)
    if skill_file is None:
        print(f"Error: no skill file found for stage '{stage}'")
        print(f"Available stages: {', '.join(list_stages())}")
        sys.exit(1)

    book_dir = BOOKS_DIR / book
    if not book_dir.is_dir():
        print(f"Error: book directory '{book_dir}' not found")
        print(f"Available books: {', '.join(list_books())}")
        sys.exit(1)

    parts: list[str] = []

    # Header
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    parts.append(f"# Prompt for: {stage}")
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
    output_path = prompts_dir / f"{stage}.prompt.md"
    output_path.write_text(prompt_text)

    line_count = prompt_text.count("\n")
    print(f"Assembled: {output_path} ({line_count} lines)")

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
        print(f"Available stages: {', '.join(list_stages())}")
        print(f"Available books: {', '.join(list_books())}")
        sys.exit(1)

    stage = sys.argv[1]
    book = sys.argv[2]
    extra_files = sys.argv[3:]

    assemble(stage, book, extra_files)


if __name__ == "__main__":
    main()
