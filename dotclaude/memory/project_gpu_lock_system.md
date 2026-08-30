---
name: shared-gpu-lock-system
description: "File-based mutex at D:\\AI_Models\\gpu_lock.py preventing Kyros/Ollama, clip-platform GPU transcribe, MiniMax H3, and Open Axis from colliding on the 8GB RTX 4060"
metadata: 
  node_type: memory
  type: project
  originSessionId: eaa41edf-2f91-4266-8c7b-75ac3f275cb4
  modified: 2026-08-17T17:38:59.048Z
---

Built 2026-08-17 alongside local MiniMax H3 setup. One 8GB card, four consumers that
didn't coordinate before: Kyros Orchestrator's Ollama fleet, clip-platform's `device=cuda`
faster-whisper transcribe, Open Axis's `ollama run` dispatch, and the new local MiniMax H3.

**Core file:** `D:\AI_Models\gpu_lock.py` — `status|acquire <owner>|release <owner>` CLI.
Lock file at `D:\AI_Models\.gpu.lock` (JSON: owner, pid, timestamp). Stale locks (dead PID)
auto-clear. `acquire` also refuses if `nvidia-smi` free VRAM < ~7000 MiB even with no lock
file present, catching anything that never bothered to use the convention.

**Critical gotcha found while building this:** on git-bash/MSYS, `$$` is an MSYS-internal
pid, NOT the real Windows pid `tasklist` checks — `os.getppid()` across separate subprocess
calls is also unstable in this environment. Fix: always pass an explicit `--pid` computed via
`cat /proc/$$/winpid` from bash, or `os.getpid()` directly from a native Windows Python
process (no MSYS layer involved there, so it's reliable as-is).

**Wired in:**
- MiniMax H3: `D:\AI_Models\MiniMax-H3\run_minimax.sh` — full pre-flight gate (checks model
  files exist, stops resident ollama models, acquires lock, trap-releases on exit/crash).
- Kyros Orchestrator: doc-level — SKILL.md tells the (me, in-session) dispatcher to check
  `gpu_lock.py status` before any `ollama run`. Not code-enforced since Kyros dispatch is
  Claude emitting shell commands, not a standing service.
- clip-platform: `clipengine/stages/transcribe.py` `_detect_device()` — code-enforced,
  falls back to CPU (not a crash) if lock unavailable.
- Open Axis: `C:\AI\control-plane\adapters\cli_dispatch.py` `dispatch()` — code-enforced,
  returns an ERROR status instead of running if GPU busy.

Full writeup: `D:\AI_Models\GPU_LOCK_README.md`.

**How to apply:** any new GPU-heavy local process on this machine should acquire/release
through this same lock before touching CUDA/Ollama. Don't build a second, incompatible
locking scheme.
