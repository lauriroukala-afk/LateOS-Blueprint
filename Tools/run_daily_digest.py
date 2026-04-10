"""
run_daily_digest.py — Daily digest main runner

Orchestrates the full pipeline:
1. Fetch results from all configured sources
2. Deduplicate against DB
3. Score with keyword engine
4. Run LLM analysis on top results
5. Send notification with results above threshold

Usage:
    python Tools/run_daily_digest.py          # standard run
    python Tools/run_daily_digest.py --dry    # no DB writes, no notifications
    python Tools/run_daily_digest.py --now    # ignore schedule, run immediately
"""

import argparse
import yaml
from pathlib import Path

from Tools.db import init_db, is_seen, mark_seen
from Tools.scorer import score_all, load_preferences
from Tools.llm_scorer import analyze_batch
from Tools.notifier import send_digest

# --- Add your sources here ---
# Import each source module and add its fetch function to this list.
# Each source must implement a fetch() -> list[dict] interface.
# See source_example.py for the expected structure.
#
# Example:
#   from Tools.source_my_job_board import fetch as fetch_my_board
#   from Tools.source_rss_feed import fetch as fetch_rss
#
SOURCES = [
    # fetch_my_board,
    # fetch_rss,
]

PREFERENCES_PATH = Path("Profile/preferences.yml")


def run(dry: bool = False):
    init_db()
    prefs = load_preferences()

    # 1. Fetch from all sources
    all_results = []
    for fetch in SOURCES:
        try:
            results = fetch()
            all_results.extend(results)
        except Exception as e:
            print(f"[warn] Source failed: {e}")

    print(f"[digest] Fetched {len(all_results)} results from {len(SOURCES)} sources")

    # 2. Deduplicate
    new_results = [
        r for r in all_results
        if not is_seen(r.get("url", ""), r.get("title", ""))
    ]
    print(f"[digest] {len(new_results)} new after deduplication")

    # 3. Keyword scoring
    scored = score_all(new_results, prefs)

    # 4. LLM analysis on top results
    # Adjust top_n and the context string to match your use case
    context = prefs.get("llm_context", "relevant results matching my interests")
    analyzed = analyze_batch(scored, context=context, top_n=10)

    # 5. Filter by threshold and send
    threshold = prefs.get("score_threshold", 30)
    to_send = [r for r in analyzed if r.get("score", 0) >= threshold]

    print(f"[digest] {len(to_send)} results above threshold ({threshold})")

    if not dry:
        if to_send:
            send_digest(to_send)
        for r in to_send:
            mark_seen(r.get("url", ""), r.get("title", ""))
    else:
        print("[digest] Dry run — no DB writes, no notifications")
        for r in to_send[:5]:
            print(f"  {r.get('score')} | {r.get('title')} | {r.get('url')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry", action="store_true", help="Dry run")
    parser.add_argument("--now", action="store_true", help="Ignore schedule")
    args = parser.parse_args()
    run(dry=args.dry)
