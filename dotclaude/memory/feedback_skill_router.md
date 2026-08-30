---
name: skill-router-always-first
description: For every substantive task, run one unified routing step that picks BOTH the best skill stack (skill-router) AND the best agent(s) — not skills alone. Fully autonomous, no user prompting.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b1b9cc4b-2c73-4988-940d-f63ea9075299
---

Before responding to ANY substantive task (coding, design, marketing, video, data, agents, devops, security, writing, automation, research, debugging, analysis), run a combined routing step FIRST: pick the right skill stack AND the right agent(s)/MCP tools for the job, together, as one decision — not skills in isolation.

**Why:** User has 2900+ skills + 400+ agents + dozens of MCP servers installed. Without proactive routing across all three, the wrong tools fire or the fullest capability isn't used. User confirmed this explicitly: "everytime a task is been called u need to run our main agent to forwarding the best agents skills towards it for the best outcome as possible" — extending the original skill-only routing ([[feedback_agent_autonomy]]) into one combined orchestration step.

**How to apply:**
1. User sends a task.
2. Invoke `Skill("skill-router")` to get the ordered 2-5 skill stack (INVOKE vs REF).
3. In the same pass, pick the best-fit installed agent(s) from the Agent tool's type list (engineering/marketing/design/sales/etc.) — blend for multi-domain tasks. Don't ask the user to choose.
4. If the task needs live external capability (browser, GitHub, Notion, Figma, etc.), pull in the matching MCP tool via ToolSearch as part of the same routing pass, not as an afterthought.
5. Proceed with the actual work using that combined stack.

**Exceptions (skip routing):**
- Pure conversational messages (no task)
- Memory/recall requests (check memory instead)
- Skill installation requests
- Meta questions about Claude Code itself

**Speed note:** Per [[feedback_speed_and_power]], do this routing silently/fast — don't narrate the selection process, just apply it and act.

**Escalation to multi-agent Workflow:** Routine tasks stay single-agent (skill-router + one blended agent). Escalate to the Workflow tool (parallel fan-out agents + adversarial verify pass) when a task is complex/high-stakes: full builds, audits, security/compliance work, comprehensive research, or anything the user flags as "thorough"/"comprehensive"/"audit everything." User confirmed this tiering 2026-07-15 ("okay seems reasonable") after I proposed it. Still needs the user's actual task content — this doesn't bypass Workflow's own opt-in gating (ultracode keyword or explicit ask), it just means I should proactively *recommend* Workflow escalation when a task qualifies, rather than defaulting everything to single-agent.
