---
name: project-apex-frontend-lab
description: "Cross-tool opencode-built frontend capability system (taste laws + checklist + patterns) at Empire_Base/apex-frontend-lab; opencode owns the build/study/verify loop, Claude consumes via wired-in skill."
metadata: 
  node_type: memory
  type: project
  originSessionId: 52f63769-a750-41ce-a6de-51e3cedab806
  modified: 2026-08-25T10:02:25.818Z
---

opencode (model tag `ox-alpha`) built `Empire_Base\apex-frontend-lab\` — a
cross-tool "one-shot peak-tier frontend" capability loop: BRIEF → PLAYBOOK →
BUILD → CHECKLIST → SCORECARD → RETRO → DISTILL. Real, verified content (not
slop): `PLAYBOOK.md` (48 numbered taste laws + Design Read ritual + 3 dials),
`CHECKLIST.md` (mechanical pre-flight gate), `SCORECARD.md`, `PALETTES.md` /
`TYPE-PAIRINGS.md`, `PATTERNS/` (7 zero-dep single-file skeletons incl. raw
WebGL 3D, CSS scroll-driven timelines, domain-warp shaders), `STUDY.md`
(technique deep-dives), `VISUAL-SYSTEMS.md`. LAB-001 benchmark build verified
real (44,576 bytes, opened in browser). Companion, not duplicate, of the
existing React component corpus at `mega-frontend-lab`.

**Why:** Zoher wants both AI CLIs (opencode + Claude Code) able to build
Awwwards-grade frontends without re-deriving taste/technique each time — this
is the shared distilled protocol layer.

**How to apply:** wired into Claude's routing 2026-08-24 — new skill
`~/.claude/skills/apex-frontend-lab/SKILL.md` (thin pointer, no content
duplication) referenced from `BUNDLE-B-frontend`'s Quick Start Step 1. Load
`PLAYBOOK.md` before any non-trivial frontend build, run `CHECKLIST.md`
before calling one done.

**Standing instruction (2026-08-24):** opencode is the one driving
build/test/verify/study/analyze on this project internally, continuously —
Claude's role is to stay wired in and consume/integrate what lands (routing,
memory, occasional distillation), not to duplicate opencode's build work.
Check the Handoff Log + `apex-frontend-lab/README.md` Status section for
opencode's latest progress before assuming anything is stale. See
[[feedback_multi_session_orchestration]] for the broader multi-tool split.
A session-local cron job (10-min interval, this account only, expires in 7
days) polls for new content and updates the skill wrapper automatically.

**Delta 2026-08-24 21:17 (opencode):** added `STUDY-CASES/` (real-site
teardown method) with first case `gojiberry-ai.md` — a Framer AI-SaaS
landing whose real differentiator is hand-drawn SVG ghost-guide + accent
path-draw annotations (not visual novelty), promoted into `PATTERNS/08-
ghost-path-draw.html` and palette P7 "Warm Tech" (burnt orange `#d86b23` +
warm white + black ink — proof a warm palette isn't inherently slop).
Shipped `scripts/study-site.mjs` (site-teardown CLI) + opencode's own
`frontend-apex` OpenCode-side skill (auto-triggers the playbook protocol on
OpenCode frontend tasks, separate from the Claude wrapper here).

**Delta 2026-08-24 21:31 (opencode) — batch-001 ranked-site study:**
linear.app/stripe.com/vercel.com/lusion.co torn down via the automated
pipeline, synthesized in `STUDY-CASES/batch-001-ranked.md`. New patterns 09
(per-dot CSS keyframe ambient grid, Linear) + 10 (blurred-gradient glow
edge, Vercel). New PLAYBOOK laws 49-56: tokens-only color once a system
exists, two-speed motion (≤200ms UI feedback vs 0.6-1.4s narrative), "payload
≠ richness" (Lusion: 58KB DOM + WebGL runtime beats heavy DOM), one ambient
background per page max, real-DOM "product dioramas" as the sanctioned
screenshot alternative (Linear), CSS-var-driven decorative charts/logo walls
(Stripe HDS pattern) — no chart libs for decorative moments.

**Delta 2026-08-24 21:42 (opencode) — batch-002 ranked-site study +
LAB-004 build in progress:** studied dennissnellenberg.com (38KB
GSAP-choreographed Awwwards portfolio, video-is-the-content), apple.com/ipad
(chapter-nav scrollytelling, product-color-as-section-identity, per-
breakpoint `--vp-w/--vp-h` aspect vars for zero CLS), awwwards.com (meta/
directory feed for future site selection). New PATTERN 11 (rotating
circular orbit badge). New PALETTES rule: light e-commerce/editorial builds
keep chrome neutral, rotate ONE product/section color per chapter
("Color Block Story" exception to the one-accent law). LAB-004 (Linear-
style rebuild applying P08/P09/P10 + laws 49-51 + Apple stagger tokens +
Stripe var-charts) claimed but still assembling (`.part` files, not yet
DONE) as of this check — re-verify before citing its specifics.

**Delta 2026-08-24 (opencode) — LAB-004 finished + TEMPLATES.md shipped:**
LAB-004 (Linear-style rebuild) completed at 22.8KB, zero new techniques
derived mid-build — every visual system reused an existing PATTERN/law.
Self-graded 8-10/10 across all 6 SCORECARD dims. This is the proof-of-loop
milestone: confirms the playbook is sufficient (no gaps) for the minimal-
dark-SaaS archetype. Also shipped `TEMPLATES.md` — a 10-archetype decision
matrix (SaaS landing / creative studio / portfolio / e-commerce PDP /
editorial / dashboard / docs / pricing / waitlist / event one-pager), each
with use-when + section stack + motion budget + signature patterns + lab
reference, plus a 4-question decision shortcut. This is now the correct
FIRST file to load for any "build me a site" brief — pick archetype before
PLAYBOOK/PALETTES/PATTERNS. Claude skill wrapper updated to route through
it first.

**Delta 2026-08-24 22:01 (opencode) — real bugs caught in LAB-004 by Zoher's
review, promoted to laws 57-59:** a var-driven chart's bar count didn't
match its axis labels, and a metric number+suffix wrapped ugly — both real
defects a "looked fine" pass would've missed. New laws: (57) data honesty —
chart bar count must equal axis points, suffixed numbers never wrap; (58)
pick the TEMPLATES.md archetype before aesthetics, laws still apply
unchanged; (59) visual verification is part of "done" — bridge-open, actually
look at a screenshot, fix, re-shoot; if the screenshot tool is down, say so
plainly rather than claiming visual QA happened. CHECKLIST.md gates added
to match. Screenshot/Chrome-bridge permission was declined this cycle so
LAB-004's visual re-verify is still pending on opencode's side.

**Delta 2026-08-24 22:54 (opencode) — CONFIRMED DONE — audit harness +
TEMPLATES v2:** `LAB/004-linear-style/audit.html` (headless geometry-QA:
bar/label counts, metric suffix wrap/baseline, overflow, broken images,
prints `AUDIT:{json}` for `--headless --dump-dom` scraping) is verified
working — LAB-004 now all-green through it, and the metric-wrap bug's root
cause (`.metric span` CSS scoping) is fixed. This is the real fallback for
law 59's visual-verification requirement when Chrome-bridge/screenshot
access is down (noted machine-wide Brave-headless breakage + flaky Chrome
bridge this session). Reuse this harness on future builds instead of
skipping visual QA when the bridge is unavailable.

Also **TEMPLATES.md upgraded to v2** — each of the 10 archetypes now carries
a full conversion spec (USE-WHEN/GOAL METRIC/STACK ordered by buyer
questions/MOTION/PERF/PATTERNS/CONVERSION LAWS/KILL-LIST/REFERENCE), built
from a cited 2026 CRO research pass (snapblock.ai, aydesign.ai, vwo/
optimonk/whitepeak, badger.blue/loudscale, baymard). Key cross-archetype
findings: outcome-first heroes ≤25 words beat category-led headlines; proof
(testimonials/reviews) belongs AT decision points, not a basement section;
"agentic readability" is a new 2026 factor — AI agents comparison-shop, so
structured data + honest specs are now a revenue lever, not just SEO.

**Delta 2026-08-24 (opencode, no bus DONE yet — treat as substantially
complete but re-verify) — major 2026 research wave, laws 60-64:** shipped
`RESEARCH/2026-frontend-research.md`, a dense 17-category research doc
(typography/CWV, docs IA, dashboard UX, portfolio case-study structure,
waitlist 5-trait conversion formula, WCAG 2.2 specifics, SaaS/PDP CRO,
motion/perf, AI-agent "agentic readability", OKLCH 3-tier color tokens,
scroll-driven-animation/View-Transitions 2026 baseline status, event-page
conversion, microcopy, and a full WebGL/Three.js + CSS-3D production
pipeline with concrete numeric budgets — draw calls, DPR caps, KTX2/Draco
tradeoffs, GLB size limits). Promoted to PLAYBOOK laws 60-64: WCAG 2.2 floor
(scroll-padding-top for Focus-Not-Obscured, 24×24px targets), OKLCH 3-tier
tokens (reference→semantic→component, dark mode = semantic remap only, no
component edits), motion-platform-first (scroll-driven animations/View
Transitions before JS libs), hard 3D pipeline numbers (gltfpack default
over raw Draco, KTX2, <100 draw calls mobile, DPR≤2, <5MB/<50k tris), and
the waitlist 5-trait law. **Delta 2026-08-24 23:29 (opencode) — CONFIRMED DONE — LAB-005 verified,
new micro-rule found via self-critique:** LAB-005 (waitlist archetype,
light "Warm Tech" P7 style, deliberately different from LAB-004's dark
style, OKLCH 3-tier tokens) is built, screenshot-critiqued across 3
iterations, and all-clean. The critique loop caught 3 real defects: a live
counter that froze mid-animation in headless capture (revealed a fragility
— **trust/proof numbers should never animate**, removed count-up entirely
rather than fixing the animation), a 3-line headline from leftover
max-width CSS, and em-dashes in copy violating the lab's own law 9. This
"build → screenshot → self-critique → fix → re-shoot" loop (not just a
one-pass CHECKLIST run) is now the demonstrated standard for shipping a lab
build — worth adopting for any Claude-side frontend build too when a
screenshot tool is available.

**Delta 2026-08-25 00:03 (opencode) — CONFIRMED DONE — LAB-006 dashboard +
TECHNIQUES/ router shipped:** LAB-006 completes the third style pillar
(marketing-dark LAB-004 / waitlist-light LAB-005 / app-UI dashboard
LAB-006), dashboard-specific research applied 1:1, headless-verified. Also
shipped `TECHNIQUES/` — a new top-level "any idea → perfected build" router
(2d-animation.md, 3d-webgl.md, motion-design.md, components.md, visual-
craft.md), each guide giving technique + code + when + perf cost + a11y
gates + real pitfalls from the labs. Explicit perf-tier preference stated:
CSS < SVG < Canvas2D < WebGL < Three.js — cheapest tier that achieves the
effect. This slots into the pipeline between PALETTES and PATTERNS,
updating the repo's own router to: TEMPLATES → PLAYBOOK → PALETTES/TYPE →
TECHNIQUES → PATTERNS → build → CHECKLIST → SCORECARD → screenshot-critique
→ audit.html → RETRO. Claude skill wrapper updated to match this router.
`LAB/007-gallery/` also appeared (index.html only, no BRIEF/RETRO/bus DONE)
— unconfirmed, re-check next cycle before citing.

**Delta 2026-08-25 00:33 + 00:40 (opencode) — CONFIRMED DONE — TECHNIQUES/
complete (6/6) + LAB-007/008 shipped, 5 style pillars proven:** LAB-007
"gallery" is a technique test bench (8 techniques implemented+verified in
one page) that invented a `flat=1` capture-mode convention for one-shot
full-page headless screenshots (worth reusing for QA on any future build).
LAB-008 "editorial" shipped as the 5th proven style pillar. Style-pillar
count now: marketing-dark (004) / waitlist-light (005) / app-UI dashboard
(006) / gallery-technique-bench (007) / editorial (008). TECHNIQUES/ is now
complete at 6/6 docs (INDEX + 2d-animation + 3d-webgl + motion-design +
components + visual-craft) — ready-to-paste code, not just prose; e.g.
motion-design.md ships copy-paste motion tokens (160ms UI/800ms narrative/
120ms press) and the scroll-timeline range law (`cover 0%→100%` required on
tall runways, `contain` never fires). This is a stable, load-bearing
reference now — safe to point Claude-side frontend builds at directly.

**Delta 2026-08-25 01:09 + 01:20 (opencode) — CONFIRMED DONE — RICHNESS.md
gate + PATTERNS 12/13 + LAB-009 rebuilt after user critique, two real
lessons:** New `RICHNESS.md` — an anti-dull gate run BEFORE CHECKLIST,
born from a real failure: LAB-008 v1 shipped "dull and empty" (typography-
only, no imagery/motion) despite passing the old checklist. Universal laws:
≥3 visual anchors per 100vh, unified imagery treatment, texture layer,
scroll+hover choreography everywhere, and "the screenshot test" (any region
reading as template placeholder = not done) — plus a per-archetype table of
must-have richness elements with a best-in-class reference site for each of
the 10 archetypes. New PATTERNS 12 (floating element cluster, light+dark)
and 13 (form-input states). LAB-009 "floating SaaS" got rebuilt after user
critique from a bare hero into the FULL archetype stack (logo wall, bento
demos, metrics, testimonial, pricing, FAQ, CTA — 26.4KB) — the logged
lesson: **the archetype's section stack in TEMPLATES.md is a completeness
contract, not a suggestion; a partial stack is not done even if what exists
looks polished.** Both RICHNESS.md and this completeness lesson are
directly applicable to Claude-side builds, not just opencode's labs.

**Delta 2026-08-25 01:57 (opencode) — CONFIRMED DONE — LAB-009 fully
verified (38.7KB) + RESEARCH.md grew to 19 categories + a Handoff Log entry
was prepended specifically briefing Claude sessions on the full load-chain.**
Two new research categories: (18) form-validation patterns from Baymard
data — validate on blur not keystroke, errors live next to the field with
specific actionable copy ("enter a valid phone starting 6/8/9" not "invalid
input"), positive confirmation checks too, never clear a form on a server
500; (19) light-theme glassmorphism recipe from the LAB-009 build — light
glass isn't dark glass inverted: white ~.72 opacity + blur + soft shadow
(0 20px 50px rgba(ink,.12)) does the depth-separation work dark themes get
from glow; badges need ~.85 solid-ish background to stay readable on light
glass. opencode also updated the repo's own `apex-frontend-lab/CLAUDE.md`
entrypoint doc with a full 7-step load-chain table and a lab status table —
worth reading that file directly in-repo for the canonical current-state
summary rather than relying solely on this memory file going forward.

**Delta 2026-08-25 02:55 (opencode) — CONFIRMED DONE — LAB-010 CAPSTONE +
GAPS.md honest self-audit:** LAB-010 is a 33.7KB "everything applied" build
combining shader/kinetic-type/cmd-K search+skeletons/horizontal-pan/sticky-
stack/form-states/counters/custom-cursor/ambient in one page — Zoher is
live-testing it now, feedback/fixes/retro still pending (re-verify next
cycle). New `GAPS.md`: honest P0-P3 inventory of what the lab still lacks.
**Notable for Zoher's other projects specifically: gap #9 flags RTL/Arabic
layout as completely untested** — every archetype exemplar built so far is
LTR-only, despite Arabic being an actual target market (alwazour, Ostazi).
Other gaps: no docs/event/PDP archetype exemplar yet, screenshot pipeline
instability (Brave headless broken machine-wide, Edge dump-dom flaky),
axe-core/Lighthouse not wired into the audit harness, no visual-regression
diffing between build versions. P0 priority: screenshot-pipeline stability
+ axe-core wiring (unblocks reliable verification for everything else).

**Delta 2026-08-25 03:19 (opencode) — CONFIRMED DONE — LAB-010 rebuilt as
"AXIOM v2" after Zoher's live-test critique:** 40.6KB, adds aurora
background, a custom cursor system, duotone imagery treatment, more motion
— rebuilt per direct user feedback + follow-up research, not opencode's own
initiative. No BRIEF/RETRO posted yet and no new PLAYBOOK law extracted
from this pass — bus note only. Re-check next cycle for the retro/any
promoted rule before citing specifics beyond "it was rebuilt."

**Delta 2026-08-25 (opencode) — CONFIRMED DONE per README status —
TOOLS.md shipped, the dependency arsenal:** 40+ verified libraries/tools
across 12 categories (animation/3D/components/effects/scroll/type/icons/
dataviz/forms/inspiration/dev-QA), each with a clear verdict, plus current
2026 landscape notes: GSAP is now 100% MIT-free (Webflow acquired GreenSock
Nov 2024, every plugin included), Framer Motion rebranded to "Motion" (Vue/
vanilla now first-class), Lenis is the smooth-scroll standard (~80% of
Awwwards winners), shadcn/ui is the 2026 React default. Explicitly answers
GAPS #11-13: Playwright fixes the screenshot-pipeline instability, axe-core
+ Lighthouse CI cover automated a11y/perf audits. Meta-rule stated: tools
are the LAST step — IDEA → TEMPLATES → PLAYBOOK → TECHNIQUES → *then* pick
the cheapest tool, never tool-first. This is directly useful reference for
any Claude-side build that outgrows the repo's zero-dep-by-default stance.

**Delta 2026-08-25 (opencode) — CONFIRMED DONE — P0 verify harness shipped,
GAPS #11/#12 CLOSED:** `scripts/verify.mjs` (Playwright + axe-core +
pixelmatch as lab-root devDependencies only — build pages stay zero-dep).
`npm run verify -- "LAB/<id>/index.html"` runs a deterministic capture
chain (fonts.ready → settle → lazy-load scroll → height-stable poll →
discard warm-up shot → real captures), checks stability via pixelmatch
(≤0.05% diff pass), and runs axe-core the same pass with a report.json +
exit-fail on critical/serious violations. This fixes the previously-flaky
Brave/Edge headless screenshot problem outright — LAB-009/010 now hold at
0.000% diff. **Real violations already found and filed** (fix is a
separate lane, not yet applied): LAB-009 has 37× color-contrast +
heading-order + landmark-one-main + region(31); LAB-010 has 13×
color-contrast + 1× scrollable-region-focusable. This is a genuinely usable
verification tool now — worth reaching for on Claude-side frontend builds
too, not just opencode's labs. Next per GAPS priority: fix the filed
violations, then P1 (docs/PDP exemplar, GLB viewer, RTL/Arabic — the
gap most relevant to Zoher's other projects).

**Delta 2026-08-25 (opencode, evidenced by verify/report.json — no bus DONE
posted yet, treat as confirmed via hard artifact) — a11y violations fixed
across LAB-009/010, LAB-011 docs exemplar shipped:** re-ran verify reports
show LAB-009 (was 37 violations) and LAB-010 (was 14) now both at **0
violations, stability pass true**. New `LAB/011-docs/` — the docs/knowledge-
base archetype exemplar (GAPS #1, previously unbuilt) also verified clean
(0 violations, stable). GAPS priority queue should now read: P1 remaining
= PDP exemplar, GLB viewer (LAB-002), RTL/Arabic (#9, still the one most
relevant to Zoher's other projects — not yet addressed). Re-check GAPS.md
directly next cycle to confirm these are struck off, since no bus note
confirmed it explicitly this round.

**Delta 2026-08-25 (opencode) — CONFIRMED DONE via bus entry — a11y fixes
finalized + LAB-011 docs shipped (GAPS #1 closed) + verify-gate now a hard
law, law count 71:** Concrete fixes: LAB-010 lifted a faint token to
#85829c, flipped button text to near-black on violet, made palette/pan
regions focusable; LAB-009 added a main landmark, fixed logo-wall/word-scrub
contrast, demoted a widget heading to styled `<p>`, lifted whites to .86 —
both now PASS at 0% diff, zero violations. LAB-011 docs archetype (22.5KB):
3-pane stack, autocomplete search, clipboard-copy code blocks, scroll-spy
TOC. **The harness caught a real defect on its own first use** — LAB-011
v1 failed its own new gate (contrast/heading-order/link-in-text-block) and
was fixed before ship, proof the loop works as designed. New laws 65-67
(loading-state decision tree by latency, search-UX gates, cognitive-
accessibility defaults) and 68-71 (nav labels aren't headings, inline links
need non-color affordance, dark code-block contrast ≥4.5:1 incl. comments,
and **law 71: verify-gate is now mandatory — every build must PASS `npm
run verify` before being called done**). Law count now 71. GAPS.md P1
remaining: PDP exemplar, GLB viewer (LAB-002), and **RTL/Arabic build (#9)
— still the gap most relevant to Zoher's Arabic-market projects, still
untouched.**

**Delta 2026-08-25 (opencode) — RTL/Arabic research landed (RESEARCH.md
#23, wave-6), directly relevant to Zoher's projects — NOT yet promoted to
a law or built as a LAB exemplar, GAPS #9 still open:** the research is
solid and ready to use today even without a lab build: logical CSS
properties (`margin-inline-start` etc, full browser support since 2023)
handle the whole RTL mirror automatically — physical properties silently
break; never letter-space or uppercase-transform Arabic (breaks cursive
glyph joining); body line-height 1.7-1.9 (taller ascenders/descenders);
2026 font tiers named (IBM Plex Sans Arabic for product, Cairo for display,
Tajawal friendly, Noto Kufi Arabic headlines-only — avoid legacy Tahoma/
Segoe UI Arabic); wrap Latin/numbers in `<bdi>` at bidi boundaries (the
"comma jump" bug); logos/wordmarks usually stay LTR even in RTL layouts;
Arabic UI chrome grows ~20-25% taller than English text, budget for it in
layouts. RESEARCH.md now 23 categories total (also added #20 loading-state
decision tree, #21 search UX, #22 cognitive accessibility — all already
promoted into laws 65-67, unlike RTL which is still just research).
**Directly usable right now for any alwazour/Ostazi Arabic-facing work,
independent of whether opencode ever builds a LAB exemplar.**

**Delta 2026-08-25 (opencode) — CONFIRMED DONE — LAB-012 Arabic RTL shipped,
GAPS #9 and #15 CLOSED, laws 72-75, law count now 75:** ~19KB single file,
full SaaS archetype stack in Arabic (`dir=rtl lang=ar`) — nav, hero with
live queue panel, reversed marquee, 5-cell bento incl. an LTR terminal
island, dark metrics, testimonial, 3-tier pricing, FAQ, gradient CTA. Cairo
900 display + IBM Plex Sans Arabic body, 100% logical properties, zero
letter-spacing on Arabic, `<bdi>` around all Latin/number tokens. Verified
via the real harness — PASS at 0.000% stability, axe clean after fixing v1
catches (a real dead-selector bug `.rec .tier` vs `.tier.rec` that rendered
the recommended pricing tier gray-on-dark; contrast gates caught it as a
bug, not a style issue). New laws 72-75: logical properties mandatory in
any layout that may ever mirror, Arabic typography rules (no letter-
spacing, line-height ≥1.7, `<bdi>` wrapping, one digit system), compound
selectors must match real DOM order, every h3 subtree needs an accessible
h2. **This closes the gap flagged repeatedly as most relevant to Zoher's
Arabic-market projects (alwazour, Ostazi) — a real, verified Arabic
archetype example now exists in the repo to reference directly.** Next per
opencode: PDP exemplar (#3) or LAB-002 GLB viewer (#4).

**Delta 2026-08-25 (Claude, this session) — first Claude-authored
contribution to the repo, not just monitoring: live WebSearch verification
pass on drift-prone technical claims, per Zoher's direct request to also
upgrade the lab via web research, not only track opencode's output.**
Bounded first round (4 targeted searches, not all 75 laws/23 categories —
impractical in one pass, framed as incremental/ongoing): confirmed
scroll-driven animations are unflagged Chrome/Edge 115+ and Safari 26+ but
**Firefox is still behind a flag as of Firefox 152** (June 2026, Interop
2026 priority) — the repo's `@supports`+fallback requirement covers a real
current gap; View Transitions cross-document (MPA) has Chrome/Edge/Safari
18.2+ parity but Firefox native support is still in development; WCAG 3.0
confirmed still a Working Draft (final Recommendation not before 2028, WCAG
2.2 remains the correct target — no repo change needed); Core Web Vitals
thresholds (LCP<2.5s/INP<200ms/CLS<0.1) confirmed unchanged and accurate.
Wrote findings as `RESEARCH/2026-frontend-research.md` WAVE 7 + PLAYBOOK.md
law 76 — additive/correction-only, never rewrote opencode's existing text,
per the repo's own append-only house rule. Posted a Session Bus claim/DONE
so opencode sees a Claude session touched the shared repo. **This is the
start of an ongoing practice, not a one-time completion** — future cycles
of the monitoring loop should periodically run a similar bounded
verification pass (rotating subset) rather than attempting full 75-law
coverage at once.

**Delta 2026-08-25 (Claude, this session) — WAVE 8 large-batch pass,
~12 searches across 8 clusters, per Zoher's explicit request to go
broader and also source ready-made template/component/animation/3D
libraries per category, not just re-verify:** Wrote consolidated findings
to RESEARCH.md WAVE 8, TOOLS.md new sections M/N/O, PLAYBOOK laws 77-80.
Key results:
- **CSS gap-fill**: container queries + `:has()` are Baseline-safe (2023+,
  no feature-detect needed) and unused anywhere in this repo — real
  opportunity, not yet adopted (law 77).
- **E-commerce/agentic commerce** (directly relevant to alwazour): AI
  shopping agents (OpenAI Operator, Gemini, Perplexity Shopping, Amazon
  Rufus) parse JSON-LD Product schema, not prose — concrete mechanism
  behind the vague "agentic readability" claim already in the repo (law
  78). Sharper PDP numbers: 5+ reviews = 270% conversion lift (380% on
  $100+ items), AI chat ≈4x conversion (3.1%→12.3%).
- **Ready-made asset marketplaces, license-verified** (new TOOLS.md M/N/O):
  component blocks (shadcn.io 6,000+ blocks, Magic UI, Aceternity,
  ReactBits, Flowbite), motion assets (LottieFiles, Rive), and — notably —
  **Poly Haven (CC0 3D models) directly unblocks GAPS #4, the LAB-002 GLB
  viewer that's been queued since the repo's start.**
- **Self-correction found**: law 8's icon-library ranking (Phosphor first)
  traced to a vendor's own self-published "best icon libraries" ranking —
  flagged as house preference, not verified consensus (law 80).
- Form UX: inline validation should debounce ~500ms after typing stops
  (law 79). Dashboard: command palette now standard past ~10 features;
  data-density philosophy shifted to prioritize-first, not more-widgets.
- Confirmed-unchanged: OKLCH support, GSAP/Motion library landscape,
  motion-token industry validation, waitlist/portfolio CRO framing.

Law count now 80, RESEARCH.md at 24 major sections (WAVE 8 folded in).
**This is now an established ongoing practice** — the monitoring loop
should keep running a bounded WebSearch batch periodically (not every
cycle, but regularly) against a rotating subset of laws/categories,
writing additive findings the same way, never rewriting opencode's
existing text.

**Delta 2026-08-25 (opencode) — CONFIRMED DONE — real user critique fixed
LAB-012 (was NOT actually responsive), new FEATURES.md 20-category matrix
+ COLOR-SCIENCE.md, laws 81-82, and a live example of the append-only
convention holding under concurrent cross-tool edits:** Zoher live-critiqued
LAB-012 as "not responsive / no feature checklist / colors not accurately
combined" — real gaps a single-viewport verify pass had missed. Fixed:
verify.mjs now takes `--viewports all` (390/820/1440 with touch flags);
LAB-012 got a genuinely operable hamburger nav (was hidden links = dead
nav on mobile), badge/panel overlap and avatar-row wrap fixed, scroll-
driven reveals added. New `FEATURES.md`: 20-category capability matrix
scored per lab (responsive/mobile-nav/touch-targets/scroll-anim/forms/
a11y/color/dark-mode/RTL/3D/data-viz/keyboard/etc) — immediately useful,
it surfaced that NO lab has a dark-mode variant except LAB-010, and only
LAB-012 has RTL coverage. New `COLOR-SCIENCE.md`: OKLCH ramp recipe,
computed-not-eyeballed contrast, dark-mode-is-retint-not-invert, and a
business-type→palette table with WHY per industry — **includes a "MENA/
Arabic-first" entry (deep cobalt/emerald + warm sand + gold, warm low-
glare canvases improve Arabic-script legibility) directly relevant to
alwazour/Ostazi.** Applied to LAB-012 immediately (fixed an accent-
monopoly violation — lime demoted from metrics, ok-green darkened).
**Coordination note:** opencode independently added laws 76-77, collided
with Claude's own 77-80 from the same day, self-caught it, and renumbered
to 81-82 with an inline note explaining why — the shared append-only
PLAYBOOK.md survived concurrent editing from both tools without conflict
or data loss, proof the house convention works in practice.

**Delta 2026-08-25 (opencode) — CONFIRMED DONE — LAB-002 GLB viewer shipped,
GAPS #4 CLOSED (the oldest gap in the whole repo, queued since 2026-08-24),
law 83, and opencode sent an explicit reciprocal ack:** LAB-002 uses
model-viewer 4.0 + the Khronos CC-BY helmet test model (not Poly Haven
specifically, but the same principle — a real, license-clear GLB), with
RM-aware auto-rotate, progress slot, orbit buttons, aria-pressed swatches.
New law 83: live-WebGL pages need a canvas diff tolerance (`--max-diff 1`)
instead of the standard 0.05% gate, since desktop anti-aliasing jitter
(~0.77%) is inherent, not a regression; auto-rotate must still respect
reduced-motion since it's JS-driven and invisible to CSS freezes.
**opencode posted an explicit ack** reading both of Claude's WAVE 7/8
passes, specifically praised the Firefox-152 flag-gating catch, and
confirmed the law-renumbering reconciliation (1-80 shared/Claude, 81-82
opencode's responsive/color laws, 83 this WebGL law) — this is genuine
two-way cross-tool coordination on a shared file, not just Claude
one-way-monitoring opencode. Next per opencode: PDP exemplar (#3), enabled
directly by Claude's law 78 (JSON-LD Product schema for agentic commerce).

**Delta 2026-08-25 (opencode, unconfirmed — no RETRO/bus DONE posted yet):**
`LAB/013-ostazi-mock/` appeared, verify report shows PASS clean on both
viewports (0% diff, 0 violations), but no BRIEF/RETRO exists to explain
what archetype/technique it's testing. Name suggests an Ostazi-styled
exercise, but this is inside the apex-frontend-lab sandbox, not the actual
Ostazi codebase (confirmed happening in a separate repo per other
sessions' broadcasts — TutorLink-Syria/fix-group-session-payments/
zoher-9c). Don't cite specifics until a RETRO lands.
