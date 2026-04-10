"""
notifier.py — Notification delivery

Sends digest results to your messaging tool of choice.
Adapt this to whatever you use: Slack, Discord, Telegram, email, etc.

Credentials are loaded from .env — see .env.example for required keys.
"""

import os


def send_digest(items: list[dict], title: str = "Daily Digest"):
    """
    Send scored results as a notification.

    Args:
        items: list of scored result dicts, sorted by score
        title: notification header

    What to implement:
    - Format items into a readable message (markdown usually works well)
    - Send via your messaging tool's API or webhook
    - Consider: how many results to include? Score threshold?
    - Optional: add a "feedback" mechanism so you can mark results as good/bad

    Example structure for each item in the message:
        [Title](url) — Company · Location
        Score: 85 | Reason: "Strong match on role and domain"

    Credentials to load from .env:
        MESSAGING_WEBHOOK_URL — simplest option, no bot setup needed
        MESSAGING_BOT_TOKEN + MESSAGING_CHANNEL_ID — for interactive features
    """

    if not items:
        print("No results to send.")
        return

    # --- Implement your notification logic here ---
    # Example with a webhook (works for Slack, Discord, etc.):
    #
    # import requests
    # webhook_url = os.environ["MESSAGING_WEBHOOK_URL"]
    # message = format_message(items, title)
    # requests.post(webhook_url, json={"text": message})

    print(f"[notifier] Would send {len(items)} results: {title}")


def send_text(message: str):
    """
    Send a plain text message — used by morning routine and weekly summary.

    Same setup as send_digest, just simpler payload.
    """

    # --- Implement your text delivery here ---
    print(f"[notifier] Would send message ({len(message)} chars)")
