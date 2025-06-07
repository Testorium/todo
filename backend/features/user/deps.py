from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi import status as status_code
from fastapi.security import APIKeyCookie
from jwt import DecodeError
from shared.database import db_manager
from shared.settings import cookie_config
from sqlalchemy.ext.asyncio import AsyncSession

from .model import User
from .service import UserService

auth_cookie_schema = APIKeyCookie(name=cookie_config.key)


import jwt
from shared.settings import jwt_config


def get_user_service(
    session: Annotated[AsyncSession, Depends(db_manager.get_session)],
) -> UserService:
    return UserService(session=session)


async def get_current_user(
    auth_cookie: Annotated[str, Depends(auth_cookie_schema)],
    user_service: Annotated[UserService, Depends(get_user_service)],
) -> User:
    try:
        payload = jwt.decode(
            jwt=auth_cookie,
            key=jwt_config.secret_key,
            algorithms=[jwt_config.algorithm],
        )
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status_code.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized",
            )

    except DecodeError:
        raise HTTPException(
            status_code=status_code.HTTP_400_BAD_REQUEST,
            detail="Cannot decode token",
        )

    user = await user_service.get_user_by_id(user_id=user_id)

    if not user:
        raise HTTPException(
            status_code=status_code.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

    return user
