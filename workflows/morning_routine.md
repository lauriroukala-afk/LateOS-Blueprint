# Workflow: Morning Routine

## Objective
Start the day with a structured check-in delivered via your messaging tool.

## When to Run
- Trigger: user says "morning routine" or equivalent
- Or scheduled automatically each morning — see `workflows/github_actions_setup.md`

## Execution

```bash
python Tools/morning_notifier.py --force
```

Tell the user: "Morning check-in sent — fill in the form there."

## Requirements
- Messaging tool credentials set in `.env`
- If using interactive buttons: bot must be running as a background process

## What Happens
1. Check-in form is sent to your messaging tool
2. User fills in: yesterday's reflection, today's priorities, tracked metrics
3. Answers are saved as a daily note in `daily-notes/`
4. Tasks with action verbs are extracted to `Tasks/`

## Notes
- Define your own check-in questions in `Profile/morning_routine.md`
- See `Profile/morning_routine.example.md` for structure and inspiration
- If the bot is not running, interactive buttons will not respond — start it first
