from fastapi import APIRouter
from features.user.routers import auth_router, user_router
from shared.settings import api_prefix_config

v1_router = APIRouter(prefix=api_prefix_config.v1.prefix)


v1_router.include_router(auth_router)
v1_router.include_router(user_router)
