#!/usr/bin/env python3
"""
Overseer Smart Selector: Intelligent bundle selection + lazy loading
Connects: skill-router → bundles → lazy-loader → OmniRoute
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

class OverseerSmartSelector:
    def __init__(self):
        self.bundle_registry = Path.home() / ".claude/overseer/BUNDLE-REGISTRY.tsv"
        self.bundles = self._load_bundles()
        self.active_bundle = None

    def _load_bundles(self) -> Dict[str, dict]:
        """Load bundle registry into memory (0 cost, small file)"""
        bundles = {}
        if self.bundle_registry.exists():
            with open(self.bundle_registry) as f:
                for line in f:
                    if line.startswith("bundle"):
                        parts = line.strip().split("\t")
                        if len(parts) >= 6:
                            name = parts[2]
                            category = parts[3]
                            desc = parts[4]
                            bundle_type = parts[5]
                            bundles[name] = {
                                "type": bundle_type,
                                "category": category,
                                "desc": desc,
                            }
        return bundles

    def select_bundle(self, user_input: str, domain: str = None) -> Tuple[str, List[str]]:
        """
        Smart bundle selection based on:
        1. Keyword matching (highest confidence)
        2. Domain matching (fallback)
        3. Generality (last resort)

        Returns: (bundle_name, [primary_skill, sub_skills...])
        """

        # Extract keywords from input
        keywords = set(re.findall(r'\b\w{3,}\b', user_input.lower()))

        # Keyword → bundle mappings (precomputed for speed)
        keyword_bundles = {
            # BUNDLE A: Backend
            ('node', 'api', 'backend'): ('BUNDLE-A-backend-api', ['nodejs-best-practices']),
            ('python', 'fastapi', 'django'): ('BUNDLE-A-backend-api', ['fastapi-patterns']),
            ('golang', 'rust', 'java'): ('BUNDLE-A-backend-api', ['backend-patterns']),

            # BUNDLE B: Frontend
            ('react', 'component', 'ui'): ('BUNDLE-B-frontend-ui', ['react-best-practices']),
            ('nextjs', 'next.js'): ('BUNDLE-B-frontend-ui', ['nextjs-best-practices']),
            ('design', 'figma'): ('BUNDLE-B-frontend-ui', ['design-system']),

            # BUNDLE D: AI/ML
            ('ai', 'llm', 'agent'): ('BUNDLE-D-ai-ml', ['llm-app-patterns']),
            ('rag', 'embedding', 'prompt'): ('BUNDLE-D-ai-ml', ['rag-implementation']),

            # BUNDLE F: Video
            ('video', 'clip', 'render'): ('BUNDLE-F-video-media', ['video-editing']),
            ('animation', 'lottie', '3d'): ('BUNDLE-F-video-media', ['motion-ui']),

            # BUNDLE L: Automation
            ('automation', 'workflow', 'n8n'): ('BUNDLE-L-automation', ['n8n-workflow-patterns']),
            ('zapier', 'integration'): ('BUNDLE-L-automation', ['zapier-make-patterns']),

            # BUNDLE P: Agents
            ('agent', 'orchestrate', 'multi-agent'): ('BUNDLE-P-agents', ['multi-agent-task-orchestrator']),
            ('router', 'skill-router'): ('BUNDLE-P-agents', ['skill-router']),

            # Specialized bundles
            ('clip', 'clipping', 'factory'): ('BUNDLE-Z1-clipping-factory', ['ai-clipping']),
            ('arabic', 'localize', 'rtl'): ('BUNDLE-Z3-arabic-localization', ['video-translate']),
            ('ugc', 'generated'): ('BUNDLE-Z2-ai-ugc', ['ugc-ads-workflow']),
        }

        # Score bundles by keyword overlap
        scores = {}
        for key_set, (bundle, skills) in keyword_bundles.items():
            overlap = len(keywords & set(key_set))
            if overlap > 0:
                scores[bundle] = (overlap, skills)

        # Return highest scoring bundle
        if scores:
            best_bundle = max(scores.items(), key=lambda x: x[1][0])
            return best_bundle[0], best_bundle[1][1]

        # Fallback by domain
        if domain == "backend":
            return "BUNDLE-A-backend-api", ["backend-patterns"]
        elif domain == "frontend":
            return "BUNDLE-B-frontend-ui", ["ui-design"]
        elif domain == "video":
            return "BUNDLE-F-video-media", ["video-editing"]

        # Last resort: generic bundle
        return "BUNDLE-O-docs", ["documentation"]

    def lazy_load(self, bundle_name: str) -> bool:
        """
        Load selected bundle into context.
        Other bundles stay in library (0 token cost).
        """
        if bundle_name not in self.bundles:
            return False
        self.active_bundle = bundle_name
        return True

    def auto_bundle_new_skill(self, skill_name: str, skill_path: Path) -> str:
        """
        Auto-categorize new skill and add to bundle.
        Called when: npx skills add, git clone, pip install
        """
        # Read skill description
        skill_md = skill_path / "SKILL.md"
        if not skill_md.exists():
            return None

        with open(skill_md) as f:
            content = f.read().lower()

        # Match to bundle by keywords in the indexed description.
        for bundle_name, bundle_info in self.bundles.items():
            desc = bundle_info.get("desc", "").lower().split()
            if desc and any(word in content for word in desc[:8]):
                # Add to bundle registry
                self._add_to_bundle(skill_name, bundle_name)
                return bundle_name

        # Fallback: add to BUNDLE-O-docs
        self._add_to_bundle(skill_name, "BUNDLE-O-docs")
        return "BUNDLE-O-docs"

    def _add_to_bundle(self, skill_name: str, bundle_name: str):
        """Add skill to bundle registry (internal)"""
        if bundle_name not in self.bundles:
            raise ValueError(f"Unknown bundle: {bundle_name}")
        rows = self.bundle_registry.read_text(encoding="utf-8").splitlines()
        if any(f"\t{skill_name}\t" in row for row in rows):
            return
        with self.bundle_registry.open("a", encoding="utf-8") as registry:
            registry.write(f"skill\tskills\t{skill_name}\t{bundle_name}\tauto\tmember\n")


# Singleton instance
_selector = None

def get_selector() -> OverseerSmartSelector:
    global _selector
    if not _selector:
        _selector = OverseerSmartSelector()
    return _selector


if __name__ == "__main__":
    selector = get_selector()

    # Example usage
    task = "Create 5 TikTok clips from a video"
    bundle, skills = selector.select_bundle(task)
    print(f"Task: {task}")
    print(f"Bundle: {bundle}")
    print(f"Skills: {skills}")
    # Output: Bundle: BUNDLE-F-video-media, Skills: ['video-editing', ...]
