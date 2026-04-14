from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from auth import TokenData, create_jwt_token, decode_jwt_token
import hash_pass

in_memory_db_users = [
    {
        "username": "hi",
        "password": "$2b$12$h34IdHSTuC1xDZRtgwsppuvdonF3CAw4fkvz8JDzWyM.mnLkT7xte",  # "hi124"
    },
    {
        "username": "myhawky",
        "password": "$2b$12$6M.aBFZ8.LQpICiiuAGBAu27/xkniOMTkcDE2OesZTCSC6wb9LvmC",  # "hi124Super"
    },
]

app = FastAPI()


@app.post("/token")
async def login_for_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> dict:
    username = form_data.username
    # check if the user is already in the database
    for u in in_memory_db_users:
        if u["username"] == username:
            # check if the password matches the one in the database
            authenticated = hash_pass.verify_password(form_data.password, u["password"])
            if authenticated:
                token = create_jwt_token({"username": username})
                return {"access_token": token, "token_type": "bearer"}

    raise HTTPException(status_code=401, detail="Invalid username or password")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
    user = decode_jwt_token(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user


@app.get("/user/me")
async def get_my_username(user: Annotated[TokenData, Depends(get_user)]):
    return user
