---
name: project-secure-by-default-gate
description: "Build-time security guardrail — secure-by-default skill + 2 hooks that fire on every code build so security mistakes are prevented while coding, not caught after. Built 2026-08-29."
metadata: 
  node_type: memory
  type: project
  originSessionId: 883fd098-546d-4355-9d00-96de63709faa
  modified: 2026-08-29T12:29:44.293Z
---

Zoher asked (2026-08-29) that security "works while they build so they don't make mistakes at all" — not just the pre-ship gate. Built a 3-layer system:

1. **`~/.claude/skills/secure-by-default/SKILL.md`** — build-time checklist, rules organized by surface (endpoint / query / auth / secrets / input / upload / SSRF / payment+webhook / CORS+headers / AI feature / deps / errors) + a 10-second post-diff self-scan. Points to curriculum "Deep Dive 1 — Security".
2. **`~/.claude/overseer/secure_build_gate.py`** — UserPromptSubmit hook (wired in settings.json after prompt_master_gate). Regex-detects build/code intent → injects a reminder to load `secure-by-default`. Silent on non-build/explain prompts.
3. **`~/.claude/hooks/secure-write-scan.js`** — PostToolUse Write|Edit|MultiEdit hook. Lints each written diff for: hardcoded secrets / live tokens, string-interpolated SQL, raw HTML sinks w/o sanitizer, `CORS *` + credentials, shell exec w/ input, webhook/payment POST handler w/o signature verify, id lookup w/o owner/tenant/session scoping (IDOR), error object sent to client, fast-hash on password. Advisory to stderr, never blocks.

Also: `security-audit/SKILL.md` gained a "three security layers" header; CLAUDE.md Rule 8 retitled "build-time gate AND pre-ship gate" with the hook details.

**How to apply:** on any code task, `secure-by-default` should already be nudged by the hook — load it and hold its rules per diff. Treat every `[secure-write-scan]` advisory as fix-now. Related: [[project_5_pillars_curriculum]], [[project_overseer]].
