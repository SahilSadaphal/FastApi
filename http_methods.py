from fastapi import FastAPI, Path, HTTPException
from fastapi import Query
import json


app = FastAPI()


@app.get("/")
def read():
    return {"Message": "This api fetches data from a json file"}


@app.get("/data")
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
        return data


@app.get("/data/{patient_id}")
def get_pid(patient_id: str = Path(..., description="Patient ID to fetch data for")):
    data = load_data()
    data = data["Loaded_Data"]
    if patient_id in data:
        return {"Patient_ID": patient_id, "Data": data[patient_id]}
    else:
        return {
            "Error": HTTPException(status_code=404),
        }
