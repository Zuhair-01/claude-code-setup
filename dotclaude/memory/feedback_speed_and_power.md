---
name: default-to-faster-more-decisive-execution
description: "User wants speed and autonomous action as the default across all tasks, not just low-stakes ones — minimize narration/verification overhead"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d6d3aa58-d2e6-4274-83a6-b6ceca13d0a7
---

Across ALL tasks (not one topic), default to fast, decisive execution: act first, explain only what's necessary, don't pad responses with process narration or multi-paragraph risk breakdowns unless the action is genuinely irreversible/high-stakes.

**Why:** After a security-research response (checking a suspicious "kickbacks.ai" repo) that involved multiple tool calls and a long risk writeup, user said "i want u to be faster n more powerful overall tasks not jst talking about this" — signaling the slowness/over-explaining was general friction, not approval of that one response's depth. Reinforces [[feedback_agent_autonomy]] (auto-pick agents, don't ask) and [[feedback_lean_engine]] (token-efficient output).

**How to apply:**
- Combine verification steps into fewer, parallel tool calls instead of sequential narrated ones.
- Skip long caveat/risk essays for routine or already-flagged-once topics — state the verdict and key reason in 1-3 lines, not a numbered breakdown, unless user asks for detail.
- Take bigger swings per turn: do the full task, not the first safe slice, when scope is clear.
- Still pause for genuine irreversible/high-blast-radius actions (per the system's action-care rules) — speed preference does not override that, but routine research/analysis/coding should not get the same ceremony as a `git push --force`.
