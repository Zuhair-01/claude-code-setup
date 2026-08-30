# OVERSEER — Design Spec
**Date:** 2026-07-15 · **Status:** designed, not built · **Origin session cost:** ~$60 (build in a fresh session)

## The idea (Zoher's words)
One agent responsible for everything: reads any incoming task → derives goals → picks the agent/team +
skills + tools → executes → then a retrospective agent studies the run, learns faster/better ways, so the
system evolves and compounds — smarter, cheaper, faster over time.

Zoher's refinement: **do not delete skills.** Organize them into real teams, extract their value, and keep
untriggered ones — "cases we just haven't reached yet" is not the same as useless. He is right about this.

---

## Measured facts (verified 2026-07-15)
| Fact | Value |
|---|---|
| Skills installed (`~/.claude/skills`) | **3045** (252 MB) |
| Context cost of the skill-name list | **~14,800 tokens, every session** |
| Distinct skills ever invoked (308 transcripts) | **9** |
| `-automation` SaaS connectors | **921** (30% of library) |
| Exact duplicate pairs (underscore vs hyphen) | **26** |
| Skill path override in `settings.json` | none → default path, so **moving works** |

**Caveat on the "9":** grep only caught explicit `Skill` tool calls matching `"skill":"..."`. Skills auto-loaded
by description-match or hooks would not appear; older transcripts may log differently. It undercounts, possibly
by a lot. Direction is not in doubt; the exact number is.

Skills observed in use: `superpowers:brainstorming` (4), `using-superpowers`, `ui-ux-pro-max`,
`superpowers:writing-plans`, `skill-router`, `redesign-skill`, `notion-template-business`,
`mpocock-obsidian-vault`, `artifact-design`.

---

## Key insight
The 14.8k tokens is **not the cost of having skills. It's the cost of listing them.** Separable.
Nothing needs deleting for the tax to disappear. This dissolves the delete-vs-keep dilemma entirely.

---

## Architecture

```
LIBRARY   all 3045 → ~/.claude/skills-library/     on disk · indexed · 0 context cost
                                                    nothing deleted · instantly restorable
TEAMS     Zoher's real domains → always loaded      ~500 tok instead of 14,800
INDEX     one small skill, greps library on demand  → first Stripe task: finds it, loads it
LEDGER    every run scored → JSONL                  the artifact that compounds
EVOLVE    weekly: ledger → rewrites team manifests
```

**The teams manifest and OVERSEER's hint table are the same file.** Teams give the router its starting map;
the ledger corrects that map as real runs come in. Zoher's "teams" idea and the hint table converged.

### Proposed teams (Zoher's 4 pillars + what he actually builds)
`clipping` · `ai-ugc` · `arabic-localization` · `b2b-netherlands` · `platform-build` · `agents-infra`
· `research-intel` · `design-frontend`

Everything not in a team goes to the library. It is not adjudicated, not deleted, not team-assigned —
just available. That is the whole point: **you never have to decide about the long tail at all.**

---

## The loop

```
Your prompt
   ↓
[UserPromptSubmit hook]  ← injects routing directive + team manifest / ledger hints
   ↓
ROUTE   goal-analyzer → task_class · skill-router → skills · agent pick → team
   ↓    writes intent row to ledger
EXECUTE
   ↓
[Stop hook] → GRADER (Haiku, ~800 tok) → verdict + score + confidence → ledger
   ↓
PROXY WATCH → next prompt back-annotates (retry? interrupt? "no"? accepted?)
   ↓
DIVERGENCE? → grader vs proxy conflict → ask Zoher (rare) → ground truth → ledger
   ↓
EVOLVE (weekly, batched) → reads ledger → rewrites team manifests
```

### The grader
Purpose-built. **Not** an off-the-shelf agent — Reality Checker / gan-evaluator are "All tools" agents with fat
prompts; spawning one per task is the exact token burn we're avoiding. Harvest their priors, build small:

- Model: **Haiku 4.5**, ~200-token system prompt, structured JSON out
- Input: `(goal, output, route, tokens, elapsed)` — **never the full transcript** (that's where cost lives)
- Steal from **Reality Checker**: the anti-sycophancy prior (defaults to NEEDS WORK, demands proof)
- Steal from **ecc:gan-evaluator**: rubric-scoring shape + actionable deltas back to the router
- Reference at build time only: `gsd-eval-planner`, `llm-evaluation`, `eval-harness`, `agent-eval`,
  `advanced-evaluation`, `trust-calibrator`
- Cost: ~800 tok/run

### Signal design (why it's a mix)
- **Grader** scores every run — cheap, total coverage.
- **Proxies** audit the grader for free — retry / rephrase / interrupt / "no" = bad run, regardless of score.
- **Human** is asked *only when grader and proxies disagree.* Agreement is silence; conflict is the trigger.
  Ground truth exactly where it has value. Ask-rate falls as the grader improves → ask-rate is itself a health metric.

**A grader cannot validate itself.** If it drifts generous, every score still looks fine and the router optimizes
toward a lie with nothing to catch it. That's why the proxy audit is load-bearing, not decoration.

---

## Ledger schema (one append-only JSONL)
```json
{"run_id":"r-0001","ts":"2026-07-15T14:22:03Z","task_class":"video-gen","goal":"<one line>",
 "route":{"skills":["seedance-2"],"agents":["Rapid Prototyper"],"model":"sonnet"},
 "tokens":12400,"elapsed_s":88,
 "grade":{"verdict":"good","score":0.84,"dims":{},"confidence":0.7,"why":"<one line>"},
 "proxy":{"retry":false,"interrupt":false,"correction":false,"accepted":true},
 "divergence":false,"human":null}
```
Timestamps ISO-8601 UTC. `task_class` MUST come from the closed vocabulary (see risk 1).

---

## Build order
0. **VERIFY FIRST** — move ~20 skills to `~/.claude/skills-library/`, restart session, confirm the listing
   shrinks and context drops. If this fails, the design changes. Do not skip.
1. Kill the 26 exact dupes (same skill twice — no judgment call needed).
2. Move the library. Nothing deleted, fully reversible.
3. Write team manifests (~500 tok total).
4. Index skill — greps library on demand, loads on hit.
5. `UserPromptSubmit` hook — injects directive + manifest. **This is what makes routing real:**
   the existing `skill-router` memory is a suggestion Claude drifts from; a hook is the harness.
6. Ledger + grader + Stop hook.
7. Proxy watcher + divergence trigger.
8. Evolve step (weekly).

**Steps 1–4 are the certain win (~15k tok/session back). Steps 5–8 are the bet.**

---

## Known risks (do not paper over)
1. **Task classification is the whole ballgame.** Hints only compound if the same task lands in the same bucket
   every time. Free-form labels → ledger shatters into 100 classes of 1 run → learns nothing while looking fine.
   **Mitigation: closed vocabulary, ~15 fixed classes. Non-negotiable.**
2. **Confounding.** "Route X scored 0.84" — was that the route, or an easy task? Nothing separates them, so the
   hint table can learn "easy tasks score well" and credit the route. No cheap fix. Accept it, don't pretend.
3. **Time to value.** Depends on task volume (unknown). At ~10 tasks/day it's weeks before any class has density.
   Not smarter tomorrow — smarter in a month, if it survives that long.
4. **Grader drift.** See signal design. Proxy audit is the only thing standing between this and self-congratulation.
5. **Overhead must pay for itself.** ~1k tok/task. One avoided bad route (a Workflow fan-out that should've been
   one Haiku call) pays for 100 runs. **If the ledger ever shows the loop costing more than it saves, kill it —
   and the ledger will show it.**

## What already exists (don't rebuild)
`skill-router` · `council` · `goal-analyzer` · `task-intelligence` · `agent-orchestrator` ·
`multi-agent-task-orchestrator` · `token-budget-advisor` · `continuous-learning` · `continuous-learning-v2` · `kaizen`

Missing, and the reason it never compounded: **an automatic trigger** (hook, not memory) and
**a learning substrate** (ledger nothing writes to, nothing reads from).

Absent despite memory claims — verify before citing: `skill-hunter`, `autopilot`, `self-heal`, `verify`, `evolve`.
