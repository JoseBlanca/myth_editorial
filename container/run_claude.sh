#!/usr/bin/env bash
# Launch an interactive Claude Code session inside the container.
#
# Because the container's filesystem view is limited to the mounted project
# directory, --dangerously-skip-permissions is safe here: Claude cannot touch
# your $HOME, /etc, other repos, etc. It still has network access so it can
# reach the Anthropic API.
#
# Pass extra arguments to Claude after `--`, e.g.:
#     ./container/run.sh -- --model claude-opus-4-7
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_common.sh"

ensure_image
ensure_volume

# Pass everything after `--` straight through to claude.
CLAUDE_ARGS=()
if [[ $# -gt 0 && "$1" == "--" ]]; then
    shift
    CLAUDE_ARGS=("$@")
fi

exec podman run \
    "${COMMON_PODMAN_ARGS[@]}" \
    -it \
    --name "${CONTAINER_NAME_PREFIX}-run-$$" \
    "$IMAGE_NAME" \
    claude --dangerously-skip-permissions "${CLAUDE_ARGS[@]}"
