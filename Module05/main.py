from typing import Annotated

from fastapi import APIRouter, FastAPI, HTTPException, Path
from fastapi.responses import PlainTextResponse

from todo_routes import todo_router

app = FastAPI(
    title="Todo Items App",
    summary="this is a summary",
    description="""
# Heading 1
test
## Heading 2

""",
    version="1.2.0",
    terms_of_service="MIT",
    contact={"name": "my name", "email": "dont-contact-me@uiowa.edu"},
)


@app.get("/items/{item_id}")
async def get_item_by_id(
    item_id: Annotated[int, Path(gt=0, le=1000, multiple_of=3)],
) -> dict:
    return {"item_id": item_id}


tesla_router = APIRouter()

app.include_router(tesla_router, tags=["Tesla"], prefix="/tesla")
app.include_router(todo_router, tags=["Todos", "Tesla"], prefix="/todos")


@app.exception_handler(HTTPException)
async def my_http_exception_handler(request, ex):
    return PlainTextResponse(str(ex.detail), status_code=ex.status_code)
