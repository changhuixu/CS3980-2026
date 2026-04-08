from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI

from config import AppSettings


app = FastAPI()


@app.get("/")
async def home():
    settings = (
        AppSettings()
    )  # This constructor will trigger the code to read the .env file every time.
    return settings


@lru_cache
def get_settings():
    return AppSettings()


@app.get("/info")
async def info():
    return get_settings()


@app.get("/info-di")
async def info_dependency_injection(
    settings: Annotated[AppSettings, Depends(get_settings)],
):
    return {"admin_email": settings.admin_email}
