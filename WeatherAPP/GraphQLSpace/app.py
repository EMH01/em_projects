from strawberry.asgi import GraphQL
from .schema import schema
import uvicorn

app = GraphQL(schema)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
