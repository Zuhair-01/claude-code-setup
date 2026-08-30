---
name: reference-public-api-directories
description: Three GitHub directories of free/public APIs to check before building a custom scraper or paying for a data provider.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 74906564-ca95-4b29-bc30-4b3dc9038a37
  modified: 2026-08-22T13:47:24.625Z
---

When a task needs an external data source and no paid provider is already decided, check these before hand-building anything (aligns with the free-first principle in [[project_nabd_opportunity_engine]] and CLAUDE.md's free-for-dev-default rule):

- https://github.com/public-apis/public-apis — the largest general-purpose free API list, categorized.
- https://github.com/public-api-lists/public-api-lists — a curated, actively maintained alternative/superset.
- https://github.com/APIs-guru/openapi-directory — machine-readable OpenAPI specs for thousands of APIs, useful when you need to generate a typed client instead of reading docs by hand.

**How to apply:** before scraping a site, paying for enrichment, or building a bespoke integration, search these three for a free tier that covers the need. Zoher surfaced these while building NABD's Free-First Opportunity Engine (2026-08-22) specifically so this check becomes a reflex, not a one-off.

**Specific free sources verified working, 2026-08-22 (NABD build)** — real, tested, not just theoretical:
- **Greenhouse/Lever/SmartRecruiters/Workable** — every major ATS exposes a free keyless public JSON API for a company's own job board (`boards-api.greenhouse.io/v1/boards/<slug>/jobs`, `api.lever.co/v0/postings/<slug>`, etc). First-party hiring data, zero ToS risk, no geography lock-in — better than any job-board aggregator for a "is this company hiring" signal.
- **Wikidata SPARQL** (`query.wikidata.org/sparql`) — free, keyless, no signup. Single-entity lookup via `wbsearchentities`, or real multi-entity discovery by structured criteria (country + business type) via a full SPARQL query. Rate-limits hard on parallel requests — sequential with a ~400ms gap is required.
- **Hacker News Algolia** (`hn.algolia.com/api/v1/search`) — free, keyless, explicitly built for third-party use.
- **Rejected as dead ends, don't re-check these**: Bing News RSS (works technically, but its own feed forbids commercial/programmatic use), GDELT doc API (persistent aggressive rate-limiting even at low volume), Adzuna/Arbeitnow (zero Middle East coverage), any LinkedIn-data reseller (Proxycurl got sued by LinkedIn/Microsoft and shut down for this exact model), UAE/GCC government business registries (no free API exists at all, confirmed).
