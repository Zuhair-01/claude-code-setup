# claude-code-setup

**A real, working [Claude Code](https://claude.com/claude-code) configuration** — 274 skills, 165 agents, a 10k+ item offline capability library, and the hooks that wire it all together. Not a curated demo list; this is an actual daily-driver setup, snapshotted straight out of `~/.claude`.

Built for migrating between machines, but browsable and forkable if you want ideas for your own setup.

## What's in here

| Path | What it is |
|---|---|
| `dotclaude/skills/` | 274 live skills — frontend/design, backend patterns, security, marketing, video/UGC pipelines, data, devops, and more |
| `dotclaude/skills-library/` `dotclaude/agents-library/` | ~10,800 additional skills/agents kept **off-context** until searched (see [OVERSEER](dotclaude/OVERSEER-DESIGN.md)) — so a session only pays token cost for what it actually uses |
| `dotclaude/agents/` | 165 specialized subagents |
| `dotclaude/hooks/` | Lifecycle hooks — session-start capability checks, secure-code-write scanning, prompt sharpening, routing gates |
| `dotclaude/overseer/` | The search/routing layer over the offline library — `search.py <keywords>` finds a matching skill before anything gets hand-built from scratch |
| `dotclaude/memory/` | A file-based cross-session memory system (user profile, standing feedback, project context, references) |
| `dotclaude/CLAUDE.md` | The global instruction set — multi-account handoff protocol, routing rules, security gates, working-style preferences |

## Why this exists

Claude Code's skill/agent/hook system gets powerful fast, and also easy to lose track of. This repo is the answer to "what did I actually build in here, and how do I get it onto another machine without starting over."

The **OVERSEER** pattern is probably the most reusable idea here: instead of loading thousands of skills into every session's context, keep most of them indexed on disk and searched on demand. Read `dotclaude/OVERSEER-DESIGN.md` for the design, `dotclaude/overseer/` for the implementation.

## Using it

**Migrating your own setup to a new machine?** See [`SETUP.md`](SETUP.md) — written so a Claude Code session can read it and execute every step itself.

**Just want ideas?** Skim `dotclaude/skills/` and `dotclaude/hooks/` — most files are self-contained Markdown or small scripts you can copy individually into your own `~/.claude`.

No credentials, API keys, or session/cache data are included — see `SETUP.md`'s "What was deliberately excluded" section.

## License

[MIT](LICENSE) — copy whatever's useful.
