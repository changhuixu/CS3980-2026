from datetime import datetime, timedelta, timezone

import jwt
from pydantic import BaseModel

SECRET_KEY = "2fa57a4d22b0a5511993295f143fb9ff6878938711df8c7adc66e4ed17195b17"
ALGORITHM = "HS256"


class TokenData(BaseModel):
    username: str
    exp_datetime: datetime


def create_jwt_token(data: dict, expires_delta: timedelta = timedelta(minutes=20)):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    payload.update({"exp": expire})
    encoded = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return encoded


# a = create_jwt_token({"hawkid": "hawk", "email": "hawk@uiowa.edu"})
# print(a)


def decode_jwt_token(token: str) -> TokenData | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("username")
        exp: int = payload.get("exp")
        if username is None or exp is None:
            return None
        exp_datetime = datetime.fromtimestamp(exp)
        return TokenData(username=username, exp_datetime=exp_datetime)
    except jwt.InvalidTokenError:
        return None


# b = decode_jwt_token(a)
# print(b)
