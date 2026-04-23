#!/usr/bin/env bash
# Build the myth-claude image.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMAGE_NAME="${MYTH_CLAUDE_IMAGE:-myth-claude:latest}"

cd "$SCRIPT_DIR"

echo "Building $IMAGE_NAME from $(pwd)/Containerfile ..."
podman build \
    --tag "$IMAGE_NAME" \
    --build-arg USER_UID="$(id -u)" \
    --build-arg USER_GID="$(id -g)" \
    --file Containerfile \
    .

echo
echo "Built $IMAGE_NAME"
echo "Next steps:"
echo "  ./container/run_claude.sh          # interactive Claude session"
echo "  ./container/shell.sh        # plain bash inside the container"
echo "  ./container/exec_cmd.sh <cmd>   # run a one-off command"
