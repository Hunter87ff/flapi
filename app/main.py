from fastapi import FastAPI, Response

from routers import v1 
app = FastAPI()
app.include_router(v1.apiv1)

@app.get("/")
def home():
    # redirect to /docs
    return Response(status_code=307, headers={"Location": "/docs"})
