from fastapi import APIRouter, FastAPI, Response, status

from tesla_models import TeslaModel


app = FastAPI()

router = APIRouter(prefix="/tesla", tags=["Tesla"])
items_router = APIRouter(prefix="/items", tags=["Items"])


@app.get("/")
async def welcome() -> dict:
    return {"message": "hello"}


@items_router.get("/")
async def get_items() -> list[str]:
    return ["item1", "item2"]


@items_router.get("/")  # this API wins
async def get_items2() -> list[str]:
    return ["item3", "item4"]


@app.get("/users/me")
async def get_me() -> str:
    return "me"


@app.get("/users/me")  # the previous API is overwritten
async def get_me2() -> str:
    return "me2"


@app.get(
    "/users/{id}"
)  # if passing {id}="me", then the previous API will be matched first and return
async def get_by_id(id) -> str:
    return "here " + id


@items_router.get("/{id}")
async def get_item_by_id(id: int, response: Response) -> dict | None:
    if id == 1:
        return {"name": "item1"}
    if id == 2:
        return {"id": 2, "name": "item2"}
    else:
        response.status_code = status.HTTP_204_NO_CONTENT
        return None


@items_router.post("/")
async def add_new_item(new_item: str) -> list[str]:
    items = ["item1", "item2"]
    items.append(new_item)
    return items


add_new_item("hello")


@router.get("/{name}")
async def get_tesla_model(name: TeslaModel) -> str:
    if name is TeslaModel.model_x:
        return "price: 2000"
    if name is not TeslaModel.model_s:
        return "Model S: $30,000"
    return f"Model {name}, do you have budget?"


app.include_router(router)
app.include_router(items_router)
