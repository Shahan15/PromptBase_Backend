from fastapi import HTTPException, APIRouter, status
from app.services.supabase_client import SupabaseClient
from app.models.favourites import RequestFavourites, ResponseFavourites
from fastapi import Depends
from app.core.security import get_current_user

client = SupabaseClient()
router = APIRouter()

# CREATING ONE FAVOURITE
@router.post("/favourites", response_model=ResponseFavourites, status_code=status.HTTP_201_CREATED)
def create_favourites(favourite: RequestFavourites,user = Depends(get_current_user)):
    # **fav unpacks dictionary which is returned by created_favourites into keyword arugments e.g. id : "abc"

    prompt_entry = {
        "original_prompt" : favourite.original_prompt,
        "optimised_prompt": favourite.optimised_prompt,
        "user_id" : user["id"]
    }

    try:
        #FIRST WE INSERT THE PROMPT INTO THE PROMPT TABLE
        created_prompt = client.insert(table="prompts",data=prompt_entry)

        if not created_prompt:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Failed to save Prompt text")

        favourite_data = favourite.model_dump() 
        new_prompt_id = created_prompt[0]["id"] 

        favourite_entry = {
            "prompt_id" : new_prompt_id,
            "user_id" : user["id"]
        }

        created_favourites = client.insert(table='favourites', data=favourite_entry)
        if created_favourites:
            result_data = created_favourites[0]
            result_data["original_prompt"] = favourite.original_prompt
            result_data["optimised_prompt"] = favourite.optimised_prompt

            return ResponseFavourites(**result_data)
            
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating favourite: {str(e)}"
        )
