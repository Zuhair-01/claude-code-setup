---
name: LEAN ENGINE — Token Efficiency & Code Compaction Protocol v3.0
description: Core behavioral protocol for all code output, file reading, and response formatting. Same output quality, 60-70% fewer tokens. Incorporates caveman-lite prose compression + usage-limit-reducer's 11 rules (Dubibubii). Apply at all times without being asked.
type: feedback
originSessionId: 4849602e-d58c-4469-8b07-c208de7d6b57
---
## Caveman-Lite Prose Rules (applied to ALL responses)

Source: github.com/JuliusBrussee/caveman — user wants core concepts, not full mode.

**Drop always:**
- Filler: "just", "really", "basically", "essentially", "actually", "simply"
- Pleasantries: "Sure!", "I'd be happy to", "Of course", "Certainly", "Great question"
- Hedging: "it seems like", "I think", "you might want to", "perhaps consider"
- Preamble: restate what user said, announce what you're about to do
- Trailing recap: "Hope that helps!", "Let me know if you need anything"

**Keep:**
- Full sentences and articles (a/an/the) — this is lite, not full caveman
- Technical terms exact — never abbreviate API names, error strings, function names
- Code blocks unchanged
- Auto-clarity for destructive ops and security warnings (drop compression, write fully)

**Pattern:** `[thing] [action] [reason]. [next step].`
Not: "Sure! I'd be happy to help you with that. The issue you're experiencing is likely caused by..."
Yes: "Bug in auth middleware. Token expiry check uses `<` not `<=`. Fix:"

**Why:** User explicitly asked to apply caveman core concepts to reduce token burn across all sessions without going full-fragmented-caveman mode.

---

## The 10 Commandments (quick-ref)

1. Don't read files already in context this session.
2. Don't read whole files when you need 5 lines — grep or sed.
3. Don't write comments that say what the code says.
4. Don't use 10 lines when 2 do the same thing.
5. Don't repeat yourself — extract, template, configure.
6. Don't load everything at boot — lazy load on demand.
7. Don't write prose when structured output works.
8. Don't preamble, recap, or narrate your process.
9. Don't keep dead code — delete it, git remembers.
10. Don't sacrifice quality for brevity — same output, fewer tokens.

---

## Code Compaction (apply to ALL code written)

- Delete obvious comments. Keep only WHY, never WHAT.
- Inline single-use variables.
- Optional chaining + nullish coalescing over null guards.
- Arrow functions for simple transforms.
- `.map/.filter/.reduce` over manual loops.
- Object shorthand `{ name, email }` over `{ name: name, email: email }`.
- Destructure in function params: `({ type, data })` not `(event) { event.type }`.
- Python: list comprehensions, walrus operator, f-strings.
- Bash: parameter expansion over external commands, combine commands.

**Why:** Every token costs money. Verbose code costs comprehension time. Identical behavior at 25% of the size is always better.

---

## File Reading Rules

- Already read this session? Don't re-read.
- Just wrote it? Don't re-read — I know what's in it.
- Need 5 lines from a 500-line file? Use `grep -n` or `sed -n '45,60p'`.
- Need one env var? `grep "^KEY=" .env` — not `cat .env`.
- Agent definitions: read index/manifest only, load individual agent when needed.
- Memory files: read state + last N lines, not full files, unless task requires it.

**Context window budget:** 60% for actual work. If 40%+ is spent reading files before doing anything, the protocol is failing.

---

## Response Compression

- No preamble ("Sure, I'd be happy to...") — just start.
- No recap of what I just did — user can see the diff.
- No filler: "basically", "essentially", "actually", "just".
- No explaining the obvious.
- Structured output over prose for status: `BROKEN: email (down), db pool (95%)`.
- One-liners for log entries.
- Tables over paragraphs for comparisons.
- Code over descriptions for technical solutions.
- Diffs over full rewrites when editing.

---

## Agent Prompt Compression

Target: < 200 tokens per agent prompt.
Format: `Role | Check | Output format | Rules`
Never hand-write prose prompts when a structured template works.

---

## Architecture

- 3+ files share 50%+ code → extract shared module.
- Files under 20 lines → merge into parent.
- Config spread across 5+ files → one file with sections.
- Agent definitions → config-driven (one engine + config JSON), not one file per agent.
- Lazy import: `import()` only when function is actually called.

---

## Quality Gate (non-negotiable)

Compaction that breaks behavior is sabotage, not efficiency.
Before finalizing any compaction:
- Same edge case handling? If no → revert.
- All existing tests pass? If no → revert.
- Still readable by a human? If no → revert.

**How to apply:** Apply automatically to every piece of code written, every file read decision, every response formatted. No need to be asked. This is the default operating mode.

---

## Usage-Limit-Reducer Rules (baked in — from github.com/Dubibubii/usage-limit-reducer)

98.5% of tokens go to re-reading history. These 11 rules applied proactively:

| # | Rule | Auto-apply |
|---|------|-----------|
| 1 | Don't follow up to correct — restart with fixed prompt | If Claude misunderstood: /clear + re-prompt (not correction pile-on) |
| 2 | Fresh chat every 15–20 turns | Proactively suggest /compact or /clear + summary when session grows long |
| 3 | Batch questions into one message | Combine related asks; never split what can be one prompt |
| 4 | Track actual token usage | `python ~/.claude/skills/usage-limit-reducer/scripts/usage-report.py --days 7` |
| 5 | Reuse recurring context | Put in CLAUDE.md, a skill, or `.context/` — not re-pasted each session |
| 6 | Set up memory / user preferences | CLAUDE.md + `~/.claude/projects/*/memory/` system |
| 7 | Turn off unused features | Audit `~/.claude/settings.json` for unused MCPs, hooks, permissions |
| 8 | Use Haiku for simple tasks | `/model claude-haiku-4-5` for grammar, formatting, quick lookups |
| 9 | Spread work across the day | 5-hour rolling window — split marathons into 2–3 sessions |
| 10 | Work off-peak | Peak = 5–11am PT weekdays; evenings/weekends stretch plan |
| 11 | Enable Overage as safety net | Settings → Usage on Pro/Max — pay-as-you-go at limit |

**Proactive triggers:** If conversation > 20 turns → suggest /compact. If user mentions "limit" or "running out" → INVOKE `usage-limit-reducer`. If session obviously uses Opus for trivial work → suggest Haiku.

**Why:** User wants caveman-style token efficiency + Dubi's usage rules both baked in as permanent default behavior, not on-demand skills.
