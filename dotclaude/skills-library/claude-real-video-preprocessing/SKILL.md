# claude-real-video Integration (BUNDLE 3 Preprocessing)

Use this when you need to extract frames + transcript from video before clipping/editing.

## What it does
- Extracts key frames from video (local, no API calls)
- Generates transcript via Whisper
- Detects scene boundaries
- Returns structured data for downstream skills

## When to use
- Before ai-clipping (frame extraction makes scene detection faster)
- Before video-editing (transcript helps with caption generation)
- Preprocessing step in video-production-pipeline

## Usage
\\\python
from claude_real_video import extract_frames

result = await extract_frames(
    video_url="https://...",
    fps=2,  # Sample every 0.5 sec
    max_frames=100
)
# Returns: {frames: [...], transcript: "...", scenes: [...]}
\\\

## Integration with BUNDLE 3
This skill sits BEFORE ai-clipping:

video-input
  → claude-real-video (extract + transcript)
  → ai-clipping (detect key moments in extracted frames)
  → youtube-clipper (auto-split based on scenes)
  → video-editing (render + caption using transcript)
