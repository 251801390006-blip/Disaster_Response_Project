
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import uuid

from app.api import deps
from app.schemas.shelter import ShelterCreate, ShelterUpdate, ShelterResponse, ShelterOccupancyUpdate, ShelterImageSchema
from app.core.cloudinary_config import upload_image, delete_image
# from app.crud import crud_shelter # Mocking CRUD for now

router = APIRouter()

# Mock Dependency for allowed roles
def officer_or_admin(user = Depends(deps.RoleChecker(["officer", "admin"]))):
    return user

@router.post("/", response_model=ShelterResponse, status_code=status.HTTP_201_CREATED)
def create_shelter(
    shelter_in: ShelterCreate,
    db: Session = Depends(deps.get_db),
    current_user = Depends(officer_or_admin)
):
    # Mock return
    return ShelterResponse(
        id=uuid.uuid4(),
        **shelter_in.dict(),
        current_occupancy=0,
        available_capacity=shelter_in.max_capacity,
        occupancy_percentage=0.0,
        created_at="2023-10-01T00:00:00Z"
    )

@router.get("/", response_model=List[ShelterResponse])
def read_shelters(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = None,
    ward: Optional[str] = None,
    zone: Optional[str] = None,
    status: Optional[str] = None
):
    # Returns empty list for mock
    return []

@router.get("/{id}", response_model=ShelterResponse)
def read_shelter(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db)
):
    raise HTTPException(status_code=404, detail="Shelter not found (Mock)")

@router.put("/{id}", response_model=ShelterResponse)
def update_shelter(
    id: uuid.UUID,
    shelter_in: ShelterUpdate,
    db: Session = Depends(deps.get_db),
    current_user = Depends(officer_or_admin)
):
    raise HTTPException(status_code=404, detail="Shelter not found (Mock)")

@router.put("/{id}/occupancy", response_model=ShelterResponse)
def update_occupancy(
    id: uuid.UUID,
    occupancy_in: ShelterOccupancyUpdate,
    db: Session = Depends(deps.get_db),
    current_user = Depends(officer_or_admin)
):
    # Validate against max_capacity in actual implementation
    raise HTTPException(status_code=404, detail="Shelter not found (Mock)")

@router.delete("/{id}")
def delete_shelter(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
    current_user = Depends(officer_or_admin)
):
    return {"message": "Shelter soft deleted successfully"}

@router.post("/{id}/images", response_model=ShelterImageSchema)
def upload_shelter_image(
    id: uuid.UUID,
    file: UploadFile = File(...),
    db: Session = Depends(deps.get_db),
    current_user = Depends(officer_or_admin)
):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    url = upload_image(file.file)
    return ShelterImageSchema(id=uuid.uuid4(), url=url)

