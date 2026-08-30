---
name: project_voice_cloning_openvoice_voicebox
description: "OpenVoice V2 + Voicebox (Chatterbox Multilingual) set up 2026-08-24 as local voice-clone/TTS, registered in OVERSEER for auto-discovery."
metadata: 
  node_type: memory
  type: project
  originSessionId: 8f28ec96-fb70-4908-839f-1afaad191bb9
  modified: 2026-08-24T15:48:13.857Z
---

Set up two local voice-clone/TTS engines and registered them in OVERSEER
(`~/.claude/skills-library/voice-cloning-local/SKILL.md`, indexed) so future
sessions find them via `overseer/search.py` instead of missing them or
building from scratch.

- **Voicebox** (primary, Chatterbox Multilingual, Arabic-capable) — was
  installed but not running, and its documented port (17493) was stale
  (defaulted to 8000). Fixed with a GPU-lock-aware launcher at
  `Empire_Base\Arabic_Localization\voicebox_launch.py` — always launch
  Voicebox through this, not the raw exe, so it acquires/releases the
  shared RTX 4060 lock ([[project_gpu_lock_system]]). CUDA backend download
  triggered via its `/backend/download-cuda` endpoint (was CPU-only).
- **OpenVoice V2** — cloned to `clip-platform/services/OpenVoice`, needed a
  Python 3.11 uv venv (repo's setup.py pins ancient `faster-whisper==0.9.0`
  which fails to compile on modern toolchains — relaxed to `>=1.0` in both
  `setup.py` and `requirements.txt`). No native Arabic support (only
  en/es/fr/zh/ja/ko) — secondary engine, not the Arabic Localization answer.

**Why:** Zoher asked "how can we use OpenVoice" then "wire it to the
system"; mid-setup it turned out Voicebox already existed for this exact
job (Arabic dubbing + AI-UGC voiceovers) and does it better (native
Arabic), so both were kept for a side-by-side comparison rather than
picking blind.

**How to apply:** Before adding any paid TTS/voice-clone API or building a
new voice pipeline, check `voice-cloning-local` first. Launch Voicebox only
via `voicebox_launch.py`. See [[feedback_check_before_download]] — this is
the case that prompted checking OVERSEER mid-task and catching the
redundancy.
