from fastapi import APIRouter
from .gen import router as gen

dev = APIRouter(
    tags=["Generator (Development)"],
    prefix="/dev"
)
dev.include_router(gen)