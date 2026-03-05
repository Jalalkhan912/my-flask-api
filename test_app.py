import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"

def test_greet(client):
    res = client.get("/greet/World")
    assert res.status_code == 200
    assert "Hello, World!" in res.get_json()["message"]