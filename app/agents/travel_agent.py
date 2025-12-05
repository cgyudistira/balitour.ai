from app.services.chromadb_service import chroma_service
from app.services.groq_service import groq_service

class TravelAgent:
    def __init__(self):
        self.chroma = chroma_service
        self.llm = groq_service
        self.system_prompt = """
        You are the 'Bali Travel Recommendation Agent'.
        Suggest destinations based on user preferences.
        """

    def recommend_places(self, category: str, location: str, preferences: str):
        query = f"{category} in {location} for {preferences}"
        
        # 1. RAG Retrieval
        results = self.chroma.query(query, n_results=5)
        context = ""
        if results['documents']:
            context = "\n".join(results['documents'][0])

        # 2. LLM Recommendation
        prompt = f"""
        Context (Available places):
        {context}

        User Request: Recommend 3 {category} spots in {location} for someone who likes {preferences}.
        Provide name, short description, and why it fits.
        """
        
        response = self.llm.generate_response(prompt, system_prompt=self.system_prompt)
        return response

travel_agent = TravelAgent()
