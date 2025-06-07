from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi import status as status_code
from features.user.deps import get_current_user, get_user_service
from features.user.model import User
from features.user.schemas import UserCreate, UserCredentials
from features.user.service import UserService
from shared.exceptions.auth import IncorrectPassword
from shared.exceptions.database import AlreadyExistsError, DatabaseError, NotFoundError
from shared.settings import api_prefix_config, cookie_config

router = APIRouter(prefix=api_prefix_config.v1.auth, tags=["Auth"])


# /login
@router.post("/login", status_code=status_code.HTTP_200_OK)
async def login_user(
    response: Response,
    data: UserCredentials,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    try:
        token = await user_service.authenticate_user(data)

    except NotFoundError as e:
        raise HTTPException(status_code=status_code.HTTP_404_NOT_FOUND, detail=str(e))

    except IncorrectPassword as e:
        raise HTTPException(status_code=status_code.HTTP_400_BAD_REQUEST, detail=str(e))

    response.set_cookie(
        key=cookie_config.key,
        max_age=cookie_config.max_age,
        value=token,
        samesite=cookie_config.samesite,
        httponly=cookie_config.httponly,
        secure=cookie_config.secure,
    )


# /logout
@router.post("/logout", status_code=status_code.HTTP_200_OK)
async def logout_user(
    response: Response,
    current_user: Annotated[User, Depends(get_current_user)],
):
    response.delete_cookie(
        key=cookie_config.key,
        httponly=cookie_config.httponly,
        secure=cookie_config.secure,
        samesite=cookie_config.samesite,
    )


# /register
@router.post("/register", status_code=status_code.HTTP_201_CREATED)
async def create_new_user(
    data: UserCreate,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    try:
        new_user = await user_service.create_user(data)

    except AlreadyExistsError as e:
        raise HTTPException(status_code=status_code.HTTP_400_BAD_REQUEST, detail=str(e))

    except DatabaseError as e:
        raise HTTPException(
            status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
