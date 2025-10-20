from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_long():
    payload = {"username": "admindsddsadjsadgasgdiadgjasdasgdasgdshadbadbsadga", "password": "admin"}
    resp = client.post("/login", json=payload)
    assert resp.status_code == 422 , "Длина username and password должна быть ограничена"
