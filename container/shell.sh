#!/usr/bin/env bash
# Drop into a bash shell inside the container — useful for debugging the
# toolchain (asciidoctor, pandoc, gem paths) without invoking Claude.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_common.sh"

ensure_image
ensure_volume

exec podman run \
    "${COMMON_PODMAN_ARGS[@]}" \
    -it \
    --name "${CONTAINER_NAME_PREFIX}-shell-$$" \
    "$IMAGE_NAME" \
    /bin/bash
