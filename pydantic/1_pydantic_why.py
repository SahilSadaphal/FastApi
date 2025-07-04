from pydantic import BaseModel, EmailStr, Field, PositiveFloat
from typing import Optional, Annotated, List, Dict


class Patient(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    married: Annotated[bool, Field(default=None, description="Is the patient married?")]
    contact: Annotated[
        Optional[Dict[str, str]],
        Field(default=None, description="Contact details of the patient"),
    ]


patient_info = {
    "name": "Sahil",
    "email": "sahil@gmail.com",
    "contact": {"phone1": "1234567890", "phone2": "0987654321"},
    "allergies": ["pollen", "dust"],
}
patient = Patient(**patient_info)
print(patient)


def view(patient_info: Patient):
    print("Patient Information:")
    print(f"Name: {patient_info.name}")
    print(f"Email: {patient_info.email}")
    print(f"Allergies: {patient_info.allergies}")
    print(f"Married: {patient_info.married}")


view(patient)
