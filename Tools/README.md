# Tools

Python scripts that handle all execution in the WAT pipeline.

The agent (Claude Code) reads workflows and calls these scripts. AI handles decisions, scripts handle execution. This keeps accuracy high across multi-step pipelines.

## What's included

These are blueprint scripts — the structure and interfaces are complete, but the implementation details are yours to fill in. Each file has comments explaining what to build and why.

| Script | Purpose |
|---|---|
| `run_daily_digest.py` | Main entry point — orchestrates sources, scoring, and notification |
| `db.py` | SQLite deduplication — tracks what you've already seen |
| `scorer.py` | Keyword scoring engine — fast first pass before LLM |
| `llm_scorer.py` | LLM analysis — evaluates top results from scorer |
| `notifier.py` | Notification delivery — adapt to Slack, Discord, email, etc. |
| `source_example.py` | Source template — copy this for each feed you want to add |
| `morning_notifier.py` | Morning check-in delivery |
| `generate_summary.py` | Weekly report generator |
| `transcribe_call.py` | Call recording, transcription, and summarization |

## Source interface

Every source script follows the same interface: `fetch() -> list[dict]`

Each result dict must have at minimum:
- `title` (str)
- `url` (str)
- `source` (str)

Add `description`, `published`, `location`, `company` and anything else relevant to your use case. The scorer will use whatever fields you provide.

To add a source: copy `source_example.py`, rename it, implement `fetch()`.

## What you bring

- Your sources (job boards, RSS feeds, APIs — see `source_example.py`)
- Your API keys in `.env` — see `.env.example`
- Your preferences in `Profile/preferences.yml`
- Your LLM provider (anything OpenAI-compatible works: Groq, OpenAI, Anthropic)
- Your messaging tool credentials (Slack, Discord, Telegram, email — adapt `notifier.py`)

## Running scripts

```bash
python Tools/run_daily_digest.py --dry    # test without DB writes or notifications
python Tools/run_daily_digest.py          # full run
python Tools/generate_summary.py --days 7
python Tools/morning_notifier.py --force
python Tools/transcribe_call.py recording.mp3 --title "Team meeting"
```

## Dependencies

```bash
pip install -r requirements.txt
```

Optional, for live call recording:
```bash
pip install sounddevice numpy scipy
```
