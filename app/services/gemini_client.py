from google import genai
from app.core.config import settings

class GeminiClient:
    def __init__(self):
        api_key : str = settings.GEMINI_API_KEY
        model = settings.GEMINI_MODEL

        if not api_key:
            raise ValueError(  
                "Missing GEMINI_API_KEY"
            )
        
        self.client = genai.Client(api_key=api_key)
        self.model = model

        self.context = "Optimize the following prompt by refining clarity and " \
        "effectiveness while preserving its original intent and essence. " \
        "Avoid adding unnecessary detail or complexity, focus on making it " \
        "concise, natural, and well-structured without changing the core meaning. The optimized prompt must be 100 words or fewer."

    def generateOptimisedPrompt(self,prompt : str) -> str: 
        
        # SENDS PROMPT TO GEMINI TO BE OPTIMISED

        response = self.client.app.models.generate_content(
            model = self.model,
            contents = self.context + f"\n PROMPT:{prompt}" 
        )

        return response.text

        

        
