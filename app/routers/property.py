from fastapi import APIRouter, HTTPException
from app.models.schemas import ImagePair

router = APIRouter()

@router.post("/properties/{property_id}/upload-pair")
def upload_image_pair(property_id: str, image_pair: ImagePair):
    # In a real app, we would save this to a database or storage
    # and perform compliance checks.
    # For now, we return the compliance_id from the input as requested.
    return {"compliance_id": image_pair.compliance_id}
