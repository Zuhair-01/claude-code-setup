#!/usr/bin/env python3
"""
UserPromptSubmit hook - build-time security guardrail.

When the user's prompt looks like it involves writing or changing code
(building a feature, adding an endpoint, auth, payments, webhooks, uploads,
new project scaffolding, etc.), inject a short reminder to load and apply
the `secure-by-default` skill WHILE building - not as an afterthought.

Silent for non-build prompts. Never blocks. ~1ms.
"""
import sys
import re

BUILD_PATTERNS = re.compile(
    r"\b("
    r"build|building|scaffold|bootstrap|set ?up (a|the|my) (app|api|project|backend|server)|"
    r"new project|start (a|the) project|create (a|an|the) (app|api|endpoint|route|feature|form|page|service)|"
    r"add (a|an|the)? ?(endpoint|route|api|feature|auth|login|signup|sign-up|register|payment|checkout|"
    r"subscription|webhook|upload|form|admin|dashboard|user|role|permission)|"
    r"implement|integrate|wire up|hook up|"
    r"auth(entication|orization)?|login|signup|sign ?up|oauth|jwt|session|password|"
    r"stripe|paddle|lemon ?squeezy|payment|checkout|billing|subscription|webhook|"
    r"file ?upload|image ?upload|s3 bucket|presigned|"
    r"database|schema|migration|prisma|drizzle|supabase|postgres|sql query|"
    r"cors|api route|rest api|graphql|"
    r"fetch (a|the)? ?url|proxy|scrape|"
    r"ai (feature|endpoint|agent)|llm (feature|endpoint)|tool[- ]call"
    r")\b",
    re.IGNORECASE,
)

# Prompts that are clearly NOT build work even if a keyword matches
SKIP_PATTERNS = re.compile(
    r"\b(explain|what is|what's the difference|summar(y|ize)|review the|audit|"
    r"pentest|analy(s|z)e|research|compare|which (is|should)|pros and cons|"
    r"how does .* work)\b",
    re.IGNORECASE,
)

MESSAGE = (
    "[SECURE-BUILD GATE] This looks like build/code work. Before and WHILE you write "
    "the diff (not as a later pass), load the `secure-by-default` skill and hold its "
    "rules for every surface the change touches - deny-by-default + ownership-in-the-"
    "query on new endpoints, parameterized queries, no hardcoded/logged secrets, "
    "validate-at-boundary + escape-on-output, SSRF/allow-list on external URLs, "
    "signature-verify + idempotent + server-side-price on payment/webhook handlers, "
    "explicit CORS + security headers, fail-closed error paths, permission-checked AI "
    "tool-calls. Run its 10-second self-scan after each code diff. When the build is "
    "DONE, run `security-audit` Phase 0; for real payments/PII, escalate to "
    "`pentest-checklist` + `threat-modeling-expert`."
)


def main() -> None:
    try:
        raw = sys.stdin.read()
    except Exception:
        return
    m = re.search(r'"prompt"\s*:\s*"((?:[^"\\]|\\.)*)"', raw)
    prompt = m.group(1) if m else raw
    if not prompt:
        return
    if SKIP_PATTERNS.search(prompt) and not re.search(
        r"\b(build|implement|integrate|scaffold|add (a|an|the)? ?(endpoint|route|auth|payment|webhook|upload))\b",
        prompt, re.IGNORECASE,
    ):
        return
    if BUILD_PATTERNS.search(prompt):
        print(MESSAGE)


if __name__ == "__main__":
    main()
