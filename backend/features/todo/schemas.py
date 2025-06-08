from shared.schemas import BaseSchema


class TodoRead(BaseSchema):
    id: int
    text: str
    is_completed: bool


class TodoCreate(BaseSchema):
    text: str


class TodoUpdate(BaseSchema):
    text: str | None = None
    is_completed: bool | None = None
