import sys
import datetime

from fetcher import fetch_posts
from analyser import count_word_frequency, find_most_upvoted, calculate_average_upvotes, classify_by_date
from reporter import print_report, save_report


def build_results(posts: list[dict]) -> dict:
    """Run all analysis functions and assemble the results dict."""
    by_date = classify_by_date(posts)
    most_upvoted = find_most_upvoted(posts)
    top_words = count_word_frequency(posts)

    return {
        "top_words": [[word, count] for word, count in top_words],
        "most_upvoted": most_upvoted,
        "average_upvotes": calculate_average_upvotes(posts),
        "post_count": len(posts),
        "today_count": len(by_date["today"]),
        "older_count": len(by_date["older"]),
        "fetched_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def main() -> None:
    """Fetch Reddit posts, analyse headlines, print results, save report."""
    try:
        posts = fetch_posts()
    except (ConnectionError, TimeoutError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    results = build_results(posts)
    print_report(results)

    try:
        save_report(results)
    except OSError as exc:
        print(f"Warning: could not write report.json — {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
