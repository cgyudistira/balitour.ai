import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

class WeatherAgent:
    def __init__(self):
        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        self.openmeteo = openmeteo_requests.Client(session = retry_session)
        self.url = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, latitude: float, longitude: float):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": ["temperature_2m", "is_day", "precipitation", "rain", "showers", "weather_code", "wind_speed_10m"],
            "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "uv_index_max", "precipitation_sum"],
            "timezone": "Asia/Singapore" # Bali Time
        }
        try:
            responses = self.openmeteo.weather_api(self.url, params=params)
            response = responses[0]
            
            # Process current weather
            current = response.Current()
            current_temp = current.Variables(0).Value()
            is_day = current.Variables(1).Value()
            precipitation = current.Variables(2).Value()
            weather_code = current.Variables(5).Value()

            # Process daily
            daily = response.Daily()
            daily_weather_code = daily.Variables(0).ValuesAsNumpy()
            daily_temp_max = daily.Variables(1).ValuesAsNumpy()
            
            return {
                "current_temp": round(current_temp, 1),
                "is_day": int(is_day),
                "precipitation": round(precipitation, 1),
                "weather_code": int(weather_code),
                "daily_max": round(float(daily_temp_max[0]), 1) if len(daily_temp_max) > 0 else None,
                "status": "Success"
            }
        except Exception as e:
            return {"status": "Error", "message": str(e)}

    def get_marine_safety(self):
        # Placeholder for StormGlass integration
        # In a real scenario, we would call https://api.stormglass.io/v2/weather/point
        return {
            "wave_height": "Low (0.5m)",
            "flag_color": "Green",
            "advisory": "Safe for swimming and boating."
        }

weather_agent = WeatherAgent()
