from app.orchestrator import orchestrator
from app.agents.weather_agent import weather_agent
import time

def verify_system():
    print("--- Verifying BaliTour.AI Agents ---")

    # 1. Test Weather w/ Mock/Real call
    print("\n1. Testing Weather Agent...")
    try:
        weather = weather_agent.get_weather(-8.4095, 115.1889)
        print(f"Weather Result: {weather}")
    except Exception as e:
        print(f"Weather Agent Error: {e}")

    # 2. Test Orchestrator Plan Trip
    print("\n2. Testing Orchestrator Trip Planning...")
    request = {
        "destination": "Ubud",
        "days": 2,
        "interests": ["culture", "nature"],
        "budget": "high"
    }
    try:
        trip_result = orchestrator.plan_trip(request)
        print("Trip Plan Result Keys:", trip_result.keys())
    except Exception as e:
        print(f"Orchestrator Error: {e}")
    
    # 3. Test Culture Agent (via Orchestrator)
    print("\n3. Testing Culture Agent...")
    try:
        culture_ans = orchestrator.ask_culture("What is Nyepi?")
        print(f"Culture Answer: {culture_ans}")
    except Exception as e:
        print(f"Culture Agent Error: {e}")

    print("\n--- Verification Complete ---")

if __name__ == "__main__":
    verify_system()
