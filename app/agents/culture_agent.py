from app.services.chromadb_service import chroma_service
from app.services.groq_service import groq_service

class CultureAgent:
    def __init__(self):
        self.chroma = chroma_service
        self.llm = groq_service
        self.system_prompt = """
        You are the 'Bali Culture Expert Agent'. 
        Your goal is to educate tourists about Balinese traditions, etiquette, ceremonies, and religion.
        Use the provided context to answer questions accurately. 
        If the context doesn't have the answer, use your general knowledge but mention that it's general info.
        Always be respectful and culturally sensitive.
        """

    def get_cultural_info(self, query: str):
        # 1. Retrieve relevant context from ChromaDB
        results = self.chroma.query(query, n_results=3)
        context = ""
        if results['documents']:
            context = "\n".join(results['documents'][0])

        # 2. Generate answer using Groq LLM
        prompt = f"""
        Context from knowledge base:
        {context}

        User Question: {query}
        
        Answer based on the context:
        """
        
        response = self.llm.generate_response(prompt, system_prompt=self.system_prompt)
        return response

    def get_etiquette_tips(self, location_type: str):
        # Specific helper for etiquette
        if "temple" in location_type.lower():
            return "Wear a sarong and sash. Do not enter if menstruating. Be respectful."
        return "Dress modestly and respect local customs."

culture_agent = CultureAgent()
