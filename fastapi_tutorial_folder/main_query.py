from fastapi import FastAPI

app=FastAPI()

#query parameter Lecture : 3  --> Query parameter is extra little tag provide at the end of URL like: localhost:8000/foods/dairy?hello=world, here in this "?hello=world" is query parameter


fake_items_db=[{"items_name":"Foo"},{"items_name":"Bar"},{"items_name":"Baz"}]
@app.get("/items")
async def list_items(skip:int=0, limit:int=10):
    return fake_items_db[skip:skip+limit]

# @app.get("/items/{item_id}")
# async def get_items(item_id:str,q: str|None):      #it is valid in python 3.10 or above version
#     if q:
#         return{"item_id":item_id,"q":q}
#     return {"item_id":item_id}


#this is the way to call query parameter # http://127.0.0.1:8001/items/hello?q=world
@app.get("/items/{item_id}")
async def get_items(item_id:str,q:str|None):
    if q:
        return{"item_id":item_id,q:q}
    return {"item_id":item_id}



#using url it will work: http://127.0.0.1:8001/items_option/hello?q=world&short=True
@app.get("/items_option/{items_id}")
async def get_items_new(items_id:str,q:str|None,short:bool=False):
    item={"items_id":items_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"this is krishna kumar"})
    return item



