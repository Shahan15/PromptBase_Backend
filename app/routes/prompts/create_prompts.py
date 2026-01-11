from fastapi import HTTPException, APIRouter, status
from app.services.supabase_client import SupabaseClient
from app.models.prompts import PromptGenerationRequest
from app.services.gemini_client import GeminiClient
from fastapi import Depends
from app.core.security import get_current_user

geminiClient = GeminiClient()
client = SupabaseClient()
router = APIRouter()

@router.post("/refine", status_code=status.HTTP_201_CREATED)
def create_prompt(prompt: PromptGenerationRequest,user = Depends(get_current_user)):
    # Takes in a prompt:
    # - Generates an optimised prompt using Gemini API
    try:
        optimised_prompt = geminiClient.generateOptimisedPrompt(prompt.original_prompt)

        if not optimised_prompt:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error optimising prompt"
            ) 
        
        return {"original_prompt": prompt.original_prompt, "optimised_prompt": optimised_prompt}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating prompt: {str(e)}"
        )
