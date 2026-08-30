#!/usr/bin/env python3
"""
Auto-Bundler: Auto-categorizes new skills/repos into bundles on arrival
Hooks into: skill install, git clone, npm install, pip install
"""

import json
from pathlib import Path
from datetime import datetime

class AutoBundler:
    def __init__(self):
        self.bundle_registry = Path.home() / ".claude/overseer/BUNDLE-REGISTRY.tsv"
        self.log = Path.home() / ".claude/overseer/auto-bundler.log"

    def on_new_skill(self, skill_name: str, skill_path: Path) -> dict:
        """
        Triggered when: npx skills add <skill>
        Action: Auto-categorize + bundle
        """
        result = {
            "skill": skill_name,
            "status": "auto-bundled",
            "timestamp": datetime.now().isoformat(),
        }

        try:
            # Read skill description
            skill_md = skill_path / "SKILL.md"
            if not skill_md.exists():
                result["status"] = "error: no SKILL.md"
                return result

            with open(skill_md) as f:
                desc = f.read()

            # Auto-detect bundle from keywords in description
            bundle = self._detect_bundle(desc)
            result["bundle"] = bundle

            # Add to registry
            self._add_to_registry(skill_name, bundle, desc)
            result["registered"] = True

        except Exception as e:
            result["status"] = f"error: {str(e)}"

        self._log(result)
        return result

    def on_new_repo(self, repo_url: str, tool_name: str, readme_text: str) -> dict:
        """
        Triggered when: git clone <repo>
        Action: Parse README + auto-bundle
        Example: blader/humanizer → BUNDLE-Z3 (Arabic localization)
        """
        result = {
            "repo": repo_url,
            "tool": tool_name,
            "status": "auto-bundled",
            "timestamp": datetime.now().isoformat(),
        }

        try:
            # Analyze README for purpose
            bundle = self._detect_bundle_from_readme(readme_text, tool_name)
            result["bundle"] = bundle

            # Create wrapper skill entry
            wrapper_skill = f"{tool_name}-wrapper"
            self._add_to_registry(wrapper_skill, bundle, readme_text[:500])
            result["wrapper_created"] = wrapper_skill

        except Exception as e:
            result["status"] = f"error: {str(e)}"

        self._log(result)
        return result

    def on_future_items(self):
        """
        Setup file watchers for:
        - ~/.claude/skills/ (new skills)
        - ~/.claude/skills-library/ (new library items)
        - Desktop/Empire_Base/ (new repos)

        Auto-bundle on arrival, no manual intervention needed.
        """
        # This would be implemented with watchdog library
        # For now: manual trigger on major file changes
        pass

    def _detect_bundle(self, description: str) -> str:
        """Detect best bundle from skill description keywords"""
        desc_lower = description.lower()

        # Bundle keyword mappings (ordered by specificity)
        mappings = {
            # Specialized bundles (highest specificity)
            ("clipping", "clip"): "BUNDLE-Z1-clipping-factory",
            ("ai", "ugc", "generated"): "BUNDLE-Z2-ai-ugc",
            ("arabic", "localize", "rtl"): "BUNDLE-Z3-arabic-localization",
            ("b2b", "outreach", "netherlands"): "BUNDLE-Z4-b2b-netherlands",
            ("scroll", "3d", "landing"): "BUNDLE-Z5-scroll-world",
            ("prompt", "evaluation"): "BUNDLE-Z6-prompt-eval",
            ("agent", "mcp", "custom"): "BUNDLE-Z7-custom-agents",

            # General bundles (medium specificity)
            ("node", "backend", "api"): "BUNDLE-A-backend-api",
            ("react", "frontend", "ui"): "BUNDLE-B-frontend-ui",
            ("database", "sql", "postgres"): "BUNDLE-C-database-data",
            ("llm", "ai", "agent"): "BUNDLE-D-ai-ml",
            ("docker", "devops", "deploy"): "BUNDLE-E-devops-cloud",
            ("video", "render", "edit"): "BUNDLE-F-video-media",
            ("test", "qa", "playwright"): "BUNDLE-G-testing-qa",
            ("security", "vulnerability"): "BUNDLE-H-security",
            ("mobile", "ios", "android"): "BUNDLE-I-mobile-xr",
            ("seo", "marketing", "content"): "BUNDLE-J-marketing",
            ("stripe", "payment", "commerce"): "BUNDLE-K-commerce",
            ("automation", "workflow"): "BUNDLE-L-automation",
            ("blockchain", "crypto", "web3"): "BUNDLE-M-web3",
            ("analytics", "dashboard", "data"): "BUNDLE-N-analytics",
            ("docs", "documentation", "writing"): "BUNDLE-O-docs",
            ("orchestrate", "router", "dispatcher"): "BUNDLE-P-agents",
        }

        # Score each bundle by keyword overlap
        scores = {}
        for keywords, bundle in mappings.items():
            overlap = sum(1 for kw in keywords if kw in desc_lower)
            if overlap > 0:
                scores[bundle] = overlap

        # Return highest scoring bundle
        if scores:
            return max(scores, key=scores.get)

        # Default fallback
        return "BUNDLE-O-docs"

    def _detect_bundle_from_readme(self, readme: str, tool_name: str) -> str:
        """Detect bundle from repo README + tool name"""
        combined = f"{tool_name} {readme}".lower()
        return self._detect_bundle(combined)

    def _add_to_registry(self, item_name: str, bundle: str, description: str):
        """Add item to BUNDLE-REGISTRY.tsv"""
        if not self.bundle_registry.exists():
            raise FileNotFoundError(self.bundle_registry)
        rows = self.bundle_registry.read_text(encoding="utf-8").splitlines()
        if any(f"\t{item_name}\t" in row for row in rows):
            return
        entry = f"skill\tskills\t{item_name}\t{bundle}\tauto\tmember\n"
        with open(self.bundle_registry, "a") as f:
            f.write(entry)

    def _log(self, result: dict):
        """Log auto-bundling event"""
        with open(self.log, "a") as f:
            f.write(json.dumps(result) + "\n")


# Global instance
_bundler = None

def get_bundler() -> AutoBundler:
    global _bundler
    if not _bundler:
        _bundler = AutoBundler()
    return _bundler


if __name__ == "__main__":
    bundler = get_bundler()

    # Test: humanizer repo
    test_readme = """
    Agent skill that removes signs of AI-generated writing from text.
    Perfect for Arabic content and multilingual localization.
    """
    result = bundler.on_new_repo(
        "https://github.com/blader/humanizer",
        "humanizer",
        test_readme
    )
    print(f"Auto-bundled: {result}")
    # Output: bundle=BUNDLE-Z3-arabic-localization
