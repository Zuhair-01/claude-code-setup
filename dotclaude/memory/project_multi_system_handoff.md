---
name: multi-system-handoff
description: Cross-tool/cross-account handoff protocol (2x Claude Pro + Codex) sharing state via the Second Brain vault — invoke when switching accounts/tools or resuming interrupted work
metadata: 
  node_type: memory
  type: project
  originSessionId: a970f43c-e52d-4c7c-acd3-d6679aab1713
  modified: 2026-08-15T15:10:38.310Z
---

Built 2026-08-15: a handoff system so Zoher can run two separate Claude Pro
accounts (switched via CC Switch) plus Codex, all against the same local
files, and hand work off between them without re-explaining context.

**Shared channel:** `C:\Users\Zoher\Desktop\Empire_Base\Second_Brain\Workflow\20 - Areas\Handoff Log.md`
— a log (newest entry on top, not overwritten) in the existing PARA vault,
per [[project_empire_base_agency]].

**Auto-loaded rules, one per tool:**
- Claude Code (both accounts) → `C:\Users\Zoher\.claude\CLAUDE.md`
- Codex → `C:\Users\Zoher\.codex\AGENTS.md`
Both files carry the same protocol: read the log first on session start;
only append a new entry on a real milestone / ~20-30min elapsed / a
usage-limit warning / explicit "switching" from Zoher (not every turn —
avoids token waste); if no active entry exists (hard cutoff, no warning),
reconstruct from `git log`/`git status`/`git diff` + recent file mtimes
before resuming, and say explicitly that it's reconstructing rather than
silently guessing; don't run two tools/accounts on the same task at once.

**Why:** Zoher wanted more usable capacity than a single Pro plan without
paying for Max, using two Pro accounts + existing Codex access as a "smart
switch" system instead. Rejected a standalone `.claude/HANDOFF.md` file in
favor of the vault — "everything stays there, not just files takin space
randomly."

**How to apply:** When Zoher mentions switching accounts, hitting a limit,
or asks what the other account/tool was doing mid-task, this is the
system — check the Handoff Log, don't ask him to re-explain. If extending
this system later (e.g. adding a third Claude account, or a different
tool), mirror the same pattern: one instructions file the tool auto-loads,
pointing at the same shared log.
