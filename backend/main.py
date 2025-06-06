from contextlib import asynccontextmanager

from fastapi import FastAPI
from shared.database import db_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_manager.dispose()


app = FastAPI(lifespan=lifespan)
