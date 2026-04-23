#!/usr/bin/env bash
# Inner render script. Invoked by render_book.sh; runs inside the
# myth-claude container. Do not call directly from the host.
set -uo pipefail

if [[ $# -lt 2 ]]; then
    echo "internal: missing args" >&2
    exit 2
fi

book_dir=$1
slug=$2
variant="en"
suffix=""
lang="English"

shift 2
while [[ $# -gt 0 ]]; do
    case "$1" in
        --es) variant="es"; suffix=".es"; lang="Spanish" ;;
        *) echo "unknown arg: $1" >&2; exit 2 ;;
    esac
    shift
done

[[ "$book_dir" = /* ]] || book_dir=/workspace/$book_dir

master_file=${slug}${suffix}.adoc
pdf_file=output/${slug}${suffix}.pdf
epub_file=output/${slug}${suffix}.epub
report_file=reports/validation-report${suffix}.md

# Paths for the summary line (kept absolute for clarity when printed).
pdf=$book_dir/$pdf_file
epub=$book_dir/$epub_file
report=$book_dir/$report_file

if [[ ! -f "$book_dir/$master_file" ]]; then
    echo "error: master adoc not found: $book_dir/$master_file" >&2
    exit 1
fi

# asciidoctor-bibtex resolves :bibtex-file: relative to the CWD, not the
# source document's directory — so run asciidoctor from the book dir and
# use relative paths for -o and the source file.
cd "$book_dir"

mkdir -p output reports

ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
pdf_rc=0
epub_rc=0
anti_pattern_hits=0

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

check_anti_pattern() {
    local label=$1 pattern=$2
    local hits
    hits=$(grep -rn --include="*.xhtml" -F -- "$pattern" "$tmp" 2>/dev/null || true)
    if [[ -n "$hits" ]]; then
        echo "### $label"
        echo
        echo '```'
        echo "$hits"
        echo '```'
        echo
        return 1
    fi
    return 0
}

{
    echo "# Validation report — $lang"
    echo
    echo "- book-dir: $book_dir"
    echo "- slug: $slug"
    echo "- variant: $variant"
    echo "- timestamp (UTC): $ts"
    echo
    echo "## asciidoctor-pdf"
    echo
    echo '```'
    asciidoctor-pdf -r asciidoctor-bibtex --verbose --failure-level=WARN \
        -o "$pdf_file" "$master_file" 2>&1
    pdf_rc=$?
    echo '```'
    echo
    echo "pdf exit: $pdf_rc"
    echo
    echo "## asciidoctor-epub3"
    echo
    echo '```'
    asciidoctor-epub3 -r asciidoctor-bibtex --verbose --failure-level=WARN \
        -o "$epub_file" "$master_file" 2>&1
    epub_rc=$?
    echo '```'
    echo
    echo "epub exit: $epub_rc"
    echo
    echo "## Anti-pattern scan (EPUB xhtml)"
    echo
    if [[ $epub_rc -eq 0 && -s "$epub_file" ]] && unzip -q "$epub_file" -d "$tmp" 2>/dev/null; then
        clean=0
        check_anti_pattern "EVIDENCE leftover" "EVIDENCE" || clean=1
        check_anti_pattern "COMPARATIVE-HOOK leftover" "COMPARATIVE-HOOK" || clean=1
        check_anti_pattern "empty-paren '(. [n])' artefact" "(. " || clean=1
        check_anti_pattern "'_(.footnote' artefact" "(.footnote" || clean=1
        if [[ $clean -eq 0 ]]; then
            echo "clean — no anti-patterns in EPUB."
        else
            anti_pattern_hits=1
        fi
    else
        echo "skipped (EPUB not produced or unreadable)"
    fi
} > "$report_file"

echo "--- render summary ($lang) ---"
echo "pdf:    $pdf ($(stat -c%s "$pdf_file" 2>/dev/null || echo '?') bytes, exit $pdf_rc)"
echo "epub:   $epub ($(stat -c%s "$epub_file" 2>/dev/null || echo '?') bytes, exit $epub_rc)"
echo "report: $report"

if [[ $pdf_rc -ne 0 || $epub_rc -ne 0 || $anti_pattern_hits -ne 0 ]]; then
    echo "build failed — see $report" >&2
    exit 1
fi
