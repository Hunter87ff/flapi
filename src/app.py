from fastapi import FastAPI, Query, Response, Request
import util, json


app = FastAPI()


@app.get("/get")
async def root():
    return {"message": "Hello World"}


generator = util.DataGenerator()

@app.get("/")
def home():
    # redirect to /docs
    return Response(status_code=307, headers={"Location": "/docs"})


@app.get("/gen")
async def generate_data(
    req:Request,
    amount: int = Query(default=1, ge=1, le=100),
    schema: str = Query(...)
):
    """
    Generate mock data based on provided schema
    
    :param amount: Number of objects to generate
    :param schema: JSON-like schema string defining object structure
    :return: List of generated objects
    """
    try:
        schema = schema or req.json()
        print(schema if schema=="" else "No schema provided")
        # Convert schema string to dictionary
        schema_dict = json.loads(schema)
        
        # Generate specified amount of objects
        return [generator.generate_object(schema_dict) for _ in range(amount)]
    except Exception as e:
        return {"error": str(e)}

