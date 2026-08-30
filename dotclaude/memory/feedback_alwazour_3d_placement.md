---
name: feedback-alwazour-3d-placement
description: Where and how the alwazour R3F/GLB product experience must be placed and detailed — corrected after a wrong first attempt.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 972696f7-ece3-4ff5-8a34-565c637cdaa2
  modified: 2026-08-23T11:38:39.984Z
---

Two corrections from Zoher after a first (wrong) integration attempt on the alwazour
Product Technical Experience Engine ([[project_alwazour_2026_08_22]], merged into
[[alwazour-product-visualization]] skill §2.5):

1. **The 3D/scroll experience replaces the existing scroll-story diagram slot
   (`pv-conn-art`/`pv-split-art` inside the site's existing `pv-scene`/`stage-item`
   scroll sections in `product-visuals.ts`'s `anatomyScenes()`), never the hero product
   photo.** The real photo stays where it already is, untouched, further down the page
   as a simple reference image — it is not competing space with the 3D canvas. Don't
   inject a canvas above/before the hero `<figure>`.
2. **Placeholder/fallback geometry must show real, recognizable technical detail**, not
   a plain box or cylinder stand-in. For a known connector standard (e.g. HDMI Type-A:
   19-pin, trapezoidal metal shell — a public mechanical spec), model the real
   distinguishing shape (shell + contact block + strain-relief boot) even without a
   generated GLB yet — this is "DEFINITIONAL" tier per the skill's confidence-tier
   naming, not a guess, so it's fair game before a real per-SKU GLB exists.

**Why:** the whole selling point of this build is "real accurate showcase and in-depth
technical detail" (Zoher's own phrase) — a plain cylinder or a canvas stacked over the
real photo reads as decoration bolted onto existing space, exactly the "decorate, don't
explain" failure the visualization skill's governing principle forbids.

**How to apply:** every future scene/component for this pipeline goes into the site's
existing scroll-scene slots (reuse the `--p`/`stage-item` scroll mechanism already
driving the SVG version there, don't run a second competing GSAP ScrollTrigger over the
same section unless there's a real reason), and every placeholder mesh should be built
from the real physical standard for that connector/material, not a generic primitive.
