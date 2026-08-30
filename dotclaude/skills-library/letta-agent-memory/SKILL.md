---
name: letta-agent-memory
description: Free, self-hosted, Apache-2.0 long-term memory server for AI agents (Letta, formerly MemGPT) — in-context memory management across sessions. Replaces paid agent-memory SaaS (Mem0 cloud tier, EverMind) for agents that need to remember across long-running or multi-session work. Use when an agent needs persistent memory beyond a single conversation without a subscription.
risk: unknown
source: github.com/letta-ai/letta (Apache 2.0)
date_added: 2026-08-26
---

# Letta (formerly MemGPT)

Self-hosted agent server with built-in long-term memory management —
originally the MemGPT paper's reference implementation. Manages what stays
in-context vs gets paged to persistent storage automatically. Free,
Apache 2.0, runs locally.

**Replaces**: Mem0 cloud tier, EverMind, other paid "agent memory as a
service" offerings. Note the existing dormant `mem0-automation` OVERSEER
skill wraps Mem0 via Composio (a paid connector layer) — Letta is the
actually-free self-hosted alternative to prefer.

## When to use on this box
- Kyros orchestrator's worker fleet (local Ollama models) currently has no
  persistent memory across runs beyond what's manually logged — Letta is the
  natural upgrade if worker agents need to recall past task outcomes without
  re-reading full transcripts (token-costly, already flagged as an
  anti-pattern in `feedback_no_agent_for_memory_lookup.md`).
- Not needed for this Claude Code session's own memory — that's the
  file-based `~/.claude/projects/.../memory/` system already in place and
  sufficient. Letta is for *other* local agents (Ollama-driven), not this one.

## Install
```
pip install letta
letta server
```
Exposes a REST API; agents connect via SDK or OpenAI-compatible calls.

## Capabilities
- Automatic in-context vs archival memory paging
- Persistent agent state across sessions/restarts
- Multi-agent shared memory stores
- Self-hosted, no per-seat/per-call billing
