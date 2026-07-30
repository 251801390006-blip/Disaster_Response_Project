
import uuid
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer, Float, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from geoalchemy2 import Geometry
from app.db.base_class import Base

class Shelter(Base):
    __tablename__ = "shelters"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True, nullable=False)
    code = Column(String, unique=True, index=True, nullable=False)
    type = Column(String, nullable=False)
    ward_number = Column(String, index=True, nullable=False)
    zone = Column(String, index=True, nullable=False)
    address = Column(Text, nullable=False)
    
    location = Column(Geometry("POINT"), nullable=True) # PostGIS mapped Long/Lat
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    
    contact_person = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    emergency_contact = Column(String, nullable=False)
    
    max_capacity = Column(Integer, nullable=False, default=0)
    current_occupancy = Column(Integer, nullable=False, default=0)
    
    status = Column(String, default="Open", nullable=False) # Open, Closed, Maintenance, Emergency Only, Full
    description = Column(Text, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    
    facilities = relationship("ShelterFacility", back_populates="shelter", uselist=False)
    images = relationship("ShelterImage", back_populates="shelter")

class ShelterFacility(Base):
    __tablename__ = "shelter_facilities"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    shelter_id = Column(UUID(as_uuid=True), ForeignKey("shelters.id"), nullable=False, unique=True)
    
    electricity = Column(Boolean, default=False)
    generator = Column(Boolean, default=False)
    water = Column(Boolean, default=False)
    kitchen = Column(Boolean, default=False)
    medical_room = Column(Boolean, default=False)
    toilets = Column(Integer, default=0)
    women_toilets = Column(Integer, default=0)
    child_area = Column(Boolean, default=False)
    disabled_access = Column(Boolean, default=False)
    beds = Column(Integer, default=0)
    blankets = Column(Integer, default=0)
    charging_points = Column(Integer, default=0)
    solar = Column(Boolean, default=False)
    parking = Column(Boolean, default=False)
    pet_friendly = Column(Boolean, default=False)
    
    shelter = relationship("Shelter", back_populates="facilities")

class ShelterImage(Base):
    __tablename__ = "shelter_images"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    shelter_id = Column(UUID(as_uuid=True), ForeignKey("shelters.id"), nullable=False)
    url = Column(String, nullable=False)
    public_id = Column(String, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    shelter = relationship("Shelter", back_populates="images")

class ShelterCapacityHistory(Base):
    __tablename__ = "shelter_capacity_history"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    shelter_id = Column(UUID(as_uuid=True), ForeignKey("shelters.id"), nullable=False)
    previous_occupancy = Column(Integer, nullable=False)
    new_occupancy = Column(Integer, nullable=False)
    updated_by = Column(UUID(as_uuid=True), nullable=True) # Optional audit
    created_at = Column(DateTime(timezone=True), server_default=func.now())

