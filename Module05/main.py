from typing import Annotated

from fastapi import FastAPI, Path


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
