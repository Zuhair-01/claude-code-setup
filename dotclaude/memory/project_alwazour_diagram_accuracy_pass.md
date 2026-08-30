---
name: project-alwazour-diagram-accuracy-pass
description: "alwazour diagram-accuracy exhaustive pass — 202/202 SKU programmatic sweep (family cross-check + photo-hash dedup) complete 2026-08-24, zero bugs remaining at that layer, commit ab1cc97 baseline."
metadata: 
  node_type: memory
  type: project
  originSessionId: 3a75539a-5a96-4d11-807d-25b0ebc83c5f
  modified: 2026-08-24T20:16:03.897Z
---

Separate thread from [[project_alwazour_2026_08_23_sweep]] (that one was the earlier photo-duplicate
sweep; this one is the "diagram-accuracy" pass — content/self-contradiction/family-mismatch bugs in
`alwazour`'s per-SKU product-page diagrams, not just photos). 14 real bugs found+fixed across a first
representative-sample pass (commit `ab1cc97`), then Zoher asked for exhaustive SKU-by-SKU coverage
instead of sampling.

**Method that worked, reusable for future catalog sweeps**: don't manually screenshot 640 pages one
by one — script it. (1) group every SKU by `enrichment.json`'s `_family`, read every `name_en` per
group side-by-side to catch a product that doesn't belong (this is exactly how the
`signal-converter`/`keystone` bugs were found earlier). (2) MD5-hash every real product photo
(`is_real_photo=true` in `images.csv`) and group by hash — any SKU sharing a photo with a
*visually-different* sibling (different gender, depth, color) is a real bug; sharing among
genuinely-identical siblings (same product, different cable length) is the legitimate "family photo"
pattern and not a bug. (3) for any `visual_type` group that isn't the default (`connector`/`switch`/
generic templates applied to non-obvious products), read the full rendered HTML text for
self-contradiction, not just diagram-vs-photo.

**Completed 2026-08-24**: both catalog slices (cables/extenders/surveillance/telephony = 107 SKUs,
accessories/cabinets/networking = 95 SKUs, 202 total) swept this way — zero new bugs found in either.
Honest placeholder photos (5 PSU + 4 cabinet SKUs, all correctly flagged `is_real_photo=false`) are a
known, non-blocking, still-open gap — not a bug, just unsourced real photos.

**Explicit scope limit**: this method is exhaustive at the family-consistency/photo-hash/text-
self-contradiction layer, NOT a literal browser-rendered screenshot of all 640 pages. A purely-visual
defect that only shows up live in a rendered SVG (not reflected in the underlying data) would not be
caught by this method — if Zoher wants that layer too, it's a fresh ask (Playwright screenshot pass),
not a re-run of this one.

**Why**: same standing goal as [[project_alwazour_2026_08_23_sweep]] — Zoher wants the catalog
genuinely, not just visually, accurate; this session's explicit ask was "exhaustive, not sampling."

**How to apply**: if asked to continue/verify alwazour diagram accuracy again, don't restart from
scratch — check the Handoff Log's "BOTH slices now exhaustively swept" entry first, and if a fresh
pass is warranted (new SKUs added, or Zoher wants the visual-only layer), reuse the 3-step method
above rather than re-deriving it.
