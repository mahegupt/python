from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app instance
app = FastAPI()

# Pydantic model for request body


class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


items_db = {}
# Root route


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

# Route with path parameter


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return items_db.get(item_id, {"error": "Item not found"})

# Route to accept POST request


@app.post("/items/")
def create_item(item: Item):
    items_db[item.id] = item
    return item
