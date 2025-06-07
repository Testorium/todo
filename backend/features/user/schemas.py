from shared.schemas import BaseSchema


class UserCredentials(BaseSchema):
    username: str
    password: str


class UserRead(BaseSchema):
    id: int
    username: str

    first_name: str
    last_name: str


class UserCreate(BaseSchema):
    username: str
    password: str
    first_name: str
    last_name: str


class UserUpdate(BaseSchema):
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
