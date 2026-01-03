from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime



class RequestFavourites(BaseModel):
    original_prompt : str
    optimised_prompt : str


class ResponseFavourites(BaseModel):
    id: str
    created_at: datetime
    prompt_id: str
    user_id : str



class FavouritesUpdateSchema(BaseModel):
    prompt_id: Optional[str] = None

  
