---
name: Higgsfield UGC Skills Pack
description: 19 installed Claude Code skills for Higgsfield AI — UGC video pipeline, Seedance 2.0 automation, prompt styles. Auto-select based on task type.
type: project
originSessionId: 4849602e-d58c-4469-8b07-c208de7d6b57
---
## What's Installed
19 skills in `C:\Users\Zoher\.claude\skills\` from github.com/AKCodez/higgsfield-claude-skills.
Playwright MCP registered as `playwright` (npx @playwright/mcp@latest).
Higgsfield account required (free tier available). Login manually in Playwright browser on first use.

## Auto-Selection Rules (use these without being asked)

| Trigger | Skill to invoke |
|---------|----------------|
| "UGC ad", "UGC video", "faceless ad", full pipeline | `/ugc-video-auto` |
| "UGC girl", "female character", "hot girl for ads" | `/ugc-hot-girl` → `/higgsfield-image-auto` |
| "generate image on higgsfield" / image only | `/higgsfield-image-auto` |
| "seedance video", "generate video from image" | `/seedance-auto-generate` |
| "cinematic", "film style", "dramatic lighting" | `/01-cinematic` |
| "3D", "CGI", "Pixar style", "rendered" | `/02-3d-cgi` |
| "cartoon", "animation", "cel-shaded" | `/03-cartoon` |
| "comic", "manga", "webtoon" | `/04-comic-to-video` |
| "fight scene", "action", "martial arts" | `/05-fight-scenes` |
| "motion design", "SaaS ad", "app promo" | `/06-motion-design-ad` |
| "ecommerce ad", "product ad", "TikTok shop" | `/07-ecommerce-ad` |
| "anime", "shonen", "mecha" | `/08-anime-action` |
| "product 360", "turntable", "product reveal" | `/09-product-360` |
| "music video", "beat-synced" | `/10-music-video` |
| "social hook", "TikTok hook", "scroll-stopping" | `/11-social-hook` |
| "brand story", "origin story", "company video" | `/12-brand-story` |
| "fashion", "lookbook", "runway" | `/13-fashion-lookbook` |
| "food", "restaurant", "recipe video" | `/14-food-beverage` |
| "real estate", "property tour", "house video" | `/15-real-estate` |

## Empire Integration
- **AI-UGC pillar**: `/ugc-video-auto` is the primary content production tool
- **Clipping Factory**: use style skills (`/11-social-hook`, `/01-cinematic`) to craft prompts before batch clip generation
- **B2B Netherlands**: `/12-brand-story`, `/06-motion-design-ad` for client deliverables
- **Arabic Localization**: generate base video with UGC pipeline, then apply Arabic audio/subs in post

## Default Settings (Higgsfield)
- Image model: Soul 2.0 (`/image/soul-v2`)
- Image ratio: 3:4, resolution: 2K
- Video model: Seedance 2.0 (`/create/video?model=seedance_2_0`)
- Video duration: 8s, ratio: 9:16 (TikTok/Reels), resolution: 720p

## Key Notes
- Playwright opens its own controlled browser — normal
- Always ask user confirmation before clicking Generate (uses credits)
- Prompt bar needs JS clear between batch runs (skills handle this automatically)
- `/ugc-video-auto` is one-shot: image + video in a single command
- For batches, create `SESSION-RESUME.md` for crash recovery
