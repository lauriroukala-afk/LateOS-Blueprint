"""
scorer.py — Keyword-based scoring engine

Fast first pass before any LLM analysis. Scores results against your
preferences profile so only the most relevant items go to the LLM step.

Scoring weights are loaded from Profile/preferences.yml.
See preferences.example.yml for the expected structure.
"""

import yaml
from pathlib import Path


PREFERENCES_PATH = Path("Profile/preferences.yml")


def load_preferences() -> dict:
    """Load scoring config from your preferences file."""
    with open(PREFERENCES_PATH) as f:
        return yaml.safe_load(f)


def score(item: dict, prefs: dict) -> dict:
    """
    Score a single result against your preferences.

    Args:
        item: dict with at least 'title' and 'description' keys
        prefs: loaded preferences dict

    Returns:
        item with added 'score' (int) and 'score_breakdown' (dict) keys

    Scoring categories to implement:
    - Role match: does the title match your target roles?
    - Domain match: is the company in a domain you want?
    - Must-have keywords: non-negotiable requirements
    - Nice-to-have keywords: bonus points
    - Seniority: does the level match?
    - Location: remote / city / hybrid preference

    Weights for each category are defined in preferences.yml.
    """
    score = 0
    breakdown = {}

    text = f"{item.get('title', '')} {item.get('description', '')}".lower()

    # --- Implement your scoring logic here ---
    # Example pattern:
    #
    # for keyword in prefs.get("must_have", []):
    #     if keyword.lower() in text:
    #         score += prefs["weights"]["must_have"]
    #         breakdown["must_have"] = breakdown.get("must_have", 0) + 1

    item["score"] = score
    item["score_breakdown"] = breakdown
    return item


def score_all(items: list[dict], prefs: dict | None = None) -> list[dict]:
    """Score a list of results. Returns sorted by score descending."""
    if prefs is None:
        prefs = load_preferences()
    scored = [score(item, prefs) for item in items]
    return sorted(scored, key=lambda x: x["score"], reverse=True)
