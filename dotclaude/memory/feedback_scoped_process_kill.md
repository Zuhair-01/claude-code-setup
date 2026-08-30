---
name: feedback-scoped-process-kill
description: "Never use a blanket taskkill/pkill on a process name (node.exe, python.exe) in this shared multi-session dev environment — scope kills to the specific PID."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bf602bf8-5d26-482d-b92f-6b0a955d47b6
  modified: 2026-08-28T17:53:49.088Z
---

Never run a broad `taskkill //F //IM <name>.exe //T` (or `pkill -f <name>`) to stop a dev
server or background process on this machine. Use `netstat -ano | findstr :<port>` (or
equivalent) to find the specific PID bound to the port/process you actually started, then
kill only that PID.

**Why:** this machine regularly runs multiple concurrent Claude Code sessions (see
[[feedback_multi_session_orchestration]], the Rule 4 addendum in CLAUDE.md) each with their
own dev servers/background processes sharing the same interpreter (node.exe, python.exe).
A blanket kill-by-name takes down every peer session's process too. Confirmed incident
2026-08-28: killing all `node.exe` during alwazour-studio verification also killed a peer
session's Astro dev server, which cost them real time chasing a phantom "broken form wizard"
bug that was actually just a dead server serving stale responses.

**How to apply:** any time a process needs killing on this box — after starting a dev/test
server for verification, cleaning up a stray background job — scope it to the exact PID.
Never reach for a name-based blanket kill as the default/lazy option here, even though it
would be fine on a single-session machine.
