def test_flask_app_health_check(flask_client):
    """Test the health check endpoint."""

    response = flask_client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
