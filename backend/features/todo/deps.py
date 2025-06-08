from typing import Annotated

from fastapi import Depends
from shared.database import db_manager
from sqlalchemy.ext.asyncio import AsyncSession

from .service import TodoService


def get_todo_service(
    session: Annotated[AsyncSession, Depends(db_manager.get_session)],
) -> TodoService:
    return TodoService(session=session)
