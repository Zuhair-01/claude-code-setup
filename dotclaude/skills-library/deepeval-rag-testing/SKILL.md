---
name: deepeval-rag-testing
description: Free, open-source LLM/RAG evaluation library (DeepEval) with 50+ metrics (hallucination, answer relevancy, faithfulness, contextual precision/recall) runnable as pytest assertions. Replaces paid eval SaaS (Braintrust, Athina paid tiers) for CI-gated LLM output quality checks. Use when a project needs automated pass/fail evals on RAG or agent outputs, not just manual spot-checks.
risk: unknown
source: github.com/confident-ai/deepeval (Apache 2.0)
date_added: 2026-08-26
---

# DeepEval (RAG/LLM Testing)

Open-source LLM evaluation framework, Apache 2.0, that plugs into pytest —
metrics run as regular test assertions (`assert_test`) so RAG/agent quality
checks live in CI like any other test suite. 50+ built-in metrics: hallucination,
answer relevancy, faithfulness, contextual precision/recall/relevancy, bias,
toxicity, and custom G-Eval (LLM-as-judge) metrics.

**Replaces**: Braintrust/Athina paid eval tiers for teams that just need
metric-based pass/fail gating, not a hosted dashboard. (Existing generic
`evaluation`/`agent-evaluation`/`llm-evaluation` skills cover eval
*methodology* — this is the concrete free library to actually run it.)

## When to use on this box
- Any RAG feature (vault-search, Kyros knowledge recall, alwazour product Q&A
  if ever built) that needs a regression check before shipping a prompt or
  retrieval change — write DeepEval assertions instead of manually eyeballing
  outputs each time.
- Judge model can be a local Ollama model (point DeepEval's LLM-as-judge
  config at a local endpoint) to keep evals fully free/offline.

## Install
```
pip install deepeval
```
Write metrics as pytest tests: `deepeval test run test_rag.py`.

## Capabilities
- 50+ pre-built RAG/agent/safety metrics
- Pytest-native (CI-friendly)
- Local model support for judge calls (no API cost required)
- Dataset/golden-set management
