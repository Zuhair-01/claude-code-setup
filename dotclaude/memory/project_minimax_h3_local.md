---
name: local-minimax-h3
description: "Open-weight video/audio gen model downloading to D:\\AI_Models\\MiniMax-H3, gated by the shared GPU lock — \"Higgsfield but free\" per user framing"
metadata: 
  node_type: memory
  type: project
  originSessionId: eaa41edf-2f91-4266-8c7b-75ac3f275cb4
  modified: 2026-08-17T18:25:06.326Z
---

**Why:** user wants free local video generation instead of paying per-second for the
MiniMax H3 hosted API (~$0.13/s at 2K). Weights open-sourced 2026-08-03 under MiniMax H3
Community License (excludes EU/UK/South Korea/US — worth checking before relying on it).

**Files downloading** (~30GB total, to `D:\AI_Models\MiniMax-H3\`, on D: — C: only had 57GB
free and is already at 95% used):
- `unet/MiniMax-H3-FL2VA-Q3_K_M.gguf` (15.58GB) — smallest UNet quant that exists; no Q2_K
  UNet is published. Guides say Q3_K_M really wants 12GB+ VRAM, so on this 8GB 4060 it'll
  likely need CPU-offloaded layers via ComfyUI-GGUF, not full-speed GPU inference.
- `text_encoders/qwen3vl-32B-MiniMax-H3-Q2_K.gguf` (8.49GB)
- `vae/minimax_h3_video_vae_fp16.safetensors` (5.21GB) + `minimax_h3_audio_vae_fp32.safetensors` (0.61GB)

Source repos: `realrebelai/MiniMax-H3_GGUFs` (unet+encoder), `Comfy-Org/MiniMax-H3` (vaes).
Download script: `D:\AI_Models\MiniMax-H3\download.sh` — auto-retries/resumes through
disconnects (HF hub resumes partial files natively).

**Missing from open release:** H3-Regenerate-2K (2K upscale) and H3-Context-IR (prompt
preprocessing) stay API-only. Local gets base 768p generation only.

**Safety wiring:** `run_minimax.sh` won't run unless all 4 files exist on disk AND the
shared [[project_gpu_lock_system]] grants the lock (stops resident Ollama models first).
No ComfyUI runner installed yet — the launch script has a TODO placeholder for that; the
lock/pre-flight machinery is what's actually built and tested so far.

**Paused 2026-08-17 21:xx** — Zoher needed wifi for something else, explicitly said "I'll tell
you when to start it." Confirmed zero hf.exe/download.sh processes running before pausing
(safe, nothing orphaned). No real bytes downloaded yet in practice. Root cause of repeated
stalls found and fixed in `download.sh`: this repo is Xet-backed, and `hf-xet` was registered
in pip metadata but not importable by the interpreter `hf.exe` runs on — silent hang during
chunk negotiation. Fix: `export HF_HUB_DISABLE_XET=1` (already in the script) forces plain
HTTP transfer. NOT yet verified end-to-end. Full detail: Handoff Log 2026-08-17 entry.

**Separate lesson learned:** `TaskStop` on a background bash task does NOT reliably kill the
real Windows process tree here — it stops notifications, not the process. Caused several
rounds of orphaned `hf.exe`/`download.sh` pile-ups this session. Real kills need
`taskkill //F //PID <n>` on exact PIDs from `Get-CimInstance Win32_Process`, verified with a
follow-up check after ~15-45s (some process-tree entries are transient bootstrap shells, not
real orphans — check parent/child and creation time before killing broadly).

**How to apply:** when Zoher says to resume, run `bash "/d/AI_Models/MiniMax-H3/download.sh"`
in background, then verify with an actual growth check (~60s) before trusting it — don't
declare healthy on process-count alone. After download completes, next real step is
installing ComfyUI + ComfyUI-GGUF and wiring the launch command into `run_minimax.sh`'s TODO
line.
