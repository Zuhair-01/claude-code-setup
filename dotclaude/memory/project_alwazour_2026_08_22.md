---
name: project-alwazour-2026-08-22
description: "alwazour session 2026-08-22 — search/catalog-dedup/racks-cabinets shipped and live, AI video-gen explored for the cable-coil hero via new skill, not yet wired in."
metadata: 
  node_type: memory
  type: project
  originSessionId: 0e1fa28e-23ba-4ea5-9b19-7c5dbf7c72c8
  modified: 2026-08-25T00:25:30.387Z
---

Big session on `C:\Users\Zoher\Desktop\Empire_Base\alwazour` (real product
catalog, alwazour.vercel.app). Real fixes shipped+live: keystone photo
collision, search broken on 8 pages, catalog length-variant dedup (202→154
cards, plus a real regex bug that silently hid 7 SKUs' alternatives), a
real bug on the flagship `office-network` solution (PDU offered as a
cabinet, cable-management matched zero products ever), new `racks-cabinets`
solution backed by real inventory, cabinet-door scroll animation, topology
diagram icons, mono 6.35mm connector fix. Full detail in the Handoff Log
entry dated this same day.

**Why:** Zoher wants this catalog to be genuinely accurate — real data,
real photos where possible, honest technical illustration where not, no
fabricated specs. Recurring bug pattern this session: two products sharing
identical recorded specs while being physically different things (keystone
jack vs plug box, male vs female SMA, mono vs stereo jack, PDU filed under
cabinets). Check for that pattern before trusting a new match/filter.

**AI video-gen thread — SUPERSEDED, see [[project_alwazour_hero_video_2026_08_25]]:**
this session's coiled-cable clip was replaced 2026-08-25 by a 3-shot
cinematic sequence (RJ45 macro → server rack → office, Google Flow/Veo)
that IS wired into the live site (`motion.ts`). Kept here only for the
`ai-video-prompt-engineering` skill origin story and the still-valid
`[[feedback_user_drives_ai_gen_tools]]` rule; don't act on the old
"not yet wired in" / "Flow credits exhausted" state, it's stale.

**How to apply:** Before touching alwazour again, read this file's linked
Handoff Log entry for the exact next step. Don't re-verify already-shipped
fixes from scratch — they're live, confirmed. Don't drive Flow/Veo directly
next time without being told to.
