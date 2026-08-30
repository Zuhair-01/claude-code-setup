---
name: project-ai-clone-heygen
description: "AI clone of Zoher (real face+voice) for talking-head reels across IG/TikTok/YouTube Shorts, built on HeyGen personal avatar — in progress, blocked on Zoher recording the webcam clone step."
metadata: 
  node_type: memory
  type: project
  originSessionId: da3714ab-d878-4910-a6b3-7495281ea4dd
  modified: 2026-08-23T21:55:50.918Z
---

Goal: a real-likeness AI clone of Zoher (not a fictional persona) producing
talking-head commentary reels, posted via his existing auto-posting tools
to Instagram Reels, TikTok, and YouTube Shorts.

**Decision trail (2026-08-24):** Started as a free-tier self-hosted plan
(LivePortrait + XTTS-v2, cloned to `Desktop/Empire_Base/ai_clone/`, Python
3.12 venv partway set up, torch install was stopped mid-way). Considered
Higgsfield — rejected, confirmed via its skill file that Soul 2.0 has no
face-upload/no voice-clone, it only makes fictional prompted characters.
Zoher then chose to pay and use his **existing HeyGen account** instead
(already had `HEYGEN_AVATAR_ID`/`HEYGEN_VOICE_ID` wired into the
`super-video-maker` skill for other business use) — higher quality,
reuses infra already built.

**Why:** self-hosted is free but a quality notch below HeyGen; Higgsfield
structurally can't do identity cloning at any spend; HeyGen's built-in
"Clone yourself in 15 seconds" (webcam motion capture) + voice-clone
onboarding step is the fastest path to a real, high-quality likeness given
he's willing to pay API credits.

**How to apply:** Don't re-suggest Higgsfield or restart the self-hosted
LivePortrait/XTTS path for this unless Zoher explicitly says HeyGen isn't
working out — that ground was already covered. The self-hosted clone at
`Desktop/Empire_Base/ai_clone/` was left in place (harmless, unfinished) as
a free fallback, not deleted.

**Current blocker / next step:** Zoher needs to physically sit at the
laptop and go through HeyGen's onboarding at `app.heygen.com/home` →
"Let's go" → record ~15s webcam clip (Avatar step) → then the Voice
clone step right after. This cannot be automated (needs his live
camera/voice). Once done, get the avatar ID + voice ID from HeyGen and
set `HEYGEN_AVATAR_ID` / `HEYGEN_VOICE_ID`.

**Then:** use the new `heygen-clone-reel` skill
(`~/.claude/skills/heygen-clone-reel/SKILL.md`) — wires the real
avatar/voice into the already-working
`super-video-maker/workflows/avatar-insta-split/gen_avatar.py` engine and
the `/svm-avatar-insta-reel` / `/svm-avatar-vo-reel` recipes. Generate one
test reel end-to-end before scaling to a regular posting cadence. Remember
the AI-content label toggle at upload on all three platforms (ToS
requirement, not optional).

See also: [[heygen-clone-reel]] skill (once a skill-type memory exists for
it), [[project_higgsfield_skills]] (why it was ruled out for this specific
use case, still fine for its original UGC use).
