from fastapi import APIRouter, HTTPException, Path
from typing import Dict, Any
from ..models.schemas import ImagePair

router = APIRouter(
    prefix="/properties",
    tags=["properties"]
)

@router.post("/{property_id}/upload-pair")
async def upload_image_pair(
    image_pair: ImagePair,
    property_id: int = Path(..., description="The ID of the property")
) -> Dict[str, Any]:
    
    # Normally, you would save this to a database and generate a compliance_id here
    # For now, we will just echo back the received compliance_id, 
    # but the assignment mentions to "return a compliance_id", so we just make sure
    # we return it explicitly in a JSON response
    
    # You could also overwrite it with a newly generated one
    # import uuid
    # image_pair.compliance_id = str(uuid.uuid4())
    
    return {
        "message": "Image pair uploaded successfully",
        "property_id": property_id,
        "compliance_id": image_pair.compliance_id,
        "data": image_pair.model_dump()
    }
