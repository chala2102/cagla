import requests
import json
import time

eu_capitals = [
    {"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738},
    {"city": "Brussels", "country": "Belgium", "lat": 50.8503, "lon": 4.3517},
    # ... add all other capitals
]

base_url = "https://api.open-meteo.com/v1/forecast"
weather_data = {}

for city_info in eu_capitals:
    city = city_info["city"]
    lat = city_info["lat"]
    lon = city_info["lon"]

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m,precipitation_probability,weathercode"
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Map weather code to readable description (example)
        weather_code_map = {
            0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast"
            # extend with other codes if needed
        }

        current = data.get("current_weather", {})
        current_weather = {
            "temperature": current.get("temperature"),
            "windspeed": current.get("windspeed"),
            "weathercode": current.get("weathercode"),
            "condition": weather_code_map.get(current.get("weathercode"), "Unknown"),
            "time": current.get("time")
        }

        # Hourly forecast
        hourly_data = data.get("hourly", {})
        hourly_forecast = []
        if hourly_data:
            hours = hourly_data.get("time", [])
            temps = hourly_data.get("temperature_2m", [])
            precip = hourly_data.get("precipitation_probability", [])
            codes = hourly_data.get("weathercode", [])

            for i in range(len(hours)):
                hourly_forecast.append({
                    "time": hours[i],
                    "temperature": temps[i],
                    "precipitation_probability": precip[i],
                    "weathercode": codes[i]
                })

        # Store city data
        weather_data[city] = {
            "country": city_info["country"],
            "coordinates": {"latitude": lat, "longitude": lon},
            "current_weather": current_weather,
            "hourly_forecast": hourly_forecast
        }

        print(f"{city} data collected.")

    except requests.exceptions.RequestException as e:
        print(f"Error collecting data for {city}: {e}")

    time.sleep(0.5)  # respect API rate limits

# Save to JSON
with open("eu_weather_data.json", "w", encoding="utf-8") as f:
    json.dump(weather_data, f, ensure_ascii=False, indent=4)

print("All data saved to eu_weather_data.json")