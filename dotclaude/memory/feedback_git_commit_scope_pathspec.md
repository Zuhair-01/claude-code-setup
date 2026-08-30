---
name: feedback-git-commit-scope-pathspec
description: "In a shared git tree, `git add <paths>` alone doesn't scope a commit — `git commit -m \"...\"` with no pathspec commits everything already staged, including another session's WIP."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bf602bf8-5d26-482d-b92f-6b0a955d47b6
  modified: 2026-08-28T20:19:10.715Z
---

`git add <specific paths>` only stages those paths — it does NOT limit what `git commit`
includes if something else was already staged in the index beforehand. Always scope the
commit itself too: `git commit -m "..." -- <same paths>`, not just the add.

**Why:** confirmed real incident, 2026-08-28, alwazour-studio (shared monorepo, multiple
concurrent Claude Code sessions per [[feedback_multi_session_orchestration]] and CLAUDE.md
Rule 4's addendum). Ran `git add <my 15 explicit files>` correctly, then `git commit -m
"..."` with no pathspec. A peer session (zoher-06) had separately staged their own files
(WhatWeBuild.astro, content.ts, services pages) before my commit ran — those rode along into
my commit since `git commit` with no pathspec commits the full index, not just what the most
recent `git add` touched. Initially misdiagnosed this as not-a-bug (checked `git show --stat`
but only read the first ~25 lines of long output and missed the file list) — had to be
corrected by the peer session re-verifying, then confirmed properly on a second look.

**How to apply:** in this shared multi-session tree, treat `git add <paths>` as necessary but
not sufficient. Every commit that follows must also pass `-- <paths>` to `git commit` itself,
so the commit is scoped to exactly the intended files regardless of what else sits staged in
the index from a concurrent session. When verifying a commit's contents after the fact, read
the FULL `git show --stat` output (or pipe through `wc -l` to sanity-check line count first),
not just the first screen — a long commit message can push the actual file list past what a
truncated read shows.
