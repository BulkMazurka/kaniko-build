import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_content(client):
    response = client.get('/')
    assert b"An error occurred" not in response.data

