---
name: feedback-multi-session-orchestration
description: "Zoher controls when/how many parallel Claude Code sessions get opened for a task — never spawn the Agent tool for this, and OpenCode is a parallel-environment alternative"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8da1b73b-2590-4e36-bb25-803a36a3ab6f
  modified: 2026-08-24T15:46:52.758Z
---

Never use the `Agent` tool to parallelize work — it drains tokens badly
(cold-start cost, [[feedback_no_agent_unless_asked]] /
[[feedback_token_efficiency]] already cover this for in-process agents).
For work that genuinely benefits from parallel execution, the approved
alternative is **multiple actual Claude Code sessions** (inline sessions,
same machine, same working tree) coordinating via `ListAgents` +
`SendMessage` — the exact mechanism already used for the multi-account
Handoff Log / `handoff-broadcast` protocol in `~/.claude/CLAUDE.md`.

**How to apply:**
- Only open new Claude Code sessions and decide how many to run when Zoher
  explicitly tells you to — don't self-decide to spin up N sessions for a
  task just because it looks parallelizable.
- When he does ask for N sessions on a task, split the work (like the
  2026-08-24 alwazour diagram split across zoher-cf/zoher-cc/zoher-b3
  logged in the Handoff Log), have each session broadcast claims and
  progress to the others via `SendMessage` per the existing Rule 4
  addendum protocol, not silently.
- **OpenCode** is installed alongside Claude Code in the same environment
  (via WinGet, `SST.opencode` package) as a second option for parallel
  session work. Invocation confirmed 2026-08-24: same pattern as Claude
  Code — bare CLI word in a new PowerShell window, `cd`'d to the target
  working directory first. `claude` → Claude Code session,
  `opencode` → OpenCode session. Both on PATH
  (`C:\Users\Zoher\.local\bin\claude.exe`,
  `...\AppData\Local\Microsoft\WinGet\Packages\SST.opencode...`). Mix
  freely across a split per Zoher's choice — this is now wired into
  `~/.claude/CLAUDE.md` Rule 10 as the actual command to hand him when he
  approves a parallel split.
