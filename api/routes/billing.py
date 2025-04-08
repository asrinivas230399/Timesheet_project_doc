from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, ValidationError
from typing import Dict, Union

# Assuming BillingService and the models are imported from their respective modules
from billing_service import BillingService, FixedRate, TimeAndMaterial

router = APIRouter()
billing_service = BillingService()

class BillingOption(BaseModel):
    option_type: str
    data: dict

# Dependency to validate project_id
async def validate_project_id(project_id: str):
    if not project_id.isalnum():
        raise HTTPException(status_code=400, detail="Invalid project ID")
    return project_id

@router.get("/billing/{project_id}", response_model=Union[FixedRate, TimeAndMaterial, None])
async def get_billing_option(project_id: str = Depends(validate_project_id)):
    option = billing_service.retrieve_billing_option(project_id)
    if option is None:
        raise HTTPException(status_code=404, detail="Billing option not found")
    return option

@router.post("/billing/{project_id}")
async def set_billing_option(project_id: str = Depends(validate_project_id), billing_option: BillingOption = Depends()):
    try:
        billing_option = BillingOption(**billing_option.dict())
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

    if billing_option.option_type not in ['fixed_rate', 'time_and_material']:
        raise HTTPException(status_code=400, detail="Invalid billing option type")
    billing_service.toggle_billing_option(project_id, billing_option.option_type, billing_option.data)
    return {"message": "Billing option set successfully"}