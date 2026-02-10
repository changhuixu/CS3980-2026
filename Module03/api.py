from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def welcome() -> dict:
    return {"message": "Hello world"}


@app.get("/hi")
async def welcome1() -> dict:
    return {"message": "hi world"}
