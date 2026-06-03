import pytest
from app import app, add, subtract


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# --- Unit tests for business logic ---

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6

def test_subtract_negative():
    assert subtract(3, 5) == -2


# --- Integration tests for routes ---

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"

def test_add_route(client):
    response = client.get("/add/3/4")
    assert response.status_code == 200
    assert response.get_json()["result"] == 7

def test_subtract_route(client):
    response = client.get("/subtract/10/3")
    assert response.status_code == 200
    assert response.get_json()["result"] == 7
