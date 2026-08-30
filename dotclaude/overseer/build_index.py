#!/usr/bin/env python3
"""Rebuild the OVERSEER library index: kind, location, category, name, description.
Char-safe truncation (never cuts a multibyte char). Run after moving/adding skills or agents.
"""
import os, re, sys
HOME = os.path.expanduser("~/.claude")
OUT = os.path.join(HOME, "overseer", "index.tsv")
DESC = re.compile(r'^description:\s*(.*)$', re.I | re.M)
NAME = re.compile(r'^name:\s*(.*)$', re.I | re.M)

# --- category rules: first match wins. (regex over "name desc")
RULES = [
    ("saas-connector", r'-automation$'),
    ("cloud",          r'^(azure|aws|gcp)-|cloudflare|kubernetes|terraform|docker|helm|serverless|vercel|netlify|k8s'),
    ("language",       r'^(python|typescript|javascript|golang|go|rust|java|csharp|cpp|c|php|ruby|swift|kotlin|dart|scala|perl|elixir|haskell|bash|sql|lua)-?(pro|patterns|testing|coding-standards|expert)?$|^(posix-shell|modern-javascript)'),
    ("web-frontend",   r'react|next|nuxt|vue|svelte|angular|tailwind|css|frontend|ui-|design-system|shadcn|threejs|motion|gsap|animation|webgl|artifact'),
    ("backend-api",    r'fastapi|django|laravel|spring|rails|express|nestjs|backend|api-design|graphql|grpc|rest|microservice|hexagonal|ddd|cqrs|event-sourc'),
    ("database",       r'postgres|mysql|redis|mongo|sqlite|database|sql-|prisma|drizzle|supabase|neon|clickhouse|nosql|vector|pgvector|migration'),
    ("mobile",         r'ios|android|flutter|react-native|swiftui|expo|mobile|app-store|harmonyos'),
    ("ai-ml",          r'llm|rag|embedding|langchain|langgraph|prompt|agent|openai|anthropic|claude|gemini|huggingface|pytorch|tensorflow|ml-|mlops|fine-tun|eval|transformers|diffusion'),
    ("media-video",    r'video|clip|ffmpeg|youtube|reel|shorts|seedance|veo|sora|runway|kling|remotion|editing|subtitle|thumbnail'),
    ("media-image",    r'image|photo|nano-banana|midjourney|flux|imagen|logo|avatar|faceswap|upscale|poster|canvas|figma|design'),
    ("media-audio",    r'audio|voice|speech|tts|music|elevenlabs|podcast|whisper|transcri|sound'),
    ("security",       r'security|pentest|vulnerab|exploit|owasp|threat|malware|forensic|crypto-?graph|auth|oauth|secrets|compliance|hipaa|gdpr|pci|soc2|reverse-engineer|injection'),
    ("testing-qa",     r'test|tdd|qa|playwright|cypress|selenium|jest|pytest|e2e|benchmark|fuzz|lint'),
    ("devops-ci",      r'ci|cd|github-action|gitlab|jenkins|pipeline|deploy|monitor|observab|grafana|prometheus|incident|sre|slo|logging|tracing'),
    ("data-eng",       r'etl|airflow|dbt|spark|pandas|polars|dask|warehouse|lakehouse|data-pipeline|scraper|scraping|crawl'),
    ("science",        r'bio|chem|genom|molecul|protein|astro|physic|scanpy|rdkit|qiskit|quantum|clinical|medical|health|pubmed|scientific|statistic'),
    ("marketing-seo",  r'seo|aeo|geo-|marketing|content|copywrit|blog|social|instagram|tiktok|linkedin|twitter|reddit|xiaohongshu|douyin|weibo|zhihu|bilibili|wechat|ads|campaign|email-|newsletter|growth|viral|brand'),
    ("sales-crm",      r'sales|crm|lead|outreach|prospect|pipeline|deal|proposal|hubspot|salesforce|pipedrive'),
    ("finance",        r'finance|financial|accounting|invoic|billing|payment|stripe|paypal|tax|budget|trading|investment|quant|bookkeep|payroll'),
    ("commerce",       r'shopify|woocommerce|ecommerce|e-commerce|product-listing|amazon|store|cart|checkout|retail|inventory'),
    ("web3",           r'blockchain|solidity|smart-contract|nft|defi|ethereum|bitcoin|wallet|token|web3|evm|lightning'),
    ("docs-office",    r'pptx|docx|xlsx|pdf|excel|word|powerpoint|spreadsheet|document|slide|deck|report|notion|obsidian|wiki|readme|changelog'),
    ("productivity",   r'workflow|automation|n8n|zapier|make|calendar|meeting|task|todo|jira|linear|asana|trello|slack|discord|telegram|whatsapp|gmail|email-ops'),
    ("game-xr",        r'unity|unreal|godot|roblox|game|blender|shader|vr|ar|xr|spatial|visionos|3d'),
    ("meta-agent",     r'skill|agent|orchestrat|router|council|memory|context|token|loop|harness|mcp|subagent|hook'),
    ("business-ops",   r'hr|recruit|onboard|legal|contract|customer|support|project-manage|okr|strategy|consult|research|market-research|competitor'),
]
def categorize(name, desc):
    n = name.lower()
    base = n.rsplit("/", 1)[-1]
    if base.endswith("-automation"):
        return "saas-connector"
    blob = n + " " + desc.lower()
    for cat, pat in RULES:
        if cat == "saas-connector":
            continue
        if re.search(pat, base) or re.search(pat, blob):
            return cat
    return "other"

def clean(s, n=200):
    s = re.sub(r'\s+', ' ', s).strip().strip('"').strip("'")
    s = "".join(ch for ch in s if ch == ' ' or ch.isprintable())
    return s[:n]                      # CHAR-based: never splits a multibyte char

def meta(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            head = fh.read(6000)
    except OSError:
        return "", ""
    d = DESC.search(head); n = NAME.search(head)
    return (clean(n.group(1)) if n else ""), (clean(d.group(1)) if d else "")

rows = []
SKIP_MIRROR_DIRS = {".agents", ".cursor", ".kiro", "docs"}
PROMOTED_NAMES = {
    "brandkit",
    "brutalist-skill",
    "gpt-tasteskill",
    "image-to-code-skill",
    "imagegen-frontend-mobile",
    "imagegen-frontend-web",
    "minimalist-skill",
    "output-skill",
    "soft-skill",
    "stitch-skill",
    "taste-skill",
    "taste-skill-v1",
}

def add_skill(loc, key, path):
    _, d = meta(path)
    rows.append(("skill", loc, categorize(key, d), key, d))

for loc, base in (("library", "skills-library"), ("live", "skills")):
    root = os.path.join(HOME, base)
    if not os.path.isdir(root): continue
    for name in sorted(os.listdir(root)):
        if loc == "library" and name in PROMOTED_NAMES:
            continue
        d = os.path.join(root, name)
        if not os.path.isdir(d): continue
        top = os.path.join(d, "SKILL.md")
        if os.path.isfile(top):
            add_skill(loc, name, top)
        else:
            for dp, dns, fns in os.walk(d):
                dns[:] = [child for child in dns if child not in SKIP_MIRROR_DIRS]
                if dp.count(os.sep) - root.count(os.sep) > 4:
                    dns[:] = []; continue
                if "SKILL.md" in fns and dp != d:
                    rel = os.path.relpath(dp, root).replace("\\", "/")
                    add_skill(loc, rel, os.path.join(dp, "SKILL.md"))

for loc, base in (("library", "agents-library"), ("live", "agents")):
    root = os.path.join(HOME, base)
    if not os.path.isdir(root): continue
    for fn in sorted(os.listdir(root)):
        if not fn.endswith(".md"): continue
        key = fn[:-3]
        _, d = meta(os.path.join(root, fn))
        rows.append(("agent", loc, categorize(key, d), key, d))

rows.sort()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    for r in rows:
        fh.write("\t".join(r) + "\n")

raw = open(OUT, "rb").read()
try:
    raw.decode("utf-8"); ok = "valid utf-8 OK"
except UnicodeDecodeError as e:
    ok = f"INVALID: {e}"
def c(k,l): return sum(1 for r in rows if r[0]==k and r[1]==l)
print(f"index: {OUT}  ({len(raw)/1024:.0f} KB, {ok})")
print(f"  skills  library={c('skill','library'):>5}  live={c('skill','live')}")
print(f"  agents  library={c('agent','library'):>5}  live={c('agent','live')}")
print(f"  total rows: {len(rows)}")
from collections import Counter
print("\ncategories:")
for cat, n in Counter(r[2] for r in rows).most_common():
    print(f"  {n:>5}  {cat}")
