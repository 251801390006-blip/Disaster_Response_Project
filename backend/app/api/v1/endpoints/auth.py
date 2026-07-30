
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from app.core import security
from app.core.config import settings
from app.schemas.user import UserCreate, UserLogin, Token, UserResponse
from app.models.user import User
import uuid

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(
    user_in: UserCreate,
    db: Session = Depends(deps.get_db)
):
    # crud.user.get_by_email(db, email=user_in.email) check here
    # Mock return for now
    return UserResponse(
        id=uuid.uuid4(),
        email=user_in.email,
        full_name=user_in.full_name,
        mobile_number=user_in.mobile_number,
        role=user_in.role,
        is_active=True,
        is_email_verified=False,
        is_phone_verified=False,
        created_at="2023-10-01T00:00:00Z"
    )

@router.post("/login", response_model=Token)
def login_access_token(
    user_in: UserLogin,
    db: Session = Depends(deps.get_db)
):
    # user = crud.user.authenticate(db, email=user_in.email, password=user_in.password)
    # Mocking auth
    if user_in.email != "admin@test.com" or user_in.password != "password":
         raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        subject="mock_user_id", role="admin", expires_delta=access_token_expires
    )
    refresh_token = security.create_refresh_token(subject="mock_user_id")
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }

@router.post("/refresh", response_model=Token)
def refresh_token(refresh_token: str, db: Session = Depends(deps.get_db)):
    # Verify refresh token and issue new access token
    pass

