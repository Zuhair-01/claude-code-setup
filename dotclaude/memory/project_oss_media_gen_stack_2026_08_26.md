---
name: project_oss_media_gen_stack_2026_08_26
description: Media-gen lane of the 3-session free/OSS AI tool research sweep - curated OSS replacements for HeyGen/ElevenLabs/Runway/Topaz/remove.bg
metadata: 
  node_type: memory
  type: project
  originSessionId: 38e32ffb-614a-45fd-af55-812772a6c05e
  modified: 2026-08-26T01:02:54.976Z
---

Built `oss-media-gen-stack` skill (registered in OVERSEER, category media-video) covering video-gen, avatar/talking-head, lip-sync, background removal, upscaling, and captions. Part of a 3-way session split zoher-8f initiated 2026-08-26: this session took media-gen, zoher-8f took local LLM/agent-orchestration/RAG (see [[project_free_oss_ai_stack_research_2026_08_26]]), zoher-9d took devops/paid-dep audit.

**Why:** Zoher wants paid AI tools replaced with free/local/OSS wherever practical, wired into both OVERSEER (for reuse) and live projects.

**How to apply:** Don't redo [[project_voice_cloning_openvoice_voicebox]] (TTS already solved). Key picks that actually fit this box's ~8GB VRAM ceiling: rembg/BiRefNet (bg removal), Real-ESRGAN/GFPGAN (upscaling, should replace whatever `image-restoration-accuracy` uses for alwazour photos), faster-whisper/WhisperX (captions - check clip-platform isn't already paying for transcription), SadTalker/MuseTalk (avatar/lip-sync, commercial-safe licenses, unblocks [[project_ai_clone_heygen]]'s webcam-recording bottleneck since SadTalker works from a still photo instead). Heavier video-gen models (Wan2.1, HunyuanVideo) don't fit this GPU - only CogVideoX/LTX-Video are realistic local picks; otherwise keep using the free Flow/Veo quota via `ai-video-prompt-engineering`. Full comparison table + install commands in the skill file itself.
