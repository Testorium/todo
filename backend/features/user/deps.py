from typing import Annotated

from fastapi import Depends
from shared.database import db_manager
from sqlalchemy.ext.asyncio import AsyncSession

from .model import User
from .service import UserService


def get_user_service(
    session: Annotated[AsyncSession, Depends(db_manager.get_session)],
) -> UserService:
    return UserService(session=session)
