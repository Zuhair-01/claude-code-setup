---
name: project_free_oss_devops_stack_2026_08_26
description: Dev-ops/automation lane of the 3-session paid-to-free/OSS sweep — curated tool list + paid-dependency audit of live projects.
metadata: 
  node_type: memory
  type: project
  originSessionId: 20e3924f-dde4-4521-9f79-38aab5b3c8a8
  modified: 2026-08-26T01:04:52.477Z
---

Built `free-oss-devops-stack` OVERSEER skill (`~/.claude/skills-library/free-oss-devops-stack/SKILL.md`) covering web scraping (Firecrawl, Crawlee, browser-use), monitoring (Uptime Kuma, Grafana+Prometheus, SigNoz), error tracking (self-hosted Sentry), CI/CD (GitHub Actions free tier, Woodpecker CI), secrets (Infisical, Vaultwarden), object storage/backup (MinIO, restic), analytics (self-hosted PostHog/Umami), notifications (ntfy) — each with what it replaces, why, and self-host effort. Reindexed into OVERSEER (`build_index.py`), searchable under devops-ci/security keywords.

Paid-dependency audit of live projects (checked `.env`/`package.json`): clip-platform, alwazour, and Kyros orchestrator are all already clean — no paid AI/SaaS API calls, already disciplined about local/free-tier defaults before this sweep even started. Ostazi could not be audited — **not locally cloned on this machine**, needs a session with the repo present.

**Why:** part of Zoher-approved 3-way research split (2026-08-26) — this session's lane was dev-ops/automation tooling + paid-dependency audit; `[[project_ai_revenue_engine]]` session covered local LLM/RAG, a third covered media-gen (see `oss-media-gen-stack` OVERSEER skill).

**How to apply:** check `free-oss-devops-stack` before proposing or paying for any scraping/browser-automation/monitoring/CI/secrets/backup/analytics SaaS. Complete the Ostazi audit next time that repo is available locally — don't re-do the other three, they're confirmed clean.
