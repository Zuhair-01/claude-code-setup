# Claude Memory Ownership

Use one system for each kind of information. Do not copy the same learning
into every store.

| Store | Owner | Use |
| --- | --- | --- |
| `~/.claude/CLAUDE.md` | User configuration | Durable global instructions and safety rules |
| Project `CLAUDE.md` / `.claude/rules/` | Project | Repository-specific conventions |
| `~/.claude/projects/*/memory/` | Claude auto memory | Local project discoveries and recurring fixes |
| Claude-Mem | Session search | Searchable short-term session history |
| Second Brain vault | Human-curated knowledge | Cross-session decisions, handoffs, and durable notes |
| `telemetry/`, `history.jsonl`, `metrics/` | Runtime diagnostics | Operational records, not instructions |

Never treat telemetry, generated session history, or auto memory as a security
policy. Review and promote useful findings into the correct durable store.
