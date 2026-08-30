---
name: reference_local_playwright_screenshots
description: "Local headless Playwright (Python) is fully installed and working on this machine — self-controlled screenshot verification for ANY frontend/motion/3D work, no Chrome extension dependency"
metadata: 
  node_type: memory
  type: reference
  originSessionId: e06ce096-08c3-4f75-8dcb-581c38bc3c90
  modified: 2026-08-20T00:36:51.808Z
---

`pip show playwright` confirms it's installed (pulled in as a browser-use
dependency 2026-08-20), and `python -m playwright install chromium` has
been run — Chrome for Testing 151.x, Firefox, and Webkit binaries are all
present at `C:\Users\Zoher\AppData\Local\ms-playwright\`. Verified working
end-to-end same day: screenshotted a live localhost dev server, read the
PNG back via the Read tool, confirmed it matched what the user saw.

**Why this matters**: [[feedback_no_blind_frontend_claims]] documents the
actual failure mode this fixes — building/claiming frontend quality
without ever seeing the rendered output, because the interactive
Chrome-extension MCP tools weren't connected. This gives an independent,
always-available verification path that doesn't depend on that extension
at all.

**How to apply**: for ANY frontend, motion, or 3D/WebGL work in ANY
project, before claiming it looks right or matches a design bar, run a
real headless screenshot and Read it back:

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto("http://localhost:5173/")
    page.wait_for_timeout(1000)  # let animations/motion settle if needed
    page.screenshot(path="verify.png")
    browser.close()
```
Then `Read` the PNG — it renders as an image in context, so the actual
pixels can be checked against the design bar before claiming anything.
For motion/3D specifically, also capture `page.on("console", ...)` output
to catch silent WebGL/JS errors that produce a blank canvas with no
visible error.

Always delete the screenshot file after checking it (scratch artifact,
not a deliverable) unless the user asked to keep it. If a project's dev
server needs starting first, start it backgrounded, screenshot, then
kill it again afterward — don't leave dev servers running idle.
