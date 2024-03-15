#part:4
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class Item(BaseModel):
    name:str
    decription:str |None=None
    price:float|None=None
    tax:float

@app.post("/items")
async def creat_item(item:Item):
    return item