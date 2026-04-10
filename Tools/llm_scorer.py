"""
llm_scorer.py — LLM analysis for top-scoring results

Runs after scorer.py. Takes the top N results from keyword scoring
and asks an LLM to evaluate fit, flag anything interesting, and add
a short human-readable reason.

Uses the LLM provider configured in your .env. Compatible with any
OpenAI-compatible API — Groq, OpenAI, Anthropic via proxy, etc.
"""

import os
import json


def analyze(item: dict, context: str) -> dict:
    """
    Send one result to the LLM for analysis.

    Args:
        item: scored result dict (title, description, score, etc.)
        context: brief description of what you're looking for,
                 loaded from Profile/preferences.yml

    Returns:
        item with added 'llm_reason' (str) and 'llm_score' (int 0-100) keys

    What to implement:
    1. Build a prompt that includes the item details and your context
    2. Call your LLM API of choice
    3. Parse the response — ask for JSON output to keep it reliable
    4. Add 'llm_reason' and 'llm_score' to the item dict
    5. Handle API errors gracefully — fall back to keyword score if LLM fails

    Example prompt structure:
        "You are evaluating a result for someone looking for [context].
         Result: [title] — [description]
         Rate fit 0-100 and give one sentence explaining why."
    """

    # --- Implement your LLM call here ---
    # Suggested libraries: openai (works with Groq/OpenAI), anthropic
    # API key from: os.environ["LLM_API_KEY"]
    # Base URL from: os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1")

    item["llm_reason"] = ""   # replace with actual LLM output
    item["llm_score"] = None  # replace with int 0-100
    return item


def analyze_batch(items: list[dict], context: str, top_n: int = 10) -> list[dict]:
    """
    Run LLM analysis on the top N items by keyword score.
    Items below top_n are returned unchanged.
    """
    top = items[:top_n]
    rest = items[top_n:]
    analyzed = [analyze(item, context) for item in top]
    return analyzed + rest
