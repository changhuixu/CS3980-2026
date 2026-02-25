from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, status

from todo import Todo, TodoRequest


todo_router = APIRouter()

todo_list = []
global_id = 0


@todo_router.get("")
async def get_all_todos() -> list[Todo]:
    return todo_list


@todo_router.post("")
async def create_new_todo(todo: TodoRequest) -> Todo:
    global global_id  # important, so that this variable will have value and tracked for every request
    global_id += 1
    new_todo = Todo(id=global_id, title=todo.title, desc=todo.desc)
    todo_list.append(new_todo)
    return new_todo


@todo_router.get("/{id}")
async def get_todo_by_id(id: Annotated[int, Path(gt=0, le=1000)]) -> Todo:
    for todo in todo_list:
        if todo.id == id:
            return todo

    raise HTTPException(status_code=404, detail=f"Item with ID={id} is not found.")


@todo_router.delete("/{id}")
async def delete_todo_by_id(
    id: Annotated[
        int,
        Path(
            gt=0,
            le=1000,
            title="This is the ID for the desired Todo Item to be deleted",
        ),
    ],
) -> dict:
    for i in range(len(todo_list)):
        todo = todo_list[i]
        if todo.id == id:
            todo_list.pop(i)
            return {"msg": f"The todo with ID={id} is deleted."}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} is not found."
    )
