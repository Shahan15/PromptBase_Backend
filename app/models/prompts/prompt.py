from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class RequestPrompt(BaseModel):
    original_prompt: str
    is_private: bool
    tags: str
    user_id: str


class ResponsePrompt(BaseModel):
    id: UUID
    created_at: datetime
    original_prompt: str
    optimised_prompt: str
    is_private: bool
    tags: str
    user_id: str



class PromptUpdateSchema(BaseModel):
    is_private: Optional[bool] = None
    tags: Optional[str] = None

