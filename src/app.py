from fastapi import FastAPI, Request
import util

app = FastAPI()


@app.get("/get")
async def root():
    return {"message": "Hello World"}


@app.get("/generate")
async def generate(req:Request, amount:int=1, ):
    _json = await req.json()
    return util.generate_payload(_json, amount)
