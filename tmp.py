from fastapi import FastAPI, Query, Path, Body, Cookie
from pydantic import BaseModel, Required
from typing import Union
import uvicorn

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class Item(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "foo",
                "description": "A very nice Item",
                "price": 35.5,
                "tax": 3.2,
            }
        }


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get", ge=0, le=100),
    q: str = Query(
        default=Required, description="testsette", title="Query string", max_length=30
    ),
):
    results = {"items": item_id}
    if q:
        results.update({"q": q})
    return results


@app.put("/item/{item_id}")
@app.get("/item/{item_id}")
async def update_items(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: Union[str, None] = None,
    item: Union[Item, None] = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


@app.post("/post")
async def create_iem(item: Item = Body(embed=True)):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


if __name__ == "__main__":
    uvicorn.run(app="tmp:app", host="127.0.0.1", port=8888, reload=True)
