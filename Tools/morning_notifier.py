"""
morning_notifier.py — Morning check-in delivery

Reads your check-in questions from Profile/morning_routine.md and sends
them to your messaging tool. When you answer, responses are saved as a
daily note in daily-notes/.

Usage:
    python Tools/morning_notifier.py
    python Tools/morning_notifier.py --force   # skip schedule check
"""

import argparse
from datetime import date
from pathlib import Path

from Tools.notifier import send_text

MORNING_ROUTINE_PATH = Path("Profile/morning_routine.md")
DAILY_NOTES_PATH = Path("daily-notes")


def load_questions() -> list[str]:
    """
    Parse check-in questions from Profile/morning_routine.md.

    Expected format: any line starting with a number or bullet
    is treated as a question. Adapt the parsing to match your
    morning_routine.md structure.

    See Profile/morning_routine.example.md for reference.
    """
    if not MORNING_ROUTINE_PATH.exists():
        raise FileNotFoundError(
            f"Missing {MORNING_ROUTINE_PATH} — copy from morning_routine.example.md"
        )

    questions = []
    with open(MORNING_ROUTINE_PATH) as f:
        for line in f:
            line = line.strip()
            # --- Adapt this parsing to your file format ---
            # Example: treat lines starting with digits or dashes as questions
            if line and (line[0].isdigit() or line.startswith("-")):
                questions.append(line.lstrip("0123456789.-) ").strip())

    return questions


def save_daily_note(date_str: str, content: str):
    """Save answers as a daily note."""
    DAILY_NOTES_PATH.mkdir(exist_ok=True)
    note_path = DAILY_NOTES_PATH / f"{date_str}.md"
    note_path.write_text(content)
    print(f"[morning] Saved daily note: {note_path}")


def run(force: bool = False):
    today = date.today().isoformat()

    # Check if already run today (skip if force)
    if not force:
        note_path = DAILY_NOTES_PATH / f"{today}.md"
        if note_path.exists():
            print(f"[morning] Already ran today ({today}). Use --force to override.")
            return

    questions = load_questions()
    if not questions:
        print("[morning] No questions found in morning_routine.md")
        return

    # --- Implement your delivery method here ---
    # Option A: Send as a simple text message with questions listed
    # Option B: Send an interactive form (requires a bot, not just a webhook)
    # Option C: Print to terminal for manual copy-paste
    #
    # For interactive forms, you'll need a running bot that listens for
    # responses and calls save_daily_note() when the form is submitted.

    message = f"*Morning check-in — {today}*\n\n"
    message += "\n".join(f"{i+1}. {q}" for i, q in enumerate(questions))

    send_text(message)
    print(f"[morning] Check-in sent with {len(questions)} questions")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    run(force=args.force)
