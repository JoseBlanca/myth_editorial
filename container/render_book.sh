#!/usr/bin/env bash
# Render a book to PDF and EPUB via the myth-claude container.
# Writes deliverables to <book-dir>/output/ and a build log to
# <book-dir>/reports/.
#
# Usage:
#   ./container/render_book.sh <book-dir> <slug> [--es]
#
# <book-dir>  Path to the book directory, relative to the repo root
#             (e.g. books/sumer) or absolute inside /workspace.
# <slug>      Book slug. Master adoc is <book-dir>/<slug>.adoc (English)
#             or <book-dir>/<slug>.es.adoc (Spanish, with --es).
# --es        Render the Spanish variant.
#
# Exits non-zero on any asciidoctor WARN/ERROR or anti-pattern hit in
# the rendered EPUB.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ $# -lt 2 ]]; then
    echo "usage: $0 <book-dir> <slug> [--es]" >&2
    exit 2
fi

exec "$SCRIPT_DIR/exec_cmd.sh" bash /workspace/container/_render_book_inner.sh "$@"
