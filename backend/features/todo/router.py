from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi import status as status_code
from features.todo.deps import get_todo_service
from features.todo.schemas import TodoCreate, TodoRead, TodoUpdate
from features.todo.service import TodoService
from features.user.deps import get_current_user
from features.user.model import User
from shared.settings import api_prefix_config

router = APIRouter(prefix=api_prefix_config.v1.todos, tags=["Todo"])

from shared.exceptions import DatabaseError, NotFoundError


@router.post("/", response_model=TodoRead)
async def create_new_todo(
    data: TodoCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    todo_service: Annotated[TodoService, Depends(get_todo_service)],
):
    try:
        todo = await todo_service.create_todo(data, current_user.id)

    except DatabaseError as e:
        raise HTTPException(
            status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )

    return todo


@router.get("/", response_model=List[TodoRead])
async def get_all_user_todos(
    current_user: Annotated[User, Depends(get_current_user)],
    todo_service: Annotated[TodoService, Depends(get_todo_service)],
    is_completed: bool | None = None,
):
    try:
        todos = await todo_service.get_all_user_todos(current_user.id, is_completed)

    except DatabaseError as e:
        raise HTTPException(
            status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )

    return todos


@router.delete("/{todo_id}", status_code=status_code.HTTP_204_NO_CONTENT)
async def delete_todo(
    todo_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    todo_service: Annotated[TodoService, Depends(get_todo_service)],
):
    try:
        todo = await todo_service.delete_todo_by_id(todo_id, current_user.id)

    except NotFoundError as e:
        raise HTTPException(status_code=status_code.HTTP_404_NOT_FOUND, detail=str(e))

    except DatabaseError as e:
        raise HTTPException(
            status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.patch("/{todo_id}", response_model=TodoRead)
async def update_todo(
    todo_id: int,
    data: TodoUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    todo_service: Annotated[TodoService, Depends(get_todo_service)],
):
    try:
        todo = await todo_service.update_todo_by_id(data, todo_id, current_user.id)

    except NotFoundError as e:
        raise HTTPException(status_code=status_code.HTTP_404_NOT_FOUND, detail=str(e))

    except DatabaseError as e:
        raise HTTPException(
            status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )

    return todo
