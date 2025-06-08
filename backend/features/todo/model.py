from shared.models.base import Base
from shared.models.mixins import INTPrimaryKeyMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Todo(Base, INTPrimaryKeyMixin):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    text: Mapped[str]
    is_completed: Mapped[bool] = mapped_column(default=False)
