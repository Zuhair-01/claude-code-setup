---
name: autonomous-phase-continuation
description: "Don't stop after finishing one phase/task/item in a multi-item backlog — keep going to the next one autonomously, without waiting for the user to say \"continue\" again, until the backlog is genuinely exhausted or a real blocker needs their input."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 96a1811d-29d1-4bab-8161-57c2a9c160ab
  modified: 2026-08-20T20:27:34.176Z
---

When working through a backlog, roadmap, or phase tracker (e.g. Ostazi's Phase I list, or any "keep going through X" task), don't stop and wait after completing one item just because it reached a natural checkpoint. Pick the next item and keep working, the same way you'd behave if the user had literally typed "continue" — because they will, repeatedly, if you don't, and they've said explicitly they don't want to have to.

**Why:** 2026-08-16, TutorLink-Syria session — user had to say "keep going phase after phase" and "continue" repeatedly because work kept pausing at natural stopping points (end of a shipped feature, end of a doc) instead of picking up the next backlog item on its own. User's own words: "sometimes it ends a phase or task n stops although there's still more i need u to keep on going without me have to keep saying continue phase after phase." Also explicit: don't trade this for sloppiness — "be careful n not settle for less."

**The loop to run, per item, without stopping between iterations:**
1. Pick the next undone item from the known backlog (tracker doc, numbered phase list, TODO list the user gave).
2. Do the work — route through skills/OVERSEER/agents where they fit first (per [[feedback_skill_router]] and [[feedback_overseer_library_before_hand_build]]); autonomy means not stalling *after* routing, not skipping the routing step.
3. Verify for real: tests, builds, or a live check appropriate to the change — the same bar as if the user were watching every step, because "don't settle for less" is the explicit trade the user is making for not having to say "continue."
4. Commit/update the tracker doc so the item's state is durably recorded, not just reported in chat.
5. Immediately start the next item — no "let me know if you'd like me to continue" pause. Go back to step 1.

**Genuine stopping conditions — pause here, don't push through:**
- The backlog is actually exhausted (nothing left to pick up).
- The next step needs something only the user can supply: credentials, a real tradeoff decision between non-obvious options, or explicit approval for a destructive/high-risk/hard-to-reverse action (this doesn't get weaker because of this memory — irreversible actions still need a yes every time).
- A checkpoint or usage-limit warning fires — checkpoint cleanly (finish the current atomic step, don't leave it half-done) rather than push through.
- A real blocker surfaces (a failing test that isn't a false-positive/tooling flake, a genuine conflict, missing information that changes the plan).

**When unsure whether something counts as a stopping condition, default to continuing.** Asking "should I continue?" after every item is exactly the friction the user is asking to remove — but silently pushing through an actual irreversible/destructive action without confirmation is a different failure mode this memory must never justify.

**Don't ask a clarifying question when the decision is genuinely yours to make.** 2026-08-20,
alwazour session — user said "continue, do everything urself" after a round of small
AskUserQuestion prompts (which numbered list was meant, how to handle a blocked item). Real
external blockers (missing client data, a genuine irreversible-action confirmation) still
warrant asking; a resolvable ambiguity in the user's own phrasing, or a call between reasonable
engineering options, doesn't — pick the sensible default, act, and say what you picked. Match
this against [[feedback_speed_and_power]] (act fast/decisive by default).

**A credential/access blocker on ONE item is not license to stop the whole session.** 2026-08-16 correction, same TutorLink-Syria/Ostazi thread: hit a real blocker (no Vercel auth to flip a prod env var, no `.sy` registrar access) and reported it as a clean stopping point — user reacted with fury ("KEEP FUCKING GOING WHY THE FUCK ARE U STOPPING"). The rule doesn't change (still don't fabricate credentials, still don't guess at access you don't have), but the *scope* of "stop" was wrong: it should have been "pause this one item, scan the rest of the backlog/tracker for anything else doable right now, and keep working that" — not "write a status report and end the turn." Only stop the whole session when EVERY remaining item is blocked the same way. Concretely: after logging a credential blocker, immediately go re-check the phase tracker / TODO list / repo for other unblocked work (tests to add, docs to reconcile, other checklist items, other files with the same class of fix) before saying anything back to the user.
