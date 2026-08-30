# Claude Code System Truth

This is the authoritative operational summary for the local Claude Code
installation. Older activation and architecture documents are historical
references and may contain unmeasured performance claims.

## Runtime

- Claude Code: `2.1.233`
- GSD Core: `1.10.0`
- Platform: native Windows
- GSD runtime: `C:\Users\Zoher\.claude\gsd-core`
- Validator: `C:\Users\Zoher\.claude\overseer\validate_claude_config.py`

## Active Wiring

- `SessionStart`: registry validation plus GSD session hooks.
- `UserPromptSubmit`: Overseer directive injection.
- GSD hooks: context monitoring, injection scanning, write protection, and
  optional workflow and graphify guards.
- GSD commands and workflow assets are installed by the official
  `@opengsd/gsd-core` installer.
- Overseer search is available through `overseer/search.py`.
- All installed third-party plugins are currently disabled; see
  `PLUGIN-DECISIONS.md`.
- Global MCP configuration is empty; `claude mcp list` currently hangs during
  health discovery and no MCP server is treated as active.

## Not Guaranteed

- OmniRoute is configured but is not proven to route model calls.
- Bundle selection is a local selector, not context lazy-loading.
- Token and cost savings are not guaranteed until measured by telemetry.
- Auto-bundling is not a filesystem watcher.

## Validation

```powershell
python $HOME\.claude\overseer\validate_claude_config.py
claude doctor
claude plugin validate --strict $HOME\.claude\plugins\marketplaces\everything-claude-code
node $HOME\.claude\gsd-core\bin\gsd-tools.cjs --help
```

Restart Claude Code after changing hooks, GSD, or settings.
