#!/usr/bin/env python3
"""Record bounded, metadata-only Claude hook events locally.

This deliberately excludes prompts, file paths, command text, arguments, and
tool output. It is a local diagnostic signal, not a transcript store.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


LOG = Path.home() / ".claude" / "telemetry" / "metadata-events.jsonl"
MAX_BYTES = 5 * 1024 * 1024


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "pid": os.getpid(),
            "hook_event": payload.get("hook_event_name", "unknown"),
            "tool": payload.get("tool_name", "unknown"),
            "session": bool(payload.get("session_id")),
        }
        LOG.parent.mkdir(parents=True, exist_ok=True)
        if LOG.exists() and LOG.stat().st_size >= MAX_BYTES:
            rotated = LOG.with_suffix(".1.jsonl")
            if rotated.exists():
                rotated.unlink()
            LOG.replace(rotated)
        with LOG.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(event, separators=(",", ":")) + "\n")
    except Exception:
        # Telemetry must never block a Claude operation.
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
