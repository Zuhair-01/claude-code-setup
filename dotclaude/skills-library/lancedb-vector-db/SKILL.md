---
name: lancedb-vector-db
description: Free, embedded, serverless vector database (LanceDB) — no server process, reads/writes disk-backed columnar format directly from Python/Node. Replaces paid vector DB hosting (Pinecone, managed Qdrant Cloud) for local-first RAG. Use when a project needs semantic search/embeddings storage without running a separate DB service.
risk: unknown
source: github.com/lancedb/lancedb (Apache 2.0)
date_added: 2026-08-26
---

# LanceDB

In-process, embedded vector database. No server to start, no port to
configure — imports as a library and reads/writes directly to disk (Lance
columnar format), with disk-based IVF-PQ indexing so datasets larger than RAM
still work. Free, Apache 2.0.

**Replaces**: Pinecone, managed Qdrant/Weaviate Cloud, or spinning up a full
Chroma/Qdrant server for local-only workloads.

## When to use on this box
- [[vault-search]] (turbovec, `reference_vault_search_turbovec.md`) already
  does semantic search over Second_Brain — if that ever needs to scale past
  its current index or add disk-backed persistence without a running
  service, LanceDB is the natural swap-in (same "no server" shape it likely
  already has).
- Any new RAG feature (Kyros knowledge recall, project-specific doc search)
  that doesn't need multi-client concurrent writes — pick LanceDB over
  standing up Qdrant/Chroma as a service.
- If concurrent multi-writer access or a query API over the network is
  actually needed, use Qdrant instead (better free self-hosted option for
  that shape — 30-40ms query latency, native sparse vectors).

## Install
```
pip install lancedb
```
No Docker, no separate process. Table = a directory on disk.

## Capabilities
- Embedded vector search (ANN, IVF-PQ)
- Full-text + vector hybrid search
- Versioned tables (time-travel queries)
- Zero-copy reads via Arrow
