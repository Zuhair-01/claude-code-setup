---
name: reference-vault-search-turbovec
description: "turbovec-backed semantic search tool over the Second_Brain vault, invoked automatically via the vault-search skill"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8da1b73b-2590-4e36-bb25-803a36a3ab6f
  modified: 2026-08-24T16:16:30.294Z
---

Semantic (meaning-based) search over `Second_Brain` exists as a live skill:
`vault-search` (`~/.claude/skills/vault-search/SKILL.md`).

Built 2026-08-24: `turbovec` (pip package, Rust vector index) + local Ollama
`nomic-embed-text` embeddings. Script:
`C:\Users\Zoher\Desktop\Empire_Base\growth-os\vaultmind\turbovec_search.py`.
Indexes all 54+ markdown files under Second_Brain, chunked (~3000 chars,
300 overlap) to fit the embedder's context. Reindex is mtime-cached — only
changed files get re-embedded, so `--reindex` is cheap on every call.

Requires local Ollama with `nomic-embed-text` pulled — the script
self-heals this (checks localhost:11434, auto-runs `ollama serve` if down,
waits for it), so no manual start is needed by any session. This is
separate from the AnythingLLM/VaultMind Docker container,
which was found not running when this was built and doesn't support
custom Rust vector backends anyway (its plugin list is fixed: LanceDB,
Chroma, Qdrant, etc.) — so this is a standalone sidecar tool, not wired
into that container.

**How to apply:** any future session — either account — should invoke the
`vault-search` skill (not hand-roll grep) whenever the user asks about past
decisions/context that might be documented in the vault, and per the
skill's own instructions, announce out loud when it's being used and what
query is being run before calling it.

**Hardened 2026-08-24 after a real concurrency bug found in review:** the
original design used 3 separate sidecar files (sources.json, mtimes.json,
embeddings.npy) each written "atomically" via temp+`os.replace` — but a
concurrent second `--reindex` (proven to actually happen: a peer session's
Claude can auto-trigger this skill on its own, or the OpenCode env now
running in the same vault can too) could interleave those 3 writes and
leave them mutually inconsistent (sources referencing a row embeddings.npy
didn't have) — crashed on next read. Fixed by merging all three into one
file (`index_meta.npz`), so a single `os.replace` covers the whole state
atomically — no cross-file window to land in. Also found: Windows'
`os.replace` (unlike POSIX `rename()`) can throw `PermissionError` if
another process has the destination open for reading at that exact
instant — added a short retry-with-backoff around every replace. Stress-
tested with 3 truly simultaneous `--reindex` processes post-fix: no
corruption, no crash, consistent on-disk state confirmed by direct
inspection. **General lesson, not just for this tool:** on Windows, a
naive "write to .tmp then os.replace" is necessary but not sufficient
under concurrency — (1) split state across multiple files only if you can
tolerate them briefly disagreeing, and (2) `os.replace` itself needs
retry logic here, it isn't guaranteed to succeed on the first try the way
POSIX rename is.
