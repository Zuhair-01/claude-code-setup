---
name: frontend-upgrade-kit
description: "Curated stack of animated/3D UI component registries, icon sets, and design tools (Unlumen UI, SmoothUI, RetroUI, Magic UI, Uilora, UI Verse, Pikaicons, Khroma, Endless Tools) sourced from a batch of reels, with exact install commands for any Next.js/React project -- current and future. Use for: 'upgrade the frontend', 'add animations/3D to the UI', 'premium components', 'design system upgrade', 'what UI libraries do we have', 'set up shadcn registries in a new project'."
---

# Frontend Upgrade Kit

A reusable stack of shadcn-CLI-compatible component registries + standalone design tools, sourced
2026-08-16 from a batch of @kevin.developer Instagram reels (via [[skill_reel_intent_analyzer]]).
Installed into `clip-platform/web` as the first project; every registry below is a public URL —
any future Next.js/React project can pull the same components with the same commands, no need to
re-discover or re-copy files between projects.

## Theming recipe (general — not clip-platform-specific, added 2026-08-16)

Every component in every registry below (SmoothUI, RetroUI, Magic UI, Unlumen, shadcn) is written
against the same semantic Tailwind class names — `bg-background`, `bg-card`, `bg-primary`,
`bg-secondary`, `bg-muted`, `bg-destructive`, `border-border`, `ring-ring`, `bg-sidebar*`. None of
that is clip-platform- or Kyros-specific — it's the shadcn convention every one of these registries
was built to. To make the whole kit look on-brand on ANY project in one pass:

1. Find (or invent) that project's own raw palette tokens (background/surface color, text color,
   one or two brand accent colors, a danger/success color).
2. Map those onto the standard semantic set, **inside the project's single existing `@theme
   inline` block** (Tailwind v4) — not a separate imported file. A second/separate `@theme` block
   in an `@import`-ed file silently fails to merge; learned this the hard way on clip-platform,
   costed a full debug cycle. One block, in the main CSS entry point, always.
3. Minimum token set every component in this kit expects: `background`, `foreground`, `card`,
   `card-foreground`, `popover`, `popover-foreground`, `primary`, `primary-foreground`,
   `secondary`, `secondary-foreground`, `muted`, `muted-foreground`, `accent-foreground`,
   `destructive`, `destructive-foreground`, `border`, `input`, `ring`, `radius` (+
   `radius-sm/md/lg/xl` as `calc()` off `radius`), and 8 `sidebar-*` tokens if `ui/sidebar.tsx` is
   pulled. Map `primary` to whatever the project's one "action" color is — that's the correct home
   for it in every design system, not just Kyros's.
4. Verify with a throwaway `/dev/kit` (or similar) route rendering a few components (Button
   variants, Card, Badge, Dialog) and an actual screenshot — a clean `tsc` does NOT prove the
   colors are wired, only that the types line up. Confirmed this gap firsthand: types were clean
   while every button was unstyled.
5. Watch for a second real gotcha: some sub-registries assume Radix (`asChild` prop), others
   assume Base UI (`render={<element/>}` prop) for the exact same primitive name (Dialog, Popover,
   ComboBox, ContextMenu). Check which one the actual installed `components/ui/X.tsx` wraps
   (`@base-ui/react/X` vs `radix-ui`) before touching any call site that errors — don't
   find/replace blindly, they're not interchangeable.

## Prerequisite (any new project) — copy the template, don't re-pull

The kit lives pre-pulled at `~/.claude/skills-library/frontend-upgrade-kit/template/` (297
`.tsx` files: `components/{ui,smoothui,magicui,unlumen-ui}`, `smoothui-data/`, `utils.ts`,
`components.json`). **Copy this into a new project — don't re-run `npx shadcn add` from scratch**;
copying is instant and doesn't depend on the registries staying up.

Fixed 2026-08-16: the first template copy accidentally included clip-platform's own bespoke app
components (`Landing.tsx`, `ClipCard.tsx`, `Nav.tsx`, `WaitlistLanding.tsx`, `CaptionPresetGrid.tsx`,
etc.) alongside the real kit — those are product-specific, not reusable, and have been removed from
the template. If the template ever gets re-synced from a live project's `components/` dir again,
copy only the `ui/`, `smoothui/`, `magicui/`, `unlumen-ui/` subfolders — never the project root.

```bash
# from the new project's root:
cp -r ~/.claude/skills-library/frontend-upgrade-kit/template/components/* ./components/
cp ~/.claude/skills-library/frontend-upgrade-kit/template/utils.ts ./lib/utils.ts
cp -r ~/.claude/skills-library/frontend-upgrade-kit/template/smoothui-data ./lib/smoothui-data
cp ~/.claude/skills-library/frontend-upgrade-kit/template/components.json ./components.json
npm install clsx tailwind-merge class-variance-authority
```

**Theming is REQUIRED, not optional, every time.** The template is deliberately untheme'd (default
shadcn neutral tokens) — see "Theming recipe" below. A copy-pasted kit with no theming step applied
will render with generic/wrong colors on any real project; don't skip it and don't treat "it
compiles" as done (a clean `tsc` proves types, not colors — confirmed this gap firsthand once).

If a project has no Tailwind/`components.json` at all yet, hand-write `components.json` (the
interactive `shadcn init` wizard hangs in non-interactive shells — don't fight it):

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": { "config": "", "css": "app/globals.css", "baseColor": "neutral", "cssVariables": true, "prefix": "" },
  "aliases": { "components": "@/components", "utils": "@/lib/utils", "ui": "@/components/ui", "lib": "@/lib", "hooks": "@/hooks" },
  "iconLibrary": "lucide"
}
```

(Registry URLs are still listed below for the rare case a component gets added/updated after this
template was captured — but copying the template is the default path, not a fresh pull.)

## Registries (free, fully pulled)

| Registry | Base URL | Count | Notes |
|---|---|---|---|
| **SmoothUI** | `https://smoothui.dev/r/{name}.json` | ~168 | Full catalog free, MIT. Marketing blocks (hero/pricing/stats/footer/testimonials) + a large `ai-*` set (ai-message, ai-response, ai-loader, ai-tool-call, ai-conversation...) great for AI-product UIs. Also micro-interactions: animated-file-upload, cursor-follow, dynamic-island, siri-orb. |
| **RetroUI** | `https://retroui.dev/r/{name}.json` | 54 | Full catalog free, open source (github.com/Dksie09/RetroUI). Neobrutalist/retro shadcn-alternative — full primitive set (accordion→tooltip). |
| **Magic UI** | `https://magicui.design/r/{name}.json` | 77 | Free, well-known. Effects: marquee, globe, meteors, warp-background, grid/dot patterns, text animations. |
| **Unlumen UI** | `https://ui.unlumen.com/r/{name}.json` | 136 total, **only 1 free** (`highlight`) | Rest gated behind `?token=$UNLUMEN_LICENSE_KEY` (Pro). Skip unless a license is purchased — ask Zoher first, don't buy autonomously. |

Batch-install pattern (don't loop one-npx-per-component, it's slow — pass many URLs to one `add` call, 15-25 at a time to avoid registry timeouts):

```bash
npx shadcn@latest add \
  https://smoothui.dev/r/ai-message.json \
  https://smoothui.dev/r/dynamic-island.json \
  ... \
  --yes --overwrite
```

## Gated / needs account (found, not pulled)

- **Uilora** (uilora.com) — has its own CLI (`npx uilora@latest add <id>`, also `list`/`view`/`mcp`
  subcommands, 573+ components advertised) but the registry returned `402 Payment Required` on
  every call as of 2026-08-16, despite marketing itself as "100% free." Re-check periodically —
  might be a temporary outage rather than a real paywall.
- **Pikaicons** (pikaicons.com) — old public npm package `pikaicons@0.0.5` is deprecated/unsupported,
  don't install it. The current icon set needs manual download from the site (537 free icons,
  Figma community file, or their own React package gated behind the site/account).

## Standalone tools (no install — web tools, use directly)

- **Khroma** (khroma.co) — AI color-palette generator.
- **Endless Tools** (endlesstools.io) — browser 3D tool: SVG→3D shape, AI 3D object gen, 3D
  typography, textures. No Figma/code integration confirmed — treat as a visual asset source
  (export images/models), not a library dependency.
- **UI Verse** (uiverse.io) — community HTML/CSS/Tailwind/React snippet gallery, copy-paste
  individually, no CLI/registry — browse and hand-pick when a specific snippet is wanted.

## 3D/animation foundation deps (installed alongside the registries)

`gsap`, `three`, `@react-three/fiber`, `@react-three/drei` — added to clip-platform for actually
building the 3D-animated-website effects the reels showed off. Not yet wired into any page —
that's real per-page design work, separate from this kit-acquisition pass.

## Icons — real replacement for the dead Pikaicons path (added 2026-08-16)

Skip Pikaicons entirely (deprecated npm, no clean install path — see above). Use instead, all real
npm packages, MIT/open-source, verified 2026-08-16:

- **Tabler Icons** (`@tabler/icons-react`) — 5,500+ SVG icons, tree-shakeable React components.
- **Phosphor Icons** (`@phosphor-icons/react`) — MIT, multiple weights (thin/light/regular/bold/duotone).
- **Heroicons** (`@heroicons/react`) — 450+, built for Tailwind, from the Tailwind Labs team.
- **Lucide** — already the project's `iconLibrary` in `components.json`; this list is for variety/gaps
  Lucide doesn't cover, not a replacement.

## 3D / cursor / motion tools (added 2026-08-16)

On top of the `gsap`/`three`/`@react-three/fiber`/`@react-three/drei` foundation already installed:

- **Unicorn Studio** (unicornstudio.io) — no-code shader/WebGL effect builder, exports embeddable
  effects. Good for background/hero-section shader work without hand-writing GLSL.
- Real-glass-refraction / chromatic-aberration cursor effects are a React Three Fiber pattern, not a
  library — see the `_code_and_chill_` reel batch below (`DbXiNGVvUQA` shows this technique live).
- No new must-install dependency found beyond what's already in the project — GSAP + Three.js/R3F
  already cover the credible options; skip one-off cursor-effect npm packages, they're mostly
  copy-paste CSS/JS anyway (that's the UI Verse category).

## Hand-recreate batch: @_code_and_chill_ (Hasibul Hasan, Instagram) — added 2026-08-16

Separate content type from the registries above: hand-built vanilla HTML/CSS/JS micro-interaction
demos ("zero dependencies", "no GSAP", "no framework" — stated in almost every caption). **Not
installable** — nothing to `npm install` or pull via a registry. The only path to use these is
watching the clip and recreating the technique by hand.

12 reels downloaded to
`Second_Brain/Workflow/30 - Resources/frontend-upgrade-assets/code_and_chill_reels/{id}.mp4`
(captions were pulled earlier via `yt-dlp --dump-json`; videos pulled 2026-08-16):

| ID | Technique | Fit for clip-platform |
|---|---|---|
| `Db7fSM1v8Yg` | login↔signup card-flip, single `translateX`, real forms | auth pages |
| `DcC_M4Rv1Zp` | tab underline "light reaches for it" microinteraction | nav/tabs |
| `Db_bxUZvz2n` | order-confirm button → animated delivery-truck scene | render/export success state |
| `Db3CrouPbxz` | premium payment/checkout animation concept | billing page |
| `DbxxWJnoR2L` | OTP: last digit curls 4 boxes into spinning verified ring (2-keyframe `rotate()`) | login/register OTP |
| `DbbNr-SvJkK` | OTP boxes fuse into one violet→aqua "verified seal" | login/register OTP (alt) |
| `DbXiNGVvUQA` | real-glass-refraction navbar (`backdrop-filter`) | top nav |
| `DbV5HtBPZ5w` | loading ring unrolls into progress bar, "parachutes" the download in | export/download UX |
| `DbQODFOvmka` | non-boring delete interaction (needs frame-viewing, caption light on detail) | delete confirm on clips |
| `DbAzYoVvFu7` | click-to-open soda can, color floods in, spring physics | onboarding/easter-egg |
| `Da0iDR4vl5M` | drag-drop file upload with retry-on-fail state | **upload page — direct fit** |
| `DbsEqK2v3ih` | **separate future project, not clip-platform**: "will you go on a date" card, Yes drops a real `.ics`, No dodges forever | n/a — filed apart |

Next: pick 1-2 (upload retry-on-fail + one OTP pattern are the obvious first wins) and hand-recreate
in a real component when doing page-by-page wiring — that's still unstarted, this pass was
acquisition only, same as the registries above.

## Round 2 — widening to categories the first pass missed (added 2026-08-16)

First pass covered generic SaaS component registries + icons + 3D/cursor. It missed several
categories clip-platform actually needs. Closed the gaps that are real installable packages;
documented (not installed) the ones that are asset sources requiring manual curation.

### Installed (real npm packages, low-risk, added to clip-platform now)

- **`recharts`** — campaign/clip performance charts (views, watch-time, virality score over time).
  No charting library existed before this; clip-platform's dashboard/campaigns pages need one.
- **`react-joyride`** — guided product tour / onboarding walkthrough. For first-run UX on
  dashboard/upload — nothing existed for this before either.

Both verified clean against `tsc --noEmit` (still zero errors project-wide after adding).

### Video-editor UI (the one category no generic registry covers — clip-platform is a video tool)

None of SmoothUI/RetroUI/Magic UI/Unlumen ship timeline/waveform/trim components — they're generic
SaaS-marketing kits. Real options found, **none installed yet**, evaluate before picking one:

- **shadcn.io Waveform Editor block** (shadcn.io/blocks/music-waveform-editor) — drop-in
  shadcn-style block: waveform bars, trim markers, zoom, selection region, playhead, export button.
  Closest fit to the existing shadcn-style stack already in the project.
- **Twick** (React SDK, canvas timeline: drag/trim/resize/layer for video+audio tracks) — heavier,
  more of a framework than a component.
- `react-native-video-trim` — mobile-only, not applicable to the web app.

### Charts — decision made, see "Installed" above (Recharts chosen over Tremor/Visx: Tremor is
heavier/more opinionated, Visx is lower-level and needs more hand-composition; Recharts is the
default-safe, most-downloaded, cleanest fit for a component-by-component dashboard build).

### Illustrations / empty states (not installed — these are asset libraries, not packages)

- **unDraw** (undraw.co) — best default: no attribution required, free commercial use, one-click
  recolor to match the Kyros violet/cyan accent before download. Use this first for "no clips yet" /
  "no campaigns yet" states.
- **Storyset** (Freepik) — only free source with pre-animated (CSS) illustrated scenes, but
  requires attribution + has daily download caps — use unDraw first, Storyset only if a specific
  scene isn't in unDraw.

### Fonts (not installed — decision needed, current stack already has 3 bundled caption fonts:
Anton, Bebas Neue, Poppins SemiBold — these are for the caption/render engine, NOT the app UI)

- **Fontshare** (fontshare.com) — curated, commercial-quality free variable fonts (Satoshi, General
  Sans, Switzer, Clash Display) — a step up from default Google Fonts if a UI typeface refresh is
  ever wanted. Not urgent — no evidence the current UI font is a problem, just flagging the option.

### Lottie / motion-JSON (not installed — asset source, pick specific animations only when a specific
loading/empty state needs one, don't bulk-import)

- **LottieFiles** (lottiefiles.com) — largest free library, loading indicators + micro-interactions.
  Pairs with `lottie-react` (small runtime, not yet installed — install only alongside the first
  actual `.json` animation picked, not preemptively).

### Onboarding — decision made, see "Installed" above (`react-joyride` chosen over React Shepherd /
Intro.js: simplest API, most popular, good enough for a straightforward dashboard tour — Shepherd is
more powerful but heavier setup, not needed at this scale).

## Related

- [[skill_reel_intent_analyzer]] — how these were sourced from the original reel links.
- `BUNDLE-B-frontend` (live skill) — points here for the "get me premium/animated components" case.
