import sys
import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL   = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Foggy", 48: "Icy fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
    80: "Slight showers", 81: "Moderate showers", 82: "Violent showers",
    95: "Thunderstorm", 96: "Thunderstorm with hail", 99: "Thunderstorm with heavy hail",
}


def fetch_json(url, params=None):
    """Make a GET request and return parsed JSON, or raise on error."""
    try:
        response = requests.get(url, params=params)
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Network error. Check your internet connection.")

    response.raise_for_status()
    return response.json()


def get_coordinates(city):
    """Return (name, latitude, longitude) for the first matching city."""
    data    = fetch_json(GEOCODING_URL, params={"name": city, "count": 1})
    results = data.get("results")
    if not results:
        raise ValueError(f"City '{city}' not found. Try a different spelling.")
    loc = results[0]
    return loc["name"], loc["latitude"], loc["longitude"]


def get_weather(lat, lon):
    """Fetch current weather for given coordinates."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m,weather_code",
        "temperature_unit": "celsius",
    }
    data = fetch_json(WEATHER_URL, params=params)
    return data["current"]


def celsius_to_fahrenheit(c):
    return round(c * 9 / 5 + 32, 1)


def print_weather(city, weather):
    """Display formatted weather output."""
    temp_c = weather["temperature_2m"]
    temp_f = celsius_to_fahrenheit(temp_c)
    wind   = weather["wind_speed_10m"]
    desc   = WEATHER_CODES.get(weather["weather_code"], "Unknown conditions")

    print(f"\n{'=' * 40}")
    print(f"  Weather in {city}")
    print(f"{'=' * 40}")
    print(f"  Conditions  : {desc}")
    print(f"  Temperature : {temp_c}°C  /  {temp_f}°F")
    print(f"  Wind Speed  : {wind} km/h")
    print(f"{'=' * 40}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 exercise_2.py <city-name>")
        sys.exit(1)

    city_input = " ".join(sys.argv[1:])  # supports multi-word names like "New York"

    try:
        city_name, lat, lon = get_coordinates(city_input)
        weather = get_weather(lat, lon)
        print_weather(city_name, weather)
    except (ValueError, ConnectionError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
