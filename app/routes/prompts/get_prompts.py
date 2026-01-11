from fastapi import HTTPException, APIRouter,status
from app.services.supabase_client import SupabaseClient
from app.models.prompts import ResponsePrompt
from typing import List
from fastapi import Depends
from app.core.security import get_current_user

client = SupabaseClient()

router = APIRouter()

@router.get("/prompts", response_model=List[ResponsePrompt])
def get_prompts(user = Depends(get_current_user)):
    try:
        data = client.fetch(
            table='prompts',
            filters={"user_id" : user["id"]}
            )
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching prompts: {str(e)}"
        )
