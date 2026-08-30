---
name: project-ostazi-run1-golive-2026
description: "Ostazi RUN 1 intelligence audit -> RUN 1.5 wedge strategy -> shipped demand-capture pipeline + fixes, 2026-08-19 — full arc, current state, next steps"
metadata: 
  node_type: memory
  type: project
  modified: 2026-08-19T18:44:58.742Z
  originSessionId: 27ecd93d-bb51-4451-9046-96ee7c165162
---

Full arc, single session, `C:\Users\Zoher\Desktop\TutorLink-Syria`. Three
artifacts are the actual source of truth — this memory just indexes them
and the current operational state, don't re-derive from scratch:

- RUN 1 (intelligence audit): https://claude.ai/code/artifact/5c23e48f-1612-4079-9b79-92a0b614e320
- RUN 1.5 (war room / wedge strategy): https://claude.ai/code/artifact/68dc73b4-534a-470b-83ec-fabaf0c3bee9
- **Go-Live Kit (operational source of truth, being kept updated as real transactions happen)**: https://claude.ai/code/artifact/bda3fc83-c6b5-455d-a4b5-3f0fb2b97f47

## Core finding
Ostazi had ~40 backend phases shipped against 5 real bookings — a
feature-factory pattern. The "18 verified tutors across 14 provinces"
was seed/demo data (`apps/api/scripts/seed-demo.ts`), not real recruited
supply — a live trust issue (fake "verified" badges to real visitors),
not just a thin-liquidity number.

## Strategy chosen
Primary wedge: Damascus, Grade-12 Baccalaureate Scientific track (Math/
Physics/Chemistry/Biology), parent-payer, hybrid delivery, exam-prep
urgency. North Star: **completed lessons + repeat bookings in the
Damascus wedge** — not signups/tutor-count/traffic. Operating sequence
(see Go-Live Kit for full detail): SAFE -> REAL SUPPLY -> REAL DEMAND ->
MATCH -> TRANSACTION -> RETENTION -> REFERRAL -> DATA -> PRODUCTIZATION.
Explicit rule: do not resume feature/engineering work (RUN 2) until
there's a real Demand Ledger (the shipped TutorRequest pipeline, seeded
with real rows) and/or real recruited teachers — building ahead of that
data repeats the diagnosed problem.

## Shipped and live (commits `7810593`, `3e688c0` on `master`, deploy verified via direct prod API calls)
- Test suite restored: 287-288/288 (was silently ~16% passing).
- Demand-capture pipeline: `TutorRequest` model, full CAPTURED->
  CONTACTED->MATCHED->BOOKED->COMPLETED->NO_SUPPLY/LOST pipeline, public
  form at `/tutor-requests/new`, admin ops queue + real subject×
  governorate demand-signal aggregation, auto-completes via a booking-
  completion hook.
- `TeacherProfile.isDemoSeed` added, excluded from public search/
  profile/sitemap.
- Search filters completed: price range, mode (fixed a real inclusive-
  match bug), availability-day, on top of existing subject/gender/
  proximity.
- Teacher verification reinstate (suspend had no way back).
- Mobile booking-widget date/time overlap fixed.
- Migration safety catch: stripped unrelated pre-existing schema drift
  (RecurringBookingSeries/SavedIntent) out of a generated migration
  before it could ride along into a prod push — that drift is still real
  and undealt-with, not urgent, flag if touching those models later.

## Known open gap — needs Zoher, not more engineering
The isDemoSeed fix only stops *future* fake profiles from showing; the
18 already live in prod still show (confirmed: `GET /teachers` returned
18 post-deploy). `apps/api/scripts/backfill-demo-seed-flag.ts` is
written and locally verified (dry-run by default) but needs someone with
the prod `DATABASE_URL` to run it — not run against prod this session,
no prod credentials in this environment, by design. Exact command in the
Go-Live Kit.

## Blockers, all Zoher's / real-world, not code
WhatsApp Business Manager template approval (slow, ~24-48h, start
first), Sentry account (5 min), running the backfill script, seeding the
Demand Ledger with real rows before broad teacher recruiting, then
actual recruiting/outreach. See [[project_ostazi_run1_golive_2026]]'s Go-
Live Kit link for exact copy-paste steps and ready-to-send messages.

## For the next session that touches this project
Check the Go-Live Kit artifact FIRST (it's meant to be updated as real
transactions happen — treat it as more current than this memory if they
diverge). Don't start RUN 2 engineering until real Demand Ledger data
and/or real teachers exist. Related: [[project_ostazi_audit_log_cron_2026]],
[[feedback_ostazi_deploy_workflow]].
