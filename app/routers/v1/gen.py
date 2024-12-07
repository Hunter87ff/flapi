from fastapi import APIRouter, Query, Request
import json, core.util as util
from ext import default

router = APIRouter(
    tags=["Generator"],
    prefix="/gen"
)
generator = util.DataGenerator()


@router.get("/")
async def generate_data(
    req:Request,
    amount: int = Query(default=1, ge=1, le=100),
    schema: str = Query(default=default.GEN_QUERY)
):
    """
    ### Generate mock data based on provided schema
    
    **Parameters**
    - **amount**: Number of objects to generate
    - **schema**: JSON-like schema string defining object structure
    - **json**: It also accepts JSON body with schema

    **Returns**
    - List of generated objects
    """
    try:
        schema = schema or await req.json() or default.GEN_QUERY
        schema = str(schema).replace("'", "\"")

        # Convert schema string to dictionary
        schema_dict = json.loads(f"{schema}")
        
        # Generate specified amount of objects
        return [ generator.generate_object(schema_dict) for _ in range(amount)]
    except Exception as e:
        return {"error": str(e)}




