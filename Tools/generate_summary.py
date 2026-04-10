"""
generate_summary.py — Weekly summary generator

Reads daily notes from daily-notes/, extracts structured data,
runs LLM analysis, and generates a weekly report.

Usage:
    python Tools/generate_summary.py            # Last 7 days
    python Tools/generate_summary.py --days 14  # Last 14 days
    python Tools/generate_summary.py --days 30  # Monthly
"""

import argparse
from datetime import date, timedelta
from pathlib import Path

from Tools.notifier import send_text

DAILY_NOTES_PATH = Path("daily-notes")
SUMMARIES_PATH = Path("summaries")


def load_notes(days: int) -> list[dict]:
    """
    Read daily notes from the last N days.

    Returns a list of dicts — one per day that has a note file.
    Each dict should contain the parsed fields from your daily note format.

    What to implement:
    - List note files in daily-notes/ for the date range
    - Parse each file — extract priorities, energy, metrics, reflections
    - Return empty list for days with no note (common for weekends)

    Your daily note structure is in daily-notes/example.md.
    The parsing logic depends on how you format your notes.
    Regex or simple line-by-line parsing both work well here.
    """
    notes = []
    today = date.today()

    for i in range(days):
        day = today - timedelta(days=i)
        note_path = DAILY_NOTES_PATH / f"{day.isoformat()}.md"
        if note_path.exists():
            content = note_path.read_text()
            # --- Implement your parsing logic here ---
            notes.append({
                "date": day.isoformat(),
                "content": content,
                # Add parsed fields: energy, priorities, completions, etc.
            })

    return notes


def analyze_with_llm(notes: list[dict]) -> str:
    """
    Send note data to LLM for pattern analysis.

    What to ask the LLM:
    - What recurring themes or priorities appear across the week?
    - What kept getting postponed?
    - Any notable patterns in energy or mood?
    - Concrete recommendations for next week

    Returns a markdown string with the analysis.
    """

    # --- Implement your LLM call here ---
    # Build a prompt with the note summaries, ask for structured analysis
    # Return the LLM's response as a string

    return "<!-- LLM analysis not implemented yet -->"


def generate_report(notes: list[dict], days: int) -> str:
    """Assemble the full weekly report in markdown."""
    today = date.today()
    week_label = today.strftime("week-%Y-W%V")

    if not notes:
        return f"# {week_label}\n\nNo daily notes found for the last {days} days."

    analysis = analyze_with_llm(notes)

    report = f"# {week_label}\n\n"
    report += f"_{len(notes)} days with notes out of {days} days_\n\n"

    # --- Add your report sections here ---
    # Suggested structure (adapt to your note format):
    #   ## Completion stats
    #   ## Daily metrics (energy, tracked values)
    #   ## Recurring themes
    #   ## LLM analysis
    report += "## Analysis\n\n"
    report += analysis
    report += "\n\n## Reflection\n\n_Write your own notes here after reviewing._\n"

    return report


def run(days: int = 7):
    SUMMARIES_PATH.mkdir(exist_ok=True)

    notes = load_notes(days)
    print(f"[summary] Found {len(notes)} notes in the last {days} days")

    report = generate_report(notes, days)

    today = date.today()
    filename = f"week-{today.strftime('%Y-W%V')}.md"
    output_path = SUMMARIES_PATH / filename
    output_path.write_text(report)
    print(f"[summary] Report saved to {output_path}")

    send_text(f"Weekly summary ready: {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=7)
    args = parser.parse_args()
    run(days=args.days)
