from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "Application Running"}


def test_create_employee():
    payload = {
        "id": 1,
        "name": "Alice",
        "department": "Platform Engineering",
    }

    response = client.post("/employees", json=payload)

    assert response.status_code == 200
