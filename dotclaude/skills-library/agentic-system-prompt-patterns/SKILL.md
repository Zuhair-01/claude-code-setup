---
name: agentic-system-prompt-patterns
description: Distilled patterns mined from public/leaked system prompts of production agent products (Cursor, Devin, Manus, v0, Windsurf, Replit, Lovable, Claude, GPT, Gemini, Grok, Warp, Xcode) and curated role-prompt libraries. Use when authoring or auditing a subagent/system prompt, not for general prompt-engineering theory (see prompt-engineering-patterns for that).
license: MIT
source: https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools, https://github.com/asgeirtj/system_prompts_leaks, https://github.com/f/prompts.chat
---

# Agentic System Prompt Patterns

What actually recurs across shipped, production agent system prompts — as opposed to prompt-engineering theory. Use when writing a new `.claude/agents/*.md` subagent or reviewing an existing one.

## Structural patterns that recur across top tools

1. **Identity + explicit non-goals first.** One or two sentences: who the agent is, what it's for, what it explicitly does NOT do. This is what prevents scope creep on turn 5, not a general "stay focused" instruction.
2. **Tool-call discipline.** Explicit rule for when to call a tool vs. answer directly, and a hard ban on narrating a call ("I will now call X") instead of just calling it.
3. **Plan-before-act for multi-step work.** Devin/Manus/Cursor-style prompts force an explicit plan or todo list before non-trivial edits and require checking items off as they complete — the mechanism, not a vague "be organized" instruction.
4. **Mandatory verification loop.** Every serious coding-agent prompt has a step requiring tests/lint/build to run before declaring done — success claims must be evidence-backed, never assumed.
5. **Terse, non-sycophantic default voice.** Production prompts explicitly ban filler ("Great question!", apologizing) and cap response length by default, expanding only when the task needs it.
6. **Concrete over abstract.** File paths with line numbers, exact commands, exact diffs — never prose descriptions of a change in place of the change itself.
7. **Guardrails as concrete triggers, not vibes.** Destructive-action rules are phrased as specific triggers ("before rm -rf", "before force-push") near the top of the prompt, not a blanket "be careful" — specificity is why they get followed.
8. **Explicit escape hatches for ambiguity.** Good prompts state when to ask vs. pick a reasonable default, instead of leaving it implicit — this is what prevents both over-asking and silent wrong guesses.

## Applying this when writing a new subagent

- Lead with identity + explicit non-goals.
- Give it one concrete verification step it must run before reporting success.
- State its default verbosity and the trigger for breaking from it.
- If it has destructive tool access, name the specific dangerous actions and the check required before each.

## Curated role-prompt seeds (from prompts.chat)

Starting skeletons only — always adapt identity/scope to the actual task, don't use verbatim:
- **Expert code reviewer**: "Focus on correctness, security, maintainability. For every issue, cite file:line and the concrete failure scenario, not just the rule violated."
- **Socratic teacher**: "Ask one guiding question at a time until the user reaches the answer themselves — never give it directly."
- **Devil's advocate reviewer**: "Find the strongest reason this plan fails. Do not soften the critique or suggest fixes unless asked."
- **Spec-to-tasks translator**: "Convert this spec into an ordered task list where each task is independently verifiable with an explicit Definition of Done."

## Deeper mining (not preloaded — read on demand)

- x1xhlol/system-prompts-and-models-of-ai-tools — 30+ tools, full prompt text per vendor.
- asgeirtj/system_prompts_leaks — Claude/GPT/Gemini/Grok/etc. leaked prompts by vendor.
- f/prompts.chat — community role-prompt library (PROMPTS.md).

Clone locally with `git clone --depth 1 <url>` when a specific tool's exact prompt structure is needed for a deep comparison; don't preload the raw text here to keep this skill cheap to index.
