from app.services.groq_service import groq_service
from app.agents.weather_agent import weather_agent
from app.agents.transport_agent import transport_agent

class ItineraryAgent:
    def __init__(self):
        self.llm = groq_service
        self.weather = weather_agent
        self.transport = transport_agent
        self.system_prompt = """
        You are the 'BaliSmart Itinerary Agent'.
        Create detailed day-by-day itineraries.
        Consider weather and travel times provided in the context.
        """

    def generate_itinerary(self, location: str, days: int, interests: list, budget: str):
        # 1. Gather Context
        # Flatten interests list to string if needed
        interests_str = ", ".join(interests)
        
        # Get Weather Forecast (Mocking coords for Bali general or specific location logic needed)
        # Using Denpasar coords: -8.6705, 115.2126
        weather_info = self.weather.get_weather(-8.6705, 115.2126)
        
        # 2. Generate Itinerary Plan
        prompt = f"""
        Request: Create a {days}-day itinerary for {location}.
        Interests: {interests_str}
        Budget: {budget}
        
        Real-time Context:
        - Weather Forecast: {weather_info}
        
        Output format:
        Day 1:
        - Morning: [Activity]
        - Afternoon: [Activity]
        - Evening: [Activity]
        (Include travel tips and estimated costs)
        """
        
        response = self.llm.generate_response(prompt, system_prompt=self.system_prompt)
        return response

itinerary_agent = ItineraryAgent()
