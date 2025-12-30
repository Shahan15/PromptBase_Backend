from fastapi import HTTPException, APIRouter, status
from services.supabase_client import SupabaseClient
from models.favourites import RequestFavourites, ResponseFavourites
from typing import List

client = SupabaseClient()

router = APIRouter()

# CREATING ONE FAVOURITE
@router.post("/favourites", response_model=List[ResponseFavourites], status_code=status.HTTP_201_CREATED)
def create_favourites(favourite: List[RequestFavourites]):
    # **fav unpacks dictionary which is returned by created_favourites into keyword arugments e.g. id : "abc"
    try:
        favourite_data = [fav.model_dump() for fav in favourite]
        created_favourites = client.insert(table='favourites', data=favourite_data)
        return [ResponseFavourites(**fav) for fav in created_favourites]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating favourite: {str(e)}"
        )
