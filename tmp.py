from fastapi import FastAPI

import uvicorn

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    # uvicorn.run(app=app, host="127.0.0.1", port=8082)
    ...
