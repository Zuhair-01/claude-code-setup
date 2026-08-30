---
name: use-own-tools-before-builtin
description: "When Zoher's own stack has a tool for a task (self-hosted Firecrawl, OVERSEER skills), use it instead of a generic built-in tool"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a39b4d8b-85b5-4d23-af73-420ee92f601e
  modified: 2026-08-17T13:52:37.127Z
---

Before reaching for a built-in tool (WebSearch, WebFetch, hand-rolled logic), check whether
Zoher's own stack already has the right tool live and use that instead.

**Why**: 2026-08-17, during AI Automation Factory market research, used the built-in WebSearch
tool for competitor/pricing research while a self-hosted Firecrawl instance (LeadForge,
[[project_ai_revenue_engine]]) was running on localhost:3006 — built specifically for this kind
of scrape/research task this session. Also skipped checking whether a dedicated `market-research`
skill (present in the live skill list) or OVERSEER had a better-fit workflow first. Called out
directly: "OUR ENTIRE OVERSEER SYSTEMS exist for this."

**How to apply**: Before any research/scrape/data-gathering step, ask (a) is there a live
self-hosted service in this session/project that already does this (check docker ps / recent
work), and (b) does `python3 ~/.claude/overseer/search.py <terms>` or an already-listed skill
(e.g. `market-research`) cover it — per CLAUDE.md Rule 6 and [[feedback_overseer_library_before_hand_build]].
Only fall back to generic built-in tools (WebSearch etc.) when neither applies. This isn't just
about OVERSEER's off-context library — it includes tools/services built earlier in the *same*
session.
