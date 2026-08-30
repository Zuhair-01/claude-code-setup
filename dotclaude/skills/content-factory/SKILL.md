---
name: content-factory
description: >-
  End-to-end producer for social content that Claude Code builds itself — reels
  (script + shotlist + captions + assembly), carousels (copy + designed slides
  rendered to PNG), and text posts. Orchestrates research → hook → structure →
  design/production → export, wiring the existing skill stack. Use when the ask
  is "make me a reel/carousel/post about X", "turn this into content", "batch a
  week of posts", "design these slides", "produce this video". Each stage can be
  run alone ("just write the hooks", "just design the slides from this script").
triggers:
  - make a reel
  - make a carousel
  - produce this video
  - design these slides
  - turn this into content
  - batch a week of content
  - content factory
  - script this reel
---

# content-factory

Textbook: `Second_Brain/30-Resources/Curriculum/Product_Business_5_Pillars_Mastery.md` §5E.
This skill = the assembly line. It calls other skills per stage; it does not replace them.

## Stage map (run all, or jump to one)

| Stage | What Claude does | Skills / tools used |
|---|---|---|
| 0 RESEARCH | Pull the niche's current hooks/angles; check what's trending; find 5 reference accounts + their patterns | `WebSearch`, `open-pinterest` (visual refs), `reel-intent-analyzer`, `seek-and-analyze-video` |
| 1 STRATEGY | Pick format (reel vs carousel vs post) for the message; define the ONE target person; awareness stage | `marketing-psychology`, `social-growth-science` |
| 2 HOOK | 10 hook variants, score by "would I stop scrolling", pick 1–2 | `marketing-psychology` (§4 U's, awareness), `copywriting` |
| 3 STRUCTURE | Reel: beat sheet (0–3 hook / 3–15 deliver / re-hook / loop-CTA). Carousel: slide-by-slide (slide1 hook → stakes → 1 idea/slide → recap → CTA). Post: inverted-pyramid draft | `social-growth-science` |
| 4a DESIGN (carousel/post) | Write ONE self-contained HTML file, one `<section class="slide">` per slide at 1080×1350 (4:5), consistent tokens; render each to PNG with Playwright | `taste-skill` / `canvas-design` for the look; `playwright-skill` / local Playwright for export |
| 4b PRODUCE (reel) | Option A: AI video via `seedance-2`/`higgsfield-image-auto`/`avatar-video`/`sora`. Option B: talking-head/screen-record shotlist for Zoher to film. Option C: motion-graphics reel built as HTML/CSS/Canvas → screen-capture → mp4 | `ai-video-prompt-engineering`, `video-shortform`, `remotion-video-creation`, `motion-ui`, `ffmpeg` |
| 5 CAPTIONS | Burned-in captions (short-form needs them — 50%+ watch muted), on-screen text for first frame | `ffmpeg` (subtitles), `video-editing` |
| 6 ASSEMBLE | Stitch clips, add音 audio/music, trim to <30s where possible, 9:16 1080×1920, no watermark | `ffmpeg`, `auto_clipper.py` (Zoher's, `--gpu`) |
| 7 PACKAGE | Post caption (hook line + value + soft CTA + question), 3–5 niche hashtags, alt text, suggested post time; save to project `content/` folder | — |
| 8 REVIEW | Run the `social-growth-science` hard-rules check + retention-risk read of the first 3s before calling it done | `social-growth-science` |

## Carousel render recipe (the part Claude fully owns)

```
1. Build slides.html — <section class="slide"> × N, each 1080×1350px, position:relative.
   Shared: --bg, --ink, --accent, one display font + one body font. Slide number + @handle on every slide.
2. Slide 1: 60–90px headline, one promise, max contrast. Slides 3–N: one idea, ≤25 words, big.
   Second-to-last: recap (bullet list of the N ideas). Last: "Follow @X · Save this · [question]".
3. Render: playwright → for each .slide, element.screenshot({path: `slide-${i}.png`}).  (headless, deviceScaleFactor 2)
4. Output: content/<slug>/slide-1..N.png + caption.txt + the source slides.html.
```

## Reel motion-graphics recipe (no camera, no AI credits)

```
1. Build reel.html at 1080×1920, an animated sequence: keyframed CSS/Canvas, text pops synced to a beat.
2. Timeline via Web Animations API or a simple requestAnimationFrame clock; total ≤ 25s.
3. Capture: playwright page.video / or screen-record the tab / or render frames + ffmpeg -framerate 30.
4. ffmpeg: add audio track, -vf for safe margins, export H.264 mp4 9:16, faststart, no watermark.
```

## Batch mode ("a week of content")
Stage 0–1 once for the week's theme → generate 12–15 hooks → assign 5 to reels, 3 to carousels, 5 to posts → run stages 3–7 per item → dump all into `content/week-NN/` with a `calendar.md` (item, format, hook, caption, suggested day/time).

## Output contract
Always produce actual files in a `content/<slug>/` folder (PNGs, mp4, caption.txt, source html), not just text. End with a one-screen summary table: item · format · hook · file path · predicted weak point.

## Hard rules
- Hook first, every stage serves the first 3 seconds. A great slide 4 can't save a dead slide 1.
- Captions burned in for all short-form. Text on the first frame stating the payoff.
- 9:16 1080×1920 video / 4:5 1080×1350 carousel. No platform watermark. Has audio.
- Never fabricate stats/testimonials in the copy (kills trust + reach).
- Consistency of slide design > cleverness — swiping must feel effortless.
- If positioning/message is unclear, stop at stage 1 and fix it — don't produce 10 polished posts of a muddy message.
