# Workflow: Daily Digest

## Objective
Fetch new results from configured sources, score them against your profile, and send a notification with the top matches.

## Inputs Required
- `Profile/preferences.yml` — scoring config (single source of truth)
- `.env` — messaging tool credentials
- `.tmp/lateos.db` — run history for deduplication

## Tools Used
- `Tools/run_daily_digest.py` — main runner
- `Tools/db.py` — SQLite deduplication
- `Tools/scorer.py` — keyword scoring engine
- `Tools/llm_scorer.py` — LLM analysis for top results
- `Tools/notifier.py` — notification delivery (adapt to your messaging tool)
- `Tools/source_[your-site].py` — add your own sources here

## Execution

### Manual run
```bash
python Tools/run_daily_digest.py --now
```

### Dry run (no DB writes, no notifications)
```bash
python Tools/run_daily_digest.py --dry
```

### Scheduled
See `workflows/github_actions_setup.md`

## Output
- Results saved to your preferred output folder (score above threshold)
- Notification delivered via your messaging tool with top matches

## Incremental Logic
- First run: fetches last 14 days
- Subsequent runs: fetches only results published after last successful run
- Deduplication: URL-unique + SHA256(title + company + location)

## Scoring Weights (from preferences.yml)
| Category | Weight |
|---|---|
| Role match | 30 |
| Domain match | 20 |
| Must-have | 20 |
| Nice-to-have | 10 |
| Seniority | 10 |
| Location | 10 |

## Edge Cases
<!-- Update this section when you discover issues -->
