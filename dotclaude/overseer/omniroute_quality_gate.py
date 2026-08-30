#!/usr/bin/env python3
"""
OmniRoute Quality Gate: Validates outputs from free-tier providers
Prevents low-quality results from fallback models
"""

import json
from typing import Dict, Tuple
from enum import Enum

class ModelTier(Enum):
    PREMIUM = "claude-opus-5"      # Primary (best quality, higher cost)
    STANDARD = "claude-sonnet-5"   # Fallback 1
    FREE = "gemini-2.0"            # Fallback 2 (free but variable quality)
    BUDGET = "gpt-4-turbo"         # Fallback 3
    LAST_RESORT = "claude-2"       # Fallback 4 (avoid if possible)

class QualityGate:
    """
    Quality assurance for free-tier model outputs.
    Rules: Use free tiers only when:
    1. Task complexity is LOW
    2. Output length is SHORT
    3. No domain-specific expertise required
    4. Output validation PASSES
    """

    def __init__(self):
        self.rules = {
            # Task complexity → allowed model tier
            "complex": [ModelTier.PREMIUM, ModelTier.STANDARD],          # AI coding, arch
            "standard": [ModelTier.PREMIUM, ModelTier.STANDARD, ModelTier.FREE],  # General
            "simple": [ModelTier.PREMIUM, ModelTier.STANDARD, ModelTier.FREE, ModelTier.BUDGET],  # FAQ

            # Domain → allowed tiers
            "security": [ModelTier.PREMIUM, ModelTier.STANDARD],         # No free tiers
            "medical": [ModelTier.PREMIUM, ModelTier.STANDARD],          # No free tiers
            "legal": [ModelTier.PREMIUM, ModelTier.STANDARD],            # No free tiers
            "financial": [ModelTier.PREMIUM, ModelTier.STANDARD, ModelTier.FREE],
            "technical": [ModelTier.PREMIUM, ModelTier.STANDARD],        # Code/arch
            "creative": [ModelTier.PREMIUM, ModelTier.STANDARD, ModelTier.FREE, ModelTier.BUDGET],
            "general": [ModelTier.PREMIUM, ModelTier.STANDARD, ModelTier.FREE],
        }

    def validate_provider_for_task(self, provider: str, task_complexity: str, domain: str) -> Tuple[bool, str]:
        """
        Check if provider is appropriate for this task.
        Returns: (is_valid, reason)
        """
        provider_tier = self._string_to_tier(provider)

        # Check against complexity rules
        allowed_by_complexity = self.rules.get(task_complexity, [ModelTier.PREMIUM, ModelTier.STANDARD])
        if provider_tier not in allowed_by_complexity:
            return False, f"Free tier '{provider}' not allowed for '{task_complexity}' complexity"

        # Check against domain rules
        allowed_by_domain = self.rules.get(domain, [ModelTier.PREMIUM, ModelTier.STANDARD, ModelTier.FREE])
        if provider_tier not in allowed_by_domain:
            return False, f"Free tier '{provider}' not allowed for '{domain}' domain"

        return True, "✓ Provider allowed"

    def validate_output(self, output: str, criteria: Dict) -> Tuple[bool, list]:
        """
        Validate output quality.
        Returns: (passes_all, [failures])
        """
        failures = []

        # Length check
        min_length = criteria.get("min_length", 10)
        max_length = criteria.get("max_length", 10000)
        if len(output) < min_length:
            failures.append(f"Output too short: {len(output)} chars (min {min_length})")
        if len(output) > max_length:
            failures.append(f"Output too long: {len(output)} chars (max {max_length})")

        # Content quality checks
        if criteria.get("no_placeholders", False):
            if "[" in output and "]" in output:
                failures.append("Contains [placeholder] markers (unfinished)")

        if criteria.get("requires_code", False):
            if not any(lang in output.lower() for lang in ["def ", "function", "class ", "const "]):
                failures.append("No code found (but required)")

        if criteria.get("requires_structure", False):
            if "\n" not in output:
                failures.append("No structure/newlines (should be formatted)")

        return len(failures) == 0, failures

    def get_recommended_provider(self, task_complexity: str, domain: str, cost_budget: str = "balanced") -> str:
        """
        Recommend provider based on task + budget.
        budget: "cheapest" | "balanced" | "best"
        """
        allowed = self.rules.get(task_complexity, [])
        domain_allowed = self.rules.get(domain, [])

        # Intersection: both rules must allow
        intersection = [t for t in allowed if t in domain_allowed]

        if not intersection:
            return ModelTier.PREMIUM.value  # Safest default

        if cost_budget == "cheapest":
            return intersection[-1].value  # Last (cheapest)
        elif cost_budget == "best":
            return intersection[0].value   # First (best quality)
        else:  # balanced
            # Return middle tier or first available
            return intersection[0].value if len(intersection) <= 2 else intersection[1].value

    @staticmethod
    def _string_to_tier(provider_str: str) -> ModelTier:
        """Convert provider string to tier"""
        provider_str = provider_str.lower()
        if "opus" in provider_str:
            return ModelTier.PREMIUM
        elif "sonnet" in provider_str:
            return ModelTier.STANDARD
        elif "gemini" in provider_str:
            return ModelTier.FREE
        elif "gpt" in provider_str:
            return ModelTier.BUDGET
        else:
            return ModelTier.LAST_RESORT


# Configuration: When to use each tier
OMNIROUTE_CONFIG = {
    "tier_strategy": "balanced",  # "cheapest" | "balanced" | "best"

    # Rules: when to use free tiers
    "use_free_for": {
        "simple": True,      # FAQ, simple questions
        "creative": True,    # Writing, brainstorming
        "docs": True,        # Documentation
    },

    "never_use_free_for": {
        "security": True,    # Security audits
        "medical": True,     # Medical/health
        "legal": True,       # Legal advice
        "code_quality": True,  # Code review (use premium)
        "production": True,  # Production deployment
    },

    # Quality gates
    "output_validation": {
        "min_quality_score": 7.0,  # Out of 10
        "require_explanation": True,  # Justification for decisions
        "reject_placeholders": True,  # [TODO], [FIXME], [...]
    },

    # Monitoring
    "log_all_outputs": True,  # Track quality per provider
    "alert_on_low_quality": True,  # Flag subpar results
}


# Global instance
_gate = None

def get_quality_gate() -> QualityGate:
    global _gate
    if not _gate:
        _gate = QualityGate()
    return _gate


if __name__ == "__main__":
    gate = get_quality_gate()

    # Example: Check if Gemini (free) is OK for security code review
    valid, reason = gate.validate_provider_for_task(
        provider="gemini-2.0",
        task_complexity="complex",
        domain="security"
    )
    print(f"Security code review with Gemini: {valid}")
    print(f"Reason: {reason}")
    # Output: False - "Free tier 'gemini-2.0' not allowed for 'security' domain"

    # Example: Check if Gemini OK for creative writing
    valid, reason = gate.validate_provider_for_task(
        provider="gemini-2.0",
        task_complexity="simple",
        domain="creative"
    )
    print(f"\nCreative writing with Gemini: {valid}")
    print(f"Reason: {reason}")
    # Output: True - "✓ Provider allowed"

    # Recommend provider for task
    recommended = gate.get_recommended_provider(
        task_complexity="simple",
        domain="general",
        cost_budget="cheapest"
    )
    print(f"\nCheapest provider for simple/general: {recommended}")
    # Output: gemini-2.0
