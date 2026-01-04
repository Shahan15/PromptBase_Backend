from app.services.supabase_client import SupabaseClient
from fastapi import HTTPException, APIRouter,status
from uuid import UUID  
from fastapi import Depends
from app.core.security import get_current_user

client = SupabaseClient()

router = APIRouter()

@router.delete('/users/me',status_code=status.HTTP_204_NO_CONTENT)
def delete_user(current_user = Depends(get_current_user)):
    try:
        result = client.delete(
            table = 'users',
            pk_id = str(current_user['id'])
        )

        if not result or len(result) == 0:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail=f'User with user id:{current_user["id"]} could not be found'
            ) 
        return

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error deleting user id : {str(e)}'
        )