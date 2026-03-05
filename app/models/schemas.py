from pydantic import BaseModel
from typing import List, Optional

class ImagePair(BaseModel):
    id: Optional[int] = None
    compliance_id: str
    original_url: str
    edited_url: str
    property_id: Optional[int] = None

class Property(BaseModel):
    id: Optional[int] = None
    address: str
    unit_number: Optional[str] = None
    city: str
    state: str
    zip_code: str
    images: List[ImagePair] = []
