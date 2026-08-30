---
name: editor-experience
description: Interviews a professional video editor about their editing philosophy and preferences, then converts the interview into a structured clip-platform preset (caption + edit params matching clipengine's EDITING_STYLE_PRESETS schema) and pushes it to a shared GitHub repo for Kyros to pick up. Trigger on "editor experience", "interview me about editing", "grill me on editing", "build my preset".
---

# Editor Experience — Interview → Preset → GitHub

You are extracting one professional editor's real knowledge into a preset Zoher's
Kyros clipping engine can run. Two phases. Do not skip phase 1 to rush to JSON —
the freeform answers are the actual product; the JSON is just a compressed view of them.

## Setup (first run only)

Check for `EDITOR_INTEL_REPO` and `EDITOR_INTEL_TOKEN` in the shell env or a
`.env` in this skill's directory. If missing, ask the editor for:
1. The GitHub repo URL Zoher gave them (format `https://github.com/<owner>/editor-intel`)
2. The fine-grained PAT Zoher sent them (scoped to that repo only — write access)

Clone it once to `~/editor-intel-workspace` if not already present:
```bash
git clone https://<token>@github.com/<owner>/editor-intel.git ~/editor-intel-workspace
```
Never print the token back to the user or commit it into any file. Store it only
in the shell env for this session (`export EDITOR_INTEL_TOKEN=...`).

## Phase 1 — Freeform interview

Ask these one at a time, conversationally — react to each answer, dig one level
deeper when an answer is vague ("fast-paced" → "fast compared to what, give me
a cuts-per-10-seconds feel"), don't just march through a checklist:

1. What kind of content do you edit most (talking head / podcast clips / kinetic
   text / cinematic story / other)? What's your name/handle, for the preset name?
2. Walk me through your cut rhythm — how often do you cut on a talking-head clip,
   what makes you punch in vs hold?
3. Captions — words per caption chunk, position, case (upper/lower), do you
   highlight keywords, karaoke-style word-by-word or phrase blocks, do you cut
   filler words ("um", "like") from the caption or leave them?
4. Punch-ins / zooms — do you use them, how aggressive (subtle 1.1x vs hard 1.4x),
   max punches per clip, cooldown between them?
5. Color — do you grade at all, subtle or heavy, any saturation bump on payoff/punchline
   moments?
6. Audio — music ducking under dialogue, sound effects on cuts/reveals, how much?
7. Pacing philosophy in your own words — what's the one rule you never break when
   cutting for retention?
8. Anything else that makes your edits distinctly yours that the above didn't cover?

Write the raw transcript to `~/editor-intel-workspace/interviews/<handle>-<date>.md`
(their words, lightly cleaned, not paraphrased into corporate summary).

## Phase 2 — Structured extraction

Convert the transcript into JSON matching this EXACT schema (this is
`clipengine/config.py`'s `EDITING_STYLE_PRESETS` shape — do not invent new keys,
only use these; omit a key if the editor gave no clear answer for it rather than
guessing):

```json
{
  "caption": {
    "words_per_caption": 1,
    "position": "lower | center",
    "uppercase": true,
    "emoji_keywords": false,
    "karaoke": true,
    "hide_filler_words": true,
    "speaker_colors_enabled": false
  },
  "edit": {
    "punch_ins": true,
    "punch_zoom": 1.1,
    "punch_max": 4,
    "punch_cooldown": 5.0,
    "slow_zoom": false,
    "slow_zoom_max": 0.05,
    "slow_zoom_secs": 10.0,
    "color_grade": false,
    "grade_strength": 0.8,
    "payoff_saturation_bump": 0.125,
    "music_ducking": false,
    "sfx_enabled": false,
    "sfx_variety": false,
    "deadpan_holds": false
  }
}
```

Write it to `~/editor-intel-workspace/presets/<handle>.json`. Also append one
line to `~/editor-intel-workspace/presets/INDEX.md`: `- <handle>: <one-line style summary> (added <date>)`.

## Push

```bash
cd ~/editor-intel-workspace
git add interviews presets
git commit -m "editor preset: <handle>"
git push
```

Tell the editor: "Pushed — Zoher's Kyros will pick this up on its next sync."
Do not push anything outside `interviews/` and `presets/` — this repo has no
other purpose and the PAT should never touch anything else.
