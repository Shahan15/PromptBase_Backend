from services.supabase_client import SupabaseClient
from fastapi import HTTPException, APIRouter,status
from models.favourites import ResponseFavourites
from typing import List

router = APIRouter()
client = SupabaseClient()

@router.get('/favourites',response_model=List[ResponseFavourites])
def get_favourites():
    try:
        data = client.fetch('favourites')
        print(data)
        return data
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching favourites: {str(e)}")