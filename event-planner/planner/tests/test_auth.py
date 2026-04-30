import pytest
from httpx import AsyncClient

from auth import jwt_handler
from auth.hash_password import hash_password
from models.users import User


@pytest.mark.anyio
async def test_signup_creates_user(default_client: AsyncClient) -> None:
    payload = {"email": "test-user@example.com", "password": "strong-password"}
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = await default_client.post("/auth/signup", json=payload, headers=headers)

    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}

    db_user = await User.find_one(User.email == payload["email"])
    assert db_user is not None
    assert db_user.email == payload["email"]
    assert db_user.password != payload["password"]
    assert db_user.active is True


@pytest.mark.anyio
async def test_signup_returns_conflict_for_existing_user(
    default_client: AsyncClient,
) -> None:
    email = "existing-user@example.com"
    await User.insert_one(
        User(
            email=email,
            password=hash_password("secret-password").decode("utf-8"),
        )
    )

    payload = {"email": email, "password": "another-password"}
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    response = await default_client.post("/auth/signup", json=payload, headers=headers)

    assert response.status_code == 409
    assert response.json()["detail"] == "User with email provided exists already."


@pytest.mark.anyio
async def test_signin_returns_token_response(default_client: AsyncClient) -> None:
    email = "signin-user@example.com"
    password = "valid-password"
    await User.insert_one(
        User(
            email=email,
            password=hash_password(password).decode("utf-8"),
        )
    )

    data = {"username": email, "password": password}
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = await default_client.post("/auth/sign-in", data=data, headers=headers)

    assert response.status_code == 200

    body = response.json()
    assert body["username"] == email
    assert body["role"] == "BasicUser"
    assert isinstance(body["access_token"], str)
    assert "expiry" in body

    token_data = jwt_handler.verify_access_token(body["access_token"])
    assert token_data.username == email
    assert token_data.role == "BasicUser"


@pytest.mark.anyio
async def test_signin_rejects_invalid_password(default_client: AsyncClient) -> None:
    email = "wrong-password@example.com"
    await User.insert_one(
        User(
            email=email,
            password=hash_password("correct-password").decode("utf-8"),
        )
    )

    data = {"username": email, "password": "incorrect-password"}
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = await default_client.post("/auth/sign-in", data=data, headers=headers)

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid details passed."


@pytest.mark.anyio
async def test_signin_rejects_inactive_user(default_client: AsyncClient) -> None:
    email = "inactive-user@example.com"
    password = "inactive-password"
    await User.insert_one(
        User(
            email=email,
            password=hash_password(password).decode("utf-8"),
            active=False,
        )
    )

    data = {"username": email, "password": password}
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = await default_client.post("/auth/sign-in", data=data, headers=headers)

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid details passed."
