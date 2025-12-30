from fastapi import HTTPException, APIRouter,status
from services.supabase_client import SupabaseClient
from uuid import UUID

client = SupabaseClient()

router = APIRouter()

@router.delete('/prompts/{prompt_id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_prompt(prompt_id : UUID):
    #Deletes prompt via its prompt id
    try: 
        result = client.delete(
            table = 'prompts',
            pk_id = prompt_id,
        )
    
        if not result or len(result) == 0: 
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Prompt with Prompt_id:{prompt_id} not found'
            )
        return
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error deleting Prompt : {str(e)}'
        )