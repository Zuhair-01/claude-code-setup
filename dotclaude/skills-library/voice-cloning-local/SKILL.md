---
name: voice-cloning-local
description: "Local voice-clone + TTS engines already installed on this machine (Voicebox/Chatterbox Multilingual, OpenVoice V2) — use for Arabic dubbing, AI-UGC voiceovers, clip-platform audio, or any task needing a cloned voice speaking new text, before reaching for a paid API (ElevenLabs etc)."
risk: safe
source: local-install
date_added: "2026-08-24"
---

# Local Voice Cloning (Voicebox + OpenVoice)

## Overview

Two local, already-installed voice-clone/TTS engines on this machine. Check
this skill before building a new voice pipeline, adding a paid TTS API, or
saying "no local option exists" for any dubbing/voiceover/voice-clone task.

## Engines

### Voicebox (primary — use first)
- App: `C:\Program Files\Voicebox\voicebox-server.exe` (Chatterbox Multilingual backend, 23 languages **including Arabic**)
- Launch via GPU-lock-aware wrapper (don't launch the exe directly):
  `python "C:\Users\Zoher\Desktop\Empire_Base\Arabic_Localization\voicebox_launch.py"`
- REST API once running: `http://localhost:17493` (OpenAPI at `/openapi.json`)
  - `POST /profiles` + `POST /profiles/{id}/samples` — create a voice profile from a 5s+ audio sample (clone)
  - `POST /generate` `{"text": "...", "profile_id": "...", "language": "ar"}` — synthesize
  - `GET /backend/cuda-status` / `POST /backend/download-cuda` — GPU backend (CPU by default until downloaded)
- Data dir: `C:\Users\Zoher\Desktop\Empire_Base\Voicebox_data`
- Best for: Arabic Localization pillar, AI-UGC voiceovers — natively multilingual, already wired.

### OpenVoice V2 (secondary — cross-lingual tone transfer, no native Arabic)
- Repo: `C:\Users\Zoher\Desktop\Empire_Base\clip-platform\services\OpenVoice` (`.venv`, Python 3.11 via uv)
- Checkpoints: `checkpoints_v2/` (base speakers en/es/fr/zh/ja/ko + tone converter)
- No native Arabic base speaker — only useful for EN/ES/FR/ZH/JA/KO clone+TTS, or as a
  tone-color converter on top of audio from another engine.
- Use only when Voicebox's quality/output doesn't fit, or for a non-Arabic language it does cover.

## GPU lock

Both are GPU-capable; the RTX 4060 (8GB) is shared with Kyros/MiniMax H3/clip-platform
transcription. See `D:\AI_Models\GPU_LOCK_README.md`. Voicebox's launcher
(`voicebox_launch.py`) already acquires/releases the shared lock around the server
process lifetime — a `ponytail:` known simplification, since Voicebox is a closed
binary: the lock is held for the whole server lifetime, not per-request. Upgrade path
if this ever blocks something: only acquire around actual `/generate` calls via a thin
reverse-proxy, not at server start.

## When NOT to use these

- Real-time/streaming conversational voice → see `voice-ai-engine-development` skill instead.
- Non-clone, generic TTS-only need with no local requirement → paid API (ElevenLabs) may still
  be simpler; check `free-for-dev` guidance first regardless.
