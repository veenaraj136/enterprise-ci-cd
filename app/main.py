from fastapi import FastAPI
from app.models import Employee
from app.services import add_employee, get_employees

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "Application Running"}


@app.post("/employees")
def create_employee(employee: Employee):
    return add_employee(employee)


@app.get("/employees")
def fetch_employees():
    return get_employees()
