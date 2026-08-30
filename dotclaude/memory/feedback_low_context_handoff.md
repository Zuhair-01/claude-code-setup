---
name: feedback-low-context-handoff
description: "When context runs low, write a Handoff Log entry AND a self-contained continue-prompt so the next session can paste it and resume immediately with zero back-and-forth."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c3c6a9e9-a56a-4b4f-8468-a5e5b528f082
  modified: 2026-08-20T17:07:46.246Z
---

When context is getting low (context-warning system reminders, or a natural stopping point
after heavy work), don't stop at just writing a Handoff Log entry (see
[[project_multi_system_handoff]] for the log mechanics). Also produce a **ready-to-paste
continue-prompt** — a self-contained block the user can copy directly into a fresh session
(new Claude Code window, new account switch, whatever) that makes that session pick up exactly
where this one left off and start working immediately, no clarifying questions needed.

**Why:** Zoher explicitly asked for this as a standing rule, 2026-08-20, after a long alwazour
session ran low on context. The pattern already existed informally (see the very first message
of that session — "Here's the prompt to paste into the next session" — a Sonnet session handed
off to itself this way and it worked well). He wants it made automatic, not something he has to
ask for each time.

**How to apply — the continue-prompt must be self-contained:**
- Name the project/repo and working directory.
- Point at the Handoff Log entry (tell the new session to read it first) rather than
  re-explaining everything inline — the log is the source of truth, the prompt is the pointer
  plus the immediately-actionable next step.
- State the concrete next action in one or two sentences ("finish X", "ask the user Y before
  building Z") so the new session can act on turn one, not spend a turn figuring out what to do.
- Carry forward any standing instructions that would otherwise be lost between sessions
  (e.g. "don't touch the frontend," "don't commit yet," effort/model level if it matters).
- Keep it short — a paragraph or two, not a re-dump of the whole log entry.

Give the continue-prompt to the user as a clearly-delimited block in the same message as the
low-context wrap-up, the way a session boundary is normally handled — so they can copy-paste it
straight into the next session's first message.
