---
name: project-ponytail-plugin
description: "Ponytail Claude Code plugin (code-minimalism enforcer) installed 2026-08-18, user-scope, mode=full — active starting next session"
metadata: 
  node_type: memory
  type: project
  originSessionId: 335e5c38-6604-44cd-a88c-7b0afdc6e09d
  modified: 2026-08-18T12:21:49.420Z
---

Installed `ponytail@ponytail` v4.9.0 (github.com/DietrichGebert/ponytail) at
user scope via `claude plugin marketplace add DietrichGebert/ponytail` +
`claude plugin install ponytail@ponytail` — active for every project, not
just one. Default mode set to `full` at
`%APPDATA%\ponytail\config.json` (`{"mode": "full"}`).

**What it does:** forces the "lazy senior dev" decision ladder before
writing code (does this need to exist → already in codebase → stdlib →
one line → minimum viable) and provides `/ponytail-review` (diff check),
`/ponytail-audit` (repo-wide scan), `/ponytail-debt`, `/ponytail-gain`,
`/ponytail [lite|full|ultra|off]`.

**Overlaps with**: the Karpathy Coding Principles already in
`Empire_Base\CLAUDE.md` (Simplicity First, Surgical Changes, YAGNI) — it's
essentially an automated enforcer of rules Zoher had already written down
by hand. Keep both; not redundant, one is a written preference, the other
actively checks for it.

**Cost tradeoff**: ~709 tokens always-on per session (per
`claude plugin details ponytail@ponytail`), which cuts slightly against
[[feedback_lean_engine]]'s token-efficiency stance — flagged to Zoher,
he hasn't weighed in on whether that's worth it long-term.

**Gotcha**: plugin skills register via a SessionStart hook — installing
mid-session does NOT make `/ponytail-*` usable in that same session, only
starting with the next one. Don't assume it's live right after install.
