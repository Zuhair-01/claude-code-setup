---
name: oss-media-gen-stack
description: Free/self-hostable replacements for paid AI media-generation tools (TTS/voice cloning, video-gen, avatar/talking-head, lip-sync, background removal, upscaling, captions). Use before recommending or paying for HeyGen, ElevenLabs, Runway, Topaz, remove.bg, or similar.
category: ai-ml
---

# OSS Media-Gen Stack

Curated 2026 free/open-source replacements for paid media-gen tools, vetted for this box (Windows, ~8GB VRAM — see hardware note per category). Built to extend, not duplicate, the existing `voice-cloning-local` skill (Voicebox + OpenVoice, already set up).

## Hardware reality check (this box)
GPU is ~8GB VRAM (see `project_gpu_lock_system` memory) and Kyros runs sequential-only. That rules out the heaviest local video-gen models (HunyuanVideo needs 24GB+, Wan2.1 14B wants 12-16GB). For those, either use the free tiers of Google Flow/Veo (already wired via `ai-video-prompt-engineering` skill) or run the lighter LTX-Video model below. Everything else in this doc (TTS, lip-sync, bg-removal, upscaling, captions) fits comfortably in 8GB.

## 1. Voice / TTS — already done
Don't redo. See `voice-cloning-local` skill: Voicebox (primary, Arabic-capable) + OpenVoice, replaces ElevenLabs.

## 2. Video generation (text-to-video / image-to-video)
Replaces: Runway, Pika, paid Veo/Sora access.

| Tool | Replaces | Why | VRAM | Install |
|---|---|---|---|---|
| **LTX-Video** (Lightricks) | Runway/Pika quick clips | Orders of magnitude faster than the others, only OSS model that's actually practical on 8-16GB cards | 8GB+ (low-res), 16GB comfortable | `pip install ltx-video` or via ComfyUI custom node; weights on HuggingFace (`Lightricks/LTX-Video`) |
| **Wan 2.1/2.2** (Alibaba) | Runway (photorealistic) | Best photorealistic quality/human subjects among OSS; 14B model | 12-16GB min | ComfyUI-WanVideoWrapper node, or `diffusers` pipeline |
| **CogVideoX** | Runway (budget) | Runs on consumer 8-16GB cards, good quality-for-VRAM ratio | 8-12GB | `pip install diffusers`, model `THUDM/CogVideoX-5b` |

Given the 8GB ceiling, **CogVideoX or LTX-Video are the realistic local picks**; Wan2.1 is a stretch goal if a bigger GPU gets added later. Wire in: extend `ai-video-prompt-engineering` skill with a "local generation" fallback section pointing here, for when the free Flow/Veo quota runs out.

## 3. Avatar / Talking-head (replaces HeyGen)
| Tool | Why | License | VRAM |
|---|---|---|---|
| **SadTalker** | Single photo → talking head with natural head movement; easiest to stand up first | Apache-2.0 (commercial-safe) | Modest, runs on 8GB |
| **MuseTalk** | Best default for syncing a face you already have (not generating one); real-time capable | MIT (commercial-safe) | Runs on 4GB+ |
| **LivePortrait** (Kuaishou) | Closest to live/real-time lip-sync in OSS, treats whole face as controllable | Check repo license before commercial use | Mid-range |
| **ai-avatar-system** (github.com/PunithVT/ai-avatar-system) | Full pre-wired stack: photo upload + voice clone + real-time lip-sync using Whisper+Chatterbox+MuseTalk — closest single-repo HeyGen clone | OSS, check license | Depends on components |

**Recommended stack for this box**: SadTalker (photo→video) or MuseTalk (existing footage) first — both fit 8GB and are commercial-safe. Skip Hallo3/LatentSync/Sonic — they want A10/RTX4090-class VRAM, not available here.

Wire in: replaces the blocked `heygen-clone-reel` skill's dependency on Zoher recording a webcam clone — SadTalker/MuseTalk can generate from an existing photo instead if the webcam session stays blocked.

## 4. Lip-sync only (audio → existing video)
| Tool | Why | License note |
|---|---|---|
| **MuseTalk** | MIT, commercially usable, runs on 4GB | Best all-around pick |
| **Wav2Lip** | Simplest, runs on any mid-range card | OSS version is **non-commercial only** — don't use for client work |

## 5. Background removal (replaces remove.bg)
| Tool | Why | Install |
|---|---|---|
| **rembg** | Most widely deployed OSS bg-remover — Python lib/CLI/HTTP server/Docker, MIT, built on U2-Net/IS-Net | `pip install rembg` |
| **BiRefNet** | MIT, 6 model variants trading speed for accuracy, unrestricted commercial use | HuggingFace `ZhengPeng7/BiRefNet` |

Wire in: `open-pinterest` skill already does "background-cut if only the subject matters" — point that step at rembg/BiRefNet instead of a paid tool if one was being used.

## 6. Upscaling (replaces Topaz Photo AI / Gigapixel)
| Tool | Why | Install |
|---|---|---|
| **Real-ESRGAN** | Same architecture Topaz Photo AI ($199) is built on, free | `pip install realesrgan` or ComfyUI node |
| **Upscayl** | Free desktop GUI app, local GPU, no upload/account | Windows installer from github.com/upscayl/upscayl |
| **GFPGAN / CodeFormer** | Face-specific restoration (better than general upscalers for faces) | `pip install gfpgan` |

Wire in: `image-restoration-accuracy` skill (alwazour product photo cleanup) should use Real-ESRGAN/GFPGAN as its local engine instead of any paid upscaler.

## 7. Captions / subtitles (replaces paid caption tools)
| Tool | Why | Install |
|---|---|---|
| **faster-whisper** | Whisper reimplementation, 4x faster, same accuracy, runs local | `pip install faster-whisper` |
| **WhisperX** | Adds word-level timestamps + speaker diarization on top of Whisper — needed for auto-caption styling | `pip install whisperx` |

Already partially in use — `clip-platform` project uses GPU transcribe per memory `project_clip_platform.md`; confirm it's faster-whisper/WhisperX, not a paid API, before treating this as new.

## Priority install order (given 8GB VRAM + existing setup)
1. rembg + Real-ESRGAN/GFPGAN (lightest, immediate win for alwazour photo cleanup)
2. faster-whisper/WhisperX (if clip-platform isn't already using local Whisper)
3. SadTalker (unblocks the HeyGen-clone-reel project without needing Zoher's webcam session)
4. MuseTalk (lip-sync existing footage)
5. CogVideoX or LTX-Video (only if local video-gen becomes a real need beyond free Flow/Veo quota)
