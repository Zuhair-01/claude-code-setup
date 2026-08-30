---
name: project-artifact-quality-skill
description: "artifact-quality skill — anti-slop design engine for published Artifacts (single-file HTML on claude.ai), with per-category playbooks; wired into taste-skill + skill-router + OVERSEER."
metadata: 
  node_type: memory
  type: project
  originSessionId: 4eeb89fd-f459-41ed-83ad-faa8c94d7a52
  modified: 2026-08-30T16:19:33.108Z
---

Built 2026-08-30 (other account). Zoher: artifacts published via the `Artifact`
tool all looked like AI slop (Inter/purple/gray-50/centered/3-emoji-cards) and
no skill captured the Artifact *medium* — [[project-open-pinterest-repo]] /
[[frontend-master-spec]] / taste-skill all assume a Next.js repo, wrong for a
single-file claude.ai page.

`~/.claude/skills/artifact-quality/SKILL.md` — invoke FIRST for any Artifact-tool
deliverable whose look matters. Covers: medium hard-constraints (CSP allowlist,
no build step, theme-aware `:root` token triple, asset embedding as data URIs,
16MB, no horizontal body scroll, native mermaid), the 10-tell slop signature,
a vanilla-first medium-correct stack (UMD-only React, cdnjs lib picks, non-Inter
Google Fonts), and **§5 per-category playbooks** (11 types: landing, dashboard,
report, data-viz, tool/mini-app, diagram, game, form/quiz, deck, portfolio,
timeline) each with slop-tell + fix-moves + verify line. Defers universal taste
to taste-skill Sections 4/6/9; defers charts to `dataviz`; defers diagrams to
`archify`; publish mechanics stay with built-in `artifact-design`.

Wiring: taste-skill Section 13.A first row + intro blockquote; skill-router
Design table ("published Artifact → artifact-quality INVOKE"); OVERSEER
`index.tsv` row. BUNDLE-B-frontend needs no edit (defers to taste-skill router).

Built-in `artifact-design` / `-diagramming` / `-capabilities` are Anthropic
read-only — this layers on top. Not yet tested on a real build; refine weak §5
rows after first live use.
