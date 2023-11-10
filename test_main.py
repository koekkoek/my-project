import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello World!" in response.data


def test_contact(client):
    response = client.get("/contact")
    assert response.status_code == 200
    assert "info@my-project.nl" in response.data
