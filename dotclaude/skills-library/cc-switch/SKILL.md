---
name: cc-switch
description: >
  Use when managing AI CLI tool providers, switching API keys/endpoints, installing skills across tools,
  browsing/resuming sessions, managing MCPs, or syncing prompts. Triggers on: "switch provider",
  "change API key", "install skill", "resume session", "browse sessions", "manage MCP", "track usage",
  "hot-switch", "cc-switch", or any multi-tool AI CLI management task.
---

# CC Switch — AI CLI Tool Manager

CC Switch is a Tauri 2 + Rust + React desktop app that centrally manages Claude Code, Codex, Gemini CLI, OpenCode, and OpenClaw from one GUI.

## Install

Windows: Download `CC-Switch-{version}-Windows.msi` from https://github.com/farion1231/cc-switch/releases and run it.

Data lives at: `~/.cc-switch/cc-switch.db` (SQLite) + `~/.cc-switch/settings.json`

## Core Features & How to Use

### 1 — Provider Switching (most-used feature)

Switch API providers (official Anthropic, proxy services, third-party endpoints) without manually editing JSON/TOML/.env files.

**Claude Code**: Hot-switch — takes effect immediately, no restart needed. CC Switch writes to `~/.claude/settings.json`:
```json
{ "env": { "ANTHROPIC_API_KEY": "...", "ANTHROPIC_BASE_URL": "..." } }
```
**Codex**: Requires terminal restart after switch.
**Gemini CLI**: Hot-switch — re-reads `~/.gemini/.env` on each request.

Via system tray: right-click CC Switch icon → app submenu → click provider.
Via main UI: click "Enable" on provider card.

### 2 — Skills Management

CC Switch manages skill installation across ALL tools from one panel.

- Click **Skills** in top nav
- Browse pre-configured repos (Anthropic Official, ComposioHQ, Community Picks) or add custom GitHub repos
- One-click **Install** → copies to `~/.claude/skills/`, `~/.codex/skills/`, `~/.gemini/skills/`, `~/.opencode/skills/`
- **Update All** button batch-updates outdated skills (SHA-256 content hash detection, v3.13.0+)
- **Restore from Backup** — restores uninstalled skills from `~/.cc-switch/skill-backups/`
- Add custom repo: Owner + Name + Branch + optional Subdirectory

Storage location: `~/.cc-switch/skills/` (default) or `~/.agents/skills/` (community convention)

### 3 — Session Manager

Browse and resume sessions from all AI CLI tools in one place.

Session locations:
| App | Path |
|-----|------|
| Claude Code | `~/.cache/claude/projects/*.jsonl` |
| Gemini CLI | `~/.cache/gemini/tmp/<hash>/chats/` |
| OpenCode | `~/.local/share/opencode/` |
| OpenClaw | `~/.openclaw/agents/<agent>/sessions/*.jsonl` |

Features:
- Full-text search across session ID, title, summary, project dir
- Filter by provider
- **Resume** button → launches preferred terminal in session's project dir with resume command
- **Directory picker** (Claude sessions, v3.13.0+) — override project dir before resume (useful when project was moved)
- On Windows: resume command copied to clipboard (terminal launch is macOS only)
- Batch delete sessions

### 4 — MCP Server Management

Manage Model Context Protocol servers for all tools from the Extensions → MCP panel.

### 5 — Prompts Sync

Manage system prompt presets (CLAUDE.md equivalents) for quick scenario switching via Extensions → Prompts.

### 6 — Local Proxy + Failover

- Start a local proxy that logs all requests and tracks usage/cost
- Auto-failover: switches to backup provider when primary fails
- Circuit breaker: prevents repeated retries against a down provider
- Token usage tracking + cost estimation per provider

### 7 — Usage Dashboard

Track API calls, token usage, and cost per provider per tool. Accessible via the Usage tab.

## Key Config Files Modified by CC Switch

| App | File(s) |
|-----|---------|
| Claude Code | `~/.claude/settings.json` |
| Codex | `~/.codex/auth.json`, `~/.codex/config.toml` |
| Gemini CLI | `~/.gemini/.env`, `~/.gemini/settings.json` |

## When to Invoke This Skill

- User wants to switch API provider / endpoint for any AI CLI tool
- User wants to install, update, or manage skills across tools
- User wants to browse, search, or resume past sessions
- User wants to track API usage or costs
- User wants to add a custom skill repository
- User wants to set up automatic failover between providers
- CC Switch itself is broken or misconfigured

## Troubleshooting

**Switch fails — config locked**: Close the running CLI tool first.
**Switch fails — permissions**: Check write permissions on the config directory.
**Skills list empty**: Network issue or wrong repo config → click Refresh.
**Session not showing**: Click the circular-arrow Refresh in the Sessions panel.
