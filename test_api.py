import json
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Union
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


# @app.middleware("http")
# async def log_req_params(request: Request, call_next):
#     await set_body(request)
#     # body = await request.body()
#     json = await request.json()
#     # print(body)
#     print(json)
#     resp = await call_next(request)
#     return resp


# async def set_body(request: Request):
#     receive_ = await request._receive()

#     async def receive():
#         return receive_

#     request._receive = receive


@app.post("/test")
async def test1(item: Item, request: Request):
    res = {
        "method": request.method,
        "query": request.url.query,
        "query_params": request.query_params,
        "path_params": request.path_params,
        "body": await request.body(),
        "json": await request.json(),
    }
    return res


@app.get("/data")
async def test2(q: int, p: str, request: Request):
    res = {
        "method": request.method,
        "query": request.url.query,
        "query_params": request.query_params,
        "path_params": request.path_params,
    }
    return res


if __name__ == "__main__":
    uvicorn.run(app="test_api:app", host="127.0.0.1", port=8888, reload=True)
