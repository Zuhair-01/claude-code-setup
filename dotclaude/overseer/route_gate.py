#!/usr/bin/env python3
"""OVERSEER route gate -- PreToolUse hook (Write|Edit|MultiEdit matcher).
Enforces CLAUDE.md Rule 7: blocks the FIRST code-producing tool call of a
session unless this session already shows evidence of routing (see
route_marker.py) -- an overseer search.py call or a skill-router invocation.
One-time per session: once the marker exists, this gate is a permanent no-op
for the rest of the session. Fails open on any internal error -- never
blocks due to a bug in this script itself.

Escape hatch: touch ~/.claude/overseer/.route-gate-disabled to disable.
"""
import sys, os, json

MARK_DIR = os.path.expanduser("~/.claude/overseer/.session-routed")
DISABLE_FLAG = os.path.expanduser("~/.claude/overseer/.route-gate-disabled")
CLAUDE_HOME = os.path.expanduser("~/.claude").replace("\\", "/").rstrip("/")

def allow():
    sys.exit(0)

def block(reason):
    out = {
        "decision": "block",
        "reason": reason,
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        },
    }
    print(json.dumps(out))
    sys.exit(0)

def main():
    if os.path.exists(DISABLE_FLAG):
        return allow()

    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw else {}
    except Exception:
        return allow()

    tool_name = data.get("tool_name") or ""
    if tool_name not in ("Write", "Edit", "MultiEdit"):
        return allow()

    tool_input = data.get("tool_input") or {}
    file_path = tool_input.get("file_path") or tool_input.get("path") or ""
    norm = str(file_path).replace("\\", "/")

    # Self-config / meta work (editing skills, memory, plans, hooks) is exempt --
    # routing to find a skill to edit the skill system is circular, not useful.
    if CLAUDE_HOME.lower() in norm.lower():
        return allow()

    # GSD project-state files -- settings.json's permissions block already
    # special-cases .planning/* and STATE.md as GSD's own structured workflow
    # (which embeds its own phase/routing logic). Gating GSD's own internal
    # writes behind this separate router would be redundant friction, not a
    # missing check.
    lower_norm = norm.lower()
    if "/.planning/" in lower_norm or lower_norm.endswith("/state.md") or lower_norm == "state.md":
        return allow()

    session_id = data.get("session_id") or "unknown"

    try:
        marker = os.path.join(MARK_DIR, session_id)
        if os.path.exists(marker):
            return allow()
    except Exception:
        return allow()

    reason = (
        "CLAUDE.md Rule 7: no routing evidence yet this session. Before the first "
        "write/edit, run `python3 ~/.claude/overseer/search.py <keywords>` (or invoke "
        "the skill-router skill) to check for a better-fit skill, then retry this edit. "
        "This fires once per session only."
    )
    return block(reason)

if __name__ == "__main__":
    try:
        main()
    except Exception:
        allow()
