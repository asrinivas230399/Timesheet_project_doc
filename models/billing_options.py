from pydantic import BaseModel
from typing import Optional

class FixedRate(BaseModel):
    rate: float
    currency: str

class TimeAndMaterial(BaseModel):
    hourly_rate: float
    currency: str
    estimated_hours: Optional[float] = None
