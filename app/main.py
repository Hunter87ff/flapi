"""
## Flapi
A free and open source api for devs to get data of their given api structure. 
it helps to make development faster without the headache of data collection.
"""


from fastapi import FastAPI, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from routers import v1
from routers.pages import info

static = StaticFiles(directory="templates/static")
templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="Flapi",
    version="1.0.1",
    description="A free and open source api for devs to get data of their given api structure. it helps to make development faster without the headache of data collection.",
)
app.mount("/static", static)

# Setup CORS
@app.middleware("http")
async def add_cors_header(request, call_next):
    response:Response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

app.include_router(info.router)
app.include_router(v1.apiv1)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
