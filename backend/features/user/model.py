from shared.models import Base
from shared.models.mixins import INTPrimaryKeyMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base, INTPrimaryKeyMixin):
    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]

    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
