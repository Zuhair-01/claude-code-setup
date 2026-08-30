---
name: feedback_alwazour_studio_auto_push
description: "Zoher wants every alwazour-studio (Empire_Base) fix committed+pushed immediately, not batched or asked about"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7536e7d1-7b3b-4743-8243-8608ac921b2f
  modified: 2026-08-29T13:40:49.225Z
---

On alwazour-studio / Empire_Base work, commit and push each fix as soon as it's
built+verified — don't wait to be asked ("push n comit mate always", 2026-08-29).

**Why:** Vercel deploys straight from `master` on this project, and Zoher wants
fixes live without a separate push prompt each time.

**How to apply:** After any Empire_Base/alwazour-studio edit passes its build
check, `git add` the exact files touched (never `-A` in this shared tree —
see [[feedback_git_commit_scope_pathspec]]), commit, push to origin, done —
no confirmation step needed for this specific repo/workflow. Still `git status`
before every commit per the multi-session protocol (CLAUDE.md Rule 4 addendum).
