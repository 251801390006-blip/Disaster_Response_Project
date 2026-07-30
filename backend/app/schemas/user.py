
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    mobile_number: str

class UserCreate(UserBase):
    password: str
    role: str = "citizen"
    # Optional fields based on role
    address: Optional[str] = None
    ward: Optional[str] = None
    emergency_contact: Optional[str] = None
    family_size: Optional[str] = None
    organization: Optional[str] = None
    skills: Optional[str] = None
    availability: Optional[str] = None

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    mobile_number: Optional[str] = None
    address: Optional[str] = None
    ward: Optional[str] = None
    emergency_contact: Optional[str] = None
    family_size: Optional[str] = None

class UserResponse(UserBase):
    id: UUID
    role: str
    is_active: bool
    is_email_verified: bool
    is_phone_verified: bool
    address: Optional[str] = None
    organization: Optional[str] = None
    created_at: datetime
    
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: Optional[str] = None
    role: Optional[str] = None

