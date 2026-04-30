from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"msg": "Hello World"}


@app.get("/async")
async def home_async():
    return {"msg": "Hello World Async"}
