from app.services.supabase_client import SupabaseClient
from fastapi import HTTPException, APIRouter,status
from uuid import UUID 

client = SupabaseClient()
router = APIRouter()

@router.delete('/favourites/{favourite_id}')
def delete_favourites(favourite_id : UUID):
    try:
        # fetch to find the associated prompt_id
        records = client.fetch(table='favourites', filters={'id': favourite_id})
        
        if not records:
            raise HTTPException(status_code=404, detail="Favourite not found")
            
        target_prompt_id = records[0].get('prompt_id')

        # 2. Delete the PROMPT
        client.delete(
            table='prompts',
            pk_id=target_prompt_id 
        )

        return {"message": "Success: Prompt and favourite removed"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))