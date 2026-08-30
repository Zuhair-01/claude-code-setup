---
name: project_3way_oss_sweep_consolidated_2026_08_26
description: "3-way free/OSS research sweep — final state, what was actually installed/wired in vs. what's still waiting on Zoher"
metadata: 
  node_type: memory
  type: project
  originSessionId: 2dd75671-3d8f-4364-b84c-4007200836db
  modified: 2026-08-26T11:23:17.107Z
---

3 peer sessions (zoher-8f/a1/9d) ran ~30 rounds of free/OSS tooling research 2026-08-26, logged to `Second_Brain/Workflow/30 - Resources/Open_Source_Self_Host_Stack.md`. This session (zoher-c9) watched, verified independently (ran `claude mcp list` myself, grepped for cookie-consent code, checked which skills shipped to disk), wrote the ranked decision list to the Handoff Log, then Zoher said "utilize all" — executed the list. Full round-by-round detail lives in the resource doc and the Handoff Log's `zoher-c9` entries; this memory is the final-state summary, not the research log.

**EXECUTED (all committed/running, not just flagged):**
- **Gitleaks** — installed (winget), pre-commit hook wired into both [[project_clip_platform]] and alwazour (alwazour's went into its existing shared hook script, not the pre-commit framework — that framework broke on a Windows/git legacy-hook shebang quirk). History scan found and fixed a real leak: clip-platform's `tunnel.log` had 13 committed JWT tokens — now gitignored/untracked (repo is private, so contained; git history still has the old ones, rewriting history was NOT done, that's a separate destructive call).
- **Trivy** — installed (winget), CI workflow added to both repos.
- **Renovate** — `renovate.json` added to both repos. The hosted GitHub App itself still needs Zoher's manual install click at github.com/apps/renovate (can't be done via API token).
- **Sequential Thinking + Context7 MCP servers** — both added user-scoped (`claude mcp list` confirms connected), Context7 running keyless/rate-limited since no API key was available.
- **LLM Guard** — `pip install`'d successfully. Available, not yet wired into any specific endpoint — that's a real integration task (which endpoint, what to sanitize) better scoped explicitly than done blind.
- **Silktide cookie-consent** — live in clip-platform's `web/app/layout.tsx`, verified CDN URLs+integrity hashes (fetched from silktide.com, not guessed), gates Umami analytics behind explicit consent. `next build` verified clean before commit.
- **Vikunja, Weblate+LibreTranslate, Presenton, Mailpit, Reacher** — added to `Empire_Base/selfhost/docker-compose.yml` (on-demand, `restart: "no"`, matching the file's existing pattern — not auto-started, pull them up via `start.ps1` when needed). Credentials/URLs logged in `selfhost/.credentials.local`.
- All commits pushed to origin (clip-platform's commits needed author-email rewritten to the GitHub noreply format first — real repo push-protection block, fixed via `git filter-branch` on the unpushed range only).

**NOT executed, still needs Zoher:**
- **SadTalker** — held back on purpose: needs a large model download (violates [[feedback_no_large_downloads]]) AND its commercial-license status is genuinely unresolved (open GitHub issue, no maintainer answer) — Zoher should read that thread himself before using it for the commercial [[project_ai_clone_heygen]] work. Install path is fully specced and ready.
- **axe-core/Playwright a11y testing** — neither repo actually has a Playwright test suite (the "Playwright already running" catalog claim referred to Claude's own screenshot tool, not project test infra) — standing up a new test framework is a scope decision, not a wire-in.
- **Renovate GitHub App install** — config is ready, needs Zoher's own click (GitHub App install isn't API-tokenable).
- Everything else cataloged (litellm-gateway, lancedb, letta, unsloth, deepeval, Grafana OnCall, Kimai, OpenShorts/Presenton-as-competitive-awareness, Bumblebee, OpenClaw, Cloudflare AI Gateway, Perplexica+SearXNG, etc.) is correctly left as OVERSEER/catalog candidates — no current trigger, per ponytail/YAGNI.

**Real gotchas found during execution** (useful for whoever touches these next):
- Reacher needs outbound port 25 — blocked on most residential ISPs/all major clouds by default, untested on this box.
- alwazour's `.git/hooks/pre-commit` is a hand-written shared script (not the pre-commit framework) — any future hook addition there should append to that script directly, not run `pre-commit install` (breaks on Windows legacy-hook shebang resolution).
