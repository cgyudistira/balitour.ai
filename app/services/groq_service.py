import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(override=True)
# Force reload for new keys

class GroqService:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY is not set in environment variables")
        self.client = Groq(api_key=self.api_key)
        self.model = "llama-3.3-70b-versatile"  # Updated to stable model

    def generate_response(self, prompt: str, system_prompt: str = "You are a helpful assistant.") -> str:
        print(f"[GroqService] Sending request... Prompt len: {len(prompt)}")
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model,
                temperature=0.7,
                max_tokens=1024,
                timeout=30.0 # Add explicit timeout
            )
            print("[GroqService] Response received.")
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"[GroqService] Error: {e}")
            return "Sorry, I encountered an error while processing your request."

groq_service = GroqService()
