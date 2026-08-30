---
name: feedback-broadcast-only-no-held-messages
description: Never rely on direct SendMessage to peer sessions that may hold pending user approval — use Handoff Log broadcast (vault file) as the only cross-session channel.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9c5fd7cf-2c93-40d6-9c8d-ba317d81fc86
  modified: 2026-08-28T00:22:47.802Z
---

Do not use direct `SendMessage` to peer Claude Code sessions for task coordination when the
recipient is Remote-Control-connected — those sends can be held pending the recipient's own
user's approval and never actually deliver. Zoher's explicit correction, 2026-08-28: "DO NOT SENT
HELD PEER MESSAGE AT ALL ALWAYS USE BROADCAST ONLY."

**Why:** during the Alwazour Studio OS multi-lane build, a `SendMessage` to zoher-9e (Remote
Control-connected) came back with a "held for recipient user's approval" notice — meaning the
message content is invisible to that session until its own user acts, which could be indefinite.
Relying on it for real coordination is unreliable.

**How to apply:** default to writing/updating the Handoff Log entry (`Second_Brain/Workflow/20 -
Areas/Handoff Log.md`) as the primary cross-session channel — every session reads it per
[[multi_session_orchestration]]/CLAUDE.md Rule 1. Only use `SendMessage`/the `handoff-broadcast`
skill as a supplementary fast-path when `ListAgents` shows a peer that is NOT Remote-Control-only
(a plain local/bg session), and even then don't treat it as the sole delivery path — the Handoff
Log entry must always carry the full state regardless, per Rule 2's existing requirement that the
log entry itself be self-contained for a cold reader. If a SendMessage comes back "held for
approval," don't retry it or wait — the Handoff Log write already covers it; move on.
