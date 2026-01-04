from fastapi import HTTPException, APIRouter
from app.services.supabase_client import SupabaseClient
from app.models.users import ResponseUser
from typing import List
from fastapi import Depends
from app.core.security import get_current_user


client = SupabaseClient()

router = APIRouter()


@router.get("/users/me",response_model=List[ResponseUser])
def get_users(user = Depends(get_current_user)):
    try:
        data = client.fetch(table='users',filters={"id" : user['id']})
        return data
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching users: {str(e)}")
