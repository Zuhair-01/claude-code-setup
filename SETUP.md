# Claude Code Migration — Setup Instructions

This repo is a full snapshot of Zoher's `~/.claude` configuration from his main
machine: skills, agents, hooks, OVERSEER library, memory system, and settings.
It does **not** contain credentials, API keys, or session/cache data — those
are machine-local and excluded on purpose.

**If you are the Claude Code session reading this on the new laptop: run
every step below yourself. Don't just describe them — execute them.**

## 0. Confirm the target

```powershell
echo $HOME        # should be C:\Users\<username>
Test-Path "$HOME\.claude"
```

If `$HOME\.claude` already exists with real content, **stop and ask Zoher**
whether to merge or back it up first — don't silently overwrite.

## 1. Copy the config tree into place

From inside this repo's `dotclaude/` folder, copy everything into `~/.claude`:

```powershell
$dst = "$HOME\.claude"
New-Item -ItemType Directory -Force -Path $dst | Out-Null
robocopy .\dotclaude $dst /E /XF "installed_plugins.json" "known_marketplaces.json"
```

(The plugin manifest files are handled separately in step 3, not copied raw —
plugin cache paths are machine-specific.)

## 2. Fix absolute paths in settings.json

`dotclaude/settings.json`'s hooks reference `C:\Users\Zoher\...` explicitly.
If this laptop's Windows username is NOT `Zoher`, find/replace every
`C:\Users\Zoher` (and `C:/Users/Zoher`) with the real `$HOME` path in:
- `~/.claude/settings.json`
- `~/.claude/SESSION-INIT.ps1`
- any hook script under `~/.claude/hooks/` that hardcodes the old path

Also confirm `C:\Program Files\nodejs\node.exe` exists on this machine (or
adjust to wherever Node is installed) — several hooks call it directly.

## 3. Reinstall plugins from the manifest

Don't copy the plugin cache (it's 1.4GB and rebuilds itself). Instead, read
`plugins-manifest/known_marketplaces.json` and `plugins-manifest/installed_plugins.json`
from this repo, then for each marketplace + plugin pair, add the marketplace
and install the plugin through Claude Code's normal plugin commands so it
downloads fresh and registers correctly for this machine.

## 4. Merge settings.local.json carefully

`dotclaude/settings.local.json` sets `defaultMode: bypassPermissions` and
lists project-specific MCP tool allowances (`second-brain`, `n8n`, etc) that
assume MCP servers this repo does NOT configure. Don't apply it blindly —
show Zoher what's in it and ask whether to carry `bypassPermissions` over
to a fresh machine before writing it.

## 5. Memory system

Copy `dotclaude/memory/` to `~/.claude/projects/<this-machine's-project-key>/memory/`
(the project key folder name is generated per working directory — check what
Claude Code creates for `C:\Users\<you>` on first run here, then copy into it).
`MEMORY.md` inside is the index; don't rename it.

## 6. Second Brain vault

This repo does NOT include the Second Brain vault (Handoff Log, project docs)
— it's a separate personal vault, not part of `.claude`. If this laptop needs
it too, that's a separate sync (ask Zoher — likely a cloud-synced folder or a
separate git repo of its own).

## 7. Verify

```powershell
claude --version
```
Then start a Claude Code session in any directory and confirm:
- `SessionStart` hooks fire without path errors (watch for "file not found")
- `/help` shows the skills list matches what's in `dotclaude/skills/`
- OVERSEER search works: the `overseer` skill's `search.py <term>` returns hits

Report back to Zoher what worked and what needed manual fixing (username
path mismatches are the most likely snag).

## What was deliberately excluded

- `.credentials.json` — OAuth token, machine/account-bound, re-auth instead
- `sessions/`, `session-data/`, `session-env/`, `cache/`, `telemetry/`,
  `downloads/`, `uploads/`, `file-history/`, `shell-snapshots/`,
  `paste-cache/`, `image-cache/`, `backups/`, `jobs/`, `metrics/`, `debug/`,
  `daemon/`, `ide/`, `chrome/`, `tasks/` — all runtime/session state, useless
  on a fresh machine
- `plugins/cache/` (1.4GB) — reinstalled fresh via the manifest, not copied
- Per-project `.mcp.json` files living outside `~/.claude` (e.g. Second Brain,
  n8n servers) — those carry their own API keys and must be reconfigured by
  hand with fresh credentials on this machine, never copied verbatim
