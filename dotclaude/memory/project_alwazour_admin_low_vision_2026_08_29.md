---
name: project_alwazour_admin_low_vision_2026_08_29
description: "Alwazour admin panel low-vision readability pass + A/A+/A++ text-size toggle — done 2026-08-29, admin only"
metadata: 
  node_type: memory
  type: project
  originSessionId: 176f8c93-782a-4534-8c3a-4aec4e1a4a81
  modified: 2026-08-29T12:53:26.366Z
---

The Alwazour business owner who runs the **admin panel** daily has weak vision
and could not read the small Arabic text. On 2026-08-29 shipped a readability
pass — **admin panel only** (public site + Ostazi explicitly out of scope; if
asked to extend, that's new work).

What changed (all in `alwazour/server/`, not committed — `server/` is a
standing never-commit choice, changes apply on the admin server's next
restart / Render redeploy):
- `ui.ts` `SHELL_STYLE` → rem-based scale off 16px root, readable floor
  (tables 15px, nothing <13px), uppercase + letter-spacing stripped from
  section headers, muted→inkSoft for contrast, tap targets ≥36px,
  `:focus-visible` outlines. Arabic: root 17px + `body{font-weight:500}` +
  line-height 1.75 (IBM Plex Sans Arabic 400 reads thin).
- `i18n.ts` — `injectLangToggle` renamed `injectA11yDock`: bottom-corner dock
  with **A / A+ / A++** (أ / أ+ / أ++) buttons above the language pill. Pure
  client-side — `document.documentElement.dataset.ts` + `localStorage
  ['alwazour_admin_ts']`, levels sm/lg(18.4px)/xl(20.8px). No reload.
- `ui.ts` `HEAD_A11Y` — sync `<head>` script restores the level pre-paint
  (no flash), in both `shell()` and `renderLogin()`.
- `index.ts` `html()` calls `injectA11yDock` now.

Also that session: added a **"View live site ↗"** link to the admin topbar
(→ `ALWAZOUR_SITE_BASE_URL` env / `alwazour.vercel.app`). And: the hidden
admin entry point is the **copyright year** in the public-site footer
(`src/site/shell.ts`, `.ftr-admin` — disguised link to `/admin`).

Verified on the login page via Playwright (toggle sets level, persists across
reload no-flash, Arabic→rtl+larger). Authed table pages NOT screenshot-verified
— local `.env.local` has real Supabase + real creds so `admin`/`change-me-now`
401s; they share the same shell path so covered by construction. See
[[project_alwazour_2026_08_22]].
