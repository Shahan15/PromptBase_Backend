from fastapi import HTTPException, APIRouter
from services.supabase_client import SupabaseClient
from models.users import ResponseUser
from typing import List


client = SupabaseClient()

router = APIRouter()


@router.get("/users",response_model=List[ResponseUser])
def get_users():
    try:
        data = client.fetch('users')
        return data
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching users: {str(e)}")
