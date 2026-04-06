import re
import datetime
import collections

STOPWORDS = frozenset({
    "the", "a", "an", "to", "and", "of", "in", "is", "it",
    "for", "on", "at", "by", "be", "as", "are", "was", "with",
    "that", "this", "from", "has", "have", "not", "but", "or",
    "its", "will", "into", "than", "more", "over", "after",
    "new", "now", "about", "up", "how", "what", "says", "your",
    "their", "they", "we", "he", "she", "you", "i", "so", "do",
    "his", "her", "all", "just", "been", "would", "could", "get",
    "out", "can", "if", "my", "no", "s", "us",
})


def count_word_frequency(posts: list[dict], top_n: int = 20) -> list[tuple[str, int]]:
    """Return top_n (word, count) pairs from all post titles, excluding stopwords.

    Normalises to lowercase, strips non-alphanumeric characters, and ignores
    single-character tokens and stopwords.
    """
    counter: collections.Counter = collections.Counter()

    for post in posts:
        title = post.get("title")
        if not title:
            continue
        cleaned = re.sub(r"[^a-z0-9\s]", "", title.lower())
        tokens = [w for w in cleaned.split() if len(w) > 1 and w not in STOPWORDS]
        counter.update(tokens)

    return counter.most_common(top_n)


def find_most_upvoted(posts: list[dict]) -> dict:
    """Return the post dict with the highest 'score' value.

    Returns an empty dict if posts is empty.
    """
    if not posts:
        return {}
    return max(posts, key=lambda p: p.get("score", 0))


def calculate_average_upvotes(posts: list[dict]) -> float:
    """Return mean score across all posts, rounded to 2 decimal places.

    Returns 0.0 if posts is empty.
    """
    if not posts:
        return 0.0
    total = sum(p.get("score", 0) for p in posts)
    return round(total / len(posts), 2)


def classify_by_date(posts: list[dict]) -> dict[str, list[dict]]:
    """Split posts into 'today' and 'older' based on UTC date.

    A post is 'today' if its created_utc falls on or after UTC midnight today.
    """
    today = datetime.datetime.utcnow().date()
    cutoff = int(datetime.datetime(today.year, today.month, today.day).timestamp())

    result: dict[str, list[dict]] = {"today": [], "older": []}
    for post in posts:
        created = int(post.get("created_utc", 0))
        if created >= cutoff:
            result["today"].append(post)
        else:
            result["older"].append(post)

    return result
