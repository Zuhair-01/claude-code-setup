---
name: project_alwazour_hero_video_2026_08_25
description: "alwazour homepage hero video — DONE, live: 3-shot cinematic Flow sequence (RJ45 macro -> rack -> office), wired into motion.ts, verified in-browser 2026-08-25."
metadata: 
  node_type: memory
  type: project
  modified: 2026-08-25T00:26:01.867Z
  originSessionId: 957baca7-ea79-41d4-8419-07387a23e28c
---

Supersedes [[project_alwazour_2026_08_22]]'s old coiled-cable clip. Zoher rejected an
initial Claude-Design photoreal-3D attempt (tool can't do photoreal) and a first
Flow shot ("cable zoom-in, bad — something general and much more than just a
cable"). Rewrote prompts to full-scale-journey-per-clip (not static macro),
generated 3 shots on Google Flow (Veo 3.1-Lite, free tier): RJ45 macro → pull
back through cabinet → office space → brand-plate wall. Stitched with 0.5s
crossfades + fade-to-black loop wrap (23s total, CRF 26, 2.9MB). Deliberately
did NOT bake "ALWAZOUR" text into the video (Veo unreliable at exact text) —
turned out unnecessary anyway since the site's real hero text is a persistent
DOM overlay on `.hero-bg-video-wrap`, not a scripted reveal.

**Wired in:** `src/site/motion.ts`'s `VIDEO_MOTION_SCRIPT` (`bg.src` one-liner),
file at `data/real/video/cat6-cable-hero-cinematic.mp4`. Raw source shots kept
at `docs/hero-video-source-shots/` (not served). Verified end-to-end in a real
browser (local server + claude-in-chrome), confirmed no conflict with a
concurrent peer session's frontend redesign on the same `home.ts`/`tokens.ts`.

**Build-pipeline gotcha:** `catalog-build.ts`'s video-copy step can't handle a
subdirectory under `data/real/video/` — only drop the single served file there.

**Not committed/pushed yet** as of 2026-08-25 — waiting on the peer redesign
session to finish, then a coordinated multi-session compare-and-push (Zoher's
explicit ask, so every session's local changes go live together, not just one).

**How to apply:** if hero video ever needs revisiting, the prompt doc is
`alwazour/docs/hero-video-flow-prompts.md` (note: slightly stale, describes an
earlier 6-shot plan vs. the 3-shot version actually shipped) and 23 curated
Pinterest refs are at `alwazour/design-refs/pinterest/hero-cinematic-2026-08-25/`.
