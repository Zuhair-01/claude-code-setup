---
name: reference-supabase-accounts
description: Which Supabase accounts/orgs exist and which projects live under each — check before creating a new Supabase project for any client site.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 53b2560f-1237-4feb-a083-61de7c6a239d
  modified: 2026-08-26T18:52:08.904Z
---

Two Supabase accounts in use, each on the free plan (2 active project limit per account):

**Account 1 — axissummer@gmail.com** ("axissummer@gmail.com's Org")
- `alwazour` — alwazour project
- `axissummer@gmail.com's Project` — currently paused
- `ostazi-sy` — Ostazi project

**Account 2 — bizwithzuhair** ("bizwithzuhair's Org")
- `dania-makeup-site` — Dania Shoshra makeup-artist site backend (bookings + earnings tables,
  RLS: public insert-only on bookings, authenticated-only on everything else). Project ref
  `jnushaebyxgnanjcgfbk`, region eu-central-1 (Frankfurt). Admin login: dania@gmail.com.
  Related: [[project_dania_makeup_site]] (if/when that memory exists).

When starting a new client project that needs Supabase, check this file first — pick whichever
account has a free project slot rather than assuming a new account is needed.
