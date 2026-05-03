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

# --- Clipboard forwarding ----------------------------------------------------
# Forward the host's display socket so xclip / wl-copy inside the container
# reach the host clipboard. Conditional: skipped on headless hosts so the
# script still works there.
CLIPBOARD_ARGS=()
if [[ -n "${WAYLAND_DISPLAY:-}" && -n "${XDG_RUNTIME_DIR:-}" \
      && -S "$XDG_RUNTIME_DIR/$WAYLAND_DISPLAY" ]]; then
    CLIPBOARD_ARGS+=(
        -v "$XDG_RUNTIME_DIR/$WAYLAND_DISPLAY:/tmp/wayland-0"
        -e "WAYLAND_DISPLAY=wayland-0"
        -e "XDG_RUNTIME_DIR=/tmp"
    )
fi
if [[ -n "${DISPLAY:-}" && -d /tmp/.X11-unix ]]; then
    CLIPBOARD_ARGS+=(
        -v "/tmp/.X11-unix:/tmp/.X11-unix"
        -e "DISPLAY=$DISPLAY"
    )
fi

exec podman run \
    "${COMMON_PODMAN_ARGS[@]}" \
    "${CLIPBOARD_ARGS[@]}" \
    -it \
    --name "${CONTAINER_NAME_PREFIX}-run-$$" \
    "$IMAGE_NAME" \
    claude --dangerously-skip-permissions "${CLAUDE_ARGS[@]}"
