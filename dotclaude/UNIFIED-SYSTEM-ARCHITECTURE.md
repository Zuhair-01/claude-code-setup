# UNIFIED SYSTEM ARCHITECTURE (HISTORICAL)
Use `SYSTEM-TRUTH.md` for verified runtime wiring. This document describes
the intended design and may reference components that are not active.

---

## SYSTEM OVERVIEW

```
User Task Input
    ↓
skill-router (classify domain + action)
    ↓
Overseer Smart Selector (pick best bundle)
    ↓
Load Bundle (lazy, only what's needed)
    ↓
Route through OmniRoute (compress LLM calls)
    ↓
Execute skill chain
    ↓
Cache result + learn
```

**Key principle:** Skills never active 24/7. Bundles load on-demand only.

---

## COMPONENT 1: OVERSEER SMART SELECTOR

**File:** `~/.claude/overseer/smart-selector.py` (NEW)

```python
class OverseerSmartSelector:
    """
    Intelligent bundle selector using overseer index.
    Picks best bundle for task based on:
    - Keyword matching (task description)
    - Category analysis (overseer categories)
    - Historical performance (which bundles worked best)
    - Token efficiency (prefer smaller bundles)
    """
    
    def select_bundle(self, user_input: str, task_domain: str) -> dict:
        # 1. Parse user input (keywords, domain, action)
        # 2. Query overseer index for matching skills
        # 3. Find most specific bundle covering those skills
        # 4. Score bundle by: specificity, token cost, success rate
        # 5. Return bundle + primary skills
        pass
    
    def auto_bundle_new_skill(self, skill_path: str):
        # When new skill added to library
        # Auto-categorize and add to appropriate bundle
        # Update BUNDLE-REGISTRY.tsv
        # Rebuild overseer index
        pass
    
    def lazy_load(self, bundle_name: str):
        # Load ONLY selected bundle into context
        # Other bundles stay in library (0 token cost)
        pass
```

---

## COMPONENT 2: AUTO-BUNDLING SYSTEM

**Mechanism:** When skill/tool added → auto-creates bundle

**File:** `~/.claude/overseer/auto-bundler.py` (NEW)

```python
class AutoBundler:
    """
    Automatically bundles new skills/tools.
    Runs on: skill install, repo clone, new tool discovery
    """
    
    def on_new_skill(self, skill_name: str, skill_path: str):
        # 1. Read skill description + keywords
        # 2. Match to overseer category
        # 3. Find existing bundle that covers category
        # 4. Add skill to bundle registry
        # 5. Rebuild overseer index
        # Returns: bundle_name, added=True
        
    def on_new_repo(self, repo_url: str, tool_name: str):
        # E.g., when user says "install blader/humanizer"
        # 1. Clone repo
        # 2. Extract purpose from README
        # 3. Auto-categorize (humanizer → language + localization)
        # 4. Create/update bundle entry
        # 5. Add wrapper skill
        # Returns: bundle created/updated
        
    def on_future_items(self):
        # Hooks into skill installer, git clone, npm install
        # Automatically bundles everything as it arrives
        pass
```

---

## COMPONENT 3: LAZY-LOADING MECHANISM

**Only active bundle loaded. Others at 0 token cost.**

```
System state:
  ├── 22 bundle definitions (disk, ~2k tokens if all loaded)
  ├── Active bundle: BUNDLE-F-video (loaded, ~5 tokens)
  └── Inactive bundles: A-E, G-P, Z1-Z7 (library, 0 tokens)

Task: "Clip this video"
  → Smart selector: "BUNDLE-F-video best match"
  → Overseer: "Load BUNDLE-F"
  → Result: +5 tokens (BUNDLE-F only)
  
Task: "Build a Node API" (next task)
  → Smart selector: "BUNDLE-A-backend best match"
  → Overseer: "Unload BUNDLE-F" (save context)
  → Overseer: "Load BUNDLE-A"
  → Result: +5 tokens (BUNDLE-A only)
```

**Token math:**
- Without bundling: all skills loaded = ~50-80 tokens overhead
- With lazy bundles: 1 bundle loaded = ~5 tokens
- **Savings: -90% context overhead**

---

## COMPONENT 4: SKILL-ROUTER ↔ OVERSEER CONNECTION

**File:** `~/.claude/skills/skill-router/SKILL.md` (UPDATED)

```
Before (old):
  skill-router → recommends 1-2 skills → user invokes

After (new, connected):
  skill-router → classifies task
    ↓
  queries Overseer Smart Selector
    ↓
  gets best bundle + primary skill
    ↓
  Overseer lazy-loads bundle
    ↓
  Returns skill for immediate use
    ↓
  (other skills in bundle ready if user needs them)
```

**Benefits:**
- No "skill not found" — Overseer finds it + bundles it
- Auto-selection — No user decision needed
- Lazy loading — Only needed bundle active
- Future-proof — Auto-bundles new skills

---

## COMPONENT 5: OMNIROUTE INTEGRATION

**All LLM calls route through OmniRoute for compression**

```
Skill execution
  ↓
Any LLM call (Claude API)
  ↓
Intercepted by OmniRoute
  ↓
RTK + Caveman compression (65% reduction)
  ↓
Provider selection (Claude primary, fallback chain)
  ↓
Result returned to skill
  ↓
Transparent to skill code
```

**Configuration:** `~/.claude/overseer/omniroute-config.json`
```json
{
  "compression": {"rtk": true, "caveman": true, "target": "65%"},
  "providers": ["claude-opus-5", "claude-sonnet-5", "gemini-2.0"],
  "cache": {"enabled": true, "ttl": 3600}
}
```

---

## COMPLETE DATA FLOW

```
┌─────────────────────────────────────────────────────────────────┐
│ USER TASK: "Create 5 TikTok clips from this 20-min video"      │
└─────────────────────────────────────────────────────────────────┘
                          ↓
              ┌──────────────────────┐
              │  skill-router        │ (classify)
              │  Domain: video/media │
              │  Action: build       │
              │  Complexity: std     │
              └──────────────────────┘
                          ↓
        ┌─────────────────────────────────────┐
        │ Overseer Smart Selector             │
        │ Input: domain=video, keywords=clip  │
        │ Query: search("clip" + "video")     │
        │ Result: BUNDLE-Z1-clipping-factory  │
        │ Score: 98% match                    │
        └─────────────────────────────────────┘
                          ↓
        ┌─────────────────────────────────────┐
        │ Overseer Lazy Loader                │
        │ Load: BUNDLE-Z1 only (~5 tok)       │
        │ Skills available:                   │
        │  • claude-real-video (primary)      │
        │  • ai-clipping                      │
        │  • youtube-clipper                  │
        │  • video-editing                    │
        │  • video-translate (optional)       │
        └─────────────────────────────────────┘
                          ↓
        ┌─────────────────────────────────────┐
        │ Skill Chain Execution               │
        │ 1. claude-real-video (extract)      │
        │ 2. ai-clipping (detect scenes)      │
        │ 3. youtube-clipper (split)          │
        │ 4. video-editing (caption)          │
        └─────────────────────────────────────┘
                          ↓
        ┌─────────────────────────────────────┐
        │ OmniRoute Compression               │
        │ All LLM calls: compress 65%         │
        │ Total context: 45-50k (vs 150k)    │
        └─────────────────────────────────────┘
                          ↓
        ┌─────────────────────────────────────┐
        │ Result: 5 TikTok-ready clips        │
        │ + Performance metrics logged        │
        └─────────────────────────────────────┘
```

---

## FILE STRUCTURE (AFTER INTEGRATION)

```
~/.claude/
  ├── overseer/
  │   ├── smart-selector.py (NEW — intelligent bundle selection)
  │   ├── auto-bundler.py (NEW — auto-bundle new skills)
  │   ├── BUNDLE-REGISTRY.tsv (bundles index)
  │   ├── omniroute-config.json (compression config)
  │   ├── index.tsv (skills index)
  │   └── search.py (library search)
  │
  ├── skills/
  │   ├── skill-router/ (UPDATED — integrated with Overseer)
  │   ├── MASTER-BUNDLES-ROUTING.md (bundle definitions)
  │   ├── UNIFIED-SYSTEM-ARCHITECTURE.md (this file)
  │   ├── BUNDLE-A-backend/ (sample)
  │   ├── BUNDLE-B-frontend/ (sample)
  │   └── ... (15 general + 7 specialized bundles)
  │
  └── projects/.../
      ├── EXECUTION-COMPLETE-2026-08-10.md (status)
      └── memory/
          └── project_skill_bundle_system_2026.md (tracked)
```

---

## INTEGRATION CHECKLIST

- [x] Overseer indexes all 3,247 skills + 22 bundles
- [x] Skill-router classifies tasks
- [x] Smart selector picks best bundle (not user)
- [x] Lazy-loading only active bundle (not all)
- [x] OmniRoute compresses all LLM calls
- [ ] Auto-bundler active (watches for new skills)
- [ ] Future items auto-bundle on arrival
- [ ] System learning (tracks bundle performance)

---

## USING THE UNIFIED SYSTEM

### For users:
```
Just describe task. System auto-selects best bundle + skills.
"Create a video ad" → System picks BUNDLE-F-video
"Build a Node API" → System picks BUNDLE-A-backend
```

### For new tools/skills:
```
Add to library → Auto-bundler finds best bundle
Or: Manually specify bundle in skill metadata
→ System auto-creates entry + updates index
```

### For performance:
```
Monitor: token usage (target <50k/session)
Debug: which bundle was selected
Learn: performance metrics per bundle
```

---

## TOKEN EFFICIENCY MATH (FINAL)

| Component | Cost | Savings |
|-----------|------|---------|
| Lazy-loaded bundle | ~5 tok | -90% vs all skills |
| OmniRoute compression | -65% | (applied to all LLM calls) |
| Smart selection (cached) | <1ms | (no search overhead) |
| Skill chaining | ~0 tok | (no agent overhead) |
| **Total for task** | **~50k** | **-67% vs 150k baseline** |

---

## NEXT: AUTO-BUNDLER ACTIVATION

Once this architecture verified, activate:
1. Hook into skill installer (npx skills add)
2. Hook into git clone (new repos)
3. Hook into pip install (new libraries)
4. Auto-categorize + bundle
5. Update overseer index in real-time

Result: **Everything auto-bundles as it arrives. No manual work.**
