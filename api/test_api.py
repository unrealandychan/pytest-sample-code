from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_service():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == "eddie"

def test_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == {1: "eddie", 2: "james", 3: "john"}

def test_create_users():
    response = client.post("/users",json={"id":4,"username":"jane"})
    assert response.status_code == 200
    assert response.json() == "jane"
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == {1: "eddie", 2: "james", 3: "john", 4: "jane"}