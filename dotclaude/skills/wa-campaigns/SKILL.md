---
name: wa-campaigns
description: Multi-project WhatsApp campaign platform for personalized outreach (per-person pitches, opt-out safety, dedupe ledger, dry-run default). Use when Zoher wants to contact users/leads/teachers/students via WhatsApp, run re-engagement campaigns, or set up outreach for ANY project (Ostazi, future products). Works identically from OpenCode and Claude Code.
---

# WhatsApp Campaign Platform (shared infra)

Location: `C:\Users\Zoher\.local\share\wa-campaigns\` - read its README.md first.
Full usage guide: `C:\Users\Zoher\.config\opencode\skills\wa-campaigns\SKILL.md` (same content, maintained by OpenCode).

## Commands

```
node C:\Users\Zoher\.local\share\wa-campaigns\wa-send.mjs <project>           # DRY RUN (default, no creds needed)
node C:\Users\Zoher\.local\share\wa-campaigns\wa-send.mjs <project> --live    # SEND (only after Zoher approves the preview)
node C:\Users\Zoher\.local\share\wa-campaigns\wa-send.mjs status <project>
node C:\Users\Zoher\.local\share\wa-campaigns\wa-send.mjs optout <phone>      # global, cross-project, permanent
```

## Hard rules

1. ALWAYS dry-run first; show Zoher the preview; `--live` only on his explicit go
2. Phone numbers never leave this folder - not into chat, vault, repos, or logs
3. Anyone replying "إيقاف"/"stop" -> run optout command immediately
4. New numbers: keep first campaigns under ~50 recipients (Meta quality rating)
5. Business-initiated WhatsApp requires Meta-approved templates per project
   (marketing category for pitches - see TutorLink-Syria docs/WHATSAPP-OTP-SETUP.md Step 4b)

## Adding a new project

Copy `projects/ostazi/` as the pattern: config.json + compose.mjs + audience.jsonl.
Feed audience from anywhere (DB exports, signups, scrapes). Ledger auto-prevents
double-contacting the same person for the same campaign.
