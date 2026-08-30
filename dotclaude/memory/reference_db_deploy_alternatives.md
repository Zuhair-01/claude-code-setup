---
name: reference-db-deploy-alternatives
description: "Free Postgres (Supabase vs Neon) and deployment platform (Vercel vs Railway/Render/Fly/Cloudflare) alternatives, researched from Ostazi's Supabase Nano perf bottleneck."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 12f7f182-ddc0-4da5-8270-33fdb94f47ef
  modified: 2026-08-29T00:37:09.218Z
---

Vault doc: `Second_Brain/Workflow/30 - Resources/Free_Tier_Stack.md`
(Database and "Vercel — 10 alternatives" sections, updated 2026-08-29).
Covers:

- Supabase Free/Nano vs Neon Free compute+idle tradeoffs — Neon auto-scales
  and resumes fast, Supabase Nano is fixed-size and was found sitting at
  ~50% sustained utilization on Ostazi (root cause of a site-wide
  slowness complaint, not a code bug). Storage/Auth on Supabase are
  separate products from DB compute — can swap just `DATABASE_URL` to
  Neon free tier without touching file storage.
- Vercel vs Railway/Render/Fly.io/Cloudflare Pages for a Next.js+Express
  monorepo — Vercel serverless is a mediocre fit for a persistent
  Express+Prisma API (cold starts + per-invocation DB connections);
  Railway/Render give a persistent process instead.

Check this before picking a DB or deploy platform on any future project,
or before paying to upgrade an existing Supabase/Vercel tier — see
[[feedback_free_for_dev_default]]. Not yet acted on for Ostazi as of
2026-08-29 — Zoher deferred the migration, wanted the research on record
for later.
