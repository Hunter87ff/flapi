"""
"""
from fastapi import APIRouter, Query, Request
import json, core.dev_util as util
from ext import default

router = APIRouter(
    tags=["Generator (Development)"],
    prefix="/gen"
)

@router.get("/")
async def generate_data(
    req:Request,
    amount: int = Query(default=1, ge=1, le=100),
    schema: str = Query(default=default.DEV_GEN_QUERY)
):
    """
    ### Dev Generate mock data based on provided schema
    
    **Parameters**
    - **amount**: Number of objects to generate
    - **schema**: JSON-like schema string defining object structure
    - **json**: It also accepts JSON body with schema

    **Returns**
    - List of generated objects
    """
    try:
        schema = (schema if schema!=default.DEV_GEN_QUERY else None) or await req.json() or default.DEV_GEN_QUERY
        schema = str(schema).replace("'", '"')
        schema_dict = json.loads(str(schema))
        return  util.Gen.generate_object(schema_dict, amount)
    
    except Exception as e:
        return {"error": str(e)}




