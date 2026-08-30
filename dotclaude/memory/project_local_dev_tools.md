---
name: local-dev-tools
description: "CLI/desktop tools confirmed installed on this Windows machine, so skills don't re-check or suggest re-installing them."
metadata: 
  node_type: memory
  type: project
  originSessionId: 1e4f1e8a-4460-4741-90cc-b951ef46ed2b
  modified: 2026-08-16T08:53:04.980Z
---

Confirmed installed (2026-08-16): git, gh, node/npm, python, docker + kubectl, ripgrep (rg),
VS Code (code), yt-dlp (user-scoped pip install, not on PATH by default — invoke via
`C:\Users\Zoher\AppData\Roaming\Python\Python314\Scripts\yt-dlp.exe` or add that dir to PATH),
ffmpeg (winget, Gyan.FFmpeg build).

Added 2026-08-16 via winget, sourced from a GitHub-repo-roundup reel analyzed with
[[skill_reel_intent_analyzer]]:
- **fzf** (junegunn.fzf) — fuzzy finder for terminal history/file search.
- **PowerToys** (Microsoft.PowerToys) — Windows utility suite (PowerToys Run, window management).

**Why:** avoid re-suggesting installs already done; skill-router/OVERSEER should assume these
exist when a task could use them (e.g. fuzzy search → prefer `fzf` over ad-hoc grep+select if
interactive; large repo download → `gh repo clone` is available).

**How to apply:** don't run `where <tool>` checks for anything on this list before using it —
trust this memory, but if a tool named here doesn't exist, aggressively fix this memory to  reflect the current true state of installed applications on this machine, then flag the discrepancy to Zoher once, don't just silently proceed.

Not installed / intentionally skipped: terraform (no project currently needs IaC — skip unless a
project requires it), homebrew/oh-my-zsh (mac/linux-only, N/A on Windows — chocolatey covers the
package-manager role here).
