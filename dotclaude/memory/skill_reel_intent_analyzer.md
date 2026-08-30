---
name: skill_reel_intent_analyzer
description: "Skill that analyzes a video/reel link for content+intent, or dev-tutorial repo/stack extraction, without paid video-AI APIs."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1e4f1e8a-4460-4741-90cc-b951ef46ed2b
  modified: 2026-08-16T08:53:16.245Z
---

Built 2026-08-16. Lives in the OVERSEER library (dormant, zero context cost until pulled), not
the always-loaded `~/.claude/skills/` folder: `C:\Users\Zoher\.claude\skills-library\reel-intent-analyzer\SKILL.md`.

Pulls from `video-download` (yt-dlp) + `ffmpeg` (keyframes) + Claude's own multimodal vision —
no Memories.ai or other paid video API. Two modes: marketing/content breakdown (hook, goal, CTA),
or dev/reference mode (extract repo links/stack from tutorial-style content, check against an
existing project for real gaps before reporting them).

**Why:** requested to handle "what does this reel want from me" analysis, then extended to also
cover dev-content videos meant as build reference/training material. See
[[project_local_dev_tools]] for an example run (GitHub-repo-roundup carousel → fzf/PowerToys gap
found and installed).

**How to apply:** when a reel/short/TikTok/video link shows up, pull this from the library via
`python C:\Users\Zoher\.claude\overseer\search.py <keywords>` rather than assuming it's not there
— it won't show in the live skill list.

Falls back to `mcp__claude-in-chrome` when yt-dlp can't get the content (private posts, or
image-only carousels which yt-dlp's Instagram extractor doesn't support — confirmed on
2026-08-16, had to use a user-provided screen recording instead).
