from pydantic import BaseModel, Field
from typing import List, Optional

class ImagePair(BaseModel):
    id: Optional[int] = None
    compliance_id: str
    original_url: str
    edited_url: str
    property_id: Optional[int] = None
    ai_confidence_score: Optional[float] = Field(default=None, le=1.0, description="Confidence score from 0.0 to 1.0")

class Property(BaseModel):
    id: Optional[int] = None
    address: str
    unit_number: Optional[str] = None
    city: str
    state: str
    zip_code: str
    images: List[ImagePair] = []
