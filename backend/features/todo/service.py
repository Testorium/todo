from typing import TYPE_CHECKING, List

from sqlalchemy import select

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

from shared.exceptions import AlreadyExistsError, DatabaseError, NotFoundError

from .model import Todo
from .schemas import TodoCreate, TodoUpdate


class TodoService:
    def __init__(self, session: "AsyncSession"):
        self._session = session

    async def create_todo(self, todo_data: TodoCreate, user_id: int) -> Todo:
        new_todo = Todo(**todo_data.model_dump(), user_id=user_id)

        try:
            self._session.add(new_todo)
            await self._session.commit()
            await self._session.refresh(new_todo)

        except Exception:
            await self._session.rollback()
            raise DatabaseError("Failed to create new todo.")

        return new_todo

    async def get_todo_by_id_and_user(self, todo_id: int, user_id: int) -> Todo | None:
        statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)

        try:
            result = await self._session.execute(statement)
            todo = result.scalar_one_or_none()

        except Exception as e:
            # logger.exception("Failed to retrieve todo.")
            raise DatabaseError("Failed to retrieve todo.")

        if not todo:
            raise NotFoundError("User not found.")

        return todo

    async def delete_todo_by_id(self, todo_id: int, user_id: int) -> None:
        todo = await self.get_todo_by_id_and_user(todo_id, user_id)
        try:
            await self._session.delete(todo)
            await self._session.commit()

        except Exception as e:
            # logger.exception("Failed to delete todo.")
            raise DatabaseError("Failed to delete todo.")

    async def update_todo_by_id(
        self, new_data: TodoUpdate, todo_id: int, user_id: int
    ) -> Todo:
        todo = await self.get_todo_by_id_and_user(todo_id, user_id)

        values = new_data.model_dump(exclude_none=True, exclude_unset=True)

        for key, value in values.items():
            setattr(todo, key, value)

        try:
            await self._session.commit()
            await self._session.refresh(todo)
            return todo

        except Exception as e:
            # logger.exception("Failed to update todo.")
            raise DatabaseError("Failed to update todo.")

    async def get_all_user_todos(
        self, user_id: int, is_completed: bool | None
    ) -> List[Todo]:
        statement = select(Todo).where(Todo.user_id == user_id)

        if is_completed:
            statement = statement.where(Todo.is_completed == is_completed)

        try:
            result = await self._session.execute(statement)
            todos = result.scalars().all()

        except Exception as e:
            # logger.exception("Failed to retrieve todos.")
            raise DatabaseError("Failed to retrieve todos.")

        return todos
