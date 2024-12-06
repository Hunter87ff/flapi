from fastapi import APIRouter
from .gen import router as gen

apiv1 = APIRouter(
    tags=["Generator"],
    prefix="/v1"
)
apiv1.include_router(gen)