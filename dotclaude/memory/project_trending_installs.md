---
name: GitHub Trending Installs — Apr 2026 Batch
description: 4 tools installed from GitHub Trending Apr 14 2026. Plugins active, Voicebox downloading.
type: project
originSessionId: 4849602e-d58c-4469-8b07-c208de7d6b57
---
## Installed (2026-04-25)

### andrej-karpathy-skills (plugin)
`/plugin install andrej-karpathy-skills@karpathy-skills` — active globally.
4 behavioral principles injected into CLAUDE.md: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution.
**How to apply:** These run automatically via the plugin. No invocation needed.

### superpowers (plugin)
`/plugin install superpowers@claude-plugins-official` v5.0.7 — active globally.
Skills: brainstorming, writing-plans, TDD, systematic-debugging, subagent-driven-development, requesting-code-review, using-git-worktrees, finishing-a-development-branch.
**How to apply:** Auto-triggers when building software. No manual invocation needed for structured tasks.

### claude-mem (plugin)
`npx claude-mem install` v12.3.9 — active globally.
Auto-captures all Claude sessions → SQLite + ChromaDB → injects relevant context back.
Worker runs on `http://localhost:37777`. Search past sessions: `/mem-search` in Claude Code.
Start worker: `npx claude-mem start`
**How to apply:** Automatic. Past session context appears in new sessions. Use `/mem-search` to query history.

### Voicebox v0.4.5 (local TTS studio)
MSI: `C:\Users\Zoher\Desktop\Empire_Base\Voicebox_0.4.5_setup.msi`
REST API after install: `http://localhost:17493`
Arabic support: Chatterbox Multilingual engine (23 languages incl. Arabic).
**Pillars served:** Arabic Localization (dubbing) + AI-UGC (faceless voiceovers).
**Key endpoint:** `POST /generate` `{"text":"...", "profile_id":"...", "language":"ar"}`
Clone workflow: record/upload 5s+ audio → create profile → use profile_id in all generations.

## Skipped
- **hermes-agent** (NousResearch) — Requires WSL2, overlaps with existing n8n + Automaton setup.
- **markitdown** (Microsoft) — Useful for B2B doc processing but not urgent.
- **virattt/ai-hedge-fund** — Not aligned with current pillars.
- **Apollo-11** — Historical, not applicable.
- **pascalorg/editor** — 3D architecture, not applicable.
