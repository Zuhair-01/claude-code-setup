# MCP Catalog

The direct user-profile MCP entries were removed because `claude mcp list`
health-checked every configured stdio process and hung on stale `npx` servers.
No MCP server is currently configured for Claude Code.

Re-add only what is needed, with credentials supplied through environment
variables rather than `.claude.json`:

```powershell
claude mcp add second-brain -s local -- cmd /c npx -y @modelcontextprotocol/server-filesystem C:\Users\Zoher\Desktop\Empire_Base\Second_Brain
claude mcp add n8n -s local -e N8N_API_KEY=$env:N8N_API_KEY -- cmd /c npx -y n8n-mcp -e N8N_API_URL=http://localhost:5678
```

Validate each server individually with `claude mcp get <name>` before adding
another. Do not restore the old bulk list or inline API keys.
