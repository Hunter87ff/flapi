from fastapi import FastAPI, Response

from routers import v1 
app = FastAPI()


# Setup CORS
@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


app.include_router(v1.apiv1)

@app.get("/")
def home():
    # redirect to /docs
    return Response(status_code=307, headers={"Location": "/docs"})
