from pydantic import BaseModel, Field, EmailStr, computed_field
from typing import Optional, Annotated, List, Dict


class Patient(BaseModel):
    name: str
    weight: float
    height: float
    email: Optional[EmailStr] = None

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi


patient_info = {
    "name": "Sahil",
    "weight": 70.0,
    "height": 1.75,
    "email": "sahil@gmail.com",
}
patient = Patient(**patient_info)
print(patient)
