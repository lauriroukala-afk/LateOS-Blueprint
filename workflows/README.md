# Workflows

Plain-language instructions that tell the agent what to do and how.

Before acting, Claude Code reads the relevant workflow. This keeps the agent focused on orchestration rather than improvising — it follows a documented process, handles edge cases defined in advance, and improves the workflow when it finds better methods.

## Available workflows

| Workflow | Purpose |
|---|---|
| `daily_digest.md` | Scrapes sources, scores results, sends notification via your messaging tool. |
| `morning_routine.md` | Sends daily check-in, defines what to track and why. |
| `weekly_summary.md` | Generates weekly report from structured daily notes. |
| `transcribe_call.md` | Transcribes audio, summarizes, saves as structured note. |
| `github_actions_setup.md` | How to schedule workflows using GitHub Actions. |

## How workflows are written

Each workflow covers:
- **Objective** — what this workflow accomplishes
- **Inputs** — what the agent needs before starting
- **Steps** — what to do in order, including which tools to call
- **Edge cases** — known failure modes and how to handle them
- **Output** — what done looks like

Workflows evolve. When the agent finds a better method or hits an unexpected constraint, the workflow gets updated. That is how the system improves over time.

## Adding your own

Workflows are just markdown files. Write them the way you would brief a capable colleague — clear enough that they can make judgment calls, not so prescriptive that every edge case needs its own rule.
