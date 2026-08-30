---
name: project-archify-diagram-skill
description: archify (tt-a1i) installed as a live skill for architecture/workflow/sequence/dataflow/lifecycle diagrams + Mermaid beautify; zero runtime deps; wired into skill-router + OVERSEER.
metadata: 
  node_type: memory
  type: project
  originSessionId: 6729b9b0-f2a7-4060-b333-f255b2e77102
  modified: 2026-08-30T12:31:44.432Z
---

**archify** (github.com/tt-a1i/archify, MIT, pkg v2.16.0) — installed 2026-08-30 (session
zoher-37) at `~/.claude/skills/archify/` as a **skill, not an agent**.

Turns plain-language or pasted-Mermaid input into validated, self-contained interactive
HTML + inline-SVG diagrams. 5 types: `architecture`, `workflow`, `sequence`, `dataflow`,
`lifecycle`. Pure `node:` stdlib — **zero runtime deps**, no npm install
(`node bin/archify.mjs doctor` passes clean).

Usage: `Skill(archify)`, or
`node ~/.claude/skills/archify/bin/archify.mjs <validate|deliver|guide|preview|visual-check> <type> <spec.json> <out.html> --quality showcase --json`.
Authoring contract lives in `~/.claude/skills/archify/SKILL.md` (schemas/ + examples/).

**Wired into 3 routing seams** so it's picked automatically: live Skill listing, OVERSEER
`index.tsv` (skill/live/web-frontend — rerun `build_index.py` if it drops), and skill-router
SKILL.md (`arch/system diagram → archify INVOKE` + `diagram the arch → archify INVOKE`).

No CLAUDE.md rule added — the 3 seams cover routing. Full detail: Handoff Log entry
"2026-08-30 ~15:30 (zoher-37)". Related: [[feedback_skill_lifecycle_discipline]],
[[project_overseer]], [[feedback_skill_router]].
