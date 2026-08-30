---
name: heygen-clone-reel
description: Create a real-likeness talking-head reel of Zoher using his own HeyGen personal avatar (webcam-cloned) + cloned voice, then generate/localize scripts via the API. Use when the user wants "my AI clone", "avatar reel of me", "heygen reel", or asks to extend/automate the HeyGen personal-avatar pipeline. More advanced than Higgsfield for this because it's a real face+voice clone with a working API engine, not a prompted fictional character.
---

# HeyGen Personal Clone → Reel Pipeline

Two parts: a **one-time manual identity setup** (must be done by Zoher, live,
in the browser — cannot be automated) and a **repeatable API pipeline**
(already built, this skill just wires it in) for generating reels from that
identity.

## Part 1 — One-time: create the personal avatar + voice (manual)

1. Go to `https://app.heygen.com/home` (or the in-app "Build your identity"
   onboarding if a fresh account triggers it).
2. **Avatar** → "Clone yourself in 15 seconds" → webcam records ~15s of you
   talking/moving naturally, good lighting, face centered. Outfit/background
   don't matter, can be changed later.
3. **Voice** step (follows immediately after Avatar in onboarding) → record
   or upload a clean voice sample to clone your voice. Same guidance as any
   voice clone: quiet room, varied sentence types, ~60-90s.
4. Once both finish processing, open the created avatar/voice in HeyGen and
   copy their IDs (avatar id from the avatar's detail page URL/panel, voice
   id from the voice library). Set them as env vars:
   ```
   HEYGEN_AVATAR_ID=<your avatar id>
   HEYGEN_VOICE_ID=<your voice id>
   ```
5. Note: HeyGen meters **API renders from a separate "API credits" pool**,
   distinct from the web-studio subscription — top up API credits
   separately or `/v2/videos` calls will fail with
   `MOVIO_PAYMENT_INSUFFICIENT_CREDIT` even if the web app shows credits.

## Part 2 — Repeatable: generate reels (already built, reuse it)

The actual generation engine already exists and is proven — don't rebuild
it:
- Engine: `~/.claude/skills-library/super-video-maker/workflows/avatar-insta-split/gen_avatar.py`
  — takes a script, calls HeyGen's `/v2/videos` (English) or an
  ElevenLabs-VO → HeyGen audio-lipsync path (non-English), polls, downloads,
  normalizes fps. Saves `video_id` next to the output so a timed-out poll
  recovers without re-spending credits.
- Two ready recipes that call it end-to-end:
  - `/svm-avatar-insta-reel` — split-screen: article/b-roll scroll on top,
    your avatar talking on bottom. Best for commentary-on-a-topic reels.
  - `/svm-avatar-vo-reel` — fullscreen: your avatar hook/close + fullscreen
    b-roll while your cloned voice narrates over it.

For a plain talking-head reel (avatar fills the whole frame, no b-roll),
call `gen_avatar.py` directly:
```
python3 gen_avatar.py --script-file script.txt --out reel.mp4 --avatar-id $HEYGEN_AVATAR_ID --voice-id $HEYGEN_VOICE_ID --aspect 9:16
```
then run it through the `social` skill's caption/hook overlay if captions
are wanted (word-timed captions, hook badge — same conventions as the svm
recipes).

## Script writing
Route drafting through `kyros-orchestrator` (local Ollama does the pass,
you keep judgment) using the `social` skill's short-form hook/structure
science — 3-second hook rule, ~33s spoken script (avatars render slower,
lands near 40s).

## Compliance
Only use this avatar/voice as your own licensed likeness (it is — it's you).
Still enable each platform's AI-content label at upload; HeyGen-rendered
talking-head video of a real person falls under IG/TikTok/YouTube's
synthetic-media disclosure rules regardless of authorization.

## Distribution
Hand the finished MP4 to Zoher's existing auto-posting tools — no new
integration needed here.
