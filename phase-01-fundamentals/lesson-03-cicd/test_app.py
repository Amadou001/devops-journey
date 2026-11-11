from app import app

def test_home_returns_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_home_shows_environment():
    client = app.test_client()
    response = client.get("/")
    assert b"Running in:" in response.data