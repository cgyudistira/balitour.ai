import requests
import os
from dotenv import load_dotenv

load_dotenv()

class TransportAgent:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTE_API_KEY")
        self.base_url = "https://api.openrouteservice.org/v2/directions"

    def get_route(self, start_coords: tuple, end_coords: tuple, profile: str = "driving-car"):
        """
        profile: driving-car, driving-hgv, cycling-regular, cycling-road, cycling-mountain, 
                 cycling-electric, foot-walking, foot-hiking, wheelchair
        """
        if not self.api_key:
            return {"status": "Error", "message": "API Key missing"}

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json'
        }
        
        body = {
            "coordinates": [start_coords, end_coords]
        }
        
        url = f"{self.base_url}/{profile}"
        
        try:
            response = requests.post(url, json=body, headers=headers)
            if response.status_code == 200:
                data = response.json()
                # Basic parsing
                summary = data['routes'][0]['summary']
                return {
                    "distance_km": round(summary['distance'] / 1000, 2),
                    "duration_min": round(summary['duration'] / 60, 0),
                    "profile": profile,
                    "status": "Success"
                }
            else:
                return {"status": "Error", "code": response.status_code, "message": response.text}
        except Exception as e:
             return {"status": "Error", "message": str(e)}

    def recommend_transport(self, distance_km: float, travelers: int):
        if travelers == 1 and distance_km < 10:
            return "Gojek/Grab Bike (Fastest)"
        elif travelers > 2 or distance_km > 20:
            return "Private Car Rental / Bluebird Taxi"
        elif distance_km < 2:
            return "Walking or Bicycle"
        else:
            return "Gojek/Grab Car"

transport_agent = TransportAgent()
