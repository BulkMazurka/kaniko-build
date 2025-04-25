import pytest
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

@patch('app.requests.get')
def test_home_status_code(mock_get, client):
    mock_get.return_value.text = "1.2.3.4"
    response = client.get('/')
    assert response.status_code == 200

@patch('app.requests.get')
def test_home_content(mock_get, client):
    mock_get.return_value.text = "1.2.3.4"
    response = client.get('/')
    assert b"An error occurred" not in response.data

