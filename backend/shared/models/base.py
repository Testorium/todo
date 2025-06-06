from humps import decamelize
from shared.settings import db_config
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=db_config.naming_convention)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{decamelize(cls.__name__)}s"
