---
name: reference-gemini-free-tier-media-gen
description: "Free image/video generation via Gemini API (AI Studio key, not GCP/Vertex) — Imagen + Veo"
metadata: 
  node_type: memory
  type: reference
  originSessionId: fe47de95-1ac3-4241-8bd1-1ef0b4f49cc0
  modified: 2026-08-27T17:08:37.433Z
---

Gemini API has a genuinely free tier via **AI Studio** (aistudio.google.com) —
no GCP project or billing account required, unlike Vertex AI. Get a key at
aistudio.google.com → "Get API key". Covers:
- Imagen (image generation)
- Veo (video generation)
- Gemini multimodal text/chat

Free tier is rate-limited (not for volume), fine for testing/prototyping.
Use the `gemini-api` skill (installed via [[reference_google_skills_marketplace]])
for SDK usage patterns once a key exists.

**Why:** Zoher wants free-tier image/video gen (2026-08-27), confirmed he'll
get the API key himself (account signup is user-driven, see
[[feedback_user_drives_ai_gen_tools]]) rather than Claude attempting GCP
billing setup.

**How to apply:** when a project needs quick/free image or video generation
and existing tools (Flow/Veo via browser, muapi.ai, Higgsfield) don't fit,
check if a stored AI Studio key exists before defaulting to those — this is
an additional free option, not a replacement.
