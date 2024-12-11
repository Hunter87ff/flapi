from fastapi import APIRouter, Query, Request
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/privacy")
def privacy(request: Request):
    return templates.TemplateResponse("pages/privacy.html", {"request": request})