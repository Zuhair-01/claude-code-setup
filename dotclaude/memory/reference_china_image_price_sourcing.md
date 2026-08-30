---
name: reference-china-image-price-sourcing
description: "Existing tools that find China-factory suppliers/prices from a product photo — don't build this from scratch"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 154da888-1291-40cc-bccb-cf2069fe83d6
  modified: 2026-08-27T01:08:38.644Z
---

Zoher asked (2026-08-27) for "an app to scan a photo and find the best China market prices" — he'd seen someone using something like this to source products at the lowest possible price. This already exists as a real tool category, no custom build needed:

- **AliPrice / AiPrice** (aiprice.com, aliprice.com) — browser extension, reverse-image-searches a product photo across 1688, Alibaba, Taobao, AliExpress simultaneously; built specifically for "find the cheapest factory for this product." Most comprehensive option, covers 1688 (the real wholesale/factory marketplace, not just Alibaba.com's retail-facing layer).
- **Alibaba Lens** — Alibaba's own official image-search Chrome extension.
- Both are Chrome Web Store extensions — installing requires Zoher's own click-through in his real Chrome (Google blocks scripted extension installs from the store, even via browser automation), so this can't be done for him unattended.

**How to apply:** next time working with Zoher live, install AliPrice/AiPrice in his Chrome, do a live demo search against a real alwazour product photo, and see if the supplier hits are useful enough to fold into the admin's "Photo sourcing" / "Suppliers" workflow (`server/ui.ts` renderPhotos/renderSuppliers) — e.g. a "Search by image" link next to a product's photo that opens AliPrice pre-loaded with that image, rather than reinventing the reverse-image-search/matching logic.
