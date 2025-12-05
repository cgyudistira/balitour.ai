# 🌺 BaliTour.AI – Agentic Platform for Smart Tourism in Bali

BaliTour.AI is an intelligent multi-agent tourism platform that provides personalized trip planning, real-time recommendations, cultural guidance, and automated booking for tourists in Bali. Built using Google ADK + Groq for ultra-fast agentic orchestration.

---

## 🚀 Key Features
- **AI Trip Planner** – Generates personalized itineraries based on budget, interests, and travel days.
- **Real-Time Adaptation** – Updates plans based on weather, traffic, local events.
- **Cultural Expert Agent** – Explains Balinese traditions, temples, ceremonies, and etiquette.
- **Booking Agent** – Manages hotel/villa availability and connects to local transport vendors.
- **Local Business Agent** – Recommends spas, restaurants, UMKM products, and experiences.
- **Emergency Agent** – Provides nearby hospital, police, and safety alerts.

---

## 🧠 Multi-Agent Architecture
BaliTour.AI uses 7 specialized agents:
1. **Travel Concierge Agent**
2. **Bali Culture Expert Agent**
3. **Hotel & Villa Booking Agent**
4. **Transport Agent**
5. **Event & Activity Agent**
6. **Local Business Agent**
7. **Emergency & Safety Agent**

Orchestrated via ADK with high-speed inference from Groq LLMs (Llama 3.1 / Gemma 2).

---

## 🏗️ Tech Stack
- **Python**
- **FastAPI**
- **Google ADK (Agentic Development Kit)**
- **Groq API (LLM Execution)**
- **ChromaDB / LanceDB (RAG)**
- **PostgreSQL / MongoDB**
- **Weather API, Maps API, Local Dataset**

---

## 📦 Project Structure
bali-tour-ai/
│── agents/
│ ├── concierge_agent.py
│ ├── culture_agent.py
│ ├── booking_agent.py
│ ├── transport_agent.py
│ ├── event_agent.py
│ ├── local_business_agent.py
│ └── emergency_agent.py
│
│── rag/
│ ├── culture_documents/
│ └── loader.py
│
│── api/
│ └── main.py
│
│── models/
│── tools/
│── config/
│── README.md

yaml
Copy code

---

## 🔗 APIs & Tools
- Weather forecast  
- Google Maps routing  
- Event listings  
- Local villa availability  
- RAG for cultural knowledge  

---

## 🧪 Example Query
**User:**  
*"Create a 3-day itinerary in Bali. I like culture, beaches, and local food. Budget 5 million IDR."*

**AI Output:**  
A full agent-generated itinerary with budget breakdown, routes, booking options, and cultural notes.

---

## 💼 Use Cases
- Tourism boards  
- Hotels & villa operators  
- Travel agencies  
- Local transport providers  
- Tourists seeking personalized travel planning  

---

## 📝 License
MIT License

---

## 🤝 Contribution
Pull requests are welcome!  
Contact: **</cgyudistira>**
