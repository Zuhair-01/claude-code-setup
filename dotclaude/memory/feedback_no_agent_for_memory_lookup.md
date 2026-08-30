---
name: no-agent-for-memory-lookup
description: Never wrap claude-mem get_observations/search calls in an Agent subagent
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5be085cf-a3c6-4d1a-9d14-f88ba162bede
  modified: 2026-08-02T09:35:07.693Z
---

Never spawn the Agent tool to call `mcp__plugin_claude-mem_mcp-search__get_observations` or `search`/`smart_search`. Call those MCP tools directly in the main loop.

**Why:** wrapping a single memory-retrieval lookup in a subagent cost 106k+ tokens for what should have been a near-free direct tool call — the subagent re-derives context and narrates instead of just returning data. User reaction was strongly negative (repeated in caps, "catastrophical").

**How to apply:** Any time the task is "fetch/recall past observations/details from memory," call the claude-mem MCP tools directly. Only use Agent for tasks that genuinely need independent multi-step exploration Sonnet can't do in one or two direct tool calls. In general on this account: default to direct tool calls, only escalate to Agent/Workflow when the task truly requires isolated multi-step work — see [[feedback_lean_engine]].
