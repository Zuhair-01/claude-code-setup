#!/usr/bin/env python3
"""Replace inline MCP credentials with environment references."""

from pathlib import Path
import re


CONFIG = Path.home() / ".claude.json"
text = CONFIG.read_text(encoding="utf-8")
patterns = {
    r"N8N_API_KEY=[^\"]+": "N8N_API_KEY=${N8N_API_KEY}",
    r'"SERPER_API_KEY"\s*:\s*"[^"]+"': '"SERPER_API_KEY": "${SERPER_API_KEY}"',
    r'"EXA_API_KEY"\s*:\s*"[^"]+"': '"EXA_API_KEY": "${EXA_API_KEY}"',
}
updated = text
for pattern, replacement in patterns.items():
    updated = re.sub(pattern, replacement, updated)
if updated != text:
    CONFIG.write_text(updated, encoding="utf-8", newline="\n")
    print("redacted inline MCP credentials")
else:
    print("no inline MCP credentials changed")
