#!/usr/bin/env python3
"""OVERSEER route marker -- PostToolUse hook (Bash|Skill matcher).
Writes a per-session marker file when this session shows real evidence of
running the Rule 7 routing protocol (overseer search.py, or the skill-router
skill). Read by route_gate.py before allowing the first Write/Edit/MultiEdit.
Fails open always -- never raises, never blocks anything itself.
"""
import sys, os, json

MARK_DIR = os.path.expanduser("~/.claude/overseer/.session-routed")

def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw else {}
    except Exception:
        return

    session_id = data.get("session_id") or "unknown"
    tool_name = data.get("tool_name") or ""
    tool_input = data.get("tool_input") or {}

    routed = False
    try:
        if tool_name == "Bash":
            cmd = str(tool_input.get("command", ""))
            if "overseer" in cmd and "search.py" in cmd:
                routed = True
        elif tool_name == "Skill":
            skill = str(tool_input.get("skill", "")).lower()
            if "skill-router" in skill or "overseer" in skill:
                routed = True
    except Exception:
        return

    if not routed:
        return

    try:
        os.makedirs(MARK_DIR, exist_ok=True)
        marker = os.path.join(MARK_DIR, session_id)
        with open(marker, "w", encoding="utf-8") as fh:
            fh.write(tool_name)
    except Exception:
        return

if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
