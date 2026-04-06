import requests

REDDIT_URL = "https://www.reddit.com/r/technology/top.json?limit=50"
USER_AGENT = "headline-analyser/1.0 (educational project)"
TIMEOUT = 10


def fetch_posts() -> list[dict]:
    """Fetch top 50 posts from r/technology via the public Reddit JSON API.

    Returns a list of post dicts, each containing at minimum:
        title (str), score (int), created_utc (float), url (str)

    Raises:
        ConnectionError: Network is unreachable.
        TimeoutError: Request exceeded the timeout.
        ValueError: Non-2xx response or unexpected JSON shape.
    """
    try:
        response = requests.get(
            REDDIT_URL,
            headers={"User-Agent": USER_AGENT},
            timeout=TIMEOUT,
        )
    except requests.exceptions.ConnectionError as exc:
        raise ConnectionError(f"Could not reach Reddit: {exc}") from exc
    except requests.exceptions.Timeout as exc:
        raise TimeoutError(f"Reddit request timed out after {TIMEOUT}s") from exc

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as exc:
        raise ValueError(f"Reddit returned HTTP {response.status_code}: {exc}") from exc

    try:
        children = response.json()["data"]["children"]
    except (KeyError, ValueError) as exc:
        raise ValueError(f"Unexpected API response shape: {exc}") from exc

    return [child["data"] for child in children]
