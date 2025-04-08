from typing import Dict, Union
from pydantic import BaseModel

class FixedRate(BaseModel):
    rate: float
    currency: str

class TimeAndMaterial(BaseModel):
    hourly_rate: float
    currency: str
    estimated_hours: Optional[float] = None

class BillingService:
    def __init__(self):
        self.billing_options: Dict[str, Union[FixedRate, TimeAndMaterial]] = {}

    def toggle_billing_option(self, project_id: str, option_type: str, data: dict):
        if option_type == 'fixed_rate':
            self.billing_options[project_id] = FixedRate(**data)
        elif option_type == 'time_and_material':
            self.billing_options[project_id] = TimeAndMaterial(**data)

    def save_billing_option(self, project_id: str, option: Union[FixedRate, TimeAndMaterial]):
        self.billing_options[project_id] = option

    def update_billing_option(self, project_id: str, data: dict):
        if project_id in self.billing_options:
            option = self.billing_options[project_id]
            for key, value in data.items():
                setattr(option, key, value)

    def retrieve_billing_option(self, project_id: str) -> Union[FixedRate, TimeAndMaterial, None]:
        return self.billing_options.get(project_id)