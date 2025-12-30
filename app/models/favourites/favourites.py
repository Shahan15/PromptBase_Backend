from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime



class RequestFavourites(BaseModel):
    prompt_id: str


class ResponseFavourites(BaseModel):
    id: UUID
    created_at: datetime
    prompt_id: str



class FavouritesUpdateSchema(BaseModel):
    prompt_id: Optional[str] = None

  
