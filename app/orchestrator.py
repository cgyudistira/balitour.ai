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

    def handle_chat(self, user_query: str):
        """
        Intelligent Supervisor that routes queries to appropriate agents.
        """
        from app.services.groq_service import groq_service
        
        # 1. Intent Classification via LLM
        print(f"[Orchestrator] Analyzying intent for: {user_query}")
        classification_prompt = f"""
        Analyze the user query: "{user_query}"
        
        Identify which agents are needed to answer. Return only a JSON list of agent names.
        Available agents:
        - "weather": for weather, rain, temperature, marine conditions.
        - "culture": for history, religion, etiquette, ceremonies.
        - "travel": for recommendations, places to go, things to do.
        - "itinerary": for planning a trip, day-by-day schedule.
        - "transport": for distance, route, traffic, how to get there.
        - "booking": for hotel prices, flights.
        - "general": for greetings, small talk, identity questions, or topics not covering the above.
        
        Example output: ["weather", "travel"] or ["general"]
        """
        
        try:
            intent_response = groq_service.generate_response(classification_prompt, system_prompt="You are a JSON classifier. Output only valid JSON.")
            print(f"[Orchestrator] Intent Raw Response: {intent_response}")
            # Clean up potential markdown formatting
            intent_response = intent_response.replace("```json", "").replace("```", "").strip()
            import json
            needed_agents = json.loads(intent_response)
            print(f"[Orchestrator] Identified Agents: {needed_agents}")
        except Exception as e:
            print(f"[Orchestrator] Intent Error: {e}")
            needed_agents = ["travel"] # Fallback

        context_results = {}
        
        # 2. Logic to Handle "General" or Empty intent efficiently
        if not needed_agents or "general" in needed_agents:
            # FAST PATH: Supervisor answers directly without calling sub-agents
            print("[Orchestrator] General intent detected. Supervisor answering directly.")
            direct_response = groq_service.generate_response(user_query, system_prompt="You are BaliTour.AI, a helpful and friendly AI assistant for Bali tourism. Answer the user directly.")
            return {
                "response": direct_response,
                "agents_used": ["supervisor"],
                "agent_data": {}
            }
        
        # 3. Parallel Agent Execution (Sequential for now)
        for agent in needed_agents:
            if agent == "general": continue 
            
            print(f"[Orchestrator] Calling Agent: {agent}")
            try:
                if agent == "weather":
                    # Default to Bali coords if no location extraction (Simplification)
                    context_results["weather"] = self.weather.get_weather(-8.4095, 115.1889)
                elif agent == "culture":
                    context_results["culture"] = self.culture.get_cultural_info(user_query)
                elif agent == "travel":
                    context_results["travel"] = self.travel.recommend_places("general", "Bali", user_query)
                elif agent == "itinerary":
                    # Basic extraction or default
                    context_results["itinerary"] = self.itinerary.generate_itinerary("Bali", 3, ["general"], "moderate")
                elif agent == "transport":
                     # Mock route for context if asked
                    context_results["transport"] = "Transport agent requires specific start/end points. Please use the Transport Tool for exact metrics."
                print(f"[Orchestrator] Agent {agent} finished.")
            except Exception as ae:
                print(f"[Orchestrator] Agent {agent} failed: {ae}")
                context_results[agent] = f"Error: {str(ae)}"

        # 3. Final Synthesis
        synthesis_prompt = f"""
        User Query: "{user_query}"
        
        Agent Reports:
        {json.dumps(context_results, indent=2)}
        
        Task: Synthesize a friendly, helpful response answering the user's query using the agent reports above.
        Mention which agents provided the info (e.g., "According to our Weather Agent...").
        IMPORTANT: Reply in the SAME LANGUAGE as the User Query (English, Indonesian, or Balinese).
        """
        
        final_answer = groq_service.generate_response(synthesis_prompt, system_prompt="You are BaliTour.AI, a helpful smart assistant.")
        
        return {
            "response": final_answer,
            "agents_used": needed_agents,
            "agent_data": context_results
        }


orchestrator = Orchestrator()
