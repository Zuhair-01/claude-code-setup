---
name: project-alwazour-2026-08-23-sweep
description: "alwazour 2026-08-23 — HDMI regroup, then category-by-category duplicate/wrong-photo sweep (accessories, extenders, cabinets done; cables/networking/surveillance/telephony in progress or open) run concurrently across 3-4 live sessions."
metadata: 
  node_type: memory
  type: project
  originSessionId: 37ac6794-6d66-414c-8cf2-8953f475a392
  modified: 2026-08-23T19:52:29.340Z
---

Multi-session concurrent sweep of the alwazour real product catalog
(`C:\Users\Zoher\Desktop\Empire_Base\alwazour`), same method used across
categories: md5 hash scan for SKUs sharing an identical photo, cross-check
against `docs/supplier-po/row_item_img_map.json` (real supplier invoice,
matched by each SKU's `model` field) for ground truth, visually confirm
before any swap, and — when no ground truth exists to resolve a conflict —
[[feedback_no_ground_truth_downgrade_placeholder]] rather than guess.

**Shipped this pass** (commits on `master`): HDMI family regroup
(`bac8d9d`), length-display fix (`fab7c74`), sitewide quick-facts/PDP fix
by a peer session (`71f7034`), accessories category (`a0e44f5`), extenders
category (`be58a7d`), cabinets category (`e86afed`). `npm test` 58/58 held
throughout.

**Real bugs caught, not just cosmetic**: CON-XLR-F/M shared one photo
(male/female mixed up — same shape as an earlier SMA bug); PLUG-CAT6-S/
CAT7-S shared one; two SKUs with genuinely *different confirmed
`depthMm`* (CAB-9U-450 vs CAB-9U-600) shared one identical photo — the
strongest version of the "two products, same recorded data, physically
different things" pattern this catalog keeps producing.

**Open, non-blocking gaps for whoever continues**: 5 PSU SKUs and 4
cabinet SKUs now show an honest placeholder instead of a photo, pending
someone sourcing real distinct Wikimedia/PO photos. Networking(8)/
surveillance(5)/telephony(2) categories not yet swept.

**Multi-session coordination validated in practice**: 3-4 accounts
(zoher-cd, zoher-08, zoher-eb, zoher-49 on an unrelated task) ran
concurrently on the same working tree same session. Broadcast-before-start
+ broadcast-on-finish (CLAUDE.md Rule 4 addendum #4) caught a real
in-flight collision on `data/real/images.csv` before it became a bad
merge — a peer asked to hold off touching the file until the other
committed first, which worked cleanly. Also confirmed: a `dist/` rebuild
race between two sessions produces a real-looking but false "stale render"
symptom — not a bug, per Rule 4 addendum #3.

**Why:** Zoher wants this catalog genuinely accurate, not just
visually plausible — same standing goal as
[[project_alwazour_2026_08_22]].

**How to apply:** Before touching alwazour again, read the top Handoff Log
entry for exact category-sweep state and check `ListAgents` before
starting — this sweep is designed to be picked up by any account/session
without re-deriving the method from scratch.
