import requests
import os
from dotenv import load_dotenv

load_dotenv()

class BookingAgent:
    def __init__(self):
        self.api_key = os.getenv("TRAVELPAYOUTS_API_KEY")
        self.base_url = "https://api.travelpayouts.com/v1"

    def search_hotels(self, location: str, check_in: str, check_out: str, adults: int = 2):
        # Mocking for now as Travelpayouts specifically needs location IDs/IATA codes which is complex to resolve without a helper
        # Real implementation would call /v1/prices/cheap or relevant hotel endpoint
        if not self.api_key:
            return {"status": "Error", "message": "API Key missing"}

        # Placeholder integration
        return {
            "status": "Success",
            "message": f"Found 5 hotels in {location} for {check_in} to {check_out} (Mock Data)",
            "results": [
                {"name": "Bali Paradise Hotel", "price": 500000, "stars": 4},
                {"name": "Kuta Beach Resort", "price": 350000, "stars": 3},
                {"name": "Ubud Zen Villa", "price": 1200000, "stars": 5}
            ]
        }

    def search_flights(self, origin: str, destination: str, date: str):
        # Placeholder
        return {
            "status": "Success", 
            "results": [
                {"airline": "Garuda Indonesia", "price": 1500000, "time": "10:00"},
                {"airline": "AirAsia", "price": 800000, "time": "14:00"}
            ]
        }

booking_agent = BookingAgent()
