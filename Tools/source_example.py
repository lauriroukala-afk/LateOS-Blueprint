"""
source_example.py — Example source template

Every source script follows this same interface: fetch results,
return a list of dicts with consistent fields. The scoring pipeline
handles everything after that.

Copy this file and rename it for each source you want to add:
    source_my_job_board.py
    source_rss_feed.py
    source_company_careers.py
    etc.
"""

from datetime import datetime


def fetch() -> list[dict]:
    """
    Fetch results from your source and return them in a standard format.

    Returns:
        list of dicts, each with these fields:

        Required:
            title (str)       — result title or headline
            url (str)         — direct link to the result
            source (str)      — name of this source, e.g. "LinkedIn Jobs"

        Recommended:
            description (str) — snippet or full text for scoring
            published (str)   — ISO date string, e.g. "2025-01-15"
            location (str)    — city, "Remote", etc.

        Optional (add whatever makes sense for your use case):
            company (str)
            salary (str)
            tags (list[str])

    What to implement:
    - Fetch from your source (HTTP request, RSS feed, API call, etc.)
    - Parse the response into the dict structure above
    - Handle pagination if needed
    - Handle rate limiting — add sleep() if the site is sensitive to it
    - Return an empty list on failure rather than raising — keeps the
      pipeline running even if one source is down

    Example sources:
    - Job boards: requests + BeautifulSoup for HTML scraping
    - RSS/Atom: feedparser library
    - APIs: requests with your API key from os.environ
    - Google search: Serper API or SerpAPI for targeted site searches
    """

    results = []

    # --- Implement your fetching logic here ---
    # Example structure:
    #
    # response = requests.get("https://your-source.com/feed")
    # for item in parse(response):
    #     results.append({
    #         "title": item["title"],
    #         "url": item["url"],
    #         "description": item["body"],
    #         "source": "Your Source Name",
    #         "published": item["date"],
    #         "location": item.get("location", ""),
    #     })

    return results
