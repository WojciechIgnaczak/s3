from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_verify():
    response = client.get("/verify")
    assert response.status_code == 200
    assert "signature" in response.json()
