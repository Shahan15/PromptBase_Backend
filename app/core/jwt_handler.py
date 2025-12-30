import jwt
from .config import settings
from datetime import datetime,timedelta,timezone
from fastapi import HTTPException,status

def create_JWT_Token(user_id : str) -> str:

    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_EXPIRES_MINUTES)

    payload = {
        "sub" : user_id,
        "exp" : expire
    }
    
    return jwt.encode(payload, settings.JWT_SECRET,algorithm=settings.JWT_ALGORITHM)

def decode_JWT_token(token : str) -> str:
    try:
        payload = jwt.decode(
            token, 
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
            leeway=10
            )
        
        return payload["sub"]

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expire. Please log in again"
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid Security credentials'
        )
        

    
    