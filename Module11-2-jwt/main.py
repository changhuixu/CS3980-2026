from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from auth import create_jwt_token
import hash_pass

in_memory_db_users = [
    {"username": "hi", "password": ""},
    {"username": "myhawky", "password": ""},
]

app = FastAPI()


@app.post("/token")
async def login_for_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> str:
    username = form_data.username
    # check if the user is already in the database
    for u in in_memory_db_users:
        if u["username"] == username:
            # check if the password matches the one in the database
            authenticated = hash_pass.verify_password(form_data.password, u["password"])
            if authenticated:
                token = create_jwt_token({"username": username})
                return token

    raise HTTPException(status_code=401, detail="Invalid username or password")
