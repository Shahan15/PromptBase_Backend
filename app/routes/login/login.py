from fastapi import APIRouter,HTTPException,status
from app.services.supabase_client import SupabaseClient
from app.models.login import LoginRequest
from app.core.jwt_handler import create_JWT_Token

router = APIRouter()
supabaseClient = SupabaseClient()


@router.post('/login')
async def login(data : LoginRequest):
    filters_to_use = {
        "email" : data.email
    }

    user = supabaseClient.fetch(
        table='users',
        filters=filters_to_use
    )

    if not user or len(user) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=("User not found")
        )
    
    user = user[0]
    
    if user['password'] != data.password:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED("invalid Credentials")
    )
    

    return create_JWT_Token(user_id=str(user['id']))
