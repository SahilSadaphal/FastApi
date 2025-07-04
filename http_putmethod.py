from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional, Dict
import json
from http_postmethod import DataModel

app = FastAPI()


class Patient_Update_Model(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[str], Field(default=None)]
    gender: Annotated[Optional[str], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None)]
    weight: Annotated[Optional[float], Field(default=None)]
    # bmi: Annotated[Optional[str], Field(default=None)]
    # verdict: Annotated[Optional[str], Field(default=None)]


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


def save(data):
    with open("patients.json", "w") as f:
        json.dump(data, f)


@app.put("/update/{patient_id}")
def update_data(
    patient_id: str = Path(..., description="ID of the patient to update"),
    Patient_update: Patient_Update_Model = ...,
) -> Dict[str, str]:
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient ID not found")

    existing_data = data[patient_id]
    data_to_update = Patient_update.model_dump(exclude_unset=True)

    for key, value in data_to_update.items():
        existing_data[key] = value

    existing_data["patient_id"] = patient_id
    patient_pyobj = DataModel(**existing_data)
    data[patient_id] = patient_pyobj.model_dump(exclude={"patient_id"})

    save(data)
    return {"message": "Data saved"}


# @app.put("/update/{patient_id}")
# def update_data(patient_id, Patient_update: Patient_Update_Model) -> Dict[str:str]:
#     data = load_data()
#     if patient_id not in data[patient_id]:
#         raise HTTPException(status_code=404, detail="Patient Id not found")
#     existing_data = data[patient_id]
#     data_to_update = Patient_update.model_dump(exclude_unset=True)
#     for key, value in data_to_update:
#         existing_data[key] = value
#     existing_data["patient_id"] = patient_id
#     patient_pyobj = DataModel(**existing_data)
#     data_to_update = patient_pyobj.model_dump(exclude=["patient_id"])
#     data[patient_id] = data_to_update
#     save(data)
#     return {"message": "data saved"}
