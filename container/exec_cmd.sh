#!/usr/bin/env bash
# Run a one-off command inside the container. Handy for scripted automation
# (e.g. rebuilding PDFs from a Makefile or a cron job):
#
#     ./container/exec.sh asciidoctor-pdf -o book.pdf books/sumer/book.adoc
#     ./container/exec.sh claude -p "run stage post-human-normalize on X"
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_common.sh"

if [[ $# -eq 0 ]]; then
    echo "usage: $0 <command> [args...]" >&2
    exit 2
fi

ensure_image
ensure_volume

# Only allocate a TTY if stdin/stdout are terminals — keeps this usable from
# pipelines and cron without breaking interactive use.
TTY_ARGS=()
if [[ -t 0 && -t 1 ]]; then
    TTY_ARGS=(-it)
fi

exec podman run \
    "${COMMON_PODMAN_ARGS[@]}" \
    "${TTY_ARGS[@]}" \
    --name "${CONTAINER_NAME_PREFIX}-exec-$$" \
    "$IMAGE_NAME" \
    "$@"
