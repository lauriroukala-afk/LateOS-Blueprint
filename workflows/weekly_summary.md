# Workflow: Weekly Summary

## Objective
Generate a weekly report from daily notes — completion statistics, energy patterns, recurring themes, and LLM analysis.

## When to Run
- End of week, or scheduled automatically
- Trigger: user says "weekly summary" or equivalent

## Execution

```bash
python Tools/generate_summary.py           # Last 7 days
python Tools/generate_summary.py --days 14 # Last 14 days
python Tools/generate_summary.py --days 30 # Monthly
```

## Output
- Report saved to `summaries/week-YYYY-WNN.md`
- Delivered to your messaging tool

The report includes:
- Completion stats — how many priorities were done, skipped, or postponed
- Daily metrics — energy and tracked values in chronological order
- Recurring themes — most frequent priorities across the week
- LLM analysis — patterns, blockers, recommendations
- Reflection section — left blank for manual notes

## Notes
- Reads files from `daily-notes/` — consistent daily note format required
- Reflection data only available if morning routine was followed
- The reflection section is intentionally blank — fill it in after reviewing
