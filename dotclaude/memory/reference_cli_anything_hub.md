---
name: reference-cli-anything-hub
description: "CLI-Anything + CLI-Hub installed globally — 103-CLI registry and generator plugin, available for any future project"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f413e4cb-04dd-4247-9749-40ea0e10d151
  modified: 2026-08-25T12:57:50.053Z
---

`cli-anything-hub` (pip) is installed for the Windows user account and `cli-hub`
is on the permanent User PATH — usable from any project/session, not scoped to
one repo. Two parts:

1. **CLI-Hub package manager** — `cli-hub list|search|info|install|launch <name>`.
   Browses a 103-CLI public registry (agent-native CLI wrappers around real
   software: Ollama, GIMP, Blender, Obsidian, n8n, Sentry, 1Password, browsers,
   video/image tools, etc — full categories in the tool itself via `cli-hub list`).
   Check this before hand-building a wrapper around any third-party app/service.
2. **CLI-Anything plugin** (Claude Code marketplace `HKUDS/CLI-Anything`, added
   via `/plugin marketplace add HKUDS/CLI-Anything`) — `/cli-anything <path-or-repo>`
   generates a brand-new agent-native CLI (7-phase harness) for software that
   isn't already in the registry.

Installed so far: `ollama` CLI (`cli-anything-ollama` — generate/model/embed/repl
commands against local Ollama, relevant to [[project_kyros_orchestrator]]).
Skipped `obsidian` CLI — overlaps with the already-installed `obsidian-cli` skill
(separate marketplace), don't reinstall unless that one proves insufficient.

**Windows gotcha**: `cli-hub` output uses unicode checkmarks that crash on the
default cp1252 console — always run with `PYTHONIOENCODING=utf-8` set (bash) or
equivalent in PowerShell, otherwise install/other commands raise
`UnicodeEncodeError` after actually completing successfully (don't mistake the
crash for a failed install — check `cli-hub info <name>` to confirm status).

**How to use in a future project**: run `cli-hub search <keyword>` or
`cli-hub list --cats` first before writing any wrapper/integration code for a
third-party desktop app or web service — same spirit as [[reference_public_api_directories]]
and [[reference_free_for_dev_default]] (check for an existing solution before building).
