from app.services.supabase_client import SupabaseClient
from fastapi import HTTPException, APIRouter,status
from app.models.favourites import ResponseFavourites
from typing import List
from fastapi import Depends
from app.core.security import get_current_user

router = APIRouter()
client = SupabaseClient()

@router.get('/favourites',response_model=List[ResponseFavourites])
def get_favourites(user = Depends(get_current_user)):
    try:
        data = client.fetch('favourites',filters={"user_id" : user["id"]})
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error fetching favourites: {str(e)}")