from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(
    prefix="/properties",
    tags=["properties"],
)

# Mock database
fake_properties_db = {}

# Pydantic Model
class Property(BaseModel):
    property_id: int
    name: str
    address: str
    is_compliant: Optional[bool] = None

@router.post("/", response_model=Property)
def create_property(prop: Property):
    if prop.property_id in fake_properties_db:
        raise HTTPException(status_code=400, detail="Property already exists")
    fake_properties_db[prop.property_id] = prop
    return prop

@router.get("/{property_id}", response_model=Property)
def read_property(property_id: int):
    if property_id not in fake_properties_db:
        raise HTTPException(status_code=404, detail="Property not found")
    return fake_properties_db[property_id]
