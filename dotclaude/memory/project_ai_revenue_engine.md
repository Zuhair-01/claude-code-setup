---
name: project-ai-revenue-engine
description: "7-repo AI business portfolio (Pipecat/Cline/Postiz/AnythingLLM/CrewAI/browser-use/Firecrawl) turned into productized offers, bundled as \"AI Revenue Engine\" for local businesses"
metadata: 
  node_type: memory
  type: project
  originSessionId: a39b4d8b-85b5-4d23-af73-420ee92f601e
  modified: 2026-08-20T00:16:03.614Z
---

7 GitHub repos cloned and productized as named offers under [[project_empire_base_agency]]'s
5th initiative. Codenames: RingPilot (Pipecat, AI phone receptionist), SiteForge (Cline,
AI-built sites), PostPilot (Postiz, social scheduling), VaultMind (AnythingLLM, private
knowledge assistant), CrewOps (CrewAI, orchestration), TaskRunner (browser-use, browser
automation), LeadForge (Firecrawl, lead scraping).

Full plan: `Empire_Base/Second_Brain/Workflow/10 - Projects/AI_Revenue_Engine/MASTER_PLAN.md`
Repos: `Empire_Base/external-repos/ai-business-systems/{7 dirs}`

**Why**: user wants these NOT sold individually as repo wrappers but combined into a vertical
AI operating system for local businesses (lead gen → sales → delivery → ops → recurring
revenue), bundled setup $5k-12k + retainer $1.5k-4k.

**How to apply**: postiz + firecrawl are AGPLv3 — never fork/modify their core, only call via
API or run self-hosted unmodified, to keep our proprietary layer clear of copyleft. Build
order is NOT parallel: LeadForge → VaultMind → RingPilot → SiteForge → TaskRunner → PostPilot
→ CrewOps → package+sell (see MASTER_PLAN.md phase 0-8). User's wifi is unreliable for large
git clones — use curl zip-archive downloads instead (GitHub archive endpoint does not support
resume, so a failed download restarts from zero).

**2026-08-20, VaultMind MVP built for real:** picked next per the plan's own
build order (only unstarted phase needing zero credentials from Zoher).
Fixed a real bug first — the AnythingLLM container's `STORAGE_DIR` had been
mangled to a Windows path by git-bash's automatic path conversion in an
earlier session (classic MSYS gotcha, same family as the `$$` pid issue in
[[project_gpu_lock_system]]), root-caused via `docker inspect` +
`docker-entrypoint.sh`, fixed at the `.env` source, recreated with
`MSYS_NO_PATHCONV=1`. Wired LLM+embeddings to local Ollama (`llama3.1:8b` +
`nomic-embed-text`, already running on this machine per
[[project_minimax_h3_local]]'s Ollama fleet) — zero API cost. Generated a
real API key via AnythingLLM's own `/api/system/generate-api-key` (valid
because single-user mode has no `AUTH_TOKEN`/`JWT_SECRET` set — read the
source instead of guessing, same pattern as the Postiz registration lesson
above). Ingested `growth-os/INDEX.md`+`README.md` as guinea-pig docs,
verified a real grounded RAG answer, created and tested a real embed widget
(`/api/embed/<uuid>/stream-chat` streams correct sourced answers, no key
exposed client-side). Full writeup + reuse steps for a real client:
`growth-os/vaultmind/README.md`. **Honest gap**: never visually confirmed
in an actual browser — Chrome extension wasn't connected this session.
Said so explicitly rather than claiming full completion; API-level
verification (script serves, chat streams correctly) covers function, not
cosmetic rendering. Overlap confirmed at same time: Firecrawl (LeadForge)
and Postiz (PostPilot) already had self-hosted infra live from
[[project_growth_os_registry]]'s earlier work, just not fully productized
per this plan's own MVP definitions (no lead-source config/CSV for
Firecrawl, no client OAuth connected for Postiz).

**2026-08-20, LeadForge finished + session pivoted away:** Built
`growth-os/leadforge/leadforge.py` — real Firecrawl-backed scraper,
dedupes by URL, writes CSV per business (never writes to `leads.yaml`
directly, a prospect ≠ a qualified lead). Tested live against real URLs
already sourced in each project's `evidence.md` (opus.pro/klap.app for
Kyros, scaanme.com for Ostazi) — both businesses have real prospect CSVs
now. Started TaskRunner (browser-use + ChatOllama, free/local) next but
Zoher called it token-wasting mid-install and said move to a different
project — stopped there, `pip install browser-use playwright` may still
be running in background, harmless, not worth checking on.
**Session-end state for this thread**: LeadForge + VaultMind are real
finished MVPs. RingPilot stays blocked (needs Twilio/Cal.com from Zoher).
TaskRunner/SiteForge/CrewOps/full PostPilot are still open but
deprioritized — Zoher chose to switch projects rather than keep pushing
phase-by-phase. Don't resume this thread unless he brings it up again.
