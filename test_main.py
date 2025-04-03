from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_fibonacci():
    response = client.get("/fibonacci/10")
    assert response.status_code == 200
    assert response.json() == {"nth_fibonacci": 55}

def test_fibonacci_zero():
    response = client.get("/fibonacci/0")
    assert response.status_code == 200
    assert response.json() == {"nth_fibonacci": 0}

def test_fibonacci_negative():
    response = client.get("/fibonacci/-5")
    assert response.status_code == 200
    assert response.json() == {"error": "N должно быть неотрицательным числом"}
