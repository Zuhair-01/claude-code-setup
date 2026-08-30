---
name: project-alwazour-technical-instagram-strategy-2026-08-29
description: "الوزور التقني (client, not the studio) Instagram content strategy — researched via ChatGPT, saved to vault"
metadata: 
  node_type: memory
  type: project
  originSessionId: 15b45b39-87d9-40ee-aeb1-bc47b585b4db
  modified: 2026-08-30T18:37:03.786Z
---

Researched and wrote a full Instagram content strategy for **الوزور التقني** (the technical
supplier client — cables/networking/electronics, live catalog at alwazour.vercel.app), distinct
from Alwazour Studio's own social plan ([[LANE_B_SOCIAL]]). Used ChatGPT web-browsing to research
how top-tier global B2B/technical brands (Fluke Networks, Panduit, Belden) grow on Instagram, plus
a live pass over the actual catalog.

**Core finding:** technical B2B brands use Instagram as a discovery+validation layer, not a
prettier catalog — content teaches, product is the answer. 4 pillars: Expertise 40% / Supply 30% /
Project-enablement 20% / Proof 10%. Full carousel templates, reel concepts, caption formula
(PROBLEM→FACT→APPLICATION→CTA), WhatsApp funnel structure, and a 14-day launch calendar are
written out in full at
`Second_Brain/Workflow/10 - Projects/Alwazour_Technical_Upgrade/INSTAGRAM_CONTENT_STRATEGY.md`.

**Why:** Zoher wants to start posting real products deliberately, not generic template content —
asked to route research through ChatGPT with the live site link + competitor research first.

**Data catch (resolved):** product count is **138** (verified live 2026-08-29); the earlier "202"
ChatGPT figure was wrong. Catalog treated as real per Zoher.

**2026-08-30 expansion:** backlog completed in the same doc — §17 (3 story sets + "ما لقيت القطعة"
sourcing carousel + Reel 4), §18 ("قطعة اليوم" 5-SKU single-post series), §19 (4-week posting
schedule + live tracker). All new copy uses only SKUs already verified in §14/§16, no new catalog
claims. Published artifact (d4906cd0) upgraded to match — now 14 ready pieces + schedule section.
**Arabic-only PDF** generated for the client/videographer:
`Alwazour_Technical_Upgrade/الوزور_التقني_استراتيجية_انستغرام.pdf` (16pp, source
`instagram_strategy_ar.html`, rendered via node Playwright — `scratchpad/render_pdf.js`). Nothing
published to Instagram — all 14 pieces await Zoher's sign-off.

**2026-08-30 slides BUILT + RENDERED:** 44 IG slides hand-built as HTML/SVG and rendered to PNG
via Playwright (NOT Gemini — perfect Arabic, zero fabrication, pixel-exact). Client 18 (first-3:
W1-P2/W1-R1/W3-P5) in `alwazour/design-refs/social/render/`; studio 26 (grid order, opens Post 9)
in `alwazour-studio/design-refs/social/render/`. **Full system doc:**
`Alwazour_Technical_Upgrade/slides/SOCIAL_VISUALS_DOCUMENTATION.md` (pipeline, file map, decisions,
corrections, publishing status — READ THIS FIRST). Review deck: `slides/REVIEW.html`. Sources:
`slides/client.html`, `Alwazour_Studio/slides/studio.html`; rebuild `node render.mjs <html> <out> --scale 2`.
Studio Dania/Kyros content corrected 2026-08-30 (she's a booking system not a store; project 04 = كايروس).
W3-P5 carousel STAGED in the IG dialog (alwazzour_tech), awaiting Zoher's Share click.

**2026-08-30 visuals:** both brands now have `GEMINI_VISUAL_PACK.md` **v2** (client:
`Alwazour_Technical_Upgrade/`, studio: `Alwazour_Studio/`) — every slide's Arabic verbatim from
the SMM `chatgpt_review_raw.md`, plus per-brand negative-prompt blocks + numbered generation
runsheets + Arabic-verification gates. `Alwazour_Technical_Upgrade/CHATGPT_VISUAL_PROMPT_SHARPENING.md`
is the ready paste for an optional ChatGPT art-director pass (Zoher pastes → pastes reply back →
Claude merges; never browser-extract — [[feedback-chatgpt-consult-paste-workflow]]). Renders save
to `<repo>/design-refs/social/render/`. Client first-3 = W1-P2 / W1-R1 / W3-P5; studio grid opens
Post 9, first-3 = 9→2→3. Gemini gen is Zoher-driven ([[feedback-user-drives-ai-gen-tools]]).
State tracked in Handoff Log "2026-08-30 ~16:00 (zoher-1c)".

**How to apply:** Before generating actual carousel/reel visuals for this account, check
`INSTAGRAM_CONTENT_STRATEGY.md` + the v2 `GEMINI_VISUAL_PACK.md` first — templates, pillar ratios,
identity, and exact slide copy are already decided. Don't merge this account's content with
Alwazour Studio's (agency) social plan — different entity, different audience (end customers vs
business-owner clients), different visual identity (client = LIGHT navy/amber blueprint; studio =
DARK blue/gold).
