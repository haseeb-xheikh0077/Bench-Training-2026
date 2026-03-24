
Exercise 1 fetches a GitHub user profile and their top 5 repos by stars.
Exercise 2 fetches live weather for any city by chaining two API calls together.

Commands:
python3 exercise_1.py <github-username>
python3 exercise_2.py <city-name>
python3 exercise_2.py New York   (multi-word cities work too)

Example output - Exercise 1:
========================================
  GitHub Profile: torvalds
========================================
  Bio        : No bio provided
  Public Repos: 11
  Followers   : 292412

  Top 5 Repos by Stars:
  ------------------------------------
  ⭐ 224819  linux  [C]
  ⭐  4298  AudioNoise  [C]
  ⭐  1945  uemacs  [C]
  ⭐  1838  GuitarPedal  [C]
  ⭐   958  test-tlb  [C]
========================================

Example output - Exercise 2:
========================================
  Weather in London
========================================
  Conditions  : Overcast
  Temperature : 13.6°C  /  56.5°F
  Wind Speed  : 23.0 km/h
========================================

What was hard:

The hardest part was understanding the shape of the API response. When the API sends back data it is a deeply nested dict and you have to know exactly which key to dig into. For exercise 1 the repos came back as a list of dicts so i had to sort that list myself using sorted() with a lambda to pick the right key. For exercise 2 the weather API does not give a 404 if the city is wrong, it just returns an empty results list. So i had to check the data itself with if not results instead of relying on the status code. That was confusing at first because i expected a proper error from the server.

Also the weather API returns an integer code like 3 or 61 for the weather condition, not a readable string. I had to build a WEATHER_CODES dict myself to translate those numbers into something like "Overcast" or "Slight rain". That made me realize you always have to read the API docs carefully because the response is not always in the format you expect.

Why i used a shared fetch_json function:
Both exercises make multiple API calls. Instead of repeating the requests.get logic every time i put it in one function. That way error handling lives in one place and every other function just calls fetch_json and trusts it to either return data or raise a clear error.
