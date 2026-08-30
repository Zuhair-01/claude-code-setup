---
name: project-ostazi-audit-log-cron-2026
description: "Ostazi admin audit-log page + booking/group-session auto-complete cron sweep, shipped 2026-08-18 — what's live, what's still broken/open"
metadata: 
  node_type: memory
  type: project
  originSessionId: 335e5c38-6604-44cd-a88c-7b0afdc6e09d
  modified: 2026-08-19T18:44:31.922Z
---

Shipped and verified live on 2026-08-18 (~16:35), commits `07525ef` +
`3347046` on `TutorLink-Syria` master:

1. **Admin audit log**: `/admin/audit-log*` API (filter by action/entity/
   actor/date, paginated) + "سجل التدقيق" tab in `/admin` on ostazi-edu.com.
   Backfilled `writeAuditLog` calls that were missing on register/login/
   session-revoke/package-creation so the log actually has data.
2. **Booking/group-session auto-complete cron**: fixed a real prod bug —
   the sweep that flips expired bookings/group-sessions to COMPLETED never
   ran in production at all (serverless deploy never imports the file with
   the setInterval). New `CRON_SECRET`-gated `/system/cron/sweep`, runs
   daily at 01:00 UTC via `vercel.json`'s `crons`. `CRON_SECRET` is set in
   Vercel prod env (Sensitive type — can be written via CLI but never read
   back; if you need to re-verify it works, regenerate + redeploy + curl-test
   all in one shell scope, don't try to retrieve the old value).

**Known Vercel gotchas discovered this session** (see
[[feedback_ostazi_deploy_workflow]] for the broader deploy-caution rule):
- Vercel Hobby plan caps cron schedules at once/day. A schedule violating
  that (e.g. `*/15 * * * *`) doesn't just skip the cron — it **fails the
  entire deployment**, silently, even though `git push` itself succeeds.
  Always sanity-check cron frequency against Hobby limits before adding one.
- `ostazi-api`'s git→Vercel auto-deploy does not fire reliably on push
  (`ostazi-web`'s does, same repo, same pushes). Workaround: `vercel --prod`
  CLI from the repo root (not `apps/api/`) — copy `apps/api/.vercel/project.json`
  to `<repo-root>/.vercel/project.json` first, or it errors "Root Directory
  apps/api does not exist".

**Update 2026-08-19, see [[project_ostazi_run1_golive_2026]] for the full
session:** the "auto-deploy doesn't fire reliably" gotcha above did NOT
reproduce — a normal `git push origin master` deployed correctly, verified
live via a direct API call within a couple minutes, no `vercel --prod`
CLI workaround needed. Either it was a one-off Hobby-plan cron-schedule
failure (see the gotcha above it, which explains a full deploy failure
plausibly enough on its own) or it's since been fixed some other way —
don't assume the CLI workaround is still needed, but don't fully trust
plain `git push` either until it's been reliable across a few more
pushes.

**One thing flagged but NOT fixed, still open:**
- `createNotification` (notifications.service.ts) and `logActivity`
  (activity.service.ts) are dead code — never called anywhere — but their
  read-side APIs and a live `NotificationBell.tsx` in the header ARE
  deployed. The notification bell has silently always been empty in prod.
  Needs a decision from Zoher on whether to wire the write side in.

**Resolved 2026-08-19:** the jest suite issue below is fixed — see
[[project_ostazi_run1_golive_2026]]. Original note, left for history: the
jest test suite was ~240/287 failing, root-caused to 34 test files'
`registerAndLogin()` helpers never being updated after commit `db01198`
added a required `password` field to `/auth/register`.
