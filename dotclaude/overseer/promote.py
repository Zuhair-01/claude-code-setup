#!/usr/bin/env python3
"""Move skills/agents between the library and the live set.
Usage:
  promote.py <name> [<name>...]        # library -> live (permanently in context)
  promote.py --demote <name> [...]     # live -> library (reclaim context)
Nothing is ever deleted; this only moves directories/files.
"""
import os, sys, shutil
HOME = os.path.expanduser("~/.claude")
args = sys.argv[1:]
demote = "--demote" in args
if demote: args.remove("--demote")
if not args: sys.exit(__doc__)

pairs = [("skills-library", "skills", "dir"), ("agents-library", "agents", "file")]
moved = []
for name in args:
    done = False
    for lib, live, kind in pairs:
        src_root, dst_root = (live, lib) if demote else (lib, live)
        src = os.path.join(HOME, src_root, name if kind == "dir" else name + ".md")
        dst = os.path.join(HOME, dst_root, name if kind == "dir" else name + ".md")
        if os.path.exists(src):
            if os.path.exists(dst):
                print(f"SKIP {name}: already exists at {dst}"); done = True; break
            os.makedirs(os.path.dirname(dst) or dst, exist_ok=True)
            shutil.move(src, dst)
            print(f"{'DEMOTED' if demote else 'PROMOTED'} {kind:<4} {name}  ->  {dst_root}/")
            moved.append(name); done = True; break
    if not done:
        print(f"NOT FOUND: {name} (searched {'live' if demote else 'library'} skills+agents)")
if moved:
    os.system(f'python3 "{os.path.join(HOME, "overseer", "build_index.py")}" >' + os.devnull)
    print(f"\nindex rebuilt. {len(moved)} moved. Restart session for context listing to change.")
