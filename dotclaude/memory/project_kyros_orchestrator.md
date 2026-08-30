---
name: project-kyros-orchestrator
description: "Kyros Clips master/worker control loop — cloud Claude plans, local Ollama fleet executes. Skill at ~/.claude/skills/kyros-orchestrator/"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9ca8f6e0-ac9f-43cc-b2c4-fb9644a3d24a
  modified: 2026-08-02T01:11:40.396Z
---

Kyros Clips (local video processing + AI clipping; Next.js + Python + FFmpeg + Faster-Whisper) runs a master/worker loop. Claude is Master Architect: plans, routes, emits exact worker prompts, verifies output. Local Ollama models execute.

Hardware ground truth on this laptop (verified 2026-08-02): **8 GB VRAM, one model resident at a time, sequential load/unload mandatory.** Local worker context 16k. ~77 GB disk free.

Fleet: `qwen2.5-coder:7b` (code), `deepseek-r1:8b` (reasoning/ranking/hooks), `moondream` (vision) — all installed. `llama3.1:8b` (copy) NOT installed, needs `ollama pull`. `gemma4` at 9.6 GB is BANNED — exceeds VRAM, spills to RAM.

**Why:** the user wants cloud-tier planning with extreme token efficiency, and local execution to avoid burning cloud tokens. They have explicitly said agents/subagents drain tokens — do not spawn them.

**How to apply:** invoke the `kyros-orchestrator` skill for any Kyros work or any task destined for a local model. It carries the routing table, dispatch format, VRAM sequencing, and verification loop. Related: [[feedback_lean_engine]], [[project_clip_platform]].
