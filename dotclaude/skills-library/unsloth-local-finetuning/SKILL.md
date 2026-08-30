---
name: unsloth-local-finetuning
description: Free, open-source LoRA/QLoRA fine-tuning library (Unsloth) that runs 2-5x faster with ~70% less VRAM than standard HF training, tuned for consumer GPUs. Replaces paid fine-tuning APIs (OpenAI fine-tuning, Together.ai fine-tuning) for anyone with a local NVIDIA GPU. Use when a project needs a custom-tuned local model instead of paying per fine-tune job.
risk: unknown
source: github.com/unslothai/unsloth (Apache 2.0)
date_added: 2026-08-26
---

# Unsloth (Local Fine-Tuning)

Open-source LoRA/QLoRA fine-tuning library, drop-in for Llama/Qwen/Mistral/
Gemma-family models. 2-5x faster and ~70% less VRAM than stock HuggingFace
training via custom Triton kernels — fine-tunes a 7-8B model on a single
consumer GPU (fits an RTX 4060-class card with QLoRA + small batch).

**Replaces**: OpenAI fine-tuning API, Together.ai fine-tuning, other paid
per-job fine-tuning services — for anyone with a local NVIDIA GPU, which this
box has (RTX 4060, per `Empire_Base/CLAUDE.md`).

## When to use on this box
- Any project wanting a model specialized on its own data (e.g. an
  alwazour-product-knowledge model, a brand-voice-tuned copy model) instead
  of prompting a bigger model every time or paying for a hosted fine-tune.
- Pairs with [[local-llm-expert]] for serving the tuned model afterward via
  Ollama/llama.cpp (Unsloth exports to GGUF directly).

## Install
```
pip install unsloth
```
Colab-style notebooks ship in the repo for common base models; adapt locally
by pointing at a local dataset and setting `load_in_4bit=True`.

## Capabilities
- QLoRA/LoRA fine-tuning, 2-5x speedup
- Direct export to GGUF for Ollama/llama.cpp serving
- Supports Llama, Qwen, Mistral, Gemma, Phi model families
- Runs on a single consumer GPU
