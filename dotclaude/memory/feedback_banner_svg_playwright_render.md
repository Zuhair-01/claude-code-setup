---
name: feedback-banner-svg-playwright-render
description: Confirmed frontend win — hand-built SVG banner + Playwright-rendered PNG export counts as real frontend/design progress worth repeating.
metadata:
  type: feedback
---

Zoher marked the NABD repo banner (hand-coded `.github/banner.svg` + a Playwright-rendered PNG export for GitHub's social-preview slot) as a concrete example of upgraded frontend output — not generic AI slop.

**Why:** it's a real designed asset (gradient, typography, badges) built directly in SVG rather than a stock template, then correctly exported to the exact pixel size a platform needs (1280x640 social preview) using an actual rendering pipeline (Playwright screenshot of an HTML wrapper) instead of guessing dimensions or shipping unrendered SVG.

**How to apply:** for future banners/social-preview images/static graphic assets, default to this pattern — hand-authored SVG for the design, Playwright (local, already verified per [[reference_local_playwright_screenshots]]) to render to PNG at the exact target dimensions the destination platform expects. Treat this as the bar for "polished," alongside [[frontend_master_spec]] and [[feedback_design_quality]].
