from typing import TYPE_CHECKING

from sqlalchemy import select

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

from shared.exceptions import (
    AlreadyExistsError,
    DatabaseError,
    IncorrectPassword,
    NotFoundError,
)
from shared.utils.hashing import hash_password, verify_password
from shared.utils.token import generate_token

from .model import User
from .schemas import UserCreate, UserCredentials, UserUpdate


class UserService:
    def __init__(self, session: "AsyncSession"):
        self._session = session

    async def authenticate_user(self, credentials: UserCredentials) -> str:
        user = await self.get_user_by_username(username=credentials.username)

        if not user:
            raise NotFoundError("User not found.")

        if not verify_password(
            password=credentials.password,
            hashed_password=user.hashed_password,
        ):
            raise IncorrectPassword("Incorrect user password.")

        token = generate_token(user.id)
        return token

    async def create_user(self, user_data: UserCreate) -> User:
        existing_user = await self.get_user_by_username(user_data.username)

        if existing_user:
            raise AlreadyExistsError("User already exists.")

        hashed_pwd = hash_password(user_data.password)

        user = User(
            username=user_data.username,
            hashed_password=hashed_pwd,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
        )

        try:
            self._session.add(user)
            await self._session.commit()
            await self._session.refresh(user)

        except Exception:
            await self._session.rollback()
            raise DatabaseError("Failed to create new user.")

        return user

    async def get_user_by_username(self, username: str) -> User | None:
        statement = select(User).where(User.username == username)

        try:
            result = await self._session.execute(statement)
            user = result.scalar_one_or_none()

        except Exception as e:
            # logger.exception("Failed to retrieve user.")
            raise DatabaseError("Failed to retrieve user.")

        return user

    async def get_user_by_id(self, user_id: int) -> User | None:
        statement = select(User).where(User.id == user_id)

        try:
            result = await self._session.execute(statement)
            user = result.scalar_one_or_none()

        except Exception as e:
            # logger.exception("Failed to retrieve user.")
            raise DatabaseError("Failed to retrieve user.")

        if not user:
            raise NotFoundError("User not found.")

        return user

    async def update_user_by_id(self, new_data: UserUpdate, user_id: int) -> User:
        user = await self.get_user_by_id(user_id)

        values = new_data.model_dump(exclude_none=True, exclude_unset=True)

        for key, value in values.items():
            setattr(user, key, value)

        try:
            await self._session.commit()
            await self._session.refresh(user)
            return user

        except Exception as e:
            # logger.exception("Failed to update user.")
            raise DatabaseError("Failed to update user.")
