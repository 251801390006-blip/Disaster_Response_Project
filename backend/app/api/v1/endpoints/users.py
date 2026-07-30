
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.user import UserResponse, UserUpdate
from app.models.user import User
import uuid

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    # Returns current user
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        full_name="Mock User",
        mobile_number="1234567890",
        role=current_user.role,
        is_active=current_user.is_active,
        is_email_verified=True,
        is_phone_verified=True,
        created_at="2023-10-01T00:00:00Z"
    )

@router.put("/me", response_model=UserResponse)
def update_user_me(
    user_in: UserUpdate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    # Update profile
    pass

