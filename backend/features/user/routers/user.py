from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi import status as status_code
from features.user.deps import get_current_user, get_user_service
from features.user.model import User
from features.user.schemas import UserRead, UserUpdate
from features.user.service import UserService
from shared.exceptions.database import DatabaseError, NotFoundError
from shared.settings import api_prefix_config

router = APIRouter(prefix=api_prefix_config.v1.users, tags=["Users"])


# GET /me
@router.get("/me", response_model=UserRead)
async def get_current_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user


# PATCH /me
@router.patch("/me", response_model=UserRead)
async def update_current_user(
    data: UserUpdate,
    user_service: Annotated[UserService, Depends(get_user_service)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    try:
        user = await user_service.update_user_by_id(
            new_data=data, user_id=current_user.id
        )

    except NotFoundError as e:
        raise HTTPException(status_code=status_code.HTTP_404_NOT_FOUND, detail=str(e))

    except DatabaseError as e:
        raise HTTPException(
            status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )

    return user
