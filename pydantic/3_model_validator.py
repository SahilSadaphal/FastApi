from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import Optional, Annotated, List, Dict


class Patient(BaseModel):
    name: str
    age: int
    email: Optional[EmailStr] = None
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    married: Annotated[bool, Field(default=True)]
    contact_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_email(cls, model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError(
                "Emergency contact is required for patients over 60 years old."
            )
        return model


patient_info = {
    "name": "Sahil",
    "age": 65,
    "email": "sahil@gmail.com",
    "contact_details": {"phone1": "1234567890", "emergency": "0987654321"},
    "allergies": ["pollen", "dust"],
    "married": True,
}


patient_data = Patient(**patient_info)
print(patient_data)
