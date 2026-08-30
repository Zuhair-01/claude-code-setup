---
name: feedback_design_quality
description: "User wants advanced, non-generic design for websites/apps/artifacts — real animation, deliberate color, 3D where it fits, not \"AI slop\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7e8c79f7-0420-4185-814f-df7bd989207d
---

For any website, app, or artifact build, push well past a generic/safe default: use deliberate color systems (not templated AI palettes), real typographic hierarchy, considered motion/animation (not just static cards), and 3D/WebGL where it genuinely fits the subject.

**Why:** User explicitly said (2026-07-14) he wants to be treated as "a better builder of websites, apps and artifact designer, not just AI slop but way more advanced animations, colors, 3D designs and many more." This is a direct correction against defaulting to plain/minimal treatments even for things he'll keep or show off.

**How to apply:** Before building any user-facing page/app/artifact, load the `artifact-design` skill (or equivalent) and lean toward the *editorial* treatment (bold typography pairing, motion, one real aesthetic risk) rather than the *utilitarian* treatment, unless the request is clearly a private reference doc/checklist for personal tracking. When 3D/motion tooling is relevant, consider skills like `threejs`/`threejs-*`, `gsap-*`, `webgl`-capable canvas work, or the `gpt-tasteskill`/`brutalist-skill`/`minimalist-skill` skill packs already installed, and pick deliberately rather than defaulting to plain HTML/CSS tables. Still avoid the specific AI-slop clichés (Inter/Space Grotesk, purple-blue gradient hero, cream+terracotta, emoji section markers) — "advanced" means intentional and crafted, not just more decoration.

Related: [[project_higgsfield_skills]] (has Playwright/visual pipeline already active).
