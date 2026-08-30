---
name: feedback-check-before-download
description: Always check for existing installs/tools/deps before downloading or installing anything new
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 31341b4a-f0e5-4880-bd65-28571a6e8824
  modified: 2026-08-21T20:12:24.667Z
---

Before running any install/download command (npm install, pip install, plugin install, cloning a repo, pulling a model, etc.), first check whether it's already present — check installed packages, existing binaries/dirs, `which`/`Get-Command`, node_modules, existing plugin lists, etc. Only download/install if the check confirms it's missing.

**Why:** User corrected this directly ("dont download things before u check if we got them hard code this") after a session redundantly ran a fresh Flick bootstrap (npm install of Remotion/ffmpeg/Whisper) without first checking if those deps already existed locally.

**How to apply:** This is a hard rule, not a suggestion — treat it as always-on for every install/download action across all projects, not just this one. Cheap existence checks (ls, which, pip show, npm ls, ToolSearch/OVERSEER for skills) go first, every time.
