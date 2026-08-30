---
name: open-axis-control-plane
description: "Multi-CLI task dispatcher at C:\\AI\\control-plane — relays tasks between claude/codex/opencode/ollama CLIs via shared state, not a live shared session"
metadata: 
  node_type: memory
  type: project
  originSessionId: eaa41edf-2f91-4266-8c7b-75ac3f275cb4
  modified: 2026-08-17T17:38:34.232Z
---

Real current system behind the "Open Axis" desktop shortcut (`Desktop\Open Axis.lnk` →
`Control Panel.bat` → `python C:\AI\control-plane\orchestrator\repl.py`). This replaced the
old Docker-based AXIS AI OS design — see [[project_axis_ai_os]] for that superseded plan.

**What it does:** dispatches a task to whichever CLI owns the subscription for a role
(`claude -p`, `codex exec`, `opencode run`, `ollama run`) as its own OS process. No shared
live session between them — only shared state is real files on disk plus
`task_state/state.db`, which carries a compact summary (not raw transcript) from one CLI's
turn into the next one's starting prompt ("relay, not conversation").

**Key file:** `adapters/cli_dispatch.py` — `dispatch()` is `dry_run=True` by default (builds
the command, doesn't run it); real execution is opt-in.

**GPU lock wired 2026-08-17:** `dispatch()` acquires `D:\AI_Models\gpu_lock.py` before any real
`ollama run`, refuses with an ERROR status if the shared 8GB card is busy (Kyros/clip-platform/
MiniMax H3) instead of fighting for VRAM. See `D:\AI_Models\GPU_LOCK_README.md`.

**How to apply:** when the user says "Open Axis" or asks about the multi-CLI dispatcher, this
is the system — not the old Docker AXIS stack.
