from fastapi import HTTPException, APIRouter, status
from app.services.supabase_client import SupabaseClient
from app.models.users import UserCreate, ResponseUser
from app.core.security import hash_password

client = SupabaseClient()

router = APIRouter()

@router.post("/register", response_model=ResponseUser, status_code=status.HTTP_201_CREATED)
def create_user(new_user: UserCreate):
    existing_user = client.fetch(
        table='users',
        filters={"email" : new_user.email}
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    
    try:
        password_to_hash = new_user.password.strip()
        user_data = new_user.model_dump()
        user_data["password"] = hash_password(str(password_to_hash))
        created_user = client.insert(table="users", data=user_data)
        return created_user[0]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )
