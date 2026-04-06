# Reddit Headline Analyser

Fetches the top 50 posts from r/technology using Reddit's public JSON API (no authentication required), analyses the headlines, and saves a structured report. Useful for spotting what topics are dominating tech news at any given moment.

## What it does

- Fetches up to 50 top posts from `r/technology`
- Counts word frequency across all titles and prints the top 20 (stopwords excluded)
- Finds the most upvoted post
- Calculates average upvotes across all posts
- Classifies posts as posted **today** vs **older** (based on UTC midnight)
- Saves everything to `report.json`

## How to run

**Requirements:** Python 3.6+, `requests` library.

```bash
pip install requests
cd day-7
python3 main.py
```

No arguments. No environment variables. No API key.

## Example output

```
============================================================
  REDDIT r/technology — TOP 50 HEADLINE ANALYSIS
============================================================

Fetched at : 2026-04-06T15:17:56Z
Total posts: 43

--- Top 20 Words ---
    1. ai                   11  ###########
    2. games                 4  ####
    3. iran                  3  ###
    4. data                  3  ###
    5. moon                  3  ###
    6. investigation         3  ###
    7. laser                 3  ###
    8. artemis               3  ###
    9. ii                    3  ###
   10. system                3  ###
   11. war                   3  ###
   12. billion               3  ###
   13. openais               2  ##
   14. center                2  ##
   15. abu                   2  ##
   16. dhabi                 2  ##
   17. video                 2  ##
   18. against               2  ##
   19. report                2  ##
   20. playstation           2  ##

--- Most Upvoted Post ---
  Title : Iran threatens 'complete and utter annihilation' of OpenAI's $30B Stargate AI data center in Abu Dhabi
  Score : 29,592
  URL   : https://www.tomshardware.com/tech-industry/iran-threatens-complete-and-utter-annihilation-of-openais-usd30b-stargate-ai-data-center-in-abu-dhabi-regime-posts-video-with-satellite-imagery-of-chatgpt-makers-premier-1gw-data-center

--- Upvote Stats ---
  Average upvotes : 2,280.56

--- Post Age ---
  Today : 40
  Older : 3

============================================================

Report saved to report.json
```

## Output file

`report.json` is written in the current directory after each run:

```json
{
  "top_words": [["ai", 11], ["games", 4], ...],
  "most_upvoted": {
    "title": "Iran threatens 'complete and utter annihilation'...",
    "score": 29592,
    "url": "https://...",
    "created_utc": 1775434326.0
  },
  "average_upvotes": 2280.56,
  "post_count": 43,
  "today_count": 40,
  "older_count": 3,
  "fetched_at": "2026-04-06T15:17:56Z"
}
```

## Project structure

```
day-7/
├── fetcher.py    — HTTP layer: fetch posts, handle all network errors
├── analyser.py   — Pure analysis functions: word freq, stats, date classify
├── reporter.py   — Console output and report.json writer
└── main.py       — Pipeline orchestration; the only entry point
```

## What was interesting

**Reddit requires a custom User-Agent.** The default `python-requests/x.x` string gets silently rate-limited or blocked with a 429. Setting a descriptive `User-Agent` header is all it takes to get clean responses — a good reminder that "no auth" doesn't mean "no headers matter."

**Stopwords as a `frozenset`.** Each title produces dozens of tokens, and every token is checked against the stopword list. A `frozenset` gives O(1) membership testing vs O(n) for a list. It also signals clearly in the code that the set is never mutated at runtime.

**UTC midnight cutoff.** Classifying posts as "today" vs "older" sounds simple but has a subtle edge: `datetime.datetime.utcnow()` gives the current moment, but the cutoff needs to be midnight of today's UTC date, not "24 hours ago." The implementation extracts `today.year/month/day`, constructs a naive midnight datetime, then converts to a Unix timestamp for integer comparison against `created_utc`.
