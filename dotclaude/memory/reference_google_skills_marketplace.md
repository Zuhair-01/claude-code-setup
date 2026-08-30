---
name: reference-google-skills-marketplace
description: "google/skills Claude Code plugin marketplace added, use for future GCP/Gemini projects"
metadata: 
  node_type: memory
  type: reference
  originSessionId: fe47de95-1ac3-4241-8bd1-1ef0b4f49cc0
  modified: 2026-08-27T16:32:49.522Z
---

Added `google-plugins` marketplace (github.com/google/skills, Apache-2.0) via
`claude plugin marketplace add google/skills` on 2026-08-27. Needed
`git config --global core.longpaths true` first — one submodule
(cloud-bigtable-ecosystem) has a path too long for default Windows git.

Installed (user scope, always available): `google-cloud-developer@google-plugins`
(gcloud/GKE/IAM/monitoring/Well-Architected general skills) and
`gemini-api@google-plugins` (Gemini/Vertex API skills).

Not installed: per-database connector plugins (alloydb, cloud-sql-*, spanner,
bigquery, firestore-native, bigtable, looker, oracledb, data-agent-kit-*,
google-cloud-storage, knowledge-catalog, dataproc, db-context-engineering) —
each is its own GitHub repo pulled in as a plugin. Install only when a future
project actually uses that specific Google service:
`claude plugin install <name>@google-plugins`.

**Why:** none of the current projects (clip-platform, alwazour, Kyros, Ostazi)
use GCP — Supabase/Vercel/self-hosted is the stack. This is pre-positioning
for a future project that does.

**How to apply:** when starting a new project that touches Google
Cloud/Gemini, check this marketplace before hand-building GCP integration —
install the specific per-service plugin needed.
