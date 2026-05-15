from app.services import add_employee, get_employees


def test_add_employee():
    employee = {"id": 1, "name": "John", "department": "DevOps"}

    add_employee(employee)

    employees = get_employees()

    assert len(employees) > 0
