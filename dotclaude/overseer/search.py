#!/usr/bin/env python3
"""OVERSEER library search -- find skills/agents that are NOT in context.

Usage:
  search.py <terms...>              search by keyword (ranked, rare terms win)
  search.py <terms> --cat <cat>     restrict to a category
  search.py --cat <cat> --list      list everything in a category
  search.py --cats                  show all categories + counts
Flags: --kind skill|agent   --all (include live)   -n N (default 12)
"""
import os, sys, re, math
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HOME = os.path.expanduser("~/.claude")
IDX = os.path.join(HOME, "overseer", "index.tsv")
if not os.path.isfile(IDX):
    sys.exit(f"index missing: {IDX}  (run: python3 ~/.claude/overseer/build_index.py)")

rows = []
with open(IDX, encoding="utf-8", errors="replace") as fh:
    for line in fh:
        p = line.rstrip("\n").split("\t")
        while len(p) < 5: p.append("")
        if len(p) == 5: rows.append(p)      # kind, loc, cat, name, desc

args = list(sys.argv[1:])
def take(flag):
    if flag in args:
        i = args.index(flag); v = args[i+1]; del args[i:i+2]; return v
    return None
kind = take("--kind"); cat = take("--cat")
limit = int(take("-n") or 12)
only_lib = True; do_list = False; show_cats = False
for f, var in (("--all", "only_lib"), ("--list", "do_list"), ("--cats", "show_cats")):
    if f in args:
        args.remove(f)
        if f == "--all": only_lib = False
        elif f == "--list": do_list = True
        else: show_cats = True

if show_cats:
    c = Counter(r[2] for r in rows if r[1] == "library")
    print(f"{'category':<18} library items")
    for k, v in c.most_common():
        print(f"  {k:<16} {v:>5}")
    print(f"\n  total library: {sum(c.values())}")
    print("\nlist one:  search.py --cat <category> --list -n 40")
    sys.exit()

pool = [r for r in rows if (not kind or r[0] == kind) and (not cat or r[2] == cat)]
if only_lib:
    pool = [r for r in pool if r[1] == "library"]

def show(r, s=None):
    k, loc, c, name, desc = r
    base = {"skill": ("skills-library", "skills"), "agent": ("agents-library", "agents")}[k]
    root = base[0] if loc == "library" else base[1]
    path = os.path.join(HOME, root, name, "SKILL.md") if k == "skill" else os.path.join(HOME, root, name + ".md")
    tag = f"[{s:>5.0f}] " if s is not None else "  "
    print(f"{tag}{k:<5} {c:<15} {name}\n        {desc[:150]}\n        -> {path}")

if do_list or not args:
    if not cat:
        sys.exit("give search terms, or --cat <category> --list, or --cats")
    for r in sorted(pool, key=lambda r: r[3])[:limit]:
        show(r)
    print(f"\n({len(pool)} in '{cat}', showing {min(limit, len(pool))})")
    sys.exit()

terms = [t.lower() for t in args if t.strip()]
df = {t: 0 for t in terms}
for _, _, _, name, desc in rows:
    blob = (name + " " + desc).lower()
    for t in terms:
        if t in blob: df[t] += 1
N = max(len(rows), 1)
idf = {t: math.log(N / (1 + df[t])) + 1.0 for t in terms}

def score(r):
    n, d = r[3].lower(), r[4].lower()
    s = 0.0; matched = 0
    for t in terms:
        w = idf[t]; hit = False
        if t == n: s += 100 * w; hit = True
        elif re.search(rf'(^|[-_/ ]){re.escape(t)}([-_/ ]|$)', n): s += 40 * w; hit = True
        elif t in n: s += 18 * w; hit = True
        if t in d: s += 6 * w; hit = True
        if hit: matched += 1
    if matched == len(terms): s *= 1.4
    return s

hits = sorted(((score(r), r) for r in pool), key=lambda x: (-x[0], x[1][3]))
shown = 0
for s, r in hits:
    if s <= 0: break
    show(r, s); shown += 1
    if shown >= limit: break
if not shown:
    print("no library matches" + (" (try --all to include live)" if only_lib else ""))
