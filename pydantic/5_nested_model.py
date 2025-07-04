from pydantic import BaseModel, Field
from typing import List, Optional, Annotated, Dict


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


class Patient(BaseModel):
    name: str
    age: int
    email: str
    address: Address
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]


address_dict = {
    "city": "New York",
    "state": "NY",
    "street": "123 Main St",
    "zip_code": "10001",
}
address1 = Address(**address_dict)

patient_dict = {
    "name": "John Doe",
    "age": 30,
    "email": "sahil@gmail.com",
    "address": address1,
}
patient = Patient(**patient_dict)
print(patient)

json_data = patient.model_dump_json(indent=2, exclude_none=True)
print(json_data)
