"""
## Flapi
A free and open source api for devs to get data of their given api structure. 
it helps to make development faster without the headache of data collection.
"""


from fastapi import FastAPI, Response
from routers import v1 , dev
app = FastAPI(
    title="Flapi",
    version="1.0.0",
    description="A free and open source api for devs to get data of their given api structure. it helps to make development faster without the headache of data collection.",
)


# Setup CORS
@app.middleware("http")
async def add_cors_header(request, call_next):
    response:Response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


app.include_router(v1.apiv1)
app.include_router(dev.dev)
@app.get("/", tags=["Home"])
def home():
    # redirect to /docs
    return Response(status_code=307, headers={"Location": "/docs"})
