import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello World!" in response.data


def test_contact(client):
    response = client.get("/contact")
    assert response.status_code == 200
    assert b"info@my-project.nl" in response.data
