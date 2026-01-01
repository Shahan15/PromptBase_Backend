from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class RequestPrompt(BaseModel):
    original_prompt: str
    is_private: bool
    tags: str
    user_id: UUID


class ResponsePrompt(BaseModel):
    id: UUID
    created_at: datetime
    original_prompt: str
    optimised_prompt: str
    is_private: bool
    tags: str
    user_id: UUID

class PromptGenerationRequest(BaseModel):
    user_id: Optional[str] = None 
    original_prompt: str
    is_private: Optional[bool] = True
    tags: Optional[str] = ""

class PromptGenerationResponse(BaseModel):
    id: str 
    created_at: datetime
    original_prompt: str
    optimised_prompt: str
    user_id: Optional[str] = None
    is_private: bool
    tags: Optional[str] = ""


class PromptUpdateSchema(BaseModel):
    is_private: Optional[bool] = None
    tags: Optional[str] = None

