---
name: feedback-no-large-downloads
description: Never download/install anything 1GB+ without explicit confirmation first
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 84ee4fab-9201-433a-b1db-56acd74df066
  modified: 2026-08-26T01:04:39.006Z
---

Never download or install a file/model/package 1GB+ (weights, checkpoints,
large datasets, big binaries) without asking first and getting explicit
confirmation on the specific item and its size.

**Why:** stated as a standing hard rule (2026-08-26), during the free/OSS
AI-stack research sweep ([[project_free_oss_ai_stack_research_2026_08_26]])
where multiple lanes were about to reach for local model weights (video-gen
checkpoints, avatar models, fine-tuning base models) that commonly run
several GB each.

**How to apply:** before any `pip install` that pulls large weights, any
direct model-weight download (HuggingFace, civitai, GitHub releases with
model files), or any Docker image pull that's model-heavy — check the
expected size first (repo README, HF model card, `du`-able comparison) and
ask before proceeding if it looks like 1GB+. Installing the *library*
(pip package itself, usually MB-scale) is fine; it's pulling the actual
model weights that needs a check-in. Applies across all concurrent sessions,
not just this one — see [[feedback_multi_session_orchestration]].
