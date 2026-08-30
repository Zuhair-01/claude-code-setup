# Multi-Account Handoff Protocol

Zoher runs Claude Code from two separate Claude Pro accounts (switched via
CC Switch), both pointed at the same local files. Neither account can see
the other's conversation directly. The Second Brain vault is the durable,
always-available channel between them and stays the single source of
truth for this — a peer session being live right now (check `ListAgents`)
adds a fast live push on top of it via `SendMessage`, see Rule 2's
addendum below (`handoff-broadcast` skill); it is never a substitute for
the vault entry. Handoff log lives at:

`C:\Users\Zoher\Desktop\Empire_Base\Second_Brain\Workflow\20 - Areas\Handoff Log.md`

(same PARA vault as autopilot_log.md, claude_mem.log, etc — nothing lives
outside it for this).

## Rule 1 — Read it first
At the start of any session, read the top (newest) entry in the Handoff
Log. If it's marked active, that's the other account's in-progress work —
resume from its "Next step," don't restart or re-derive from scratch.

## Rule 2 — Log entries are cheap, don't spam them
Do NOT write a new entry on every reply — that burns tokens for no reason.
Append a new entry only when ONE of these happens:
- A major milestone finishes (a phase, a working feature, a passing test
  suite, a shipped fix — not "edited a function").
- ~20-30 min of continuous work has passed since the last entry (rough
  gauge, not a stopwatch — use judgment).
- A usage/rate-limit warning appears (session limit, weekly limit,
  "running low," etc) — write immediately, this can't wait, the limit may
  cut you off mid-response with zero further warning.
- Zoher explicitly says he's switching, stopping, or hit a limit.

Each entry: timestamp, account, task, done-so-far (delta since last entry
is enough, don't re-summarize the whole history), exact next step,
blockers, files touched. Specific enough that a cold instance with zero
memory could pick it up. Mark it `active` while true; the next reader
marks it `resolved` once picked up (don't delete old entries — the trail
is the point).

**Every time you write a Handoff Log entry, the continue-prompt lives INSIDE
that entry itself, not only in the chat reply.** Write it as its own
"Continue-prompt for next session/context reset" block at the end of the
entry, in the vault file — a short, self-contained block for pasting into
the next session (new window, new account switch, whatever). Point it at
this log entry (tell the next session to read it first) rather than
re-explaining everything inline, state the concrete next action in 1-2
sentences, and carry forward any standing instructions that would otherwise
be lost (e.g. "don't push yet," "frontend revamp is now authorized,"
effort/model level if it matters). The reason it has to be IN the entry, not
just relayed to Zoher in chat: a cold session picking up the vault file
directly (another account, a session reconstructing per Rule 3, a peer
reading it mid-task) never saw that chat message — if the continue-prompt
only exists there, it's lost to everyone except the one person it was typed
to. Also paste the same block into the chat reply as before (that part
hasn't changed) — do both, every time, automatically, without being asked.

**Rule 2 addendum — broadcast it live when a peer is actually running.**
After writing the entry, run `ListAgents`. If it shows any live peer
session, also invoke the `handoff-broadcast` skill: send the same handoff
(pointer to the entry + condensed summary + open decision points + a
claim/dedup line so two sessions don't grab the same work) via
`SendMessage` to every peer it finds whose project/repo plausibly overlaps
with this one — same working tree, same repo, or a shared file/module you
touched — not just the vault file. Skip a peer that is verifiably on a
different, unrelated project (different repo entirely, no plausible file
overlap) — the vault log entry alone is correct for them; a direct
SendMessage to an unrelated peer is noise, not a handoff. When in doubt
about overlap, broadcast — this exception is for clear-cut "different
project" cases only, not a reason to skip broadcasting by default. Skip
broadcasting entirely when `ListAgents` shows no peers — the file entry
alone is correct then, same as before this addendum existed. This is what actually happened when
Zoher said "give it to the ai and handoff and everything so the main
session organize n analyze it n it decides" — formalized here so it's the
default at every future milestone/rate-limit entry, not a one-off.

## Rule 3 — No log entry? Reconstruct, don't guess blind
If the top entry is stale/resolved and there's no active handoff (e.g. a
hard cutoff happened with zero warning — this WILL happen sometimes),
reconstruct the likely state before resuming:
1. `git log -10 --oneline` and `git status` / `git diff` in the relevant
   project (clip-platform, OmniRoute, etc are git repos — use them).
2. Most recently modified files (mtime) in the working directory.
3. The last resolved log entry as a baseline; treat the gap between its
   timestamp and now as "probably continued in that direction."
Tell Zoher explicitly: "no fresh handoff found, reconstructing from
git/file state, here's what I think was happening — confirm before I
continue." Never silently assume a full picture from partial signals.

## Rule 4 — Don't collide
Both accounts share the same files but should not run at the same moment
on the same task. One account works, one is idle/switched-away. If Zoher
asks "what's the other account doing," read the Handoff Log, don't guess.

**Rule 4 addendum — when Zoher DOES deliberately run multiple sessions
concurrently in the same working tree** (different threads on the same
project, e.g. one on a 3D pipeline, one on solution diagrams, one on a
photo/accuracy sweep — this has actually happened and worked). This is
allowed, not a violation of Rule 4 above, but only if every session follows
this protocol:
1. **`git status` before every single commit**, not just at session start.
   Never assume the working tree matches what you last saw — another
   session's uncommitted edits can appear between your own tool calls.
2. **Stage only the files you yourself edited this turn**, explicitly by
   name (`git add path/to/file.ts`) — never `git add -A` or `git add .` in
   a shared tree. A file another session has mid-edit and uncommitted
   (`package.json`, a config, anything you didn't touch) must never end up
   in your commit, even by accident.
3. **A stale/torn build or "photo suddenly missing" symptom is not
   automatically a real bug** when multiple sessions are writing to the
   same output directory (e.g. `dist/`) concurrently — rebuild clean first
   (delete-then-regenerate if the build tool allows it) and re-check before
   spending time debugging what may just be a torn concurrent write.
4. **Broadcast always now, not just on detected overlap — Zoher's explicit
   standing rule (2026-08-23), supersedes the old "only on real overlap"
   guidance.** Every session in a concurrent multi-session run must:
   - **Before starting a task**: run `ListAgents`; if any peer is live,
     `SendMessage` every one of them a short claim — what you're about to
     work on, which file(s)/area, so two sessions never grab the same work
     blind. Don't wait to detect an actual collision first — announce the
     claim up front, every time, not just when a conflict already looks
     likely.
   - **When you finish something** (a task, a fix, a milestone — same bar
     as a Handoff Log entry, not literally every tool call): `SendMessage`
     every live peer what you did and its real state (pushed/committed
     commit hash, tests passing, what's still open) — not just "done", the
     specifics a peer would need to avoid re-doing or colliding with it.
   - If a peer flags a collision or a bug in your lane, verify it against
     the live file state before assuming either your fix or theirs is
     wrong — they are very often complementary (one session's data-layer
     fix depends on another session's code-layer fix, or vice versa), not
     a real conflict.
   - This is heavier than the old rule on purpose — Zoher wants every
     concurrent session visible to every other one at all times, not just
     when something might collide. Use the `handoff-broadcast` skill's
     claim/dedup pattern for the message shape.
5. **Never resolve an apparent collision by discarding the other session's
   work.** If two sessions touched the same function, read both diffs, keep
   whichever is more complete/correct (usually the union of both), and
   tell the other session what you did via `SendMessage`.

## Rule 5 — This vault is the brain, not a dumping ground
Anything meant to persist across sessions/accounts (handoff state, logs,
plans, reference docs) belongs in the Second Brain vault under the right
PARA folder (00-Home, 10-Projects, 20-Areas, 30-Resources) — not as loose
files in random project folders or `.claude`. If unsure where something
goes, check the existing folder structure first before creating new ones.

## Rule 6 — Check OVERSEER before building or claiming "no skill for that"
`~/.claude/overseer/` is a separate system from the Handoff Log above — the
Handoff Log carries cross-account *state* for one project; OVERSEER is a
capability index covering ~3,650 skills/agents/tools kept off-context until
searched, so routine sessions don't pay to load a library most tasks never
touch. Before writing custom code/prompts for a nontrivial task, or before
telling Zoher "there's no skill for X," run
`python ~/.claude/overseer/search.py <keywords>` — a match may already
exist (skill, agent, or reference doc) and duplicating it wastes both
tokens and Zoher's time. `index.tsv` in that folder is the raw index if a
direct grep is faster than the search script for a specific lookup.

## Rule 7 — The standing routing protocol: understand → route → execute
For every substantive task (not simple Q&A), follow this sequence before
writing code or output, in order:
1. **Understand the task/project first.** Read what's actually being asked,
   check relevant memory/project files, and form a real picture of the goal
   before reaching for any tool — routing off a half-understood request
   produces a wrong skill stack no matter how good the router is.
2. **Route it — invoke `skill-router`'s logic** (its SKILL.md is the live
   spec: classify domain + action type, score candidate skills, output an
   ordered stack with INVOKE/REF per skill). This is the "skill-router" the
   OVERSEER hook prompt refers to as "the skill router."
3. **Cross-check OVERSEER, every time** — not just when a skill seems
   missing. `skill-router`'s Step 2 already mandates this: check the live
   skill listing first (free), then `python3 ~/.claude/overseer/search.py
   <keywords>` against the ~3,650 off-context skills/agents, then merge
   both into the stack. Never invoke a skill name that hasn't been
   confirmed to exist in one of those two checks.
4. **Execute using the best-fit skill(s) found**, most-specific-wins, and
   only after the stack is chosen — don't build custom/generic output when
   a sharper matching skill exists.
This is the intended default behavior of `skill-router` + OVERSEER
together; the automatic `UserPromptSubmit` hook (`overseer/directive.py`)
only injects a reminder text every turn — it does not, by itself, force
step 2. Treat that reminder as the trigger for this whole rule, not just
for the third-party-lookup case it literally describes.

**Frontend sub-rule:** any frontend/UI task that calls for a specific
real-world visual or motion look (not pure logic/layout with no look
requested) MUST route through `open-pinterest` first — source the actual
reference (image or video), evaluate it against the brief, download,
background-cut if only the subject matters — before handing off to
`taste-skill` / `motion-ui` / `threejs` / `frontend-design` / whichever
`BUNDLE-B-frontend` skill builds the component. This is wired into
`BUNDLE-B-frontend`'s Quick Start; this line makes it a hard requirement,
not a suggestion.

## Rule 9 — Keep the open-pinterest repo and local skill in sync
The public repo (github.com/Zuhair-01/open-pinterest) and the local skill
at `~/.claude/skills/open-pinterest/` are two separate copies. Whenever
one is edited, update the other in the same session — they drifted once
already (video-download capability landed in the repo before the local
install caught up). Repo ships as an installable Claude Code plugin
(`.claude-plugin/plugin.json` + `marketplace.json`).

## Rule 8 — Security is a build-time gate AND a pre-ship gate

**Build-time (new, 2026-08-29):** the moment a task involves writing or editing
code — an endpoint, a query, auth, a payment/webhook handler, an upload, an
external URL fetch, CORS/headers, an AI tool-call, or anything touching secrets
or user data — load the `secure-by-default` skill and hold its rules WHILE
writing the diff, then run its 10-second self-scan after each diff. This is
enforced by two hooks: `overseer/secure_build_gate.py` (UserPromptSubmit — fires
a reminder on build prompts) and `hooks/secure-write-scan.js` (PostToolUse
Write|Edit — lints the diff for hardcoded secrets, string-built SQL, raw HTML
sinks, permissive CORS, unverified webhooks, IDOR-shaped id lookups). Treat any
`[secure-write-scan]` advisory as a fix-now, not a later-TODO. Full reasoning:
`Second_Brain/30-Resources/Curriculum/Product_Business_5_Pillars_Mastery.md` →
"Deep Dive 1 — Security".

**Pre-ship:** before calling any app, website, or feature "done" or "ready to ship" —
including quick prototypes and internal tools — run the **Phase 0:
Vibe-Code Pre-Ship Gate** checklist in `~/.claude/skills/security-audit/
SKILL.md`. It covers the failure modes AI-generated code actually ships
with: exposed secrets/.env, missing auth/authz, IDOR, open DB/bucket
permissions, injection (SQL/NoSQL/command/XSS/SSRF), CORS/headers/cookie
misconfig, unprotected admin/debug routes, frontend-only payment checks,
webhook signature checks, AI-feature prompt-injection/permission bypass,
and "AI-generated code merged without human review." This is a gate, not
a suggestion — flag any unchecked item to Zoher explicitly rather than
silently shipping past it. Escalate to `pentest-checklist` /
`threat-modeling-expert` (Phases 1-7 of the same bundle) for anything
handling real payments, PII, or regulated data.

## Rule 10 — Suggest parallel sessions on complex tasks, never open them unasked

Never use the `Agent` tool to parallelize work — it drains tokens badly
(cold-start cost per spawn). The approved alternative, when Zoher wants
it, is multiple real Claude Code sessions (or OpenCode sessions — his
alt-CLI, set up in this same environment) running inline and coordinating
via `ListAgents` + `SendMessage`, the same mechanism Rule 4's addendum
already uses for concurrent multi-session work.

**Detect, then suggest — don't act.** At the start of any task complex
enough to warrant it (naturally splits into independent chunks: several
unrelated files/modules/categories, a sweep across many similar items, a
build with clearly separable subsystems — roughly the same bar as "would
justify Rule 4's addendum if Zoher were already running multiple
sessions"), surface a short suggestion before starting solo work: name the
natural split, a sane session count, and ask whether he wants it run in
parallel (Claude Code sessions, OpenCode, or a mix). Then proceed solo
unless he says yes — opening sessions or deciding a session count on your
own initiative is exactly what he told you not to do (2026-08-24,
see memory `feedback_multi_session_orchestration.md`).

**If he says yes, make it actually operational, not just a suggestion:**
1. Tell him the concrete commands/steps to open each additional session —
   he opens them, since this session cannot spawn a new terminal window
   itself. In a new PowerShell window, `cd` to the same working
   directory, then run `claude` for a Claude Code session or `opencode`
   for an OpenCode session (both bare CLI words, both on PATH — confirmed
   2026-08-24: `C:\Users\Zoher\.local\bin\claude.exe`,
   `...\WinGet\Packages\SST.opencode...`). Mix freely per his choice.
2. Once a peer appears in `ListAgents`, follow Rule 4's addendum in full:
   claim your slice via `SendMessage` before starting, broadcast on every
   milestone, `git status` before every commit, stage only your own files.
3. Split the work along the natural boundary you already identified —
   don't re-negotiate the split after the fact.

## Rule 11 — ox-alpha skill: Zoher's preferred working style

`~/.claude/skills/ox-alpha/SKILL.md` is the distilled operating system of
**ox-alpha** — the OpenCode model Zoher trusts for *how* it works, written
by that model itself ([opencode], 2026-08-26; audited + hardened same day).
Load it IN FULL whenever:

- Zoher says "use ox-alpha", "ox mode", "work like ox", or similar.
- A task is frontend/UI work, code quality-sensitive, or he asks for
  terse/efficient behavior.

What it enforces (details in the skill): sub-4-line default chat replies
with no preamble/postamble, read-before-edit + mimic-codebase-conventions +
surgical diffs, a concrete verification gate (lint/typecheck/tests actually
run before saying "done" — agrees with `sp-verification-before-completion`),
explicit git discipline (no commits unasked, stage by name only),
2-attempt retry cap with timeouts, frontend work routed through the
existing specialist stack (`open-pinterest` → `apex-frontend-lab` →
`taste-skill` per Rule 7), and honest uncertainty language.

**Terseness exemption (critical):** the short-reply rule applies to CHAT
only. Handoff Log, Session Bus, memory-log, and vault entries follow Rules
2/4/8 detail requirements in full — never write terse shared-state records
because ox mode is active.

This skill does NOT replace any rule above — it layers on top of them.
It also does not change identity: you remain Claude Code; only the
working style matches ox-alpha's.
