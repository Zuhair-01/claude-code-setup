---
name: project_open_pinterest_repo
description: "open-pinterest skill upgraded (video download, bg removal, smart eval) + published as public GitHub repo/Claude Code plugin, now mandatory routing for frontend visual tasks"
metadata: 
  node_type: memory
  type: project
  originSessionId: 8dbad396-65ff-4987-b7db-52e59bddd11d
  modified: 2026-08-21T13:52:19.321Z
---

`open-pinterest` skill upgraded 2026-08-21: now downloads video/motion-graphics pins
(`scripts/download_video.py`, yt-dlp) and background-removes subjects
(`scripts/remove_bg.py`, rembg), plus an "actually evaluate every candidate against the
brief" step instead of grabbing top-N by caption match. Published as
**github.com/Zuhair-01/open-pinterest** (public, MIT) — also packaged as an installable
Claude Code plugin (`.claude-plugin/plugin.json` + `marketplace.json`, install via
`/plugin marketplace add Zuhair-01/open-pinterest`).

**Why:** Zoher wants this skill both genuinely more capable (video, not just stills) and
used as growth — public repo with stars/follow badges, aiming for community pickup.

**Two copies exist and can drift**: the public repo and the local
`~/.claude/skills/open-pinterest/` install are separate files — the local one lagged the
repo's video-capable description once already. See [[feedback_low_context_handoff]] pattern:
always check both when editing this skill.

**Routing**: `~/.claude/CLAUDE.md` Rule 7's frontend sub-rule + `BUNDLE-B-frontend`'s Quick
Start now both require any frontend task with a specific real-world visual/motion look to
route through `open-pinterest` first, before `taste-skill`/`motion-ui`/`threejs`/
`frontend-design` build the component.

**How to apply:** when touching this skill, edit both the repo checkout and the local
install in the same pass, and re-check CLAUDE.md's Rule 9 hasn't gone stale. Repo declined
to ship any real scraped Pinterest images/banners — only original art — see repo's own Rules
section in SKILL.md for the reasoning (copyright/ToS).
