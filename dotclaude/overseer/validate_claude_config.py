#!/usr/bin/env python3
"""Validate the local Claude Code capability registry and configuration.

This is intentionally dependency-free and read-only. It reports drift without
deleting or rewriting user state, caches, credentials, or marketplace files.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path.home() / ".claude"


def load_json(path: Path, errors: list[str]) -> object | None:
    def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key: {key}")
            result[key] = value
        return result

    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_keys,
        )
    except FileNotFoundError:
        errors.append(f"missing JSON: {path}")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid JSON {path}: {exc}")
    return None


def has_frontmatter(path: Path) -> bool:
    try:
        return path.read_text(encoding="utf-8", errors="replace").startswith("---")
    except OSError:
        return False


def capability_counts() -> dict[str, int]:
    result: dict[str, int] = {}
    for name, marker in (
        ("live_skills", ROOT / "skills"),
        ("library_skills", ROOT / "skills-library"),
        ("live_agents", ROOT / "agents"),
        ("library_agents", ROOT / "agents-library"),
        ("commands", ROOT / "commands"),
    ):
        if name.endswith("skills"):
            result[name] = sum(1 for path in marker.rglob("SKILL.md")) if marker.exists() else 0
        elif name.endswith("agents"):
            result[name] = sum(1 for path in marker.rglob("*.md")) if marker.exists() else 0
        else:
            result[name] = sum(1 for path in marker.rglob("*.md")) if marker.exists() else 0
    return result


def validate_capabilities(errors: list[str], warnings: list[str]) -> dict[str, int]:
    counts = capability_counts()
    for directory, pattern in (
        (ROOT / "skills", "SKILL.md"),
        (ROOT / "agents", "*.md"),
        (ROOT / "commands", "*.md"),
    ):
        if not directory.exists():
            errors.append(f"missing capability directory: {directory}")
            continue
        for path in directory.rglob(pattern):
            if path.name == "nul":
                warnings.append(f"artifact in capability tree: {path}")
            if not has_frontmatter(path):
                warnings.append(f"missing frontmatter: {path}")

    duplicate_names = Counter(
        path.parent.name
        for path in (ROOT / "skills").rglob("SKILL.md")
        if path.parent.parent == ROOT / "skills"
    )
    for name, count in duplicate_names.items():
        if count > 1:
            warnings.append(f"duplicate live skill name: {name} ({count})")
    return counts


def validate_registry(errors: list[str], warnings: list[str]) -> dict[str, int]:
    registry = ROOT / "overseer" / "BUNDLE-REGISTRY.tsv"
    if not registry.exists():
        errors.append(f"missing bundle registry: {registry}")
        return {}

    lines = registry.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines or lines[0].split("\t") != [
        "kind",
        "location",
        "name",
        "category",
        "description",
        "bundle_type",
    ]:
        errors.append("bundle registry header does not match the canonical schema")

    bundles: set[str] = set()
    members = 0
    for line_number, line in enumerate(lines[1:], start=2):
        fields = line.split("\t")
        if len(fields) != 6:
            errors.append(f"registry line {line_number} has {len(fields)} fields, expected 6")
            continue
        kind, location, name, category, description, bundle_type = fields
        if kind == "bundle":
            if name in bundles:
                errors.append(f"duplicate bundle: {name}")
            bundles.add(name)
            if bundle_type not in {"master", "specialized"}:
                warnings.append(f"unknown bundle type on line {line_number}: {bundle_type}")
        elif kind == "skill":
            members += 1
            if bundle_type != "member":
                warnings.append(f"non-member skill row on line {line_number}")
        else:
            warnings.append(f"unknown registry kind on line {line_number}: {kind}")
        if not location or not category or not description:
            warnings.append(f"incomplete registry row on line {line_number}")
    return {"bundles": len(bundles), "members": members}


def validate_plugins(errors: list[str], warnings: list[str]) -> int:
    path = ROOT / "plugins" / "installed_plugins.json"
    data = load_json(path, errors)
    if not isinstance(data, dict):
        return 0
    plugins = data.get("plugins", {})
    installed = 0
    if not isinstance(plugins, dict):
        errors.append("installed_plugins.json: plugins must be an object")
        return 0
    for name, entries in plugins.items():
        if not isinstance(entries, list):
            errors.append(f"plugin {name}: entries must be a list")
            continue
        for entry in entries:
            installed += 1
            install_path = Path(entry.get("installPath", "")) if isinstance(entry, dict) else Path()
            if not install_path.exists():
                errors.append(f"plugin {name}: missing install path {install_path}")
    return installed


def validate_index(errors: list[str], warnings: list[str]) -> dict[str, int]:
    index = ROOT / "overseer" / "index.tsv"
    if not index.exists():
        errors.append(f"missing Overseer index: {index}")
        return {}
    counts: Counter[tuple[str, str]] = Counter()
    names: Counter[tuple[str, str]] = Counter()
    for line_number, line in enumerate(index.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        fields = line.split("\t")
        if len(fields) != 5:
            errors.append(f"index line {line_number} has {len(fields)} fields, expected 5")
            continue
        kind, location, category, name, description = fields
        if kind not in {"skill", "agent"} or location not in {"live", "library"}:
            errors.append(f"invalid index identity on line {line_number}")
            continue
        root_name = {
            ("skill", "live"): "skills",
            ("skill", "library"): "skills-library",
            ("agent", "live"): "agents",
            ("agent", "library"): "agents-library",
        }[(kind, location)]
        suffix = "SKILL.md" if kind == "skill" else f"{name}.md"
        path = ROOT / root_name / suffix if kind == "agent" else ROOT / root_name / name / "SKILL.md"
        if not path.exists():
            errors.append(f"index line {line_number} points to missing path: {path}")
        counts[(kind, location)] += 1
        names[(kind, name)] += 1
    for (kind, name), count in names.items():
        if count > 1:
            warnings.append(f"duplicate indexed {kind}: {name} ({count})")
    return {f"{kind}_{location}": count for (kind, location), count in counts.items()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    for filename in ("settings.json", "settings.local.json"):
        load_json(ROOT / filename, errors)
    counts = validate_capabilities(errors, warnings)
    registry = validate_registry(errors, warnings)
    plugins = validate_plugins(errors, warnings)
    index = validate_index(errors, warnings)
    report = {
        "root": str(ROOT),
        "counts": counts,
        "registry": registry,
        "installed_plugins": plugins,
        "index": index,
        "errors": errors,
        "warnings": warnings,
        "ok": not errors,
    }
    if args.as_json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Claude config: {'OK' if not errors else 'FAILED'}")
        print(f"Capabilities: {counts}")
        print(f"Registry: {registry}; installed plugins: {plugins}")
        for item in errors:
            print(f"ERROR: {item}")
        for item in warnings:
            print(f"WARN: {item}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
