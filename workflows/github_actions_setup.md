# Workflow: GitHub Actions Setup

## Objective

Schedule LateOS tools to run automatically without keeping a local machine running.

## How it works

GitHub Actions runs your scripts on a schedule using free CI/CD minutes. Each workflow file defines when to run and which script to call.

## Basic structure

Create a file at `.github/workflows/daily_digest.yml`:

```yaml
name: Daily Digest

on:
  schedule:
    - cron: '0 7 * * 1-5'   # 07:00 UTC, weekdays
  workflow_dispatch:          # allow manual trigger

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - run: pip install -r requirements.txt

      - run: python Tools/run_daily_digest.py
        env:
          MESSAGING_WEBHOOK_URL: ${{ secrets.MESSAGING_WEBHOOK_URL }}
          LLM_API_KEY: ${{ secrets.LLM_API_KEY }}
          # Add other required env vars here
```

## Adding secrets

In your GitHub repo: Settings → Secrets and variables → Actions → New repository secret.

Add one secret for each variable in your `.env` file that the script needs.

## Cron schedule examples

| Schedule | Cron expression |
|---|---|
| Weekdays at 07:00 UTC | `0 7 * * 1-5` |
| Every day at 08:00 UTC | `0 8 * * *` |
| Mondays at 09:00 UTC | `0 9 * * 1` |

Use [crontab.guru](https://crontab.guru) to build and test expressions.

## Notes

- GitHub Actions free tier gives 2000 minutes/month for private repos, unlimited for public.
- `workflow_dispatch` lets you trigger a run manually from the GitHub UI — useful for testing.
- If a script fails, GitHub sends an email notification by default.
- For scripts that write to a SQLite DB, the DB is local to each run and resets every time. Store persistent state externally (cloud storage, a hosted DB) if you need it to survive across runs.
