from fastapi import APIRouter
from shared.settings import api_prefix_config

from .v1 import v1_router

main_router = APIRouter(prefix=api_prefix_config.prefix)

main_router.include_router(v1_router)
