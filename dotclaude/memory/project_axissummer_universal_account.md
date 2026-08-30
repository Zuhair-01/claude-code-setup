---
name: project-axissummer-universal-account
description: "Zoher's universal account identity for GitHub/Vercel work across projects — use \"axissummer\" identity for commits/pushes, not personal email, unless told otherwise for a specific repo."
metadata: 
  node_type: memory
  type: project
  originSessionId: 74906564-ca95-4b29-bc30-4b3dc9038a37
  modified: 2026-08-21T19:47:05.302Z
---

Zoher's standing instruction (2026-08-21, during the NABD build): always push and commit under the "axissummer" identity — this is described as "our universal account for github n much more," tied to `axissummer@gmail.com` conceptually, and the Vercel account is `axissummer-8839`.

**Why:** He wants consistency across projects/sessions rather than commits attributed to ad-hoc emails picked per-repo (this session had defaulted to `bizwithzuhair@gmail.com`, which caused a real Vercel deploy block — see [[feedback_vercel_github_commit_email]]).

**How to apply:** At the start of any new repo/project work involving git commits meant to deploy via Vercel, check `git config user.email` and set it to axissummer's identity before the first commit, rather than defaulting to whatever's in the shell's ambient git config. Note: a plain `axissummer@gmail.com` was rejected by GitHub push protection (not a verified/public email on the connected account) — the noreply form `{id}+{login}@users.noreply.github.com` for the actual GitHub login tied to this account is the working fallback. Confirm with Zoher if a specific project needs a different identity.
