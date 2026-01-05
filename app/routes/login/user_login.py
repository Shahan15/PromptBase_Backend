from fastapi import APIRouter,HTTPException,status
from app.services.supabase_client import SupabaseClient
from app.core.jwt_handler import create_JWT_Token
from app.core.security import verify_password
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends


router = APIRouter()
supabaseClient = SupabaseClient()


@router.post('/login')
# Use OAuth2PasswordRequestForm instead of LoginRequest
async def login(data: OAuth2PasswordRequestForm = Depends()):
    # Note: Swagger puts the 'email' into the 'username' field 
    filters_to_use = {
        "email": data.username 
    }

    user = supabaseClient.fetch(
        table='users',
        filters=filters_to_use
    )

    if not user or len(user) == 0:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    user = user[0]
    
    # Check the password
    if not verify_password(data.password, user['password']):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials"
        )
    
    token = create_JWT_Token(user_id=str(user['id']))
    
    return {"access_token": token, "token_type": "bearer"}