from fastapi import APIRouter,HTTPException,status
from app.services.supabase_client import SupabaseClient
from app.models.login import LoginRequest
from app.core.jwt_handler import create_JWT_Token
from app.core.security import verify_password

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
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=("User not found")
        )
    
    user = user[0]
    
    verify_hash = verify_password(data.password,user['password'])
    if verify_hash == False:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED("invalid Credentials")
    )
    
    token = create_JWT_Token(user_id=str(user['id']))
    return {"access token": token,"token_type":"bearer"}
