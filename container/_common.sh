# Shared podman-run arguments for every entrypoint script.
# Sourced by run.sh, shell.sh, and exec.sh. Not meant to be executed directly.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

IMAGE_NAME="${MYTH_CLAUDE_IMAGE:-myth-claude:latest}"
CLAUDE_VOLUME="${MYTH_CLAUDE_VOLUME:-myth-claude-home}"
CONTAINER_NAME_PREFIX="${MYTH_CLAUDE_NAME_PREFIX:-myth-claude}"

# --- Why each flag matters ---------------------------------------------------
# --rm
#     Tear the container down on exit — we don't keep per-run state here
#     (persistent state lives in the named volume below).
# --userns=keep-id
#     Rootless podman remaps UIDs into a subuid range by default, so files
#     written from inside the container would show up as unknown UIDs on the
#     host. keep-id maps container UID N back to host UID N, so the project
#     directory ends up owned by you.
# -v $PROJECT_DIR:/workspace:Z
#     Bind-mount the project read-write. The :Z relabels for SELinux if it's
#     active; harmless otherwise.
# -v $CLAUDE_VOLUME:/home/myth/.claude
#     Named volume for Claude Code auth + settings. Survives container
#     removal, so you only `claude login` once.
# --security-opt label=disable
#     Required with keep-id + named volumes on SELinux systems to avoid
#     relabel conflicts. No-op where SELinux isn't enforcing.
# -e HOME / -w /workspace
#     Make the shell inside the container land in the mounted project.
COMMON_PODMAN_ARGS=(
    --rm
    --userns=keep-id
    --security-opt label=disable
    -v "$PROJECT_DIR:/workspace:Z"
    -v "$CLAUDE_VOLUME:/home/myth/.claude"
    -w /workspace
    -e HOME=/home/myth
    -e TERM="${TERM:-xterm-256color}"
)

# Ensure the named volume exists before we try to mount it.
ensure_volume() {
    if ! podman volume inspect "$CLAUDE_VOLUME" >/dev/null 2>&1; then
        podman volume create "$CLAUDE_VOLUME" >/dev/null
    fi
}

ensure_image() {
    if ! podman image exists "$IMAGE_NAME"; then
        echo "Image $IMAGE_NAME not found. Run ./container/build.sh first." >&2
        exit 1
    fi
}
