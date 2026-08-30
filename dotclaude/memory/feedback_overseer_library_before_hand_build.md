---
name: overseer-library-before-hand-build
description: "Before hand-building any frontend/design component or effect from scratch, search the OVERSEER library (dormant skills-library, not just live skills) — especially frontend-upgrade-kit's reel-derived component catalogue — for a pre-scouted reference first."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 96a1811d-29d1-4bab-8161-57c2a9c160ab
  modified: 2026-08-16T13:49:52.378Z
---

Before writing custom frontend code (animations, components, visual effects) from scratch, run `python ~/.claude/overseer/search.py <keywords>` against the **library** (dormant ~2800-skill index), not just the live skill-router pass. [[feedback_skill_router]] already covers picking from live skills+agents per task — this is the missing second check: the *dormant library* holds pre-scouted, real reference material (e.g. `~/.claude/skills-library/frontend-upgrade-kit/` with a table of Instagram reel-derived component techniques, saved mp4s under `Second_Brain/Workflow/30 - Resources/frontend-upgrade-assets/`) that OVERSEER's own search doesn't surface unless explicitly queried.

**Why:** 2026-08-16, TutorLink-Syria session — hand-built an OTP-success animation and shake/pop keyframes from scratch before checking that `frontend-upgrade-kit/SKILL.md` already catalogued two OTP-specific reel techniques (`DbxxWJnoR2L` — digits orbit into a converging verified-checkmark ring; `DbbNr-SvJkK` — boxes fuse into a "verified seal") with the actual mp4s saved and ready to frame-extract. The user had to explicitly point this out ("there is in code n chill from ig we took it while upgrading our frontend") rather than it being caught proactively.

**How to apply:**
1. Any time a task is frontend/UI/animation/component work, check `~/.claude/skills-library/frontend-upgrade-kit/SKILL.md` (or `overseer/search.py <effect/component name>`) before designing an effect from first principles.
2. If a saved reel mp4 matches, extract frames (`ffmpeg -vf fps=2`) and actually view them via Read before recreating — the caption/table entry alone is a lossy summary, not the real technique.
3. Recreate in-brand (this project's actual palette/tokens), not a literal copy of the reel's colors — the point is the *technique* (e.g. orbit-converge motion, dashed-ring spinner), not the source's violet/aqua branding.
4. This applies beyond frontend-upgrade-kit — any dormant library entry (skill, reference doc, saved asset) is a candidate before building fresh. Don't wait for the user to say "use your skills" a second time.
