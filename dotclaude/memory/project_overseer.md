---
name: project-overseer
description: "OVERSEER built 2026-07-15 — library+index+hook live. Context 27.9k → 10.5k/session. Steps 0-5 done, 6-8 (ledger/grader/evolve) not built."
metadata: 
  node_type: memory
  type: project
  originSessionId: db3ce43e-84b3-42b0-b855-c2ab9dc32365
---

OVERSEER is **built and verified** as of 2026-07-15 (design spec: `C:\Users\Zoher\.claude\OVERSEER-DESIGN.md`).

**Layout**
- `~/.claude/skills/` 221 live · `~/.claude/skills-library/` ~3,110 off-context
- `~/.claude/agents/` 164 live · `~/.claude/agents-library/` 137 off-context
- `~/.claude/overseer/` — `build_index.py`, `search.py`, `promote.py`, `directive.py`, `index.tsv` (3,632 rows: kind, loc, category, name, desc)
- Restore lists: `skills-library/.moved-manifest.txt`, `agents-library/.moved-manifest.txt`. **Nothing was deleted.**
- `UserPromptSubmit` hook → `overseer/directive.py` (~143 tok/prompt). Backup: `settings.json.bak-overseer-*`

**Result:** ~27,908 → ~10,524 tok/session. Verified end-to-end in a fresh session (Xero task → hook → search → found `xero-automation` in library → correct answer).

**Corrections to the design doc (it was wrong on these):**
- The "26 exact duplicate pairs" are **not** exact — all 26 differ in content (different coverage/generations). They were moved to the library, not deleted.
- The doc never measured **agents**, which cost ~60 tok each vs ~5 for a skill — **12× more expensive**. 301 agents = ~18k tok. The agent list, not the skill list, is now the dominant cost.

**Key facts**
- Live agents (~9,419 tok) are now the biggest remaining line item. Cutting to ~40 core would reach ~3.5k/session.
- `gsd-*` (33) + `understand-*` (10) must stay live — `/gsd:*` commands spawn them by name and they exist nowhere else.
- Library agents can't be spawned via `subagent_type`; use `general-purpose` + the agent's body as prompt.
- A skill description alone does NOT reliably trigger retrieval — verified twice. The **hook** is what makes it work. [[feedback-skill-router]]

**Not built (steps 6-8):** ledger, grader, proxy watcher, evolve loop. Without them there's no usage data, so "keep only what we use" is still guesswork.

**Gotchas:** Git Bash `cut -c` counts BYTES → corrupted CJK descriptions; indexer is Python and truncates by char. Windows console is cp1252 — no unicode in print. Rebuild index after any move: `python3 ~/.claude/overseer/build_index.py`.
