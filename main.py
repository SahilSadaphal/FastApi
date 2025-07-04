from http_methods import get_pid

patient_id = "P100"
response = get_pid(patient_id)
print(
    response
)  # This will print the response from the FastAPI endpoint for the given patient
