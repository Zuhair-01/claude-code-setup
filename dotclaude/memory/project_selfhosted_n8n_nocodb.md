---
name: project-selfhosted-n8n-nocodb
description: "Self-hosted n8n and NocoDB running locally via Docker, replacing Zapier/Airtable subscriptions"
metadata: 
  node_type: memory
  type: project
  originSessionId: f413e4cb-04dd-4247-9749-40ea0e10d151
  modified: 2026-08-25T13:24:42.577Z
---

Spun up 2026-08-25 from the "9 GitHub Repos That Replace $2,122/yr" self-hosting
guide (see [[reference_cli_anything_hub]] session for the source). Both running
via plain `docker run`, `--restart unless-stopped`:

- **n8n** — http://localhost:5678, volume `n8n_data` (workflows persist here).
  Replaces Zapier. Already had [[project_skill_bundle_system_2026]]'s
  n8n-workflow-patterns skill and the CLI-Hub `n8n` harness — this is the actual
  running server those point at now.
- **NocoDB** — http://localhost:8080/dashboard, data at `~/nocodb-data`.
  Replaces Airtable. Not yet pointed at a real project's Postgres — currently
  using its bundled SQLite. Wire it to an existing project DB (e.g. Ostazi's
  `ostazi-postgres` container) if a real Airtable-style use case shows up.

**Why**: Zoher asked to act on the self-hosting-guide analysis instead of just
reviewing it — direct replacement for two paid subscriptions.

**How to apply**: don't re-suggest installing these — check `docker ps` first,
they should already be running. First-run owner-account setup was not
completed by Claude (needs Zoher's own credentials) — check with him before
assuming either is fully configured.

**Port note**: host already had `ostazi-postgres` on 5432 and `postiz` stack
(4007) before this — no conflicts hit for 5678/8080, confirmed via `netstat`
before starting.
