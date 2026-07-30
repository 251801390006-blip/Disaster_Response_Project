
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
from uuid import UUID

class FacilityBase(BaseModel):
    electricity: bool = False
    generator: bool = False
    water: bool = False
    kitchen: bool = False
    medical_room: bool = False
    toilets: int = 0
    women_toilets: int = 0
    child_area: bool = False
    disabled_access: bool = False
    beds: int = 0
    blankets: int = 0
    charging_points: int = 0
    solar: bool = False
    parking: bool = False
    pet_friendly: bool = False

class ShelterImageSchema(BaseModel):
    id: UUID
    url: str
    
    class Config:
        orm_mode = True

class ShelterBase(BaseModel):
    name: str
    code: str
    type: str
    ward_number: str
    zone: str
    address: str
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    contact_person: str
    contact_number: str
    emergency_contact: str
    max_capacity: int = Field(..., ge=1)
    status: str = "Open"
    description: Optional[str] = None

class ShelterCreate(ShelterBase):
    facilities: Optional[FacilityBase] = None

class ShelterUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    contact_person: Optional[str] = None
    contact_number: Optional[str] = None
    emergency_contact: Optional[str] = None
    max_capacity: Optional[int] = Field(None, ge=1)
    status: Optional[str] = None
    description: Optional[str] = None
    facilities: Optional[FacilityBase] = None

class ShelterOccupancyUpdate(BaseModel):
    current_occupancy: int = Field(..., ge=0)

class ShelterResponse(ShelterBase):
    id: UUID
    current_occupancy: int
    available_capacity: int
    occupancy_percentage: float
    facilities: Optional[FacilityBase]
    images: List[ShelterImageSchema] = []
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        orm_mode = True

    @validator("available_capacity", always=True)
    def calculate_available(cls, v, values):
        return max(0, values.get("max_capacity", 0) - values.get("current_occupancy", 0))

    @validator("occupancy_percentage", always=True)
    def calculate_percentage(cls, v, values):
        max_cap = values.get("max_capacity", 1)
        occ = values.get("current_occupancy", 0)
        if max_cap == 0: return 0.0
        return round((occ / max_cap) * 100, 2)

