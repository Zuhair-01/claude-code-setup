---
name: feedback-no-ground-truth-downgrade-placeholder
description: "When two records share unverifiable data (e.g. a duplicate product photo) and no ground truth exists to say which is correct, downgrade to an honest placeholder — never guess or keep an unverifiable match."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37ac6794-6d66-414c-8cf2-8953f475a392
  modified: 2026-08-23T19:52:02.524Z
---

When a duplicate-detection scan (e.g. two SKUs sharing an identical photo)
finds a conflict but there's no ground-truth source (invoice, datasheet,
labeled photo) to say which record the shared asset actually belongs to,
the correct fix is to mark it unverified / fall back to the honest
placeholder state — not to guess, and not to leave the unverifiable claim
standing just because "it was already there."

**Why:** Established and applied repeatedly in [[project_alwazour_2026_08_23_sweep]]:
generic wall-adapter photos (5 PSU SKUs, different voltage/amp ratings) and
generic cabinet photos (2 SKUs with different *confirmed* depthMm values)
were byte-identical across physically different real products, with no PO
invoice or datasheet entry to resolve which was correct. Rather than pick
one arbitrarily or keep the status quo, all conflicting SKUs were flipped
to `is_real_photo=false`, and the site's own architecture already treats
that as the correct honest state (falls back to a diagram/spec table, not
a broken image). This mirrors the project's existing Rule 1 ("no
spec/dimension ships unless it traces to real data") — an unverifiable
photo-to-SKU match is exactly the same kind of unearned claim as an
invented spec.

**How to apply:** Any time a task involves matching/deduplicating records
by a shared asset or inferred attribute (photos, categories, tags,
merged-record fields) — if two candidate targets are equally plausible and
no authoritative source distinguishes them, don't silently pick one. Fall
back to whatever "unconfirmed/unknown" state the system already supports,
and flag the gap explicitly (in a Handoff Log entry, commit message, or to
the user) rather than resolving it with a confident-looking guess.
