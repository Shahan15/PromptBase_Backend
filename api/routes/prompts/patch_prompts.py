from services.supabase_client import SupabaseClient
from fastapi import HTTPException, APIRouter,status
from models.prompts import PromptUpdateSchema
from uuid import UUID  

client = SupabaseClient()

router = APIRouter()


@router.patch('/prompts/{prompt_id}', status_code=status.HTTP_200_OK)
def update_prompt(prompt_id: UUID, promptUpdate: PromptUpdateSchema):
    try:
        update_data = promptUpdate.model_dump(exclude_unset=True)

        if not update_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='No fields provided to update'
            )

        updates = client.update(
            table='prompts',
            filters={
                'id': prompt_id,
            },
            updates=update_data
        )

        if not updates:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'prompt with id : {prompt_id} could not be found'
            )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error updating requested fields {str(e)}'
        )