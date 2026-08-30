---
name: Empire Automaton Integration
description: Automaton self-improving agent loop cloned and configured for Empire Base Agency's 4 pillars
type: project
originSessionId: cd483de6-9916-4ed9-87b9-769fa83f1ea4
---
## What was built

Automaton (Conway-Research autonomous agent framework) merged into the Empire Base Agency stack.

**Why:** Enable self-improving, autonomous operation of Empire's 4 pillars without constant human intervention — the agent earns its own compute, modifies its own tools, and spawns child agents per pillar.

## File locations

- **Automaton repo:** `C:\Users\Zoher\Empire_Base_Agency\Automaton\`
- **Empire config template:** `C:\Users\Zoher\Empire_Base_Agency\Automaton\empire_config_template.json`
- **Setup guide:** `C:\Users\Zoher\Empire_Base_Agency\Automaton\EMPIRE_SETUP.md`
- **Runtime config (after setup):** `~/.automaton/automaton.json`

## Two new Claude Code skills

1. **`/skill-hunter`** at `C:\Users\Zoher\.claude\skills\skill-hunter.md`
   - Searches for tools/agents/skills aligned with the 4 Empire pillars
   - Scores candidates on: Pillar Fit, Automation Depth, Composability, Maturity, Speed to Value
   - Auto-installs winners as skills or saves eval cards to vault

2. **`/council`** at `C:\Users\Zoher\.claude\skills\council.md`
   - Convenes 5 specialist agents in parallel: Strategist, Devil's Advocate, Executor, Finance Mind, Growth Hacker
   - Returns structured verdict: votes, top pros/cons, conditions, final recommendation
   - Council verdicts saved to `C:\Users\Zoher\Desktop\Empire_Base\Second_Brain\Workflow\10 - Projects\council_verdicts\`

## Agent architecture

```
EmpireAgent (Automaton loop) → surfaces decisions
    ↓
/council → 5-agent parallel evaluation → verdict
    ↓ approved
/skill-hunter → finds + installs tools
    ↓
EmpireAgent → self-improves with new tools → repeat
```

## Child agents (when Automaton runs)

Up to 3 child agents, one per pillar with independent wallets:
- ClipAgent (Clipping Factory)
- UGCAgent (AI-UGC + Arabic)
- B2BAgent (B2B Netherlands)

## Safety rails

- `requireCreatorApprovalForPurposeChange: true` — agent can't change its own mission
- `soulAlignmentThreshold: 0.75` — high alignment bar
- Treasury: max $0.10/turn, $2.00/day
- Constitution in `constitution.md` — immutable 3-law governance

## Automation layer (persistent, runs without Claude Code open)

3 layers of automation, all writing to `autopilot_log.md` in the vault:

**Layer 1 — n8n workflow** (import and activate for 24/7 background runs):
- File: `C:\Users\Zoher\Empire_Base_Agency\Automation_Code\n8n_Workflows\empire_autopilot_n8n.json`
- Daily pulse (8:03am, Haiku) + Weekly skill hunt (Mon 9:07am, Sonnet) + Weekly full cycle (Wed 9:03am, Sonnet)
- Calls Anthropic API directly, writes results to vault — needs Anthropic API key in n8n credentials

**Layer 2 — Windows Task Scheduler** (run once as Admin to register):
- Script: `C:\Users\Zoher\Empire_Base_Agency\Automation_Code\empire_autopilot_scheduler.ps1`
- Runs Claude CLI headlessly on the same schedule as n8n
- Command: `! powershell -ExecutionPolicy Bypass -File "C:\Users\Zoher\Empire_Base_Agency\Automation_Code\empire_autopilot_scheduler.ps1"`

**Layer 3 — Claude Code session crons** (active while Claude Code is open):
- Daily pulse job ID: a26b5632
- Weekly skill hunt job ID: b2f86147
- Auto-expire after 7 days, re-run `/schedule` or restart session to renew

## Token budget tiers (enforced across all skills)

| Tier | Model | Use | Max agents |
|---|---|---|---|
| T1 Scout | haiku | research, search, status | 1 |
| T2 Analyst | sonnet | synthesis, mini-council | 3 |
| T3 Council | sonnet+opus | major decisions | 5 |

Impact score = Revenue(1-5) + Reversibility(1-3) + Cost(1-2) → T1(<4), T2(4-7), T3(8-10)

## How to apply

When Zoher asks about automating Empire operations, refer to this integration. Suggest `/autopilot` for any multi-step empire task. Use `/council --fast` for quick calls, `/council` for scored decisions, `/council --full` for major bets. Use `/skill-hunter --fast` for known gaps, `/skill-hunter --deep` for structural gaps.
