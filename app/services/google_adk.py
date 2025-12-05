import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GoogleADKService:
    """
    Service wrapper for Google Agent Developer Kit / Generative AI.
    Acts as a fallback or alternative agent runtime.
    """
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            print("Warning: GOOGLE_API_KEY is not set. Google ADK features may not work.")
        else:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')

    def generate_content(self, prompt: str) -> str:
        if not self.api_key:
            return "Google API Key missing."
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error calling Google ADK/Gemini: {e}")
            return "Error processing request with Google ADK."

google_adk_service = GoogleADKService()
