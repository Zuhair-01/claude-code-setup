---
name: project-free-oss-ai-stack-research-2026-08-26
description: "Multi-session GitHub research sweep replacing paid AI tools with free/OSS, split 3-way across concurrent Claude sessions"
metadata: 
  node_type: memory
  type: project
  originSessionId: 84ee4fab-9201-433a-b1db-56acd74df066
  modified: 2026-08-26T01:22:44.097Z
---

3-way concurrent Claude session sweep (2026-08-26) researching free/OSS
replacements for paid AI tooling, per CLAUDE.md Rule 10/Rule 4-addendum.
Used the two idle peer sessions already running (zoher-a1, zoher-9d) rather
than opening new terminals.

Lanes:
- zoher-8f (this session): local LLM/agent-orchestration/RAG stack.
- zoher-a1: media-gen (TTS/video-gen/image-gen/avatar) free swaps.
- zoher-9d: dev-ops tooling + paid-dependency audit of live projects
  (clip-platform, Ostazi, alwazour, Kyros).

My lane's findings, registered as new OVERSEER skills (searchable via
`python3 ~/.claude/overseer/search.py <name>`):
- `litellm-gateway` — free self-hosted LLM proxy/gateway (MIT), replaces
  paid gateway SaaS, natural fit for Kyros if it ever routes to paid APIs.
- `lancedb-vector-db` — free embedded vector DB (Apache 2.0), no server
  process, candidate upgrade path for vault-search/turbovec if it ever
  needs disk-backed persistence at scale.
- `letta-agent-memory` — free self-hosted agent memory server (Apache 2.0,
  formerly MemGPT), real free alternative to the existing `mem0-automation`
  skill which is a paid-connector (Composio) wrapper around Mem0 cloud.
- `unsloth-local-finetuning` — free LoRA/QLoRA fine-tuning (Apache 2.0),
  2-5x faster/lower VRAM, fits the box's RTX 4060, exports to GGUF for
  Ollama serving. Replaces paid fine-tuning APIs (OpenAI, Together.ai).
- `deepeval-rag-testing` — free pytest-native RAG/LLM eval library
  (Apache 2.0, 50+ metrics, local-model judge support). Replaces paid eval
  SaaS (Braintrust/Athina) for CI-gated quality checks; the existing
  generic `evaluation`/`agent-evaluation` skills cover methodology only,
  this is the concrete free tool to run it.
- `microsandbox-code-exec` — free local rootless code sandbox (Apache 2.0,
  libkrun microVMs, no cluster/cloud, no model weights). Replaces paid
  sandbox APIs (E2B, CodeSandbox SDK) for safely running agent-generated
  code on this single machine.
- Confirmed `langfuse` skill already existed in OVERSEER (self-hosted
  LangSmith alternative) — not duplicated.

**6 OVERSEER skills + ~46 more catalog-only entries** (OCR, self-hosted
search, BI, feature flags, browser-agent frameworks, voice-AI frameworks,
data labeling, API testing clients) added to the vault note
`30 - Resources/Open_Source_Self_Host_Stack.md` after Zoher's second
redirect (2026-08-26): switch to research/catalog-only mode, no more
building — see [[feedback_no_large_downloads]] for the first redirect
(model downloads) and this note for the second (stop building entirely,
just log candidates for a later decision pass). Broadcast the mode switch
to zoher-a1/zoher-9d too. zoher-a1 is appending its own catalog rows to the
same vault file concurrently — re-read fresh before each edit to avoid
clobbering.

**Why:** none of these were installed as running services — per ponytail/
Rule 8, no live project currently needs them running today (Kyros already
works via direct Ollama calls, vault-search already works). They're
registered as OVERSEER reference skills so a future session reaches for
them instead of hand-rolling or defaulting to a paid SaaS, per CLAUDE.md
Rule 6.

**How to apply:** before adding a new LLM gateway, vector DB, or agent
memory layer to any project, check these three skills first via
`overseer/search.py` rather than building from scratch or picking a paid
option.

See [[project_kyros_orchestrator]], [[reference_vault_search_turbovec]],
[[project_overseer]]. Check the Second_Brain Handoff Log for what
zoher-a1/zoher-9d produced in their lanes — this memory only covers mine.
