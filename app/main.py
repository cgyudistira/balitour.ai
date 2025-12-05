from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.orchestrator import orchestrator
from app.agents.weather_agent import weather_agent

app = FastAPI(title="BaliTour.AI", description="Agentic AI Platform for Bali Tourism", version="1.0.0")

# Request Models
class TripRequest(BaseModel):
    destination: str = "Bali"
    days: int = 3
    interests: List[str] = ["culture", "beach"]
    budget: str = "moderate"
    travelers: int = 2

class CultureQuery(BaseModel):
    question: str

class RouteRequest(BaseModel):
    start_coords: tuple
    end_coords: tuple
    profile: str = "driving-car"

class ChatRequest(BaseModel):
    query: str

# Endpoints

@app.post("/api/agent-chat")
async def agent_chat(request: ChatRequest):
    try:
        result = orchestrator.handle_chat(request.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to BaliTour.AI API. Visit /docs for more info."}

@app.post("/api/plan-trip")
async def plan_trip(request: TripRequest):
    try:
        result = orchestrator.plan_trip(request.model_dump())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/ask-culture")
async def ask_culture(query: CultureQuery):
    try:
        answer = orchestrator.ask_culture(query.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/weather")
async def get_weather(lat: float = -8.4095, long: float = 115.1889):
    try:
        return weather_agent.get_weather(lat, long)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/transport/route")
async def get_route(request: RouteRequest):
    try:
        result = orchestrator.check_transport(request.start_coords, request.end_coords)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
