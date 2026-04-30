from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
import pytest
from main import app

client = TestClient(app)


def test_home():
    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


@pytest.mark.anyio
async def test_home_async():
    # Act
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test.com"
    ) as ac:
        response = await ac.get("/async")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World Async"}
