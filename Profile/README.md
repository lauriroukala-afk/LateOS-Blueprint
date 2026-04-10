# Profile

Your personal configuration. This is where LateOS learns what matters to you.

Nothing here is shared — the files in this folder are yours. The `.example` files show the structure; the content is up to you.

## Files

| File | Purpose |
|---|---|
| `preferences.example.yml` | Scoring keywords, thresholds, filters. Copy to `preferences.yml` and adapt. |
| `morning_routine.example.md` | Example check-in questions. Copy to `morning_routine.md` and write your own. |

## preferences.yml

Defines how the daily digest scores results. Key sections:

- **Keywords** — terms that increase a result's score. Organized by weight (high, medium, low).
- **Negative keywords** — terms that decrease the score or filter results out entirely.
- **Thresholds** — minimum score to include a result in the notification.
- **Filters** — hard rules (location, language, etc.) applied before scoring.

The more specific your keywords, the more useful the digest becomes. Start broad, then refine based on what the system surfaces.

## morning_routine.md

Defines the daily check-in questions sent via your messaging tool each morning. The answers are stored in daily notes and used by `generate_summary.py` for weekly analysis.

Design your questions around what you actually want to track over time. The weekly report surfaces patterns — but only from data you collect consistently.
