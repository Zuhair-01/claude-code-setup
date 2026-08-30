---
name: free-oss-devops-stack
description: Curated, vetted free/open-source alternatives to paid dev-ops and automation SaaS — web scraping, browser automation, workflow automation, monitoring/observability, CI/CD, secrets management, error tracking, analytics, backups. Check here before proposing or paying for a SaaS tool in these categories.
---

# Free/OSS Dev-Ops & Automation Stack

Researched 2026-08-26 as part of a 3-session paid→free/OSS sweep (see Second_Brain Handoff Log
and memory `project_free_oss_ai_stack_research_2026_08_26.md`). Pairs with the standing
free-for-dev rule (check `free-for-dev` list / `public-apis-directory` skill first for data APIs;
this doc covers *tooling*, not data APIs).

Each entry: what it replaces · why it's the pick · self-host effort · install.

## Already adopted in this environment — don't re-propose
- **n8n + NocoDB** (self-hosted, Docker, localhost:5678/:8080) — replaces Zapier/Airtable. See `project_selfhosted_n8n_nocodb.md`.
- **Playwright** (local, headless) — replaces paid browser-automation SaaS (Browserbase, etc.) for screenshots/E2E. See `reference_local_playwright_screenshots.md`.
- **Ollama + local models** — clip-platform, Kyros already 100% local, zero paid AI API calls (verified 2026-08-26 audit, see below).

## Web scraping & crawling
- **Firecrawl** (OSS, self-hostable via Docker; also has a live `firecrawl-scraper` skill here) — replaces paid scraping APIs (Diffbot, ScrapingBee). Turns any site into clean markdown/structured data for LLM use. `docker compose up` from github.com/mendableai/firecrawl.
- **Crawlee** (Apify, OSS, Node/Python) — replaces paid crawling-as-a-service. Handles queueing, retries, proxy rotation, headless-browser crawling in one framework.
- **browser-use** (OSS, Python) — replaces paid AI-browser-agent SaaS (Skyvern cloud). LLM-driven browser agent for form-filling/data-extraction workflows, works with any local or API LLM.

## Workflow automation
- **n8n** — already self-hosted here. 400+ node integrations, visual builder, replaces Zapier/Make entirely at $0 vs their per-task pricing.

## Monitoring & observability
- **Uptime Kuma** (OSS, self-hosted, Docker) — replaces paid uptime monitors (Better Uptime, Pingdom). Status page + multi-channel alerts (Telegram/Discord/webhook), single container.
- **Grafana + Prometheus** (OSS, self-hosted) — replaces paid metrics/dashboarding (Datadog infra tier). Standard pairing for any service exposing metrics; Grafana Cloud has a free tier too if self-hosting isn't wanted.
- **SigNoz** (OSS, self-hosted, OpenTelemetry-native) — replaces paid full-stack APM (Datadog APM, New Relic). Traces + metrics + logs in one OSS package, single docker-compose.

## Error tracking
- **Sentry (self-hosted OSS edition)** — replaces paid Sentry Cloud once volume exceeds the free-tier event cap. Same product, run via `getsentry/self-hosted` docker-compose. Worth doing only once a project's error volume is large enough that Sentry Cloud's free tier becomes the constraint — not needed yet for any project in this account (checked 2026-08-26: none hit the cap).

## CI/CD
- **GitHub Actions** — free tier is generous (unlimited for public repos, 2,000 min/month private) and is what this account already uses via `gh`; no paid CI needed at current scale.
- **Woodpecker CI** (OSS, self-hosted, Drone-compatible) — fallback if private-repo minutes are ever exceeded and self-hosting the runner is preferred over paying for more minutes.

## Secrets management
- **Infisical** (OSS, self-hostable) — replaces paid secrets managers (Doppler, 1Password Secrets Automation). End-to-end encrypted, has a CLI + SDKs, free self-hosted tier has no seat/secret caps unlike the paid competitors.
- **Vaultwarden** (OSS, lightweight Rust reimplementation of Bitwarden server) — replaces paid password/secret-vault subscriptions if a shared team vault is ever needed; single small container.

## Object storage / backups
- **MinIO** (OSS, self-hosted, S3-compatible) — replaces paid cloud object storage if a project's storage cost on a managed provider (Supabase storage, S3) grows past free tier. Not currently needed — alwazour's Supabase storage bucket is still well within free tier as of 2026-08-26.
- **restic** (OSS, CLI) — replaces paid backup services (Backblaze B2's UI layer, paid backup SaaS) for scripted, encrypted, deduplicated backups to any storage backend including free-tier B2/S3.

## Analytics
- **PostHog (self-hosted OSS edition)** — alwazour already uses PostHog Cloud (free tier, per commit `aa7a33c`); self-hosting is only worth it if/when event volume exceeds PostHog Cloud's free tier (1M events/month) — not the case yet.
- **Umami** (OSS, self-hosted, lightweight) — simpler privacy-first alternative if a project ever wants pageview-only analytics without PostHog's full feature/event-volume weight.

## Notifications
- **ntfy** (OSS, self-hostable or free public instance) — replaces paid push-notification SaaS (Pushover, OneSignal) for simple server→phone alerts (deploy pings, cron failures, low-stock alerts).

---

## Paid-dependency audit — live projects (2026-08-26)

Checked `.env`/`.env.example`/`package.json` for paid API keys across the account's active projects:

- **clip-platform**: clean. `WHISPER_MODE` + `OLLAMA_*` only — already 100% local, no paid AI calls.
- **alwazour**: clean. Deps are all OSS libs (three.js, gsap, pg, zod, etc.); env vars are Supabase (free tier) + WhatsApp Cloud API (no free alternative exists for real WhatsApp Business messaging — this is the one paid-adjacent integration and it's the only viable option) + PostHog (free tier, see above).
- **Kyros orchestrator** (`~/.kyros`): clean, Ollama-only, no paid API references found.
- **Ostazi**: **not locally cloned on this machine** — could not audit `.env`/`package.json` directly this pass. Needs a session with the repo present, or Zoher confirming the path, to complete this one. Flagged, not skipped silently.

No urgent paid→free swaps needed anywhere audited — the account's projects were already disciplined about defaulting to free/OSS/local before this sweep. The value here is mostly the standing reference list above for *future* tool choices, plus closing the Ostazi audit gap next time that repo is available.
