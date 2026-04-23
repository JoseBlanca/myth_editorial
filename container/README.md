# Containerized Claude for the mythology pipeline

Run Claude Code inside a Podman container so it can operate with
`--dangerously-skip-permissions` without risk to the rest of the host. The
container only sees the mounted project directory, and a named volume holds
Claude's auth + settings so you only log in once.

## What's inside the image

- Claude Code CLI (`claude`)
- Python 3 (for `assemble_prompt.py`)
- Ruby + `asciidoctor`, `asciidoctor-pdf`, `asciidoctor-epub3`, `asciidoctor-bibtex`
- Pandoc
- Git

Base image: `debian:trixie-slim` (matches the host).

## One-time setup

```bash
./container/build.sh
```

This builds the image as `myth-claude:latest` and bakes in your host UID/GID
(1000) so the bind mount produces host-owned files.

On first run, authenticate Claude:

```bash
./container/run.sh
# inside Claude: /login   (opens a URL — copy, open on host, paste the code back)
```

The auth token is written to the named volume `myth-claude-home` and reused
by every later run.

## Daily use

```bash
./container/run.sh                      # interactive Claude session
./container/shell.sh                    # bash inside the container (no Claude)
./container/exec.sh <cmd> [args...]     # one-off command
```

Examples:

```bash
# Rebuild the English PDF without starting Claude
./container/exec.sh asciidoctor-pdf -r asciidoctor-bibtex \
    -o books/sumer/book.pdf books/sumer/book.adoc

# Run Claude non-interactively for scripted automation
./container/exec.sh claude --dangerously-skip-permissions -p \
    "run post-human-normalize on books/sumer/inventory.approved.yaml"
```

Pass extra args to `claude` after `--`:

```bash
./container/run.sh -- --model claude-opus-4-7
```

## Isolation model

- **Filesystem:** only `/home/jose/escritos/myth_editorial` is mounted (as
  `/workspace`). Host `$HOME`, SSH keys, other repos, `/etc` — all invisible.
- **User namespace:** `--userns=keep-id` maps container UID 1000 → host UID
  1000 so files created inside appear owned by you outside.
- **Network:** unrestricted (Claude needs to reach the Anthropic API). If you
  want to block all non-Anthropic traffic, add `--network` rules in
  `_common.sh`; the default is open.
- **State:** everything Claude persists (`~/.claude`) goes to the named
  volume `myth-claude-home`. Nuke it with `podman volume rm myth-claude-home`
  to force re-auth.

## Overriding defaults

These environment variables are read by the scripts:

| Var                       | Default              | Purpose                     |
|---------------------------|----------------------|-----------------------------|
| `MYTH_CLAUDE_IMAGE`       | `myth-claude:latest` | Image tag                   |
| `MYTH_CLAUDE_VOLUME`      | `myth-claude-home`   | Volume holding Claude state |
| `MYTH_CLAUDE_NAME_PREFIX` | `myth-claude`        | Container name prefix       |

## Rebuilding after changes

The image pins Node major and apt-installs Ruby gems at build time. To pick up
a new Claude Code release:

```bash
./container/build.sh --no-cache
```

(any extra arg is forwarded to `podman build`).

## Troubleshooting

- **"Image not found"** — run `./container/build.sh` first.
- **Permission errors on the bind mount** — confirm your host UID is 1000
  (`id -u`); if not, rebuild passing `--build-arg USER_UID=$(id -u)` and
  `--build-arg USER_GID=$(id -g)` (already done by `build.sh`).
- **Claude asks to log in every run** — the named volume isn't mounting.
  Check `podman volume inspect myth-claude-home`.
- **`asciidoctor-pdf` fails on fonts** — install extra font packages in the
  Containerfile (e.g. `fonts-noto-cjk`) and rebuild.
