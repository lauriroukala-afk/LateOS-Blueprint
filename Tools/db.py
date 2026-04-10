"""
db.py — SQLite deduplication layer

Tracks which results have already been seen so the daily digest never
surfaces the same item twice across runs.

Usage:
    from Tools.db import init_db, is_seen, mark_seen

    init_db()
    if not is_seen(url, title, location):
        process(item)
        mark_seen(url, title, location)
"""

import sqlite3
import hashlib
from pathlib import Path

# Path to your SQLite database — adjust if needed
DB_PATH = Path(".tmp/lateos.db")


def init_db():
    """Create the seen_results table if it doesn't exist."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS seen_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT,
                hash TEXT UNIQUE,
                seen_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()


def _hash(title: str, company: str = "", location: str = "") -> str:
    """Generate a stable fingerprint for a result."""
    raw = f"{title}|{company}|{location}".lower().strip()
    return hashlib.sha256(raw.encode()).hexdigest()


def is_seen(url: str, title: str, company: str = "", location: str = "") -> bool:
    """Return True if this result has been seen before."""
    h = _hash(title, company, location)
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(
            "SELECT 1 FROM seen_results WHERE url = ? OR hash = ?", (url, h)
        ).fetchone()
    return row is not None


def mark_seen(url: str, title: str, company: str = "", location: str = ""):
    """Record a result so it won't be surfaced again."""
    h = _hash(title, company, location)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR IGNORE INTO seen_results (url, hash) VALUES (?, ?)",
            (url, h),
        )
        conn.commit()
