from fastapi import FastAPI, Response, status


app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "hello"}


@app.get("/items")
async def get_items() -> list[str]:
    return ["item1", "item2"]


@app.get("/items")  # this API wins
async def get_items2() -> list[str]:
    return ["item3", "item4"]


@app.get("/items/{id}")
async def get_item_by_id(id: int, response: Response) -> dict | None:
    if id == 1:
        return {"name": "item1"}
    if id == 2:
        return {"id": 2, "name": "item2"}
    else:
        response.status_code = status.HTTP_204_NO_CONTENT
        return None


@app.post("/items")
async def add_new_item(new_item: str) -> list[str]:
    items = ["item1", "item2"]
    items.append(new_item)
    return items


add_new_item("hello")
