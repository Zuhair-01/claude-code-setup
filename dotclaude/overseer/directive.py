#!/usr/bin/env python3
"""OVERSEER UserPromptSubmit hook: injects the routing directive on every prompt.
Deliberately tiny -- it must cost far less than it saves. stdout is injected as context.
"""
import sys, os
try:
    sys.stdin.read()
except Exception:
    pass

IDX = os.path.expanduser("~/.claude/overseer/index.tsv")
n = 0
try:
    with open(IDX, encoding="utf-8", errors="replace") as fh:
        n = sum(1 for line in fh if "\tlibrary\t" in line)
except OSError:
    pass

lines = [
    f"[OVERSEER] {n} skills/agents exist OFF-context in ~/.claude/skills-library + agents-library",
    "(919 are SaaS/API connectors). Your skill/agent listing is NOT the inventory -- absence from it proves NOTHING.",
    'HARD RULE: do NOT say "no skill exists" / "not installed" / "nothing for that", and do NOT build from',
    "scratch, until you have run:  python3 ~/.claude/overseer/search.py <terms>",
    "If the task names ANY third-party service, platform, language, or domain, run it FIRST (~200 tok).",
    "Then Read the returned path and follow it. Browse: --cats. Details: skill `overseer`.",
    "If this is a substantive task (not simple Q&A): follow CLAUDE.md Rule 7 -- understand the task,",
    "invoke skill-router's classify+score logic, cross-check OVERSEER, THEN execute with the best-fit skill(s).",
]
print(" ".join(lines))
