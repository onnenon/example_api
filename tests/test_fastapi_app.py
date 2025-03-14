import pytest
from fastapi import testclient


@pytest.fixture
def client():
    from book_api.fastapi_app import app

    return testclient.TestClient(app)


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
