from datetime import datetime

from beanie import Document

from pydantic import BaseModel, ConfigDict, EmailStr


class User(Document):
    email: EmailStr = ""
    role: str = "BasicUser"
    password: str = ""
    active: bool = True

    model_config = ConfigDict(
        json_schema_extra={
            "example": {"email": "python-web-dev@cs.uiowa.edu", "password": "strong!!!"}
        }
    )

    class Settings:
        name = "users"


class TokenResponse(BaseModel):
    username: str
    role: str
    token: str
    expiry: datetime


class UserDto(BaseModel):
    id: str
    email: EmailStr = ""
    role: str = "BasicUser"
    active: bool = True
