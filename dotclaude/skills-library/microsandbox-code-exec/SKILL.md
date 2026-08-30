---
name: microsandbox-code-exec
description: Free, local, rootless code-execution sandbox (Microsandbox) for running LLM/agent-generated code safely — no cluster, no cloud account, runs on a single machine via libkrun microVMs. Replaces paid sandbox APIs (E2B, CodeSandbox SDK, Daytona cloud) for local agent workflows that need to execute untrusted generated code. No model weights involved — just a runtime binary.
risk: unknown
source: github.com/microsandbox/microsandbox (Apache 2.0)
date_added: 2026-08-26
---

# Microsandbox (Local Code Execution)

Local, rootless code sandbox using libkrun microVMs — isolates
LLM-generated code execution without needing a Kubernetes cluster or a paid
cloud sandbox API. Single-machine, Apache 2.0.

**Replaces**: E2B, CodeSandbox SDK, Daytona cloud tier — paid/hosted sandbox
APIs for agents that need to run generated code safely. (Beam/Daytona
self-hosted are the alternatives if GPU workloads or a cluster are needed —
Microsandbox is the right pick for this box's single-machine, no-cluster
setup.)

## When to use on this box
- Kyros orchestrator workers (local Ollama fleet) that generate code as part
  of a task and need to actually run/verify it before returning a result,
  without trusting `exec()` directly on the host.
- Any agent workflow that currently either skips execution verification or
  shells out unsandboxed — this closes that gap for free.

## Install
No model download — it's a runtime, not a model. Binary install per repo
README (cargo install or prebuilt release), no GPU/weights required.

## Capabilities
- Rootless microVM isolation per execution
- File I/O and networking support inside the sandbox
- No cluster/cloud dependency — single machine
- Fast cold start vs full VM
