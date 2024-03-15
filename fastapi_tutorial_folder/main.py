from fastapi import FastAPI

app=FastAPI()

@app.get("/",description="this is my first route",deprecated=True)
async def root():
    return {"Hello":"world"} 

@app.post("/")
async def post():
    return {"message":"Hello from the post route"}

@app.put("/")
async def put():
    return {"message":"data changed"}

@app.get("/items")
async def list_item():
    return{"message":"list_items"}

@app.get("/items/{items}")
async def items(items:int):
    return {"message":items}


from enum import Enum
class FoodEnum(str,Enum):
    fruit="fruits"
    vegetables="vegetables"
    dairy="dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name:FoodEnum):
    if food_name==FoodEnum.vegetables:
        return {"food_name":food_name,"message":"you are healty"}
    if food_name.value==FoodEnum.fruit:
        return {"food_name":food_name,"message":"like sweet"}
    
    return {"food_name":food_name,"message":"I like chocolate milk"}


fake_items_db=[{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]
@app.get("/itemss")
async def list_items(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip+limit]

from typing import Optional

@app.get("items22/{items_id}")
async def get_items(items_id:str,q:Optional[str]=None):
    if q:
        return {"q":q}
    return {"item_id":items_id} 



