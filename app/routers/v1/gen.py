"""
"""
import traceback
from fastapi import APIRouter, Query, Request
import json, core.util as util
from ext import default

router = APIRouter(
    tags=["Generator"],
    prefix="/gen"
)

@router.get("/")
async def generate_data(
    req:Request,
    amount: int = Query(default=1, ge=1, le=100),
    schema: str = Query(default=None)
    
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
    _json:dict 
    try:
        _json = await req.json()
    except Exception:
        _json = None

    try:
        schema = schema or _json or default.GEN_QUERY

        schema = str(schema).replace("'", '"')
        schema_dict = json.loads(str(schema))
        return  util.Gen.generate_object(schema_dict, amount)
    
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}




