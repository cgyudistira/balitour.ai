<div align="center">

# 🌺 BaliTour.AI

### Agentic AI Platform for Smart Tourism in Bali

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com/)
[![Google ADK](https://img.shields.io/badge/Google%20ADK-Agentic_Framework-4285F4?style=for-the-badge\&logo=google\&logoColor=white)](https://developers.google.com/agents)
[![Groq](https://img.shields.io/badge/Groq-LPU_Inference-orange?style=for-the-badge)](https://groq.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Database-purple?style=for-the-badge)](https://www.trychroma.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

*An intelligent multi-agent ecosystem designed to revolutionize the Bali tourism experience.*

[Features](#-key-features) • [Architecture](#-system-architecture) • [Getting Started](#-getting-started) • [Contributing](#-contributing)

</div>

***

## 📖 Project Overview

**BaliTour.AI** is a cutting-edge **Agentic AI Platform** that empowers tourists and local tourism operators in Bali. By leveraging a sophisticated multi-agent system, the platform provides hyper-personalized travel recommendations, dynamic itinerary generation, real-time environmental safety updates, and deep cultural insights.

Built on the **Google ADK (Agent Developer Kit)** and powered by **Groq's LPU** for ultra-low latency inference, BaliTour.AI ensures a seamless and responsive user experience. **ChromaDB** serves as the intelligent backbone, enabling RAG (Retrieval-Augmented Generation) for accurate, context-aware interactions.

***

## 🚀 Key Features

### 🌟 User-Facing Agents

| Agent | Functionality |
| :--- | :--- |
| **🌍 Travel Recommendation** | Suggests destinations based on location, category (cultural, culinary, nature), and user persona. Powered by RAG. |
| **📅 Itinerary Generator** | Creates smart 1-7 day itineraries considering weather, travel time, and operating hours. Supports family, clean luxury, & backpacker modes. |
| **🌦️ Weather & Marine** | Real-time safety updates via **Open-Meteo** (weather) and **StormGlass** (waves, UV index, wind). |
| **🚕 Transport Route** | Optimizes travel routes for motorbikes, cars, or walking using **OpenRouteService**. Recommends vetted transport options. |
| **🏨 Booking Assistant** | Aggregates prices and availability for hotels, flights, and tours via **Travelpayouts**. |
| **🎭 Cultural Guide** | Your personal guide to Balinese etiquette, temple ceremonies, and holidays like *Galungan* and *Nyepi*. |

### 🤖 Multi-Agent Collaboration

Our agents don't work in silos. They communicate to deliver a unified experience:

> *"The Weather Agent warns of high waves 🌊 → The Itinerary Agent reschedules the beach visit 🏖️ → The Cultural Agent suggests a nearby indoor temple ceremony instead 🕍."*

***

## 🛠️ Technical Stack

* **Core Framework**: Python 3.10+
* **Agent Architecture**: Google ADK (Agent Developer Kit)
* **Inference Engine**: Groq (Llama 3 / Mixtral models)
* **Knowledge Base**: ChromaDB (Vector Search / RAG)
* **API Interface**: FastAPI
* **External APIs**: Open-Meteo, StormGlass, OpenRouteService, Travelpayouts

***

## 📐 System Architecture

```mermaid
graph TD
    User[User / Client] -->|API Request| API[FastAPI Gateway]
    API --> Orch[Orchestrator Agent]
    
    subgraph "Agent Swarm (Google ADK)"
        Orch --> TA[Travel Agent]
        Orch --> IA[Itinerary Agent]
        Orch --> WA[Weather Agent]
        Orch --> TRA[Transport Agent]
        Orch --> CA[Cultural Agent]
    end
    
    TA <--> CDB[(ChromaDB Knowledge)]
    CA <--> CDB
    
    WA <-->|REST| WeatherAPI[Open-Meteo]
    WA <-->|REST| MarineAPI[StormGlass]
    TRA <-->|REST| RouteAPI[OpenRouteService]
    
    Orch -->|JSON Response| API
```

***

## 📂 Directory Structure

```text
bali-tour-ai/
├── app/
│   ├── main.py                 # FastAPI Entry Point
│   ├── orchestrator.py         # Main Agent Orchestrator
│   ├── agents/                 # Specialized Agent Definitions
│   │   ├── travel_agent.py
│   │   ├── itinerary_agent.py
│   │   ├── weather_agent.py
│   │   ├── transport_agent.py
│   │   ├── booking_agent.py
│   │   └── culture_agent.py
│   └── services/               # External Service Wrappers
│       ├── google_adk.py
│       ├── groq_service.py
│       └── chromadb_service.py
├── data/                       # Local Knowledge Base & Datasets
├── utils/                      # Helper Utilities
├── requirements.txt            # Project Dependencies
└── .env.example                # Configuration Template
```

***

## 🚦 Getting Started

### Prerequisites

* Python 3.10 or higher
* API Keys for Groq, Open-Meteo, etc.

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/balitour-ai.git
   cd balitour-ai
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   Copy the example environment file and fill in your keys.
   ```bash
   cp .env.example .env
   ```

5. **Run the Application**
   ```bash
   uvicorn app.main:app --reload
   ```

Visit `http://localhost:8000/docs` to interact with the API Swagger UI.

***

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

***

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

***

<div align="center">
  <sub>Built with ❤️ for Bali by </cgyudistira> </sub>
</div>
