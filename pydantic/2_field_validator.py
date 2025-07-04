from pydantic import BaseModel, EmailStr, Field, AnyUrl, field_validator
from typing import Optional, Annotated, List, Dict


class Patient(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    married: Annotated[bool, Field(default=True)]
    contacts: Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domain = ["hdfc.com", "icici.com"]
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domain:
            raise ValueError(
                f"Invalid domain name: {domain_name}. Allowed domains are {valid_domain}"
            )
        return value

    @field_validator("name")
    @classmethod
    def name_validator(cls, value):
        return value.upper()


patient_info = {
    "name": "Sahil",
    "email": "sahil@hdfc.com",
    "contacts": {"phone1": "1234567890", "phone2": "0987654321"},
    "allergies": ["pollen", "dust"],
    "married": True,
}

p_data = Patient(**patient_info)
print(p_data)

import json

json_data = p_data.model_dump_json(indent=2, exclude_none=True)
# json_data = p_data.model_dump_json(indent=2, exclude_unset=True)
print(json_data)
