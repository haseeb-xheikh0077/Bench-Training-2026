import sys
import requests


BASE_URL = "https://api.github.com"


def fetch_json(url):
    """Make a GET request and return parsed JSON, or raise on error."""
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Network error. Check your internet connection.")

    if response.status_code == 404:
        raise ValueError("User not found. Check the username and try again.")
    if response.status_code == 403:
        raise PermissionError("Rate limit hit. Wait a minute and try again.")

    response.raise_for_status()
    return response.json()


def get_profile(username):
    """Fetch basic profile data for a GitHub user."""
    return fetch_json(f"{BASE_URL}/users/{username}")


def get_top_repos(username, count=5):
    """Fetch repos sorted by stars, return top `count`."""
    repos = fetch_json(f"{BASE_URL}/users/{username}/repos?per_page=100")
    sorted_repos = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)
    return sorted_repos[:count]


def print_profile(profile, repos):
    """Display the user profile and top repos."""
    print(f"\n{'=' * 40}")
    print(f"  GitHub Profile: {profile['login']}")
    print(f"{'=' * 40}")
    print(f"  Bio        : {profile.get('bio') or 'No bio provided'}")
    print(f"  Public Repos: {profile['public_repos']}")
    print(f"  Followers   : {profile['followers']}")
    print(f"\n  Top {len(repos)} Repos by Stars:")
    print(f"  {'-' * 36}")
    for repo in repos:
        lang = repo.get("language") or "Unknown"
        print(f"  ⭐ {repo['stargazers_count']:>5}  {repo['name']}  [{lang}]")
    print(f"{'=' * 40}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 exercise_1.py <github-username>")
        sys.exit(1)

    username = sys.argv[1]

    try:
        profile = get_profile(username)
        repos = get_top_repos(username)
        print_profile(profile, repos)
    except (ValueError, PermissionError, ConnectionError, RuntimeError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
