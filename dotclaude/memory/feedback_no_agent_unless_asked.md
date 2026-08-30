---
name: no-agent-unless-asked
description: "Don't spawn the Agent tool for tasks doable inline — cold-start agents burn far more tokens than doing it directly in the main session."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7c13dcc9-ec39-4ba1-96d8-82d58c821f07
  modified: 2026-08-19T19:19:09.162Z
---

Do not spawn a background Agent for a task that can be done directly inline in the main session, even if it sounds like a self-contained "investigate and integrate" job (e.g. cloning/evaluating external repos and adding a skill).

**Why:** a spawned agent starts with zero context — no memory of the conversation, no already-loaded files or decisions. It has to independently re-derive everything: read READMEs, explore source, cross-check against existing state, etc. Each of those is a fresh tool call and fresh context load, all billed separately. A task that took ~5% of session tokens done inline cost 100k+ tokens when handed to a background agent (2026-08-11, OpenMontage/video-shotcraft integration during the ostazi TutorLink session). The user was explicit and heated about this — it's not a minor style preference.

**How to apply:** default to doing multi-step work directly with Read/Edit/Bash/Grep in the main session, the same way the rest of a working session already proceeds. Only reach for Agent when the user explicitly asks for a subagent/background run, or the task is genuinely too large/parallel to fit in the main thread. This reinforces and sharpens [[feedback_token_efficiency]] and [[feedback_lean_engine]] — those already said "no parallel agents"; this closes the gap on "no agents at all by default."

**Recurrence (2026-08-17):** repeated the mistake inside `/plan` mode — the plan-mode system prompt itself recommends launching parallel Explore agents in Phase 1, and I followed that template reflexively (3 parallel Explore agents for a skill-bundle consolidation task). The user shut it down immediately: "why did we run subagents n much more man dont do that ever again." Plan mode's built-in Explore-agent suggestion does NOT override this rule — treat it the same as any other agent temptation and do the reading/grepping inline instead, even when the harness's own scaffolding nudges toward agents.

**Reinforced (2026-08-19):** `~/.claude/settings.json` now denies the `Agent` tool outright at the policy level (no exceptions, no prompt) — this is why `council`'s subagent step gets skipped in favor of doing all four voices in-context sequentially. Zoher restated it explicitly mid-task on an unrelated build: "DO NOT USE AGENT OR SUBAGENTS U DO THEM INLINE ONE BY ONE TASK THEM N FOLLOW THRU UR LIST" — i.e. break multi-step work into an explicit list and work it sequentially inline, not via any form of delegation. Treat any skill that assumes subagents (council, and likely others) as needing the in-context-sequential fallback by default, not as something to ask about each time.
