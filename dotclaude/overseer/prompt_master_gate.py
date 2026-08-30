#!/usr/bin/env python3
"""prompt-master gate -- UserPromptSubmit hook.
Reminds the model, every turn, to run the user's raw message through the
prompt-master skill's sharpening logic BEFORE acting on it -- per Zoher's
explicit request 2026-08-18: prompt-master is the mandatory first filter
between his raw input and any Claude response.
Fails open always -- prints nothing and never blocks on internal error.
"""
import sys

MSG = (
    "[PROMPT-MASTER GATE] Before doing anything else this turn: silently run the "
    "user's raw message through ~/.claude/skills/prompt-master's intent-extraction "
    "and Claude-routing logic to produce a sharper, more precise version of the ask "
    "(target = this Claude Code session, not an external tool -- so skip the "
    "'paste this elsewhere' packaging, just use the sharpened brief internally). "
    "This matters most when the raw message is unclear, fragmented, typo-heavy, in "
    "caps, or bundles multiple asks in one line -- reconstruct it into a clear, "
    "professional task statement (what's being asked, on what target, what scope) "
    "before acting, resolving ambiguous references against recent context rather "
    "than guessing cold. Then respond to the SHARPENED version, not the raw one. "
    "Skip this only for trivial one-line acknowledgements (\"yes\", \"ok\", "
    "\"continue\") where there is nothing to sharpen."
)

def main():
    try:
        sys.stdin.read()
    except Exception:
        pass
    print(MSG)

if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
