from pydantic import BaseModel
from typing import List, Optional

class ImagePair(BaseModel):
    original_url: str
    edited_url: str
    compliance_id: str

class Property(BaseModel):
    id: str
    address: str
    images: List[ImagePair] = []
