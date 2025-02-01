"""
"""
import traceback
from fastapi import APIRouter, Query, Request, Response
import json, core.util as util
from ext import default

router = APIRouter(
    tags=["Generator"],
    prefix="/gen"
)

@router.get("/")
@router.post("/")
async def generate_data(
    req:Request,
    amount: int = Query(default=1, ge=1, le=100),
    schema: str = Query(default=None)
):
    """
    ## Generate mock data based on provided schema
    
    Parameters
    ----------
    - amount: Number of objects to generate
    - schema: JSON-like schema string defining object structure
    - json: It also accepts JSON body with schema

    Returns
    -------
    - List of generated objects
    """
    _json:dict 

    # add cache header
    response = Response()
    response.headers["Cache-Control"] = "public, max-age=300"

    try:
        _json = await req.json()
    except Exception:
        _json = None


    if not schema and not _json:
        response.status_code=400
        return {"error": "The schema or json body is invalid!! check if there is a syntax error!!"}

    try:
        schema = schema or _json or default.GEN_QUERY
        schema = str(schema).replace("'", '"').replace("\n", "").replace("\t", "").replace(" ", "")
        schema_dict = json.loads(str(schema))
        response.body = json.dumps(util.Gen.generate_object(schema_dict, amount)).encode()
        response.media_type = "application/json"
        response.headers["Content-Length"] = str(len(response.body))
        return response
    
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}




