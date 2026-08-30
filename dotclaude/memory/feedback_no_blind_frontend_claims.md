---
name: feedback_no_blind_frontend_claims
description: "Never build or implicitly claim frontend visual quality without an actual visual check (screenshot/browser) - say the limitation upfront, not as an after-the-fact caveat"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e06ce096-08c3-4f75-8dcb-581c38bc3c90
  modified: 2026-08-20T00:31:14.247Z
---

Never build out UI work, or imply it "looks good"/matches a quality bar,
without having actually seen it render. When browser/visual verification
tools aren't available (Chrome extension not connected, etc), say so
plainly BEFORE starting visual work, not tucked into a caveat after
several pages are already built.

**Why**: 2026-08-20, [[project_enterprise_suite]] session — built Flowra's
Import wizard and Dashboard with real, tested backend logic, but the
frontend visual design was only checked via `tsc`/build/curl (functional
correctness), never actually seen. Documented the gap honestly in
`PHASES.md` each time ("not visually screenshotted") but kept building
more pages anyway. Zoher had to manually screenshot the running dashboard
himself to discover it looked like a plain unstyled scaffold, not a real
product. That's the wrong order: the honest caveat should have stopped
further blind building, not just been logged as a footnote. He called it
correctly: "what the actual fuck is this frontend... our 3400+ skills
fucking useless bro" — the frustration was earned, because skill
invocations (taste-skill, ui-ux-pro-max) were used but their actual
*output* was never verified against reality before presenting it as
progress.

**How to apply**: the moment visual/browser tools are confirmed
unavailable, say it immediately and ask how the user wants to proceed
(build blind and expect a check-in soon, wait for tools, or skip visual
work) rather than continuing to build page after page on faith. If
building anyway, build ONE small piece first and ask for a screenshot
check before continuing, instead of batching multiple pages/components
before the first real look. A verified-working backend does not make an
unverified frontend claim safe — they are separate checks, and skipping
the second one is the actual failure mode here, not a smaller one.
