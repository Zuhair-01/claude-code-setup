---
name: Empire Base Agency
description: Zoher's AI Video Factory — 4 pillars, $10k/mo target, full stack + vault context
type: project
originSessionId: 991f7260-4bb6-4a64-ba53-5853474f3ff9
---
## Core Mission
Zero-capital AI Digital Arbitrage. RTX 4060 replaces SaaS subscriptions. Local pipeline → automated content → multiple revenue streams → $10k/mo.

## 4 Pillars
1. **Clipping Factory** — long-form → 60s vertical clips → Whop Content Rewards → USDT payout (~$3k/mo target)
2. **AI-UGC** — AI-generated content → high-ticket SaaS affiliate funnels + brand retainers (~$4k/mo target)
3. **Arabic Localization** — dub/translate Western creator content for MENA market, 20–30% rev-share (~$3k/mo target)
4. **B2B Syria** — B2B outreach / "Revenue Recovery" to Syrian market (reconstruction, HVAC, Law firms, SMEs); ACAS Rejection Formula for sales

## Tech Stack
- Local AI: Ollama + Gemma 4 (RTX 4060); Whisper for transcription
- Automation: n8n (localhost:5678, JWT key configured in .claude.json)
- Video: FFmpeg + `auto_clipper.py` (moviepy, `--gpu` for h264_nvenc)
- Claude: 15 MCP servers configured; bypass permissions enabled

## Key File Locations
- Clip script: `C:\Users\Zoher\Desktop\Empire_Base\Clipping_Agency\auto_clipper.py`
- Strategy doc: `C:\Users\Zoher\Desktop\Empire_Base\Clipping_Agency\Master_Strategy_2026.md`
- Old vault: `C:\Users\Zoher\Empire_Base_Agency\` (legacy)
- **Active vault (Obsidian):** `C:\Users\Zoher\Desktop\Empire_Base\Second_Brain\Workflow\`
  - Dashboard: `00 - Home\Dashboard.md`
  - Projects: `10 - Projects\` (4 pillar MOC notes)
  - Areas: `20 - Areas\` (Tech Stack, Revenue Tracker, n8n Workflows, Campaign Log)
  - Resources: `30 - Resources\` (Tools Reference, Research)
  - Templates: daily note, project, campaign

## MCP Servers
- ✅ Active: filesystem, second-brain, n8n, serper, exa, puppeteer, ffmpeg
- ⚠️ Need keys: brave-search, alpha-vantage, whales, firecrawl, hubspot
- FMP REST key: `zKJp8gPF7nYBUYpqTDZ9Z7i2RQBvCYTe`

## Telegram → Claude (planned)
n8n workflow not yet built. Needs: Telegram Bot Token + Claude API key from console.anthropic.com.

## Operating Rules
- Use ACAS Rejection Formula for B2B sales
- Token efficiency: tight responses, action-first
- Never hallucinate — verify via search tools
- Always write findings to Second Brain vault via mcp__second-brain tools
- Priority: execution speed over perfection

**How to apply:** When a task arrives, identify the pillar, read the relevant MOC via second-brain MCP, then act. Write outputs back to vault.
