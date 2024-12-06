from fastapi import APIRouter, Query, Request
import json, core.util as util

router = APIRouter(
    tags=["Generator"],
    prefix="/gen"
)
generator = util.DataGenerator()


@router.get("/")
async def generate_data(
    req:Request,
    amount: int = Query(default=1, ge=1, le=100),
    schema: str = Query(default=None)
):
    """
    Generate mock data based on provided schema
    
    :param amount: Number of objects to generate
    :param schema: JSON-like schema string defining object structure
    :return: List of generated objects
    """
    try:
        schema = schema or await req.json()
        schema = str(schema).replace("'", "\"")

        # Convert schema string to dictionary
        schema_dict = json.loads(f"{schema}")
        
        # Generate specified amount of objects
        return [ generator.generate_object(schema_dict) for _ in range(amount)]
    except Exception as e:
        return {"error": str(e)}




