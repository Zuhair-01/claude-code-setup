---
name: litellm-gateway
description: Free, self-hosted, MIT-licensed LLM API gateway/proxy (LiteLLM) — one OpenAI-compatible endpoint in front of 100+ providers including local Ollama. Replaces paid gateways (Portkey Cloud, Helicone paid tier) and hand-rolled provider-routing code. Use when a project needs to route between local Ollama models and paid APIs by cost/task, track spend, or add retries/fallbacks without a SaaS bill.
risk: unknown
source: github.com/BerriAI/litellm (MIT)
date_added: 2026-08-26
---

# LiteLLM Gateway

Self-hosted LLM proxy. Runs as a local Docker/pip service exposing one
OpenAI-compatible `/chat/completions` endpoint that routes to 100+ backends
(OpenAI, Anthropic, local Ollama, etc). MIT-licensed, free — only cost is your
own hosting (runs fine on a laptop).

**Replaces**: paid LLM gateway SaaS (Portkey Cloud tier, Helicone paid tier),
hand-written multi-provider routing/retry code.

## When to use on this box
- Kyros orchestrator (`project_kyros_orchestrator.md`) already does
  master(Claude)/worker(Ollama) — LiteLLM is the natural place to add
  cost-aware routing if a third provider (paid API) ever enters the loop, or
  to get unified spend tracking across whatever calls hit paid APIs.
- Any project juggling 2+ LLM providers benefits from one endpoint + virtual
  keys + budget caps instead of per-provider SDK calls scattered in code.

## Install (Windows, this box)
```
pip install 'litellm[proxy]'
litellm --config litellm_config.yaml
```
Config maps model names to backends (`ollama/qwen2.5-coder`, etc) and sets
budgets/rate limits per virtual key. Full config schema: docs.litellm.ai.

## Capabilities
- OpenAI-compatible endpoint for 100+ providers
- Virtual keys, per-key budgets, rate limiting
- Automatic retries/fallbacks across providers
- Request/response caching (semantic cache optional)
- Cost tracking per model/key

Pairs with [[langfuse]] for tracing what the gateway routes.
