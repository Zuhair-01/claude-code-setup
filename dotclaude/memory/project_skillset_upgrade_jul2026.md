---
name: skillset-upgrade-jul-2026-batch-21-repos
description: Mined 21 user-provided GitHub repos for Claude Code skills/agents; installed 61 new skills + 43 new agents + 67 new slash commands.
metadata: 
  node_type: memory
  type: project
  originSessionId: 15f1324f-2735-43bb-843e-15bbdc604666
---

## Context

User sent 21 GitHub links on 2026-07-14 calling them all "skills repositories" and asked to extract skills/agents from each, install what works, and build agent teams to put them to use, with token efficiency in mind.

## Installed

- **gstack** (garrytan/gstack) → 48 skills as `gstack-*` in `~/.claude/skills/` (review, ship, qa, design-review, plan-*-review, spec, investigate, retro, document-generate, ios-*, make-pdf, etc.). Skipped the browser-automation pieces (`browse`, `open-gstack-browser`, `setup-browser-cookies` — 31MB+, needs its own bin/Bun runtime not present) and internal eval tooling (`benchmark*`). The root `gstack` router skill itself wasn't installed (depends on a `bin/gstack-update-check` that doesn't exist standalone) — invoke the individual `gstack-*` skills directly instead.
- **taste-skill** (Leonxlnx/taste-skill) → 12 skills installed as-is (brandkit, brutalist-skill, gpt-tasteskill, image-to-code-skill, imagegen-frontend-mobile/web, minimalist-skill, output-skill, redesign-skill, soft-skill, stitch-skill, taste-skill, taste-skill-v1). Frontend "anti-slop" design taste skills.
- **career-ops** (santifer/career-ops) → 1 skill `career-ops` (job search command center: CV gen, offer eval, application tracking).
- **get-shit-done / GSD** (gsd-build/get-shit-done, archived → moved to open-gsd/gsd-core) → 33 agents (`gsd-*`) + 67 slash commands (`/gsd:*`) — full spec-driven dev workflow system (plan-phase, execute-phase, code-review, debug, ship, etc.). Repo is archived; if commands misbehave, check open-gsd/gsd-core for the maintained fork.
- **Understand Anything** (Egonex-AI/Understand-Anything) → 10 agents renamed `understand-*` (architecture-analyzer, file-analyzer, domain-analyzer, tour-builder, etc.) — codebase → knowledge graph comprehension team. Only the agent definitions were pulled; the TS dashboard/core packages (need build) were skipped.
- **agentic-system-prompt-patterns** (new skill, synthesized) — distilled patterns from x1xhlol/system-prompts-and-models-of-ai-tools + asgeirtj/system_prompts_leaks + f/prompts.chat, for writing/auditing subagent system prompts. Raw leaked-prompt collections were NOT dumped in full (token cost) — this skill points back to the source repos for deep dives.

## Already installed pre-existing (verified, no action needed)

- kepano/obsidian-skills, affaan-m/ECC, thedotmack/claude-mem, ruvnet/ruflo, mvanhorn/last30days-skill — all live as plugins already.

## Skipped — not Claude Code-compatible

- **NousResearch/hermes-agent** — standalone Python agent CLI/product, not a Claude Code skill format. (Consistent with prior skip decision, see [[project_trending_installs]].)
- **DietrichGebert/ponytail** — a plugin *for* hermes-agent specifically (`hermes plugins enable ponytail`), not usable in Claude Code.
- **nexu-io/open-design** — full open-source Figma-alternative app, not a skill repo.
- **hesreallyhim/awesome-claude-code** — a curated links list, not skills themselves. Worth browsing (github.com/hesreallyhim/awesome-claude-code) next time a specific category of tooling is needed (slash commands, statuslines, workflows).
- **tw93/Pake, lobehub/lobehub, zhayujie/CowAgent, anthropics/claude-code** — full applications/CLI itself, not skill repos; not cloned.

**Why:** User wants Claude Code capability expansion, not unrelated standalone products. Full-app repos and other-ecosystem plugins don't integrate with the Skill/Agent tool regardless of "install" effort.

**How to apply:** New skills auto-surface via the Skill tool by description match — no manual invocation setup needed. GSD's `/gsd:*` commands and the `gsd-*`/`understand-*` agents are directly invokable. Skill/agent counts as of this batch: ~3043 skills, ~227 agents.
