from fastapi import HTTPException, APIRouter, status
from services.gemini_client import GeminiClient
from models.gemini import RequestPrompt
from typing import List



client = GeminiClient()
router = APIRouter()

@router.post('/prompts/optimise', response_model=List[RequestPrompt],status_code=status.HTTP_201_CREATED)
def optimise_prompt(prompt : RequestPrompt):
    try:
        optimise_prompt = client.generateOptimisedPrompt(
            prompt= prompt
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

        




