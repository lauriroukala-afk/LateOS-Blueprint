# Agent Instructions

> **Note for new users:** Consider also creating a global `~/.claude/CLAUDE.md` for rules that apply across all your projects — things like preferred working style, security defaults, and cross-project conventions. This file covers only what is specific to LateOS.

## What This Is

LateOS is a personal AI operating system built with Claude Code. It uses the **WAT framework** (Workflows, Agents, Tools) to automate daily tasks, process information, and surface what matters.

The system has three moving parts: Claude Code acts as the agent, Python scripts handle execution, and scheduling runs automatically in the background. Notes, tasks, ideas, and outputs are stored as markdown files — Obsidian is used as the interface for reading and writing those files, but the system does not depend on it.

It is not a compiled project. There are no build steps, tests, or linting commands.

## The WAT Architecture

**Layer 1: Workflows (The Instructions)**
- Markdown SOPs stored in `workflows/`
- Each workflow defines the objective, required inputs, which tools to use, expected outputs, and how to handle edge cases
- Written in plain language, the same way you would brief someone on your team

**Layer 2: Agents (The Decision-Maker)**
- This is your role. You are responsible for intelligent coordination.
- Read the relevant workflow, run tools in the correct sequence, handle failures gracefully, and ask clarifying questions when needed
- You connect intent to execution without trying to do everything yourself
- If you need data from an external source, do not attempt it directly. Read the relevant workflow, figure out the required inputs, then execute the right tool.

**Layer 3: Tools (The Execution)**
- Python scripts in `Tools/` that do the actual work
- API calls, data transformations, file operations, database queries
- Credentials and API keys are stored in `.env`
- These scripts are consistent, testable, and fast

**Why this matters:** When AI tries to handle every step directly, accuracy drops fast. If each step is 90% accurate, five steps in a row gives 59% success. By offloading execution to deterministic scripts, the agent stays focused on orchestration and decision-making.

## How to Operate

**1. Look for existing tools first**
Before building anything new, check `Tools/` based on what your workflow requires. Only create new scripts when nothing exists for that task.

**2. Learn and adapt when things fail**
When you hit an error:
- Read the full error message and trace
- Fix the script and retest
- Document what you learned in the workflow
- Update the workflow so the same issue does not happen again

**3. Keep workflows current**
Workflows evolve as you learn. When you find better methods or hit unexpected constraints, update the workflow. Do not create or overwrite workflows without asking unless explicitly told to.

## The Self-Improvement Loop

Every failure is a chance to make the system stronger:
1. Identify what broke
2. Fix the tool
3. Verify the fix works
4. Update the workflow
5. Move on with a more robust system

## File Structure

```
Tools/              # Python scripts for deterministic execution
workflows/          # Markdown SOPs defining what to do and how
Profile/            # Personal configuration and preferences
memory/             # Session memory — index + individual topic files
daily-notes/        # Structured daily entries
summaries/          # Auto-generated periodic reports
Ideas/              # Inbox for capturing content for later processing
Tasks/              # Active tasks and to-dos
Calls/              # Processed audio outputs
.env                # API keys — never commit this file
.tmp/               # Temporary files, regenerated as needed
```

## Security

- API keys and tokens belong in `.env`, never in code
- Never commit `.env` — verify `.gitignore` before the first commit
- If a secret ends up in git history, treat it as compromised and rotate it
- Do not hardcode paths, usernames, or machine-specific values in scripts

## Resilience

- Commit regularly — do not let significant work sit uncommitted
- Keep `.env` backed up outside the repo (password manager)
- Workflows are the most important files — they encode how everything works
- If something breaks: check git history first, then recreate from workflows or memory
