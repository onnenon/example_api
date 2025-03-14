import pytest

from book_api.flask_app import create_app


@pytest.fixture()
def flask_app():
    app = create_app()
    app.config["TESTING"] = True
    yield app


@pytest.fixture()
def flask_client(flask_app):
    return flask_app.test_client()


def test_flask_app_health_check(flask_client):
    """Test the health check endpoint."""

    response = flask_client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
