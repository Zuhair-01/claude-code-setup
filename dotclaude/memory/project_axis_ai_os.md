---
name: AXIS AI OS v9 (superseded)
description: Old local AI OS design at Desktop/axis-ai-os — superseded by Open Axis control-plane, see project_open_axis_control_plane.md
type: project
originSessionId: 44011973-260d-41c3-8d7b-2c6f976d816c
modified: 2026-08-17T17:38:24.550Z
---
**Superseded 2026-08-17** — verified this path no longer exists on disk. The "Open Axis"
desktop shortcut now launches `C:\AI\control-plane\orchestrator\repl.py`, a different system
(multi-CLI dispatcher across claude/codex/opencode/ollama, not the Docker Ollama+OpenWebUI+
ChromaDB RAG stack described below). See [[project_open_axis_control_plane]] for the current system.

Original content, kept for history only — do not treat as current state:

Full local AI OS deployed at `C:\Users\Zoher\Desktop\axis-ai-os\`.

**Why:** User wants unlimited local inference without API token costs. RTX 4060 8GB.

**Services (Docker):**
- Ollama → :11434 (GPU inference)
- Open WebUI → :3000 (ChatGPT-like UI)
- ChromaDB → :8000 (vector memory)

**Models loaded:** qwen2.5:1.5b, nomic-embed-text, qwen2.5-coder:7b, llama3.1:8b (pulled by setup.ps1). deepseek-r1:14b must be pulled manually (7.9GB, saturates 8GB VRAM).
