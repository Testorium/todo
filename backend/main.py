from contextlib import asynccontextmanager

from fastapi import FastAPI
from shared.database import db_manager
from shared.models import Base
from shared.routers import main_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with db_manager.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield
    await db_manager.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(main_router)
