from fastapi import HTTPException, APIRouter, status
from services.supabase_client import SupabaseClient
from models.users import RequestUser, ResponseUser

client = SupabaseClient()

router = APIRouter()

@router.post("/", response_model=ResponseUser, status_code=status.HTTP_201_CREATED)
def create_user(new_user: RequestUser):
    try:
        user_data = new_user.model_dump()
        created_user = client.insert(table="users", data=user_data)
        return created_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )
