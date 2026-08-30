---
name: feedback-user-drives-ai-gen-tools
description: "On AI generation tools (Flow, image/video gen, etc.), user wants to drive the actual prompting/clicking themselves — Claude opens the site and guides, doesn't operate it, unless told to do everything autonomously."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0e1fa28e-23ba-4ea5-9b19-7c5dbf7c72c8
  modified: 2026-08-22T12:12:49.037Z
---

For AI generation tools (Google Flow/Veo, image gen, etc. — anything spending
real credits/money per action), default mode is: Claude opens/navigates to
the site and tells the user what to do next (which button, what to check),
rather than typing prompts and clicking generate itself.

**Why:** Said explicitly 2026-08-22 after a session where Claude drove Flow
generation directly, burned free credits on an over-engineered second prompt
that produced a worse result than the simple first one, then hit an
exhausted credit pool on a follow-up edit. User wants direct control over
spend-per-click decisions on these tools going forward.

**How to apply:** Default to guide-mode (navigate + explain + wait for the
user's own actions) for anything that spends credits per generation. Switch
to full autonomous operation (typing prompts, clicking generate, iterating)
only when the user explicitly says so for that session/task — the default
reverts back to guide-mode next time unless they say otherwise. Applies to
Flow/Veo specifically per this conversation; treat as the general pattern
for any other paid-per-action generation tool too. See [[ai-video-prompt-engineering]]
(skill, not memory) for the actual prompt-engineering methodology this
session also produced — that skill itself is still fine to reference/recommend,
this preference is only about who clicks the buttons.
