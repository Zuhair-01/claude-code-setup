---
name: cc-switch-integration
description: "CC Switch desktop app — AI CLI tool manager for Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw. Installed as skill at ~/.claude/skills/cc-switch/. Use for provider switching, skills management, session browsing, MCP management, and usage tracking."
metadata: 
  node_type: memory
  type: project
  originSessionId: b1b9cc4b-2c73-4988-940d-f63ea9075299
---

CC Switch is a Tauri 2 + Rust + React desktop GUI that centralizes management of all AI CLI tools. Skill installed at `C:\Users\Zoher\.claude\skills\cc-switch\SKILL.md`.

**Why:** User declared it "VERY VERY IMPORTANT N VITAL THING WE NEED IN OUR SYSTEM THAT WE NEED TO BE USING 24/7 IN EVERYTHING." It solves multi-provider switching, scattered configs, no usage monitoring, and service instability.

**How to apply:** Invoke `cc-switch` skill whenever user needs to: switch API providers, install/update skills across tools, browse/resume past sessions, manage MCP servers, sync prompts, track usage/costs, or set up failover.

## Key facts

- **Install**: `CC-Switch-{version}-Windows.msi` from https://github.com/farion1231/cc-switch/releases
- **Data**: `~/.cc-switch/cc-switch.db` (SQLite) + `~/.cc-switch/settings.json`
- **Skills location**: `~/.cc-switch/skills/` → symlinked to `~/.claude/skills/`, `~/.codex/skills/`, etc.
- **Claude Code hot-switch**: takes effect immediately (writes to `~/.claude/settings.json` `env.ANTHROPIC_API_KEY` + `env.ANTHROPIC_BASE_URL`)
- **Session storage** (Claude Code): `~/.cache/claude/projects/*.jsonl`
- **Latest version**: v3.15.x (as of May 2026)
- **Key v3.13.0+ features**: Update All for skills, Directory Picker for session resume, per-app tray submenus, skills.sh public registry search

[[usage-limit-reducer-integration]]
