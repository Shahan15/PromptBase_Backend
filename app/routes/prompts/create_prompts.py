from fastapi import HTTPException, APIRouter, status
from app.services.supabase_client import SupabaseClient
from app.models.prompts import PromptGenerationRequest, PromptGenerationResponse
from app.services.gemini_client import GeminiClient

geminiClient = GeminiClient()
client = SupabaseClient()
router = APIRouter()

@router.post("/refine", response_model=PromptGenerationResponse, status_code=status.HTTP_201_CREATED)
def create_prompt(prompt: PromptGenerationRequest):
    # Takes in a prompt:
    # - Generates an optimised prompt using Gemini API
    # - Stores original and optimised prompt in Supabase 
    try:
        prompt_data = prompt.model_dump()
        optimised_prompt = geminiClient.generateOptimisedPrompt(prompt_data["original_prompt"])
        prompt_data["optimised_prompt"] = optimised_prompt
        created_prompt = client.insert(table='prompts', data=prompt_data)
        
        if not created_prompt:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error optimising prompt"
            ) 
        
        return PromptGenerationResponse(**created_prompt[0])
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating prompt: {str(e)}"
        )
