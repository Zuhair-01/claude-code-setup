---
name: project_alwazour_studio_cinematic_scroll_2026_08_30
description: "alwazour-studio 2026-08-30 'finish it fully' run — Dania/Kyros/pricing/Start-Project rebuild + full cinematic scroll layer (GSAP, in BaseLayout) + leads-DB timeout fix. HEAD 128e1d1. Full write-up in vault 20-Areas/Multi-Session Run — Alwazour 2026-08-30.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: fd7e1ddd-394c-4535-8c6d-c4f4e66a6843
  modified: 2026-08-30T13:28:44.731Z
---

alwazour-studio agency site (`Empire_Base/alwazour-studio/`, Astro, deploys from master).
2026-08-30 session: "finish it fully" run alongside peers zoher-5a (showcase rebuild) and
zoher-1c (الوزور التقني IG). All coordinated via SendMessage, no collisions.

## What shipped this session (mine)
- Dania work-card was wrong (described as a cosmetics store) → rewrote as makeup-artist
  portfolio + booking system, AR/EN. Moved ecommerce→webapps, dropped empty ecom Work filter.
- Project status badges live/production/private (later all set to "live" per Zoher).
- Pricing "$300" → "Starter from $350; larger by scope". Tiers (zoher-db assumed):
  Starter $350–700 / Growth $1,200–2,500 / System $3,000+. NOT yet synced to Lead_Gen docs.
- Real live URLs wired; **project 04 renamed Clip Platform → Kyros** (slug stays clip-platform).
- Start-Project rebuilt into a 5-step consultation (type cards w/ CSS previews → business →
  "how will we know it worked?" success metric → contact → review-with-edit-jumps).
- **Cinematic scroll layer** (scroll spec from ChatGPT, saved `.asset-prep/SCROLL-EXPERIENCE-SPEC.md`):
  - Vertical scroll-progress rail, right edge, 6 sections, ≥1280px, self-removes off-homepage.
  - Hero scroll choreography (content drifts up + fades to a floor as hero scrolls away).
  - **gsap 3.15 is now a dependency.** Process = GSAP-pinned timeline scrub; CTA space-glow
    scale+brighten on enter. In BaseLayout's 2nd `<script>`, guarded by `prefers-reduced-motion`
    + `max-width:1023px`; sets `data-cinema="on"` so the vanilla process line-fill stands down.
  - Work horizontal-scroll pin was tried and **reverted** — RTL translateX + pin timing too
    fragile for ~5 cards. Native scroll-snap filmstrip kept.

## Gotchas learned
- **Astro scopes `<style>` selectors** — styles for elements created in JS (`.review-row`,
  `.chip`, etc.) get dropped. Wrap those rules in `:global(...)`.
- **Google Flow / Gemini browser automation is unreliable here** — screenshot capture throws
  a CDP `clip.scale` deserialize error and the renderer freezes on their canvas UIs. JS
  injection still works but you're driving blind. Both this session and zoher-5a hit it.
  Fix path: restart Chrome, then retry.

## Final commit set (HEAD 128e1d1, all pushed/green)
790c883 Dania fix + badges + pricing · 126ec78 Dania render + all-live + full-bleed CTA ·
0bca3b7 live URLs + Kyros rename · 4284132 Start-Project 5-step rebuild · 3074f8a scroll
rail + hero choreography · 964a689 GSAP 3.15 + pinned Process + CTA glow · 647ca4c Work
horizontal-pin reverted · 871ec73 WHY sequential focus · d3b4081 About glow parallax ·
128e1d1 `api/leads.ts` AbortSignal.timeout(8000) — paused free-tier Supabase was hanging
the RPC fetch until the function was killed; now fails fast into the existing 502.

Peers: zoher-5a shipped the showcase (filmstrip + case-study detail pages + 5th project
Open Axis, 4803cee/e34a37d/0cd8108). zoher-1c: الوزور التقني IG content, separate vault lane.

## Going-forward session protocol + full lessons list
→ `Second_Brain/Workflow/20 - Areas/Multi-Session Run — Alwazour 2026-08-30.md` and the
Handoff Log entry "2026-08-30 ~14:30". Key: `git commit -- <paths>` to scope commits in the
shared tree; clear `node_modules/.vite` after `npm i`; free-tier Supabase auto-pauses.

## Still open
Flow hero video (blocked on browser, prompt ready in `.asset-prep/STEP-19-chatgpt-audit-and-veo-prompt.md`,
`HERO_VIDEO=false` inert wiring in Hero.astro); Kyros card image (waiting on Zoher's real
Kyros Clips screenshot → `public/work/clip-platform-mockup.webp`); optional B2 polish
(About parallax, WHY sequential reveal, SectionTransition component). See
[[project_alwazour_2026_08_22]] and the Handoff Log "2026-08-30 ~12:00" entry.
