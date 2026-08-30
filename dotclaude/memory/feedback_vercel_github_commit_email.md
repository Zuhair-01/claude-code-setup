---
name: vercel-github-commit-email
description: "Vercel deploys fail with opaque \"fetch failed\" when the git commit author email isn't a verified/public email on the connected GitHub account — check the dashboard, not just the CLI."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 74906564-ca95-4b29-bc30-4b3dc9038a37
  modified: 2026-08-21T19:45:46.843Z
---

Vercel's CLI (`vercel deploy --prod --yes`) reports a generic `{"status":"error","reason":"deploy_failed","message":"fetch failed"}` after upload/build starts — this hides the real reason. The actual cause is visible **only in the Vercel dashboard** deployment page: "Deployment Blocked — the commit email X could not be matched to a GitHub account."

**Why:** Vercel's GitHub integration checks the pushed commit's author email against emails on the connected GitHub account (a security measure). If the local `git config user.email` doesn't match a verified email on that GitHub account, the deploy silently blocks — the CLI never surfaces this, only the web dashboard does. This is the second time this exact symptom has appeared (first: clip-platform project, logged in Handoff Log 2026-08-21; second: nabd project, same session).

**Fix:** Use GitHub's own noreply address for that account instead of guessing a personal email — it always works and needs no account settings changes:
```
git config user.email "{numeric-id}+{github-login}@users.noreply.github.com"
```
Get the numeric id with `gh api user --jq '.id'`. A plain personal email (even the account owner's real Gmail) can fail two ways: (1) not matched by Vercel if unverified/not public, and (2) rejected outright by GitHub's push protection ("GH007: Your push would publish a private email address") if it's not a verified public email on the account.

**How to apply:** Whenever a Vercel CLI deploy fails with an unhelpful `fetch failed` after the build appears to start, open the deployment's Inspect URL in a real browser (`get_page_text` on the dashboard page) before retrying blindly — the CLI's error and the dashboard's error are not the same information.

**Standing instruction from Zoher (2026-08-21):** always commit/push using the "axissummer" identity — [[project_axissummer_universal_account]] — this is his universal GitHub/Vercel account for all projects, not `bizwithzuhair@gmail.com`. Since a plain `axissummer@gmail.com` email got rejected by GitHub push protection, the noreply form above is the working substitute until confirmed otherwise.
