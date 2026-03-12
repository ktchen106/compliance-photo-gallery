from fastapi import APIRouter, HTTPException
from app.models.schemas import ImagePair, Property
from typing import List

router = APIRouter()

# Mock database
properties_db = [
    Property(id="prop1", address="123 Compliance St", images=[])
]

@router.get("/properties", response_model=List[Property])
def get_properties():
    """GET /properties: How the browser 'asks' for data."""
    return properties_db

@router.get("/properties/{property_id}", response_model=Property)
def get_property(property_id: str):
    """GET /properties/{id}: How the browser 'asks' for specific data."""
    for p in properties_db:
        if p.id == property_id:
            return p
    raise HTTPException(status_code=404, detail="Property not found")

@router.post("/properties", response_model=Property)
def create_property(property: Property):
    """POST /properties: How we 'send' new data to the server."""
    properties_db.append(property)
    return property

@router.post("/properties/{property_id}/upload-pair")
def upload_image_pair(property_id: str, image_pair: ImagePair):
    for p in properties_db:
        if p.id == property_id:
            p.images.append(image_pair)
            return {"compliance_id": image_pair.compliance_id}
    raise HTTPException(status_code=404, detail="Property not found")
