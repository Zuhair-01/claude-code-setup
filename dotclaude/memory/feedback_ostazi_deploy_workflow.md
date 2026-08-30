---
name: feedback-ostazi-deploy-workflow
description: Never deploy directly to ostazi-edu.com production without explicit instruction; use Vercel preview deployments for changes instead
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 16aff1dd-0b30-4e50-ac47-e50c6a79cf4e
  modified: 2026-08-17T22:15:28.171Z
---

For the Ostazi project (`C:\Users\Zoher\Desktop\TutorLink-Syria`, Vercel projects
`ostazi-web` / `ostazi-api`), the live domain `ostazi-edu.com` must stay up and
working at all times as the default state.

**Rule:** when making code/config changes, deploy to a Vercel **preview**
deployment (`vercel deploy` without `--prod`, or a git branch/PR preview) —
never push straight to the production alias/domain — unless Zoher
*explicitly* says to apply it to the live domain.

**Why:** Zoher said this directly after a live incident where the production
site crashed (server-side exception, later traced to DB connection-pool
exhaustion under concurrent load) and he had to ask for an urgent fix. He
wants the production domain treated as a stable, always-on asset that
changes don't touch casually.

**How to apply:** For future Ostazi work — env var changes, redeploys, code
edits — default to preview/staging first, confirm it works, and only promote
to production (`vercel deploy --prod` / redeploy the prod alias) when he says
so. Exception: genuine outage fixes he's asked for urgently (like the DB
pooling fix and the OTP dev-echo flag flip already applied 2026-08-18) can go
straight to prod since the ask was explicitly "fix it now."
