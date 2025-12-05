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

### 🖥️ User Interface

This project includes a modern **Streamlit** dashboard for easy interaction.

### 🌟 Key Features

* **Unified Chat Interface**: A single chat window to interact with all agents (Weather, Travel, Culture, etc.).
* **Smart Orchestrator**: The "Supervisor" agent intelligently routes queries or answers simple greetings directly (Fast Path).
* **Multi-lingual Support**: Chat in English, Indonesian, or Balinese.
* **Trip Settings**: Customize your travel style (Relaxed/Adventure) and budget directly from the sidebar.

<br>

<div align="center">

## 🛠️ Technical Stack

* **Frontend**: Streamlit (Premium UI with Custom CSS)
* **Backend**: FastAPI
* **Agent Framework**: Custom Orchestrator + Google ADK Concepts
* **LLM Engine**: Groq (Llama-3.3-70b-versatile) for ultra-fast inference
* **Knowledge**: ChromaDB (RAG) & Real-time APIs (Open-Meteo, OpenRoute, Travelpayouts)

</div>

## 🚦 Getting Started

### Prerequisites

* Python 3.10+
* API Keys (Groq, Google, OpenRoute, etc.)

### Installation

1. **Clone & Install**
   ```bash
   git clone https://github.com/your-repo/balitour.ai.git
   cd balitour.ai
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   Rename `.env.example` to `.env` and add your API credentials.
   ```bash
   GROQ_API_KEY=gsk_...
   ...
   ```

3. **Run the Application 🚀**
   You need two terminals for the full experience:

   **Terminal 1 (Backend API):**

   ```bash
   python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

   **Terminal 2 (Frontend UI):**

   ```bash
   python -m streamlit run streamlit_app.py
   ```

   Access the UI at: **http://localhost:8501**

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
  <sub>Built with ❤️ for Bali by &lt;/cgyudistira&gt;</sub>
</div>
