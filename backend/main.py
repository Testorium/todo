from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from shared.database import db_manager
from shared.models import Base
from shared.routers import main_router
from shared.settings import cors_config


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with db_manager.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield
    await db_manager.dispose()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_config.origins,
    allow_credentials=cors_config.allow_credentials,
    allow_methods=cors_config.allow_methods,
    allow_headers=cors_config.allow_headers,
)

app.include_router(main_router)
