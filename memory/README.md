# Memory

How LateOS remembers things across sessions.

## Three levels

**1. Global memory** (`~/.claude/memory/`) — applies to all projects. Loaded automatically at the start of every session, regardless of which project is open.

**2. Project memory** (`~/.claude/projects/[project]/memory/`) — specific to one project. Loaded automatically at the start of every session within that project.

**3. Individual topic files** — both levels use the same internal structure. Each has a short `MEMORY.md` index that is always loaded. When the agent needs detail on a specific topic, it reads the relevant file from the memory folder. Those files are not loaded automatically — only when the index indicates they are relevant.

This is the key design decision: the index is small enough to fit in every session, and deeper detail is retrieved on demand. The agent always knows what it knows, but only loads what it needs.

## Why this works

Context windows are not free. Loading everything into every session creates noise and wastes space. By keeping a lightweight index and retrieving details selectively, the system stays fast and accurate regardless of how much memory has accumulated.

This mirrors what automated memory systems (e.g. MemPalace) formalize with vector search. The difference here is that retrieval is human-guided rather than automated — simpler infrastructure, more control.

## Why not automated memory?

Tools like claude-mem capture everything automatically. The problem is noise — if the system decides what to remember, irrelevant details accumulate and degrade future context quality.

In LateOS, the human curates memory. Claude proposes what to save, the human approves. This keeps the memory clean and the context useful.

## Memory types

| Type | Purpose |
|---|---|
| `user_*.md` | Who the user is, preferences, working style |
| `feedback_*.md` | What to do and what to avoid — learned from corrections and confirmations |
| `project_*.md` | Ongoing work, decisions, context that is not in the code |
| `reference_*.md` | Pointers to external systems and resources |

## When to scale

This works well up to around 50 memory files. Beyond that, a semantic search layer (MCP-based retrieval from a vector store) becomes worth the added infrastructure. Until then, the index is sufficient.
