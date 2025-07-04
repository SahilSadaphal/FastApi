from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel, computed_field, Field
from typing import Optional, Annotated, Dict, List, Any
from http_methods import load_data
import json

app = FastAPI()


class DataModel(BaseModel):
    patient_id: str
    name: str
    city: str
    age: int
    gender: str
    height: float
    weight: float

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height**2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi > 30:
            return "Obese"
        else:
            return "Underweight"


# Utility function to save data
def save_data(request: DataModel) -> str:
    data = load_data()
    if request.patient_id in data:
        raise HTTPException(status_code=400, detail="Patient ID Already Exists")
    data[request.patient_id] = request.model_dump(exclude={"patient_id"})
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=2)
    return "Data Saved Successfully"


@app.post("/upload")
def upload(data_to_save: DataModel) -> Dict[str, Any]:
    """
    Uploads data to the JSON file.
    """
    return {"Message": save_data(data_to_save)}


# data_to_save = {
#     "patient_id": "P0011123",
#     "name": "Sahil Sadaphal",
#     "city": "Mumbai",
#     "age": 22,
#     "gender": "Male",
#     "height": 1.75,
#     "weight": 70.0,
# }
# data_to_save = DataModel(**data_to_save)
# print(upload(data_to_save))
