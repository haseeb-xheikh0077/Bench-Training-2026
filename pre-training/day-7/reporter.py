import json


def print_report(results: dict) -> None:
    """Print a formatted analysis summary to stdout."""
    print("\n" + "=" * 60)
    print("  REDDIT r/technology — TOP 50 HEADLINE ANALYSIS")
    print("=" * 60)

    print(f"\nFetched at : {results['fetched_at']}")
    print(f"Total posts: {results['post_count']}")

    print("\n--- Top 20 Words ---")
    top_words = results.get("top_words", [])
    if top_words:
        for rank, (word, count) in enumerate(top_words, start=1):
            bar = "#" * min(count, 40)
            print(f"  {rank:>2}. {word:<18} {count:>4}  {bar}")
    else:
        print("  No words found.")

    print("\n--- Most Upvoted Post ---")
    mu = results.get("most_upvoted", {})
    if mu:
        print(f"  Title : {mu['title']}")
        print(f"  Score : {mu['score']:,}")
        print(f"  URL   : {mu['url']}")
    else:
        print("  No posts available.")

    print(f"\n--- Upvote Stats ---")
    print(f"  Average upvotes : {results['average_upvotes']:,.2f}")

    print(f"\n--- Post Age ---")
    print(f"  Today : {results['today_count']}")
    print(f"  Older : {results['older_count']}")

    print("\n" + "=" * 60)


def save_report(results: dict, path: str = "report.json") -> None:
    """Serialise the results dict to JSON at the given path.

    The most_upvoted entry is trimmed to title, score, url, and created_utc
    to avoid dumping the full Reddit post blob.

    Raises:
        OSError: If the file cannot be written.
    """
    serialisable = dict(results)

    mu = results.get("most_upvoted", {})
    if mu:
        url = mu.get("url", "")
        if url.startswith("/"):
            url = "https://www.reddit.com" + url
        serialisable["most_upvoted"] = {
            "title": mu.get("title", ""),
            "score": mu.get("score", 0),
            "url": url,
            "created_utc": mu.get("created_utc", 0.0),
        }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(serialisable, f, indent=2, ensure_ascii=False)

    print(f"\nReport saved to {path}")
