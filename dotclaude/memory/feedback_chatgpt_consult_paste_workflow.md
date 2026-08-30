---
name: feedback-chatgpt-consult-paste-workflow
description: "How to run a ChatGPT consult cheaply — Zoher pastes the response back, Claude never browser-extracts it"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ba2b7e9c-4fda-4f6a-bf78-0c2ff84a5a30
  modified: 2026-08-30T12:15:16.178Z
---

When a task needs a ChatGPT pass (SMM review, prompt sharpening, second opinion), do NOT drive
the whole loop in the browser. Browser JS `insert + submit` needs the message base64-encoded,
and every base64 blob + every capture chunk **echoes back into Claude's context** — one full
round-trip burns ~10k+ tokens and fills the window fast (hit 85% in one session doing this).

**The workflow Zoher wants (2026-08-30):**
1. Claude writes the exact prompt/message to paste, as a file or a code block in chat.
2. **Zoher** pastes it into ChatGPT, then selects the RELEVANT part of the response (top-to-
   bottom, not literally Ctrl+A which would grab the whole chat) and pastes it straight into
   the Claude chat "as if it's me."
3. Claude ingests that pasted text and does the merge.

Claude only drives the browser when the task genuinely needs live interaction Zoher can't do by
hand (navigating a tool, clicking through a flow). A plain "ask ChatGPT X, bring back the
answer" is always: Claude drafts → Zoher pastes both ways.

**Why:** [[feedback_smm_review_lessons]] cycles work fine this way; the browser-driven version
of the same thing cost 5x the tokens for no extra value. Also applies to any
paste-into-external-LLM step (Gemini prompt review, etc.).
