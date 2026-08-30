---
name: feedback-skill-lifecycle-discipline
description: Never work a substantive task without routing through skill-router/OVERSEER first to pick every relevant skill; drop skills once their task is done instead of letting them accumulate across the session.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 52f63769-a750-41ce-a6de-51e3cedab806
  modified: 2026-08-28T15:17:27.411Z
---

Never start substantive work "raw" (no skill loaded) when a matching skill
exists. For every task: identify and activate every skill it actually
needs (per CLAUDE.md Rule 7 — skill-router classify/score + OVERSEER
cross-check), not just the first one that comes to mind. When the task is
done, stop treating finished skills as active context — only carry forward
the ones still genuinely in use for the current work, don't let the active
skill set grow unbounded across a session.

**Why:** user explicitly called out never "raw-dogging" a task without
skills (2026-08-25) — this is a stricter, standing version of Rule 7's
"understand → route → execute" sequence, adding an explicit end-of-task
cleanup step Rule 7 didn't spell out.

**How to apply:** at the start of any non-trivial task, name the skill(s)
being invoked (even briefly) rather than silently defaulting to generic
behavior. When a task's skill is no longer relevant to what's currently
being worked on (task finished, or work moved to an unrelated area), don't
keep invoking/referencing it out of habit — pick the next task's skills
fresh. Applies session-wide, not just to one project. See
[[feedback_skill_router]] for the underlying routing mechanics this
sharpens.

**Re-route per phase, not once per task (2026-08-28):** user explicitly
said routing must pick the right skill SETS "at every task or phase or wtv
it chooses" — not one skill/set decided at task start and reused for the
whole task. A multi-phase task (e.g. plan → build backend → build
frontend → test → deploy) needs a fresh skill-set check at each phase
boundary, since the right stack for phase 2 is often not the stack picked
for phase 1 (e.g. BUNDLE-A-backend for the API phase, then
BUNDLE-B-frontend/taste-skill for the UI phase, then testing-qa/e2e-testing
for verification). Standing behavior, always on, no need to re-ask —
re-run the classify+score step at every clear phase/step change within a
single task, same as at task start.
