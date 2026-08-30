---
name: reference-cc-ecosystem-gaps
description: CC ecosystem gap sweep 2026-08-30 — MCP-server layer is the real gap (only 3 configured); Tier-1 picks Serena/Playwright-MCP/GitHub-MCP/Repomix/chrome-devtools-mcp. Skills+agents saturated.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 6729b9b0-f2a7-4060-b333-f255b2e77102
  modified: 2026-08-30T16:08:12.369Z
---

Sweep done 2026-08-30 (session zoher-37). Full doc:
`Empire_Base/Second_Brain/Workflow/30 - Resources/CC_Ecosystem_Gaps_2026_08_30.md`.

**Key finding:** skills/agents are saturated (3,200+ items, prior mining passes) —
do NOT bulk-import wshobson/agents or VoltAgent subagents, pull individually via
`search.py`. The real gap is **MCP servers**: only `sequential-thinking`,
`context7` (global) + `filesystem` (one project) are configured.

**Tier-1 MCP adds:** Serena (`oraios/serena` — installed as pinned uv tool
`uv tool install --from git+https://github.com/oraios/serena serena-agent`, MCP cmd
`cmd /c serena start-mcp-server --context ide-assistant`; the plain `uvx --from git+...`
form was flaky — timed out revalidating git each launch), Playwright MCP
(`@playwright/mcp`), Repomix (`repomix --mcp`) — **INSTALLED 2026-08-30 at user
scope, all ✔ Connected**. GitHub MCP (`github/github-mcp-server`) + chrome-devtools-mcp
(`ChromeDevTools/chrome-devtools-mcp`) — deferred (GitHub MCP needs PAT/OAuth).
Windows: `MSYS_NO_PATHCONV=1` before `claude mcp add` in Git Bash. Prior disabled
experiments (don't blindly re-add): firecrawl, exa, brave-search, serper, n8n,
second-brain, puppeteer, ffmpeg, hubspot, alpha-vantage.

**Wired into routing 2026-08-30:** `skill-router/SKILL.md` now has an "MCP Servers —
live tool routing" section + inline hints (Debug/Review tables) + 3 Mandatory-Pairing
rows: unfamiliar/large codebase → serena symbol tools (not grep+Read); full-repo
audit → repomix pack_codebase; browser e2e → playwright MCP headless. Since CLAUDE.md
Rule 7 routes every substantive task through skill-router, that's the "always in use"
mechanism. Restart sessions for the `mcp__serena__* / mcp__repomix__* / mcp__playwright__*`
tools to appear.

Self-hosted SaaS lane already deep — see [[reference-openalternative]] and the
Open_Source_Self_Host_Stack doc; no new gap found this pass. Related:
[[project_overseer]], [[project_archify_diagram_skill]], [[project_cc_switch]].
