from app.agents.travel_agent import travel_agent
from app.agents.itinerary_agent import itinerary_agent
from app.agents.weather_agent import weather_agent
from app.agents.transport_agent import transport_agent
from app.agents.culture_agent import culture_agent
from app.agents.booking_agent import booking_agent

class Orchestrator:
    def __init__(self):
        self.travel = travel_agent
        self.itinerary = itinerary_agent
        self.weather = weather_agent
        self.transport = transport_agent
        self.culture = culture_agent
        self.booking = booking_agent

    def plan_trip(self, user_request: dict):
        """
        Orchestrates a full trip planning flow.
        user_request: {
            "destination": "Bali",
            "days": 3,
            "interests": ["culture", "beach"],
            "budget": "5 million IDR",
            "travelers": 2
        }
        """
        # 1. Get Weather Context
        # Using default Bali coords
        weather = self.weather.get_weather(-8.4095, 115.1889) 
        
        # 2. Get Recommendations if specific places not mentioned
        recommendations = self.travel.recommend_places(
            category="general", 
            location=user_request.get('destination', 'Bali'), 
            preferences=", ".join(user_request.get('interests', []))
        )
        
        # 3. Generate Itinerary
        itinerary = self.itinerary.generate_itinerary(
            location=user_request.get('destination', 'Bali'),
            days=user_request.get('days', 3),
            interests=user_request.get('interests', []),
            budget=user_request.get('budget', 'moderate')
        )
        
        # 4. Compile Response
        return {
            "weather_warning": "Check rain forecast" if weather.get('precipitation', 0) > 0 else "Weather looks good",
            "recommendations": recommendations,
            "itinerary": itinerary,
            "status": "Success"
        }

    def ask_culture(self, question: str):
        return self.culture.get_cultural_info(question)

    def check_transport(self, start, end):
        return self.transport.get_route(start, end)

orchestrator = Orchestrator()
