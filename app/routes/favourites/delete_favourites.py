from app.services.supabase_client import SupabaseClient
from fastapi import HTTPException, APIRouter,status
from uuid import UUID 

client = SupabaseClient()
router = APIRouter()

@router.delete('/favourites/{favourite_id}')
def delete_favourites(favourite_id : UUID):
    try:
        result = client.delete(
            table = 'favourites',
            pk_id= favourite_id
        )

        if not result or len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Could not find favourite with favourite id : {favourite_id}'
            )
        return
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error deleting favourite: {str(e)}'
        )