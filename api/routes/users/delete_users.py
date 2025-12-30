from services.supabase_client import SupabaseClient
from fastapi import HTTPException, APIRouter,status
from uuid import UUID  # Import the UUID type

client = SupabaseClient()

router = APIRouter()

@router.delete('/users/{user_id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id : UUID):
    try:
        result = client.delete(
            table = 'users',
            pk_id=user_id
        )

        if not result or len(result) == 0:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail=f'User with user id:{user_id} could not be found'
            ) 
        return

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error deleting user id : {str(e)}'
        )