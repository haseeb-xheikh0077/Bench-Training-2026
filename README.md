# Pre-Training — 7-Day Python Intensive

A 7-day sprint covering Python fundamentals through real-world mini-projects. Each day is self-contained with its own code and README.

## Progress

| Day | Topic | What I built |
|-----|-------|--------------|
| [Day 1](day-1/) | Control flow, loops | Corporate life simulation — salary tracker, loops, conditionals |
| [Day 2](day-2/) | Lists & dicts | Exercises exploring the difference between ordered lists and key-value dicts |
| [Day 3](day-3/) | Functions & validation | OOP task tracker CLI — add/complete/list tasks persisted to `tasks.json` |
| [Day 4](day-4/) | APIs & HTTP | GitHub profile fetcher + live weather CLI chaining two API calls |
| [Day 5](day-5/) | Data analysis | Titanic dataset — survival rates, age distribution, fare stats with pandas |
| [Day 6](day-6/) | ML from scratch | Neuron + dense layer built from scratch using only NumPy |
| [Day 7](day-7/) | Mini project | Reddit Headline Analyser — word frequency, upvote stats, saves `report.json` |

## How to navigate

Each folder has its own README with what it does, how to run it, and example output. Start there.

```
pre-training/
├── day-1/    control flow + loops
├── day-2/    lists + dicts
├── day-3/    functions + CLI task tracker
├── day-4/    external APIs (GitHub, weather)
├── day-5/    data analysis (Titanic dataset)
├── day-6/    ML from scratch (neuron, dense layer)
└── day-7/    mini project (Reddit Headline Analyser)
```

## Stack

- Python 3.10+
- `requests` — HTTP calls (day 4, day 7)
- `pandas` — data analysis (day 5)
- `numpy` — matrix ops for ML layer (day 6)

Install all at once:

```bash
pip install requests pandas numpy
```
