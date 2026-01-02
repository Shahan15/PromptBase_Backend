from fastapi import HTTPException, APIRouter, status
from app.services.supabase_client import SupabaseClient
from app.models.favourites import RequestFavourites, ResponseFavourites
from typing import List

client = SupabaseClient()

router = APIRouter()

# CREATING ONE FAVOURITE
@router.post("/favourites", response_model=ResponseFavourites, status_code=status.HTTP_201_CREATED)
def create_favourites(favourite: RequestFavourites):
    # **fav unpacks dictionary which is returned by created_favourites into keyword arugments e.g. id : "abc"
    try:
        favourite_data = favourite.model_dump() 
        created_favourites = client.insert(table='favourites', data=favourite_data)
        if created_favourites and len(created_favourites) > 0:
            return ResponseFavourites(**created_favourites[0])
            
        raise HTTPException(status_code=500, detail="Failed to create favourite")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating favourite: {str(e)}"
        )
