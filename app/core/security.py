from passlib.context import CryptContext
from app.core.jwt_handler import decode_JWT_token
from app.services.supabase_client import SupabaseClient
from fastapi import HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

supabaseClient = SupabaseClient()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# FUNCTIONS FOR HASHING AND VERIFYING PASSWORDS
def hash_password(password : str) -> str:
    return pwd_context.hash(password)

def verify_password(plain : str, hashed : str) -> bool:
    return pwd_context.verify(plain,hashed)


# CHECKING FOR CURRENT USER --> if token is 
def get_current_user(token : str = Depends(oauth2_scheme)):
    decoded_token = decode_JWT_token(token)

    if not decoded_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    current_user = supabaseClient.fetch(
        table='users',
        filters={"id" : decoded_token}
    )

    if len(current_user) == 0: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not find user in database"
        )
    
    return current_user[0]