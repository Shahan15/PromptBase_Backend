from fastapi import HTTPException, APIRouter
from app.services.supabase_client import SupabaseClient
from app.models.prompts import ResponsePrompt
from typing import List

client = SupabaseClient()

router = APIRouter()

@router.get("/prompts", response_model=List[ResponsePrompt])
def get_prompts():
    try:
        data = client.fetch('prompts')
        print(f"THE DATA IS: {data}")
        return data
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching prompts: {str(e)}"
        )
