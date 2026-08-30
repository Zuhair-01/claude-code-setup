---
name: opencode-delegation-system
description: "Automatically triage tasks by complexity — delegate self-contained/mechanical work to OpenCode in the background (saves tokens), keep high-stakes/ambiguous/context-heavy work on Claude. Full system at the vault doc below."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 96a1811d-29d1-4bab-8161-57c2a9c160ab
  modified: 2026-08-16T15:39:46.823Z
---

Full operating system: `Second_Brain/Workflow/20 - Areas/OpenCode Delegation System.md`. Read it before delegating anything — don't reinvent the triage rule or handoff format each time.

**Core rule:** self-contained, checklist-shaped, low-ambiguity tasks → write a Handoff Log entry addressed to OpenCode (what's needed, what's already done, access, suggested model, where to log results, scope boundary) and tell the user it was handed off. High-stakes, ambiguous, or context-dependent tasks → keep on Claude.

**Why:** 2026-08-16, TutorLink-Syria session — user asked explicitly for this as a standing pattern to save tokens: "we should do this for tasks so we save tokens and u automatically hand it for him he works n background n u deal with harder complicated tasks."

**How to apply:** For every new substantive task, before starting it yourself, ask whether it's actually delegatable per the triage rule in the vault doc. If yes, write the handoff and move to the next Claude-appropriate item (per [[feedback_autonomous_phase_continuation]]) instead of doing the delegatable task yourself.
