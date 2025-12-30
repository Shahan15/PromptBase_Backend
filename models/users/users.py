from pydantic import BaseModel,EmailStr
from typing import Optional
from uuid import UUID


class ResponseUser(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: EmailStr


class RequestUser(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class UserUpdateSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
