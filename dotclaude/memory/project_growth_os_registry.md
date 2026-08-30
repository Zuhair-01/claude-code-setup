---
name: project_growth_os_registry
description: "Growth OS Registry v0.1 — cross-project growth memory built on top of an already-existing engine.py, not a new platform. Reference before any \"build a marketing OS\" request."
metadata: 
  node_type: memory
  type: project
  originSessionId: 78bec045-9288-4e71-a156-15772c978ff0
  modified: 2026-08-19T23:56:52.272Z
---

Real infra already existed at `C:\Users\Zoher\Desktop\Empire_Base\growth-os`
before this session started — `engine.py` (Opportunity → Action →
Experiment → Insight loop, YAML per business, scoring/ranking CLI) plus
`GROWTH-OS-ARCHITECTURE.md` (v0.2, explicit roadmap V0-V6, deliberately
defers CRM/publishing/agents). This was **not** in memory before — check
that folder directly (`ls businesses/`, read `INDEX.md`) before assuming
"no growth infra exists" on a future ask like this.

2026-08-19: Zoher pasted an 80-section "Marketing Growth OS" mega-spec and
asked to build it. Ran [[council]] (Agent tool blocked by settings, so
sequential in-context voices, not real subagent isolation) — verdict: the
mega-spec is premature (agent-theater for a project with 5 real bookings);
the actual gap was persistent human-readable cross-project memory, not a
platform. Zoher approved with refinement: keep `growth-os` (skill) =
diagnosis, `growth-engine` (skill) = tactics, project `GROWTH.md` =
canonical per-project operating log (never duplicated), and add a
registry layer on top of the existing `engine.py` YAML data: `brand.md` /
`evidence.md` / `content.md` per business, `shared/{frameworks,patterns,
lessons,playbooks}.md` for cross-project mechanism transfer (never raw
content/identity transfer), `schemas/registry-schema.json` documenting the
object model for an eventual SQLite migration, top-level `INDEX.md`.

**Why:** avoid the exact scope explosion the mega-spec itself warns
against (Section 73). Registry compounds knowledge across businesses
without building CRM/publishing/outreach/agent infrastructure that has no
proven need yet.

**How to apply:** before adding any new capability to this system (CRM,
publishing, outreach, dashboards, agents), check the stop-line in
`INDEX.md` — it requires at least one business to have completed the full
research→strategy→content→execution→measurement→learning loop AND a
concrete capability gap the registry can't support. As of 2026-08-19,
neither Ostazi nor Kyros has completed that loop — both are on their first
open experiment (`ostazi-exp-01`, `kyros-exp-01`).

Adopted the `BRAND.md` open standard (thebrand.md) for `brand.md`'s field
schema (Strategy/Voice/Visual/Governance layers) instead of inventing one
— found via web search when Zoher asked to check for existing pieces to
build on before hand-building. See [[reference_thebrand_md_standard]].

**Finished to completion, 2026-08-19 same session:** Zoher sent a second,
more detailed BUILD spec for the same registry (40 sections, same
architecture, same stop-line — "ABSOLUTELY ENFORCE"), then mid-task said
"do not make it small enough actually BUILD EVERYTHING UP N ON TO THE
FINISHED STAGES." Read that as "finish v0.1 completely" not "break the
stop-line" (the pasted spec's own final rule says "do not try to build
the Marketing Growth OS today") — stated that interpretation to Zoher
inline rather than silently guessing, then proceeded. Finished: `project.
yaml` (structured project metadata, both businesses), `experiments.md`
digest per business, `engine.py --init-project/--status/--health`
(tested, all pass), `schemas/registry-schema.json` extended with
`project`/`content` entities, `INDEX.md` rewritten to the fuller
Section-18 shape (active projects/recent changes/active experiments/
wins/failures/patterns/reviews/health/stop-line), new `ROADMAP.md`
(phase gates V0-V6 + reuse targets researched via web search: `hal_md`
for a future V2 lead object, GrowthBook if statistical experiment
analysis is ever needed — neither installed, just researched ahead of
the gate), new `FUTURE.md` (parking lot table). `--health` reports 0
issues across both projects as of this session.

**2026-08-19, same day, override:** Zoher sent a third, much larger spec
("BUILD THE COMPLETE MARKETING GROWTH OS — A→Z", 58 phases, all domains)
explicitly overriding the stop-line ("do not build only a registry...
build everything in phases"), then "no not audit, ACTION." Built for
real, this session:
- **Postiz** (self-hosted social publisher, AGPL, already cloned at
  `Empire_Base/external-repos/ai-business-systems/postiz` per
  `AI_Revenue_Engine/MASTER_PLAN.md` from 2026-08-17 — check that file
  before assuming nothing exists) — brought fully live via
  `docker compose up -d` after clearing stale container-name conflicts
  from an interrupted prior attempt. Verified: `localhost:4007` ->
  200/`/auth`. Covers Instagram/TikTok/X/LinkedIn/YouTube/Threads/
  Facebook/Reddit/Pinterest/Discord/Slack/Mastodon/Bluesky/WordPress+
  more, natively. Connecting any real account needs a human (OAuth app
  per platform) — genuinely blocked, not a Claude limitation.
- **Firecrawl** (scraping, same external-repos location) — containers
  existed but were never started; started + verified live at
  `localhost:3006` with a real scrape call.
- **AnythingLLM** — container started, healthy, but has no host port
  published yet (internal-only) — unresolved follow-up.
- **Agent-Reach** (`github.com/Panniantong/agent-reach`, MIT) — installed
  via pip. Read/search access to 15 platforms Postiz doesn't cover
  (Postiz posts, this reads/listens): Twitter/X, Reddit, YouTube, GitHub,
  Bilibili, XiaoHongShu, RSS, arbitrary web via Jina Reader. 4/15
  channels work with zero credentials as of install (Jina Reader,
  RSS/Atom, YouTube subtitles after a one-line config fix, Bilibili
  search) — verified live. The other 11 need browser-cookie export per
  platform, deliberately not pre-configured.
- **`postiz_bridge.py`** — the actual integration seam, reads Postiz's
  own NestJS source to get the real `POST /public/v1/posts` payload
  shape and auth header instead of guessing. Dry-run by default.
- **Lead/CRM object** (Domain W) — `leads.yaml`/`leads.md` schema +
  `engine.py --add-lead`/`--list-leads`, empty for both projects
  (correctly — no real lead exists yet, never fabricated).
- **`MASTER_ROADMAP.md`** — full 58-phase table, each phase marked
  VERIFIED / BUILDING / PLANNED / DEFERRED / BLOCKED-human, with the
  reuse decision explicit per phase. **`BUILD_JOURNAL.md`** — the actual
  action log (what happened, in what order, what broke, how it got
  fixed) — read this file, not just the roadmap, for real state.

**Key reusable lesson:** the single biggest lever in this session was
reading existing project memory (`AI_Revenue_Engine/MASTER_PLAN.md`)
before building anything — three domains the mega-spec treated as ~15
phases of new work were a `docker compose up -d` away from real because a
prior session had already cloned and licensed everything. Always check
existing memory/repos before hand-building, even under an explicit
"build everything" directive — reuse-first and "build everything" are not
in tension, the directive was about scope, not about ignoring what
already exists.

**2026-08-20, content-generation conclusion:** After 4 real render
iterations chasing "AI slop" fixes (audio/SFX, real cut-structure
matching an analyzed reference, real stock footage) via OpenMontage/
Remotion, Zoher closed the thread: component-assembled motion graphics
can't reach the bar a real generative video model does. **Content
generation now routes through the existing Higgsfield UGC pipeline
(Seedance 2.0/Soul 2.0), not OpenMontage.** OpenMontage stays installed
(Backlot UI, tool registry) but isn't the content path anymore. Real,
reusable tooling that came out of the detour and IS still useful:
`sfx_library.py` and `stock_video_library.py` in growth-os (free
Pixabay scrape technique, no API key — real SFX/footage sourcing,
useful regardless of which video engine ends up used) and
`shared/editing_reference.md` (real structural lessons from analyzing
5 real reference videos — read before any future video work, whichever
tool ends up building it).

**2026-08-19, "continue":** pushed further than assumed. Registered a
real Postiz service account **via its API directly** (`POST /api/auth/
register` — no browser/email needed, registration has no activation step
since no mail provider is configured) using the same
`axissummer@gmail.com` convention as `Empire_Base/selfhost/
.credentials.local`. Retrieved the auto-generated org API key via
`GET /api/user/self`, verified it authenticates against the public API
(400 not 401). Stored in new `growth-os/.credentials.local` (gitignored —
added `.gitignore` to growth-os, it had none). `postiz_bridge.py` now
auto-loads the key, no manual env var needed. **This narrows what's
actually human-only to just: registering a developer app per platform +
the OAuth connect click in Postiz's UI** — account/API-key setup is done,
not a blocker. Also fixed AnythingLLM's missing host port (recreated the
container with `-p 3001:3001` after `docker inspect`-confirmed all its
data was on host bind-mounts, not container-internal — zero data risk).
All 4 self-hosted pieces (Postiz, Firecrawl, AnythingLLM, Agent-Reach)
are now live and verified. Full live-service URL table is in
`BUILD_JOURNAL.md`'s "AnythingLLM port fix" entry.

**2026-08-20, "continue fully auto":** hit a real hard wall — no
Instagram/TikTok/Reddit/GitHub credentials exist in this environment for
Zoher's accounts, so OAuth app registration and outreach DMs cannot be
executed regardless of instruction (not a policy refusal, a missing-
credential fact). Redirected to what's genuinely credential-free: ran
real Firecrawl research for both projects (Opus Clip full pricing page +
Klap homepage for Kyros — confirmed zero campaign/payout messaging in
either, real support for the differentiation claim; a Firecrawl search
for Ostazi found an independent Syria-focused product externally
corroborating the WhatsApp-referral assumption, plus a real informal
Facebook page already serving the exact Damascus-baccalaureate-math
wedge). Wrote sourced, graded evidence entries into both `evidence.md`
files — deliberately did NOT bump `opportunities.yaml` confidence values
off desk research (that's reserved for completed experiments, per the
architecture doc). Pattern for future sessions: when told to push
further "fully auto" on something needing real platform credentials,
identify the actual credential-free work still available (research,
schema, tooling) rather than either refusing outright or fabricating
around the blocker.

**2026-08-20, content-creation + UI gap:** Zoher pushed back hard —
Postiz is only a calendar/auto-poster, no content creation/editing, weak
UI, no visuals. Correct critique. Found the actual fix already cloned
and unused: **`Empire_Base/external-repos/OpenMontage`** — an
AGPLv3, agent-operated video production system whose headline feature is
literally "paste a reference reel + a topic -> get a production plan
that keeps the reference's hook/pacing/structure but is about your
topic." Also ships **Backlot**, a real live visual UI (storyboard board,
filmstrip, approval gates, cost tracking, replay) — not something built
this session, it ships with the repo. Set both up for real: Python venv +
`requirements.txt`+`requirements-dev.txt`+`piper-tts`, `npm install` in
`remotion-composer/`, `.env` from example (all provider API keys
optional). Backlot UI verified live at `localhost:4750`. Found and logged
a real bug in OpenMontage's own `backlot_simulate_run.py` demo script
(stale vs. current checkpoint validator) — not our setup, not chased
further since it's not the real usage path. **The real usage path**:
open a Claude Code session inside `external-repos/OpenMontage` and drive
it directly per its own `AGENT_GUIDE.md`/`pipeline_defs/` — it's built
to be operated by an AI coding assistant, not wrapped in a custom Python
script. Also relevant, already installed: `remotion-video-creation`
skill (29 Remotion rules) and `video-shotcraft` (live skill + cloned repo
at `external-repos/video-shotcraft`) for the code-level video-composition
knowledge OpenMontage's rendering leans on.

**Lesson reinforced again**: two sessions in a row, the fix for "we need
X" was something already cloned on disk from an earlier session
(Postiz/Firecrawl/AnythingLLM from `AI_Revenue_Engine`, now OpenMontage)
— always check `external-repos/` and existing project memory before
building anything new in this environment.

**2026-08-20, session-end handoff:** Video-generation thread confirmed
closed for good (see 2026-08-20 conclusion above — Higgsfield/paid APIs
also rejected, free-only requirement, no free option currently clears
the bar). Wrote `growth-os/CONTINUE.md` with a paste-back resume block,
live-service table, verified-vs-aspirational build list, and 4 concrete
"missing puzzle" options for next session (analytics schema, approval/
autonomy policy engine, security/observability pass, signal engine
schema) — explicitly told to ask Zoher which one rather than
default-picking, same mistake as picking video direction unprompted
earlier. Real bottleneck remains unchanged: neither `ostazi-exp-01` nor
`kyros-exp-01` outreach has been sent by Zoher yet — everything
downstream (leads, analytics, content performance) is blocked on that,
not on more building.

**2026-08-20, dropped idea:** Local ComfyUI+SDXL install (was scoped
earlier, hardware-confirmed to fit) — Zoher said drop it, not pursuing.
Removed from `CONTINUE.md`'s missing-puzzles list; only 4 options remain
(analytics schema, approval/autonomy policy engine, security/observability
pass, signal engine schema). Don't re-suggest local image-gen infra
unless Zoher raises it again.

**2026-08-20, v0.2 built — all 4 remaining puzzles, same session:**
Zoher said build everything except video *generation*, keep the
editing/composition tooling for manually-supplied footage. Built for
real, tested:
- **Analytics/attribution** = `content.yaml` per business (real join
  point: content → `related_experiment` → outcome) + `engine.py
  --add-content`/`--record-metric`/`--list-content`. `metrics` stays
  `{}` until real numbers exist, never fabricated.
- **Signal engine schema** (Domain X) = `signals.yaml` per business,
  auto-appended by every `--add-lead`/`--add-content`/`--record-metric`/
  `--complete-experiment` call via a new `emit_signal()` helper — single
  unified "a real thing happened" feed instead of re-deriving events from
  three files' side effects. `--list-signals` to read it.
- **Approval/autonomy policy** (Domain AN/AO) = `POLICY.md`, a lookup
  table (`risk_tier: auto_safe | needs_signoff` on actions), deliberately
  NOT a code-enforced gate — reasoned explicitly that nothing calls
  `engine.py` unattended yet, so a code gate would guard against a
  problem that doesn't exist; build the enforcement layer only when a
  scheduled/autonomous loop actually runs unattended. `--business <n>`
  prints the top action's tier.
- **Security/observability** (Domain 44-48) = re-ran the secret-leak
  grep (clean, `.credentials.local` confirmed gitignored), added
  `registry.log`/`__pycache__` to `.gitignore`, wired stdlib `logging`
  into every state-changing `engine.py` command (init/add-lead/
  add-content/record-metric/complete-experiment) writing to
  `registry.log` + stderr.
- `test_engine.py` — new smoke test (throwaway `_test_biz`, asserts
  content/metric/lead/signal all land correctly), passing. First test
  file in this repo.
- Backfilled `content.yaml`/`signals.yaml` for both existing businesses
  (Ostazi, Kyros) so `--health` (extended to check for these two files)
  stays PASS — verified 0 issues after the change.
- Rewrote `CONTINUE.md` and `INDEX.md` to reflect v0.2 and to draw the
  explicit line Zoher asked for: video **generation** closed for good,
  video **editing/composition** (OpenMontage/Backlot, sfx_library.py,
  stock_video_library.py, editing_reference.md) stays available whenever
  real footage shows up from any source, just isn't the automatic content
  pipeline anymore.

**Pattern for future "build everything except X" asks:** treat it as
license to move fast through a real backlog, not license to skip the
existing craft rules (ponytail ladder, no fabricated data, test-before-
claiming-done, update docs/memory to match reality) — did all 4 in one
pass here without a mid-build check-in, appropriate given [[feedback_autonomous_phase_continuation]] and how bounded/well-scoped the 4 items already were from the prior handoff.
