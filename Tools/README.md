# Tools

Python scripts that handle all execution. Each script does one thing and does it well.

The agent (Claude Code) never executes tasks directly — it reads workflows and calls these scripts. This keeps accuracy high: AI handles decisions, scripts handle execution.

## Core pipeline

| Script | Purpose |
|---|---|
| `run_daily_digest.py` | Main entry point. Orchestrates sources, scoring, and Slack notification. |
| `scorer.py` | Keyword-based scoring. Fast first pass before LLM analysis. |
| `llm_scorer.py` | LLM analysis via Groq. Runs on top-scoring results from scorer.py. |
| `slack_notifier.py` | Sends results to Slack. Supports both webhook and bot API. |
| `db.py` | SQLite deduplication. Tracks what has already been seen. |

## Sources

Each source script follows the same interface: fetch content, return a list of dicts with consistent fields. Scorer handles the rest.

Supported source types:
- `source_[your-site-a].py` — HTML scraper for sites with static or server-rendered content
- `source_[your-site-b].py` — HTML scraper with detail page fetching
- `source_search.py` — finds results on specific sites via Google (using Serper API)
- `source_stubs.py` — placeholders for JS-rendered sites or sources with access restrictions

To add a new source, follow any HTML scraper as a template. No need to touch scoring or notification logic.

## Reporting and routines

| Script | Purpose |
|---|---|
| `generate_summary.py` | Weekly report. Parses structured notes and runs LLM analysis. |
| `ai_news_digest.py` | Weekly digest. Fetches and summarizes relevant content via Tavily. |
| `morning_notifier.py` | Sends a daily check-in form to Slack. |
| `show_scores.py` | Debug tool — shows scoring breakdown for recent results. |

## Optional integrations

| Script | Purpose |
|---|---|
| `slack_bot.py` | Slack bot for interactive features (buttons, modals). |
| `slack_app.py` | Handles Slack events — button clicks, form submissions. |
| `transcribe_call.py` | Transcribes audio files using AssemblyAI, summarizes with Groq. |
| `voice_input.py` | Transcribes voice input via Groq Whisper. |
| `source_discord.py` | Fetches messages from a Discord channel via bot. |
