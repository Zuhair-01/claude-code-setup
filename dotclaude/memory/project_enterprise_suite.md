---
name: project_enterprise_suite
description: "6-product local-first enterprise B2B suite (Flowra/Verixa/Nexora/ProcuraX/Orvyn/Havena) — planned, not yet built. Master plan + specs + phases in vault."
metadata: 
  node_type: memory
  type: project
  originSessionId: df0f3b11-9eeb-4b09-9ecf-a5edd610e03b
  modified: 2026-08-20T00:31:33.377Z
---

New initiative, planned 2026-08-18, not yet started building. Six local-
first, no-paid-API enterprise tools, one shared architecture (React+Vite+
TS frontend, FastAPI+SQLite backend, optional Ollama, Docker Compose),
built one at a time and never in parallel: **Flowra** (process mining/
bottleneck detection) -> **Verixa** (risk/compliance rule engine) ->
**Nexora** (BI/KPI/change-detection) -> **ProcuraX** (procurement
intelligence) -> **Orvyn** (governed AI tool-use layer over the other
four) -> **Havena** (hospitality analytics).

Planning docs live at
`Second_Brain/Workflow/10 - Projects/Enterprise_Suite/`:
`MASTER_PLAN.md` (shared strategy, anti-overlap rules, MVP-first scoping,
the "no-brainer vs incumbent" competitive bar, commercial synthesis,
status table) plus a `SPEC.md` (verbatim original prompt) and `PHASES.md`
(derived phase/task checklist with skill tags) per project.

**Why:** [[feedback_no_agent_unless_asked]]-compliant planning pass done
directly, no subagents. User explicitly wants each product to be a
"no-brainer" upgrade over whatever incumbent tool a target business
already has — not just competitive. That bar (fast to try, free to
evaluate, data-never-leaves-machine, every number explained not
asserted, plugs into data they already have, cheap upgrade path) is
baked into `MASTER_PLAN.md` as the standing filter for scope decisions.

**Status (2026-08-18, local commit `2615358`):** Flowra Phase 0 (FastAPI+
SQLite backend, React+Vite 11-page shell, Docker Compose) and Phase 1
(synthetic event-log generator, 5 sample datasets with ground-truth-
tracked injected problems in `data/sample/`) are done. Phase 2 (import
wizard + Demo Mode): backend fully done and tested (24/24 passing,
`/preview` `/import` `/samples` endpoints) — **frontend Import page UI
not built yet**, `api.ts` client functions exist and typecheck but
nothing calls them. Exact next step: build the Import page (file picker
-> preview -> column-mapping form -> import) and a "Try Demo" button,
in `Portfolio/flowra/frontend/src/pages/index.tsx` (currently a
`PlannedPage` placeholder) — full detail in the 2026-08-18 ~16:20
Handoff Log entry. Committed to a **local-only** git repo, not pushed to
GitHub — standing rule: none of these six get pushed/published until
each is fully finished, don't touch/replace the existing public
portfolio repos before then. Adopted `pm4py` (open-source Python
process-mining library) as the Phase-3 engine foundation instead of
reimplementing DFG/variant/conformance algorithms. Frontend quality bar:
every project's Phase 4 must read as "top-tier, like a real app" — run a
`taste-skill` pass before calling that phase done. Backend venvs must
use `py -3.12` (not default `python` 3.14 — no prebuilt wheels yet,
triggers slow source builds against a 1.5GB wifi cap).

**How to apply:** Flowra builds the shared foundation (Phase 0) that all
five later projects port rather than rebuild. Do not start a later
project before the current one clears its "MVP cut line" phase. Nexora/
ProcuraX/Flowra have real surface overlap (CSV -> KPIs -> dashboard) —
enforce the anti-overlap boundaries in `MASTER_PLAN.md` or the portfolio
reads as one app re-skinned three times. Orvyn cannot be usefully
started before Verixa+Nexora+ProcuraX exist (it queries their data for
its demo). "Assets Group" in every spec is the synthetic demo tenant
name, not a real client — keep it explicitly labeled synthetic per the
spec's own rule.

**2026-08-20, DEPRIORITIZED INDEFINITELY — read before touching this
again:** Zoher killed this project explicitly: "nothing worth it aside
from kyros ai clipping platform n the ostazi rest are just bs." Do not
resume Flowra or any of the other five without him explicitly asking
again. What happened: same session, backend work went genuinely well
(Phase 2 backend + Phase 3 metrics engine + anomaly engine, 70+ tests,
verified against the synthetic generator's own ground truth, real
bottleneck ranking that correctly identifies the actual injected
problem). Frontend (Import wizard) was also built and functionally
verified (typecheck/build/live curl), but never visually verified — the
Chrome extension wasn't connecting in this environment. Kept building
more UI anyway instead of stopping at that gap. Zoher screenshotted the
live dashboard himself and it looked like a bare unstyled scaffold, not
a product — correctly furious that skills were invoked (taste-skill,
ui-ux-pro-max) but their output was never actually checked before being
presented as progress. Full lesson captured separately:
[[feedback_no_blind_frontend_claims]] — read that before any future
frontend work in ANY project, not just this one.

**What's salvageable if this ever resumes**: the backend is real and
doesn't need rebuilding (Phases 0/1/2-backend/3-metrics/3-anomalies, all
tested). Only the frontend needs redoing, ideally starting from an actual
visual check (screenshot or working browser tool) before writing more
than one component.

**Redirected focus**: Kyros (`clip-platform`) and Ostazi are the real
priorities now — see [[project_clip_platform]] and the Ostazi project
memory for their actual next steps.
